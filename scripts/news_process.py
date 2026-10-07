#!/usr/bin/env python3
"""Turn fetched HTML (news/raw/fetch/<md5>.html, listed in fetch_log.tsv) into
news/<YYYY-MM-DD>_<outlet>_<slug>.txt (+ news/html/<same>.html) and news/raw/manifest.tsv.
Run with the scratchpad venv python (needs trafilatura)."""
import json, re, os, shutil, sys, html as htmlmod
from urllib.parse import urlparse
import trafilatura

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'news')
RAW = f'{BASE}/raw'
OUTLETS = {
    'opb.org': ('opb', 'OPB'), 'oregonlive.com': ('oregonian', 'The Oregonian/OregonLive'),
    'wweek.com': ('wweek', 'Willamette Week'), 'portlandtribune.com': ('portlandtribune', 'Portland Tribune'),
    'kgw.com': ('kgw', 'KGW'), 'koin.com': ('koin', 'KOIN'), 'kptv.com': ('kptv', 'KPTV'),
    'katu.com': ('katu', 'KATU'), 'streetroots.org': ('streetroots', 'Street Roots'),
    'portlandmercury.com': ('mercury', 'Portland Mercury'), 'theskanner.com': ('skanner', 'The Skanner'),
    'axios.com': ('axios', 'Axios Portland'), 'k12dive.com': ('k12dive', 'K-12 Dive'),
    'facilitiesdive.com': ('facilitiesdive', 'Facilities Dive'), 'chalkbeat.org': ('chalkbeat', 'Chalkbeat'),
    'yahoo.com': ('yahoo', 'Yahoo News (syndicated)'), 'youroregonnews.com': ('youroregonnews', 'Your Oregon News (Pamplin syndication)'),
    'kxl.com': ('kxl', 'KXL'), 'northpeninsulareview.com': ('northpeninsulareview', 'North Peninsula Review'),
    'pps.net': ('pps', 'Portland Public Schools (official)'), 'savepdxschools.org': ('savepdxschools', 'Save PDX Schools (parent group)'),
    'pdxteachers.org': ('pat', 'Portland Association of Teachers'), 'ppsclosures.info': ('ppsclosures', 'ppsclosures.info (independent data site)'),
    'citizenportal.ai': ('citizenportal', 'Citizen Portal (AI meeting summaries)'), 'grantspasstribune.com': ('grantspasstribune', 'Grants Pass Tribune'),
    'newpittsburghcourier.com': ('pittsburghcourier', 'New Pittsburgh Courier'),
}

def outlet_for(url):
    host = urlparse(url).hostname.replace('www.', '')
    for k, v in OUTLETS.items():
        if host.endswith(k):
            return v
    return (host.split('.')[0], host)

def date_from_url(url):
    m = re.search(r'/(20\d\d)/(\d\d)/(\d\d)/', url)
    if m: return '-'.join(m.groups())
    m = re.search(r'/(20\d\d)/(\d\d)/', url)
    if m: return f'{m.group(1)}-{m.group(2)}-00'
    return None

MONTHS = {m: i for i, m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], 1)}
def parse_any_date(v):
    v = (v or '').strip()
    m = re.match(r'(20\d\d)-(\d\d)-(\d\d)', v)
    if m: return '-'.join(m.groups())
    m = re.search(r'([A-Za-z]+)\.? (\d{1,2}), (20\d\d)', v)
    if m and m.group(1).lower() in MONTHS: return f'{m.group(3)}-{MONTHS[m.group(1).lower()]:02d}-{int(m.group(2)):02d}'
    m = re.match(r'(\d{1,2})/(\d{1,2})/(20\d\d)', v)
    if m: return f'{m.group(3)}-{int(m.group(1)):02d}-{int(m.group(2)):02d}'
    return None

def meta_date_author(raw):
    date = None
    for pat in [r'"datePublished"\s*:\s*"([^"]+)"', r'article:published_time"\s+content="([^"]+)"', r'"publishedDate"\s*:\s*"([^"]+)"']:
        m = re.search(pat, raw)
        if m:
            date = parse_any_date(m.group(1))
            if date: break
    names = re.findall(r'"author"\s*:\s*\[?\s*\{[^}]*?"name"\s*:\s*"([^"]+)"', raw)
    author = '; '.join(dict.fromkeys(n for n in names if n and 'staff' not in n.lower() or n == 'KATU Staff'))
    return date, author

# Exact duplicates / off-topic pages fetched during discovery; not written to the corpus.
SKIP = {
    'https://katu.com/newsletter-daily/pps-plans-would-close-six-schools-serving-more-low-income-families-title-one-inequity-poor-portland-public-school-teachers-students-parents-money-budget-funding',
    'https://katu.com/newsletter-daily/portland-public-schools-to-discuss-closing-15-elementary-schools-tuesday-oregon-closure-education-pps-children-teenagers-board-district',
    'https://katu.com/newsletter-daily/pps-keeps-cutting-millions-so-why-is-another-major-shortfall-is-looming-portland-public-schools-money-education-teachers-students-families-parents-local',
    'https://www.facilitiesdive.com/news/portland-public-schools-ponders-up-to-18-school-closures/830020/',
    'https://youroregonnews.com/2026/10/06/portland-public-schools-proposes-closing-up-to-14-schools-in-rightsizing-plan/',
    'https://www.yahoo.com/news/us/articles/pps-proposes-closing-14-schools-001401522.html',
    'https://www.yahoo.com/news/us/articles/pps-releases-list-proposed-school-004741033.html',
    'https://www.kgw.com/education',
    'https://www.pdxteachers.org/the_time_to_get_it_right',
    'https://www.pdxteachers.org/pat_news',
    'https://savepdxschools.org/schools/',
    'https://savepdxschools.org/transcripts/',
}

STOP = set('a an the of to and in on for at as is are be its it by with from that this what will could may up'.split())
def slugify(title, n=7):
    t = htmlmod.unescape(title or '').lower()
    t = re.sub(r"[’'`]", '', t)
    words = [w for w in re.split(r'[^a-z0-9]+', t) if w and w not in STOP]
    return '-'.join(words[:n]) or 'untitled'

def clean_title(t, outlet_name):
    t = htmlmod.unescape(t or '').strip()
    t = re.sub(r'\s*[|\-–]\s*(OPB|KGW|kgw\.com|Axios Portland|The Portland Tribune|Your Oregon News|KXL|Portland School District|Citizen Portal|OregonLive\.com|oregonlive\.com)\s*$', '', t)
    return t

def main():
    rows = [l.split('\t') for l in open(f'{RAW}/fetch_log.tsv').read().splitlines() if l.strip()]
    os.makedirs(f'{BASE}/html', exist_ok=True)
    manifest = []
    used = set()
    for r in rows:
        h, url, status = r[0], r[1], r[2]
        if not status.startswith('200') or url in SKIP: continue
        src = f'{RAW}/fetch/{h}.html'
        if not os.path.exists(src): continue
        raw = open(src, encoding='utf-8', errors='replace').read()
        d = trafilatura.bare_extraction(raw, with_metadata=True, include_comments=False, include_tables=True, favor_recall=True)
        if d is not None and not isinstance(d, dict): d = d.as_dict()
        d = d or {}
        code, oname = outlet_for(url)
        title = clean_title(d.get('title'), oname)
        mdate, mauthor = meta_date_author(raw)
        date = date_from_url(url)
        if not date or date.endswith('-00'):
            date = mdate or (d.get('date') or '')[:10] or (date or '0000-00-00')
        author = (d.get('author') or '').strip() or mauthor
        author = re.sub(r';\s*(Juliasilverman|The Oregonian|OregonLive|Oregonlive)\b', '', author)
        if author.strip().lower() in ('updated', 'published', 'by', 'staff'): author = ''
        parts = [a.strip() for a in author.split(';') if a.strip()]
        parts = [re.sub(r'^Olive\w+\s*', '', a) for a in parts]
        parts = [a for a in parts if a and a not in ('FOX', 'KATU', 'Mfriesen', 'Oliveoreglet', 'Oliveoregedb')]
        if len(parts) > 1: parts = [a for a in parts if a.lower() not in ('letters',)] or parts
        author = '; '.join(dict.fromkeys(parts))
        text = (d.get('text') or '').strip()
        text = re.sub(r'^\|\s*Getting your Trinity Audio player ready\.\.\.\s*\|\s*$', '', text, flags=re.M)
        if '/video/' in url and 'kptv.com' in url:
            m = re.search(r'<meta[^>]+(?:property|name)="(?:og:)?description"[^>]+content="([^"]*)"', raw)
            text = 'VIDEO PAGE (no transcript available). Page description: ' + htmlmod.unescape(m.group(1) if m else '(none)')
        note = ''
        if code == 'citizenportal': note = 'PARTIAL: login wall ("Sign up to keep reading"); only the lede is public. AI-generated meeting summary, not journalism.'
        elif len(text) < 900 and code not in ('pps','savepdxschools','ppsclosures'): note = f'SHORT ({len(text)} chars): page may be video-only, gated, or a brief.'
        if 'koin.com' in url: note = (note + ' ' if note else '') + 'Fetched via AMP version (canonical returned 403 to curl).'
        if code in ('pps', 'savepdxschools', 'ppsclosures'):
            note = (note + ' ' if note else '') + f'Live web page retrieved 2026-10-07 (filename uses retrieval date; page metadata date: {date}).'
            date = '2026-10-07'
        if status.endswith('(browser)'): note = (note + ' ' if note else '') + 'Fetched via browser (curl blocked with 403).'
        slug = slugify(title)
        base = f'{date}_{code}_{slug}'
        i = 2
        while base in used:
            base = f'{date}_{code}_{slug}-{i}'; i += 1
        used.add(base)
        hdr = [f'Title: {title}', f'Outlet: {oname}', f'Author: {author or "(not listed)"}', f'Date: {date}', f'URL: {url}']
        if note: hdr.append(f'Note: {note}')
        open(f'{BASE}/{base}.txt', 'w', encoding='utf-8').write('\n'.join(hdr) + '\n\n' + text + '\n')
        shutil.copyfile(src, f'{BASE}/html/{base}.html')
        manifest.append([date, oname, title, base + '.txt', url, author, str(len(text)), note])
    manifest.sort()
    with open(f'{RAW}/manifest.tsv', 'w', encoding='utf-8') as f:
        f.write('date\toutlet\ttitle\tfile\turl\tauthor\tchars\tnote\n')
        for m in manifest: f.write('\t'.join(x.replace('\t', ' ') for x in m) + '\n')
    print(len(manifest), 'articles written')

if __name__ == '__main__':
    main()
