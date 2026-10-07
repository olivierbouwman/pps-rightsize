# PPS "Rightsizing" — news and community coverage index

This index covers news and community coverage of Portland Public Schools' (PPS) "Rightsize. Right Support. Right for Students." process. It was compiled on 2026-10-07 and covers January 2025 through October 7, 2026.

**What's in this folder**

- `*.txt`: 173 items. Each starts with header lines (Title, Outlet, Author, Date, URL, and an optional Note), followed by the cleaned article text.
  - Filenames follow `YYYY-MM-DD_outlet_short-slug.txt`.
  - Live web pages are dated by retrieval (`2026-10-07`). This covers PPS pages, Save PDX Schools and ppsclosures.info.
- `html/`: the raw HTML for each item, with the same basename as its `.txt` (172 files; the PDF item is in `docs/`).
- `docs/`: PDFs, currently the Save PDX Schools evidence deck.
- `raw/`: working files.
  - `urls.txt` lists the candidate URLs; `fetch_log.tsv` records the HTTP result for each one.
  - `manifest.tsv` holds the metadata for every item.
  - `board_mentions.txt` and `stakeholder_mentions.txt` hold every paragraph that names a director or stakeholder.
  - The scraped OregonLive archive and opinion link lists are also here.
- Scripts are in `../scripts/news_*` (fetch, browser import, extract/process, table builder).

**How the files were fetched**

- **Plain curl** worked for OPB, WW, KATU, KPTV, Tribune, Mercury, K-12 Dive, North Peninsula Review and PPS.
- **KOIN** returned 403 to curl. These pages were fetched through their `/amp/` versions.
- **KGW, OregonLive, Axios and Citizen Portal** also returned 403 to curl. They were fetched in a real browser session (Playwright). No forms were submitted and no accounts were created.

**Board roster** (current as of 2026-10-07, from `2026-10-07_pps_board-members.txt` plus coverage):

| Zone | Director | Term | Notes |
|---|---|---|---|
| 1 | Christy Splitt | 7/2025–6/2027 | Appointed Jan 2025, elected May 2025. Not running in 2027 (WW 6/30/26). |
| 2 | Michelle DePass | 7/2023–6/2027 | Longest-serving member. The PPS page still lists her as Vice-Chair. |
| 3 | Patte Sullivan | 7/2023–6/2027 | Not running in 2027 (Oregonian 3/12/26). |
| 4 | Rashelle Chase-Miller | 7/2025–6/2029 | Unseated incumbent Herman Greene in May 2025. Called **Vice Chair** in Sept–Oct 2026 coverage (Oregonian 9/2, WW 9/16, WW 10/6). |
| 5 | Virginia La Forte | 7/2025–6/2029 | Elected May 2025, replacing Gary Hollands. |
| 6 | Stephanie Engelsman | 7/2025–6/2029 | Elected May 2025, replacing Julia Brim-Edwards. |
| 7 | Eddie Wang (Chair) | 7/2023–6/2027 | Target of a prospective recall petition filed 9/15/26. |
| Student rep | Rose Sandell (2026–27) | | Predecessor: Ian Ritorto (2025–26). |

> **Discrepancy:** the PPS roster page names DePass as Vice-Chair. Every news story from September and October 2026 calls Chase-Miller the vice chair, so leadership probably rotated around July 2026 and the PPS page is stale.

**Caveats**

- Citizen Portal items are AI-generated meeting summaries behind a sign-up wall. Only their ledes were saved. Treat them as leads, not as sources.
- KPTV `/video/` pages have no transcript. Only the page description was saved.
- Mercury "Good Morning, News" and OPB "First Look" items are roundups; only one item in each concerns PPS.
- Per the organization's instructions, the summaries below:
  - name officials and organizational leaders, but describe private parents and students by role rather than by name;
  - do not discuss assessments of any individual's job performance.

