#!/usr/bin/env python3
"""Import a Playwright-saved (JSON-string-encoded) outerHTML dump as fetch/<md5(url)>.html and update fetch_log."""
import sys, json, hashlib, os
url, src = sys.argv[1], sys.argv[2]
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'news', 'raw')
raw = open(src, encoding='utf-8').read()
try:
    html = json.loads(raw)
except Exception:
    html = raw
h = hashlib.md5(url.encode()).hexdigest()
open(f'{base}/fetch/{h}.html', 'w', encoding='utf-8').write(html)
os.remove(src)
log = f'{base}/fetch_log.tsv'
lines = open(log).read().splitlines() if os.path.exists(log) else []
out, found = [], False
for l in lines:
    f = l.split('\t')
    if f[0] == h:
        f[2] = '200(browser)'; f[3] = str(len(html)); found = True
    out.append('\t'.join(f))
if not found:
    out.append('\t'.join([h, url, '200(browser)', str(len(html))]))
open(log, 'w').write('\n'.join(out) + '\n')
print(h, len(html))
