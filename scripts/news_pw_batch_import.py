#!/usr/bin/env python3
"""Import a Playwright batch dump {url: {status, html}} into fetch/<md5>.html + fetch_log."""
import sys, json, hashlib, os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'news', 'raw')
src = sys.argv[1]
d = json.loads(open(src, encoding='utf-8').read())
if isinstance(d, str): d = json.loads(d)
log = f'{base}/fetch_log.tsv'
lines = open(log).read().splitlines()
idx = {l.split('\t')[0]: i for i, l in enumerate(lines)}
for url, v in d.items():
    h = hashlib.md5(url.encode()).hexdigest()
    st = str(v['status']) + '(browser)'
    if v['status'] == 200:
        open(f'{base}/fetch/{h}.html', 'w', encoding='utf-8').write(v['html'])
    row = '\t'.join([h, url, st, str(len(v['html']))])
    if h in idx: lines[idx[h]] = row
    else: lines.append(row)
    print(st, len(v['html']), url)
open(log, 'w').write('\n'.join(lines) + '\n')
os.remove(src)
