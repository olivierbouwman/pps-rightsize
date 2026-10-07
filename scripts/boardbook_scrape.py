#!/usr/bin/env python3
"""Scrape PPS BoardBook (org 915): agenda text, public notice, minutes text,
supplementals and all attachments (as PDF + extracted text) for every meeting
on or after a cutoff date."""
import html, json, os, re, subprocess, sys, time, urllib.request
from datetime import datetime

BASE = "https://meetings.boardbook.org"
ORG = 915
CUTOFF = datetime(2023, 7, 1)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "boardbook")
UA = {"User-Agent": "Mozilla/5.0 (research; PPS board materials archive)"}


def get(url, binary=False, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                data = r.read()
                return data if binary else data.decode("utf-8", "ignore")
        except Exception as e:
            print(f"  retry {i+1} {url}: {e}", file=sys.stderr)
            time.sleep(3 * (i + 1))
    return None


def text_of(h):
    h = re.sub(r"<(script|style)\b.*?</\1>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", h, flags=re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h).replace("\xa0", " ")
    h = re.sub(r"[ \t]+", " ", h)
    return re.sub(r"\n\s*\n+", "\n\n", h).strip()


def slug(s, n=90):
    s = re.sub(r"[^\w\-. ]+", "", s).strip().replace(" ", "_")
    return s[:n]


def main():
    index = get(f"{BASE}/Public/Organization/{ORG}")
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", index, re.S)
    meetings = []
    for r in rows:
        m = re.search(r"meeting=(\d+)", r)
        if not m:
            continue
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", r))).strip()
        d = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4}) at ([\d:]+ [AP]M) - (.*?) Meeting Type", t)
        if not d:
            continue
        dt = datetime.strptime(d.group(1), "%B %d, %Y")
        if dt < CUTOFF:
            continue
        yt = re.findall(r"youtube\.com/watch\?v=([\w-]+)|youtu\.be/([\w-]+)", r)
        meetings.append({
            "id": m.group(1), "date": dt.strftime("%Y-%m-%d"), "time": d.group(2),
            "title": d.group(3).replace("Cancelled", "").strip(),
            "cancelled": t.startswith("Cancelled"),
            "summary": t[:400],
            "youtube": sorted({a or b for a, b in yt}),
            "has_minutes": f"Minutes/{ORG}?meeting={m.group(1)}" in r,
        })
    os.makedirs(OUT, exist_ok=True)
    json.dump(meetings, open(os.path.join(OUT, "meetings_index.json"), "w"), indent=1)
    print(f"{len(meetings)} meetings since {CUTOFF:%Y-%m-%d}")

    for mt in meetings:
        if mt["cancelled"]:
            continue
        d = os.path.join(OUT, f"{mt['date']}_{slug(mt['title'], 60)}_{mt['id']}")
        if os.path.exists(os.path.join(d, ".done")):
            continue
        os.makedirs(d, exist_ok=True)
        print(mt["date"], mt["title"])
        files = {}
        ag = get(f"{BASE}/Public/Agenda/{ORG}?meeting={mt['id']}")
        if ag:
            body = text_of(ag)
            i = body.find("Hide Everything")
            open(os.path.join(d, "agenda.txt"), "w").write(body[i + 15 if i >= 0 else 0:].split("Web Viewer << Back")[0])
            for fid, name in re.findall(r"file=(\d+)'[^>]*><span class='fileNameValue'>([^<]*)", ag):
                files[fid] = html.unescape(name).strip()
        pn = get(f"{BASE}/Public/PublicNotice/{ORG}?meeting={mt['id']}")
        if pn:
            open(os.path.join(d, "public_notice.txt"), "w").write(text_of(pn)[:20000])
        if mt["has_minutes"]:
            mn = get(f"{BASE}/Public/Minutes/{ORG}?meeting={mt['id']}")
            if mn:
                open(os.path.join(d, "minutes.txt"), "w").write(text_of(mn))
                for fid, name in re.findall(r"file=(\d+)'[^>]*><span class='fileNameValue'>([^<]*)", mn):
                    files[fid] = html.unescape(name).strip()
        sp = get(f"{BASE}/Meeting/Supplementals/{ORG}?meeting={mt['id']}")
        if sp and "login.boardbook.org" not in sp:
            for fid, name in re.findall(r"file=(\d+)'[^>]*><span class='fileNameValue'>([^<]*)", sp):
                files[fid] = "SUPP_" + html.unescape(name).strip()
        for fid, name in files.items():
            pdf = os.path.join(d, f"{slug(name)}_{fid}.pdf")
            if os.path.exists(pdf):
                continue
            data = get(f"{BASE}/Documents/DownloadPDF/{fid}?org={ORG}", binary=True)
            if data and data[:4] == b"%PDF":
                open(pdf, "wb").write(data)
                subprocess.run(["pdftotext", "-layout", pdf, pdf[:-4] + ".txt"], capture_output=True)
            else:
                print(f"  ! not a pdf: {fid} {name}", file=sys.stderr)
            time.sleep(0.5)
        json.dump({**mt, "files": files}, open(os.path.join(d, "meeting.json"), "w"), indent=1)
        open(os.path.join(d, ".done"), "w").close()
        time.sleep(0.5)


if __name__ == "__main__":
    main()
