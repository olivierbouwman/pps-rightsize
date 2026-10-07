#!/usr/bin/env python3
"""Extract text+metadata from fetched HTML using trafilatura. Usage: news_extract.py <html> -> prints JSON."""
import sys, json, trafilatura
html = open(sys.argv[1], encoding='utf-8', errors='replace').read()
d = trafilatura.bare_extraction(html, with_metadata=True, include_comments=False, include_tables=True, favor_recall=True)
if d is None:
    print(json.dumps({})); sys.exit()
if not isinstance(d, dict):
    d = d.as_dict()
print(json.dumps({k: d.get(k) for k in ['title','author','date','sitename','hostname','text','url']}, ensure_ascii=False))
