#!/bin/bash
# Fetch each URL in urls file (if not already fetched) into news/raw/fetch/<md5>.html; log status.
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/news/raw/fetch"
LOG="$ROOT/news/raw/fetch_log.tsv"
LIST=${1:-$ROOT/news/raw/urls.txt}
touch "$LOG"
sort -u "$LIST" | grep -v '^\s*$' | while read -r url; do
  h=$(printf '%s' "$url" | md5 -q)
  if grep -q "^$h	" "$LOG"; then continue; fi
  code=$(curl -sL --compressed --max-time 40 -A "$UA" -H "Accept: text/html,application/xhtml+xml" -H "Accept-Language: en-US,en;q=0.9" -o "$DIR/$h.html" -w "%{http_code}	%{url_effective}" "$url")
  size=$(stat -f %z "$DIR/$h.html" 2>/dev/null)
  printf '%s\t%s\t%s\t%s\n' "$h" "$url" "$code" "$size" >> "$LOG"
  sleep 1
done
