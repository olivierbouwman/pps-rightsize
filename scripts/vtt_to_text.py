#!/usr/bin/env python3
"""Convert YouTube VTT captions in transcripts/raw_vtt into readable transcripts
(transcripts/text/*.txt) with a [HH:MM:SS] marker every ~60 seconds.
Handles the rolling-duplicate lines of YouTube auto-captions."""
import glob, html, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "transcripts")
TS = re.compile(r"(\d+):(\d\d):(\d\d)\.\d+ --> ")


def secs(m):
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))


def convert(path):
    cues, cur_t, buf = [], 0, []
    for line in open(path, encoding="utf-8", errors="ignore"):
        line = line.rstrip("\n")
        m = TS.match(line)
        if m:
            if buf:
                cues.append((cur_t, buf))
            cur_t, buf = secs(m), []
        elif line and not line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            t = html.unescape(re.sub(r"<[^>]+>", "", line)).strip()
            if t:
                buf.append(t)
    if buf:
        cues.append((cur_t, buf))
    # Drop rolling duplicates: keep a line only if it differs from the previous kept line.
    out, last, last_mark = [], None, -999
    for t, lines in cues:
        for l in lines:
            if l == last:
                continue
            last = l
            if t - last_mark >= 60:
                out.append(f"\n[{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}] ")
                last_mark = t
            out.append(l + " ")
    return re.sub(r" +", " ", "".join(out)).strip()


def main():
    os.makedirs(os.path.join(ROOT, "text"), exist_ok=True)
    for p in sorted(glob.glob(os.path.join(ROOT, "raw_vtt", "*.vtt"))):
        base = os.path.basename(p)
        upload, vid, rest = base.split("__", 2)
        title = re.sub(r"\.(en(-orig)?)\.vtt$", "", rest)
        m = re.match(r"(\d{4}-\d\d-\d\d)", title)
        date = m.group(1) if m else f"{upload[:4]}-{upload[4:6]}-{upload[6:]}"
        slug = re.sub(r"[^\w\-]+", "_", title.replace(date, "")).strip("_")[:100]
        dst = os.path.join(ROOT, "text", f"{date}_{slug}__{vid}.txt")
        header = f"Title: {title}\nYouTube: https://www.youtube.com/watch?v={vid}\nSource: YouTube captions ({'auto-generated' if '.en.' in base or 'orig' in base else 'captions'}) — expect transcription errors; speakers are not labelled.\n\n"
        open(dst, "w").write(header + convert(p) + "\n")
    print(len(os.listdir(os.path.join(ROOT, "text"))), "transcripts")


if __name__ == "__main__":
    main()
