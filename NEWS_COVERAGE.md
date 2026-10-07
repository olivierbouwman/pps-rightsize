# PPS "Rightsizing" — news and community coverage index

*Moved from `NEWS_COVERAGE.md`. Files named below live in `news/`.*

This index covers news and community coverage of Portland Public Schools' (PPS) "Rightsize. Right Support. Right for Students." process. It was compiled on 2026-10-07 and covers January 2025 through October 7, 2026.

**What's in this folder**

- `*.txt`: 173 items. Each starts with header lines (Title, Outlet, Author, Date, URL, and an optional Note), followed by the cleaned article text.
  - Filenames follow `YYYY-MM-DD_outlet_short-slug.txt`.
  - Live web pages are dated by retrieval (`2026-10-07`). This covers PPS pages, Save PDX Schools and ppsclosures.info.
- `news/html/`: the raw HTML for each item, with the same basename as its `.txt` (172 files; the PDF item is in `news/docs/`).
- `news/docs/`: PDFs, currently the Save PDX Schools evidence deck.
- `news/raw/`: working files.
  - `news/raw/urls.txt` lists the candidate URLs; `news/raw/fetch_log.tsv` records the HTTP result for each one.
  - `news/raw/manifest.tsv` holds the metadata for every item.
  - `news/raw/board_mentions.txt` and `news/raw/stakeholder_mentions.txt` hold every paragraph that names a director or stakeholder.
  - The scraped OregonLive archive and opinion link lists are also here.
- Scripts are in `scripts/news_*` (fetch, browser import, extract/process, table builder).

**How the files were fetched**

- **Plain curl** worked for OPB, WW, KATU, KPTV, Tribune, Mercury, K-12 Dive, North Peninsula Review and PPS.
- **KOIN** returned 403 to curl. These pages were fetched through their `/amp/` versions.
- **KGW, OregonLive, Axios and Citizen Portal** also returned 403 to curl. They were fetched in a real browser session (Playwright). No forms were submitted and no accounts were created.

**Board roster** (current as of 2026-10-07, from `news/2026-10-07_pps_board-members.txt` plus coverage):

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


## Chronological index (173 items)

Titles marked "(partial: login wall)" or "(video page)" are incomplete. The 2026-10-07 entries for PPS, Save PDX Schools and ppsclosures.info are live pages, dated by retrieval.

| Date | Outlet | Title | File | Gist |
|---|---|---|---|---|
| 2025-01-23 | Willamette Week | Preliminary Enrollment Forecasts Show Steeper Decline to Come for Portland Public Schools | [2025-01-23_wweek_preliminary-enrollment-forecasts-show-steeper-decline-come.txt](news/2025-01-23_wweek_preliminary-enrollment-forecasts-show-steeper-decline-come.txt) | In a newly released calculation, Portland State University researchers forecast that Portland Public Schools enrollment will decline by nearly 15% in the next decade. |
| 2025-04-22 | OPB | Superintendent Armstrong presents ‘sobering fiscal cliff’ in budget proposal for Portland schools | [2025-04-22_opb_superintendent-armstrong-presents-sobering-fiscal-cliff-budget.txt](news/2025-04-22_opb_superintendent-armstrong-presents-sobering-fiscal-cliff-budget.txt) | Superintendent Kimberlee Armstrong is proposing a $2 billion budget for the 2025-26 school year. |
| 2025-04-23 | The Oregonian/OregonLive | With enrollment declining and costs going up, Portland Public Schools tightens its belt — again | [2025-04-23_oregonian_enrollment-declining-costs-going-portland-public-schools.txt](news/2025-04-23_oregonian_enrollment-declining-costs-going-portland-public-schools.txt) | Oregon’s largest school district will operate next school year on a budget that is only about 1.4% more than the current year, requiring systemwide program and staffing cutbacks, Portland Schools Superintendent… |
| 2025-04-23 | Yahoo News (syndicated) | PPS Superintendent discusses ‘tough decisions’ with 2025-2026 budget proposal | [2025-04-23_yahoo_pps-superintendent-discusses-tough-decisions-2025-2026.txt](news/2025-04-23_yahoo_pps-superintendent-discusses-tough-decisions-2025-2026.txt) | KOIN (syndicated): Armstrong presents 2025-26 budget with hundreds of position cuts amid a ~$40M deficit, third straight deficit year. |
| 2025-04-27 | The Oregonian/OregonLive | Editorial endorsement: Elect Splitt, Greene, La Forte and Engelsman to Portland Public Schools board | [2025-04-27_oregonian_editorial-endorsement-elect-splitt-greene-la-forte.txt](news/2025-04-27_oregonian_editorial-endorsement-elect-splitt-greene-la-forte.txt) | Oregonian editorial board endorses Splitt (Z1), Greene (Z4), La Forte (Z5), Engelsman (Z6); candidate profiles. |
| 2025-05-02 | KGW | Here's who's running for the Portland Public Schools board in the May 20 election | [2025-05-02_kgw_heres-whos-running-portland-public-schools-board.txt](news/2025-05-02_kgw_heres-whos-running-portland-public-schools-board.txt) | Candidate guide for the May 2025 PPS board races (Zones 1, 4, 5, 6) incl. endorsements by sitting board members, PAT, councilors. |
| 2025-05-12 | Axios Portland | What to know about Portland's May special election: School bond, board seats and more | [2025-05-12_axios_know-about-portlands-special-election-school-bond.txt](news/2025-05-12_axios_know-about-portlands-special-election-school-bond.txt) | All of Oregon's 36 counties have a special election next week, and Portland voters will weigh in on four school board seats and whether to renew a bond essential to renovating older schools vulnerable to earthquakes. |
| 2025-05-21 | The Oregonian/OregonLive | Portland Public Schools voters oust incumbent board member, embrace women candidates | [2025-05-21_oregonian_portland-public-schools-voters-oust-incumbent-board.txt](news/2025-05-21_oregonian_portland-public-schools-voters-oust-incumbent-board.txt) | Voters in Portland Public Schools elected four women, all with children currently in the district, to the school board on Tuesday, including one who ousted an incumbent. |
| 2025-08-01 | The Oregonian/OregonLive | Readers respond: Boost PPS enrollment with focus areas | [2025-08-01_oregonian_readers-respond-boost-pps-enrollment-focus-areas.txt](news/2025-08-01_oregonian_readers-respond-boost-pps-enrollment-focus-areas.txt) | Letter: new board should boost enrollment with focus-area programs. |
| 2025-08-27 | Willamette Week | Murmurs: Portland Public Schools Broaches Consolidation | [2025-08-27_wweek_murmurs-portland-public-schools-broaches-consolidation.txt](news/2025-08-27_wweek_murmurs-portland-public-schools-broaches-consolidation.txt) | Armstrong, on first day of school, says a top 2025-26 priority is tackling enrollment and likely consolidating schools; PAT video decries "false promises of consolidation". |
| 2025-09-02 | North Peninsula Review | RHS enrollment steady, as PPS faces downtrend - North Peninsula Review | [2025-09-02_northpeninsulareview_rhs-enrollment-steady-pps-faces-downtrend-north.txt](news/2025-09-02_northpeninsulareview_rhs-enrollment-steady-pps-faces-downtrend-north.txt) | Enrollment and accolades have soared for Roosevelt High School and its feeder schools in recent years, despite a declining number of school-age kids in the city and nationwide. |
| 2025-09-03 | The Oregonian/OregonLive | Portland parents petition to close school for gifted students amid school consolidation talks | [2025-09-03_oregonian_portland-parents-petition-close-school-gifted-students.txt](news/2025-09-03_oregonian_portland-parents-petition-close-school-gifted-students.txt) | School closures are on the horizon for Portland Public Schools, and now several dozen parents are calling for the district to begin with Access Academy, its specialized school for talented and gifted students that… |
| 2025-09-15 | The Oregonian/OregonLive | Readers respond: Access Academy contradicts PPS’ equity commitment | [2025-09-15_oregonian_readers-respond-access-academy-contradicts-pps-equity.txt](news/2025-09-15_oregonian_readers-respond-access-academy-contradicts-pps-equity.txt) | Letter: Access Academy (TAG school) contradicts PPS equity commitment amid consolidation talk. |
| 2025-09-17 | Willamette Week | Portland School Board Leaders Want to Try a New Style of Governance | [2025-09-17_wweek_portland-school-board-leaders-want-try-new.txt](news/2025-09-17_wweek_portland-school-board-leaders-want-try-new.txt) | New board leadership (Wang, DePass) wants "big-picture" governance; La Forte and Engelsman push back on unity framing. |
| 2025-10-13 | The Oregonian/OregonLive | Portland Public Schools weighs what comes first: Seismic retrofits or school consolidations? | [2025-10-13_oregonian_portland-public-schools-weighs-comes-first-seismic.txt](news/2025-10-13_oregonian_portland-public-schools-weighs-comes-first-seismic.txt) | The school district is under pressure to quickly home in on which elementary and middle schools will be prioritized for seismic retrofits through a $100 million pot of money earmarked for that purpose in the $1.8… |
| 2026-01-14 | Axios Portland | Jefferson High to absorb more students in PPS rezoning | [2026-01-14_axios_jefferson-high-absorb-more-students-pps-rezoning.txt](news/2026-01-14_axios_jefferson-high-absorb-more-students-pps-rezoning.txt) | Board-approved NE Portland high school boundary change shifts students to Jefferson (enrollment balancing precursor). |
| 2026-01-14 | The Oregonian/OregonLive | Plan to redraw Portland high school boundaries moves forward in emotional vote | [2026-01-14_oregonian_plan-redraw-portland-high-school-boundaries-moves.txt](news/2026-01-14_oregonian_plan-redraw-portland-high-school-boundaries-moves.txt) | Portland Public School Board members signed off Tuesday on a sweeping plan to revamp high school attendance zones across North and Northeast Portland, starting in fall 2027. |
| 2026-01-21 | KGW | Portland Public Schools eyes axing nearly 300 jobs to close $50 million budget shortfall | [2026-01-21_kgw_portland-public-schools-eyes-axing-nearly-300.txt](news/2026-01-21_kgw_portland-public-schools-eyes-axing-nearly-300.txt) | Portland Public Schools floated the idea of cutting nearly 300 full-time equivalent positions in an early draft on how to close a projected $50 million budget shortfall for the 2026-27 school year. |
| 2026-01-21 | The Oregonian/OregonLive | Portland Public Schools floats plan to shed nearly 300 positions to close $50M budget gap | [2026-01-21_oregonian_portland-public-schools-floats-plan-shed-nearly.txt](news/2026-01-21_oregonian_portland-public-schools-floats-plan-shed-nearly.txt) | PPS floats shedding ~300 positions to close a $50M gap; PAT blames admin growth and state funding. |
| 2026-01-24 | The Oregonian/OregonLive | Portland schools face 3rd straight year of budget cuts. What will that mean for students? | [2026-01-24_oregonian_portland-schools-face-3rd-straight-year-budget.txt](news/2026-01-24_oregonian_portland-schools-face-3rd-straight-year-budget.txt) | Parents and teachers sought answers from Portland Public Schools officials at community forums this week meant to provide an opportunity to offer feedback about the district’s preliminary proposals to cut $50 million… |
| 2026-02-05 | KPTV | Portland school district leaders warn potential $50M cuts could eliminate 300 jobs, close school | [2026-02-05_kptv_portland-school-district-leaders-warn-potential-50m.txt](news/2026-02-05_kptv_portland-school-district-leaders-warn-potential-50m.txt) | PPS leaders warn lawmakers a $50M cut could eliminate ~300 jobs and close a school; Chair Wang calls it an emergency. |
| 2026-02-18 | Willamette Week | The PPS Seismic Safety Conversation Grows Increasingly Complicated | [2026-02-18_wweek_pps-seismic-safety-conversation-grows-increasingly-complicated.txt](news/2026-02-18_wweek_pps-seismic-safety-conversation-grows-increasingly-complicated.txt) | Seismic-retrofit prioritization collides with looming closures; Chase-Miller warns past closure decisions favored affluent, white schools. |
| 2026-02-19 | The Oregonian/OregonLive | Fury over eliminating high school grade levels at one PPS school foreshadows tough conversations on districtwide closures | [2026-02-19_oregonian_fury-over-eliminating-high-school-grade-levels.txt](news/2026-02-19_oregonian_fury-over-eliminating-high-school-grade-levels.txt) | Students, parents and teachers excoriated Portland Public Schools leaders this week over the abrupt plan to eliminate the high school grade levels at Metropolitan Learning Center in Northwest Portland, a preview of… |
| 2026-02-19 | The Oregonian/OregonLive | Readers respond: Keep Metropolitan Learning Center high school open | [2026-02-19_oregonian_readers-respond-keep-metropolitan-learning-center-high.txt](news/2026-02-19_oregonian_readers-respond-keep-metropolitan-learning-center-high.txt) | Letter from an MLC parent urging PPS to keep the MLC high school open; petition >1,500 signatures. |
| 2026-02-24 | OPB | Portland Public Schools faces mid-year cuts due to just-discovered shortages | [2026-02-24_opb_portland-public-schools-faces-mid-year-cuts.txt](news/2026-02-24_opb_portland-public-schools-faces-mid-year-cuts.txt) | In a message to staff and board members sent Monday, PPS Chief Financial Officer Michelle Morrison said staff found the gap when finalizing budget projections in the current fiscal year. |
| 2026-02-24 | The Oregonian/OregonLive | Portland Public Schools discloses unexpected $10 million gap in current year’s budget | [2026-02-24_oregonian_portland-public-schools-discloses-unexpected-10-million.txt](news/2026-02-24_oregonian_portland-public-schools-discloses-unexpected-10-million.txt) | Portland Public Schools is facing an unexpected $10 million gap in its operating budget for the current school year, Chief Fiscal Officer Michelle Morrison told the district’s nearly 3,900 employees in an email this… |
| 2026-02-24 | Willamette Week | Questions Swirl as Portland Public Schools Suddenly Closes a High School for Kids Who Struggle Elsewhere | [2026-02-24_wweek_questions-swirl-portland-public-schools-suddenly-closes.txt](news/2026-02-24_wweek_questions-swirl-portland-public-schools-suddenly-closes.txt) | PPS abruptly closes MLC high school grades; families question process (preview of districtwide closure fights). |
| 2026-02-25 | Willamette Week | Portland School Board Grapples With Abrupt MLC High School Closure | [2026-02-25_wweek_portland-school-board-grapples-abrupt-mlc-high.txt](news/2026-02-25_wweek_portland-school-board-grapples-abrupt-mlc-high.txt) | Board grapples with abrupt MLC high school closure; La Forte, Engelsman, Sullivan, Chase-Miller question process; Wang, DePass back staff. |
| 2026-03-07 | The Oregonian/OregonLive | Portland students could see shortened school year as budget gap grows to $14M | [2026-03-07_oregonian_portland-students-see-shortened-school-year-budget.txt](news/2026-03-07_oregonian_portland-students-see-shortened-school-year-budget.txt) | The Portland Association of Teachers says its members have been asked to take up to four furlough days before the end of the current school year to patch a $14 million midyear budget deficit. |
| 2026-03-10 | KATU | Budget crunch forces Portland Public Schools to weigh furloughs, school closures | [2026-03-10_katu_budget-crunch-forces-portland-public-schools-weigh.txt](news/2026-03-10_katu_budget-crunch-forces-portland-public-schools-weigh.txt) | With about three months left in the school year, the district must close an unexpected $14 million budget deficit. |
| 2026-03-10 | KATU | Portland Public Schools board mulls tough decisions amid budget woes | [2026-03-10_katu_portland-public-schools-board-mulls-tough-decisions.txt](news/2026-03-10_katu_portland-public-schools-board-mulls-tough-decisions.txt) | Board discusses possible closures alongside seismic priorities; Engelsman asks when a school would be declared "staying open". |
| 2026-03-10 | KPTV | Superintendent of Portland Public Schools: 5-10 schools may be closed next year (video page) | [2026-03-10_kptv_superintendent-portland-public-schools-5-10-schools.txt](news/2026-03-10_kptv_superintendent-portland-public-schools-5-10-schools.txt) | Video: Armstrong says 5-10 schools may close next year; central-office furloughs to address deficit. |
| 2026-03-10 | KPTV | Superintendent: 5-10 Portland schools may be closed next year | [2026-03-10_kptv_superintendent-5-10-portland-schools-closed-next.txt](news/2026-03-10_kptv_superintendent-5-10-portland-schools-closed-next.txt) | The superintendent of Portland Public Schools says the district is addressing a budget deficit with temporary furloughs for central office leadership and staff. |
| 2026-03-10 | The Oregonian/OregonLive | Portland Public Schools will cut administrator jobs amid budget shortfall | [2026-03-10_oregonian_portland-public-schools-cut-administrator-jobs-amid.txt](news/2026-03-10_oregonian_portland-public-schools-cut-administrator-jobs-amid.txt) | Multiple senior-level employees who work in administrative roles for Portland Public Schools were told Monday that they will have to reapply for their jobs for the upcoming school year — and that there will not be… |
| 2026-03-10 | Willamette Week | PPS Plans to Close Several Schools by Fall 2027 | [2026-03-10_wweek_pps-plans-close-several-schools-fall-2027.txt](news/2026-03-10_wweek_pps-plans-close-several-schools-fall-2027.txt) | Armstrong: PPS could close 5-10 of its 74 elementary/K-8/middle/alternative schools by fall 2027; recommendation due late fall 2026. |
| 2026-03-12 | The Oregonian/OregonLive | Which Portland schools could close in 2027? PPS board launches districtwide review | [2026-03-12_oregonian_which-portland-schools-close-2027-pps-board.txt](news/2026-03-12_oregonian_which-portland-schools-close-2027-pps-board.txt) | Portland school board members unanimously agreed this week to launch a nine-month review to identify underenrolled schools within the district that should be closed. |
| 2026-03-13 | KPTV | ‘I’m worried’: Parents, teachers voice concerns over possible school closures within PPS | [2026-03-13_kptv_im-worried-parents-teachers-voice-concerns-over.txt](news/2026-03-13_kptv_im-worried-parents-teachers-voice-concerns-over.txt) | Portlanders showed up at a Portland Public Schools committee meeting Thursday to voice their concerns about the tough decisions the district is making to address its budget deficit. |
| 2026-03-13 | OPB | Portland Public Schools now facing even steeper cuts with deeper budget hole | [2026-03-13_opb_portland-public-schools-now-facing-even-steeper.txt](news/2026-03-13_opb_portland-public-schools-now-facing-even-steeper.txt) | OPB interview: Armstrong says 5-10 of 74 schools may close by fall 2027; budget hole deepens; PAT criticizes admin staffing. |
| 2026-03-13 | OPB | Portland Public Schools superintendent defends approach to budget as teachers union calls for ‘systemic change’ | [2026-03-13_opb_portland-public-schools-superintendent-defends-approach-budget.txt](news/2026-03-13_opb_portland-public-schools-superintendent-defends-approach-budget.txt) | Armstrong defends budget approach as PAT blames administrators and calls for systemic change. |
| 2026-03-18 | Willamette Week | Here’s What PPS Will Consider as It Selects Schools to Close | [2026-03-18_wweek_heres-pps-consider-selects-schools-close.txt](news/2026-03-18_wweek_heres-pps-consider-selects-schools-close.txt) | On March 10, Portland Public Schools officially kicked off one of the most emotionally fraught conversations a district can have: deciding which schools to close. |
| 2026-03-21 | KGW | Portland school year set to be 3 days shorter as school district faces $14 million budget shortfall | [2026-03-21_kgw_portland-school-year-set-3-days-shorter.txt](news/2026-03-21_kgw_portland-school-year-set-3-days-shorter.txt) | This school year for Portland Public Schools will likely be three days shorter as the district attempts to plug a $14 million budget shortfall. |
| 2026-03-22 | The Oregonian/OregonLive | Readers respond: PPS erodes trust by dismissing public’s concerns | [2026-03-22_oregonian_readers-respond-pps-erodes-trust-dismissing-publics.txt](news/2026-03-22_oregonian_readers-respond-pps-erodes-trust-dismissing-publics.txt) | Letter: PPS erodes trust by dismissing public concerns (MLC/budget context). |
| 2026-03-25 | Axios Portland | Portland avoids layoffs with four teacher furlough days | [2026-03-25_axios_portland-avoids-layoffs-four-teacher-furlough-days.txt](news/2026-03-25_axios_portland-avoids-layoffs-four-teacher-furlough-days.txt) | Portland Public Schools will trim four days from teachers' schedules this school year as part of a deal that avoids layoffs while helping to close a $14 million budget gap. |
| 2026-04-01 | Willamette Week | PPS Deems Midyear Budget Hole Closed as School Board Approves Furloughs for Four Unions | [2026-04-01_wweek_pps-deems-midyear-budget-hole-closed-school.txt](news/2026-04-01_wweek_pps-deems-midyear-budget-hole-closed-school.txt) | The Portland School Board voted Tuesday night to approve furlough days for four of Portland Public Schools’ labor partners. |
| 2026-04-09 | The Oregonian/OregonLive | Portland Public Schools budget cuts: See which schools lose the most staff | [2026-04-09_oregonian_portland-public-schools-budget-cuts-see-which.txt](news/2026-04-09_oregonian_portland-public-schools-budget-cuts-see-which.txt) | High schools will bear the brunt of some $50 million in budget cuts planned for Portland Public Schools next year, according to new school-by-school breakdowns of staffing allocations provided to The… |
| 2026-04-13 | The Oregonian/OregonLive | PPS families question plan to close 5-10 schools | [2026-04-13_oregonian_pps-families-question-plan-close-5-10.txt](news/2026-04-13_oregonian_pps-families-question-plan-close-5-10.txt) | For the seven members of the Portland school board, the plan to close between five and 10 schools districtwide in the next 18 months is virtually a foregone conclusion. |
| 2026-04-14 | KATU | Community voices concern over Portland Public Schools 'rightsizing' | [2026-04-14_katu_community-voices-concern-over-portland-public-schools.txt](news/2026-04-14_katu_community-voices-concern-over-portland-public-schools.txt) | Portland Public Schools is beginning what leaders call a “rightsizing” process that could eventually change how some school buildings are used across the district. |
| 2026-04-14 | KOIN | PPS to vote on resizing the district | [2026-04-14_koin_pps-vote-resizing-district.txt](news/2026-04-14_koin_pps-vote-resizing-district.txt) | Portland Public School leaders are voting on Tuesday on a resolution that could close five to ten schools in 2027. |
| 2026-04-15 | Citizen Portal (AI meeting summaries) | Portland board authorizes districtwide ‘rightsizing’ process after fierce public comment (partial: login wall) | [2026-04-15_citizenportal_portland-board-authorizes-districtwide-rightsizing-process-after.txt](news/2026-04-15_citizenportal_portland-board-authorizes-districtwide-rightsizing-process-after.txt) | The Portland Public Schools board voted 5–2 on April 14 to adopt Resolution 7296 directing the superintendent to begin a districtwide rightsizing process that may include program consolidations, closures or boundary… |
| 2026-04-15 | Citizen Portal (AI meeting summaries) | Votes at a glance: PPS board passes rightsizing resolution, calendar and contracting rule changes (partial: login wall) | [2026-04-15_citizenportal_votes-glance-pps-board-passes-rightsizing-resolution.txt](news/2026-04-15_citizenportal_votes-glance-pps-board-passes-rightsizing-resolution.txt) | Votes at a glance: PPS board passes rightsizing resolution, calendar and contracting rule changes |
| 2026-04-15 | Willamette Week | PPS Introduces Another Metric to Inform School Closures | [2026-04-15_wweek_pps-introduces-another-metric-inform-school-closures.txt](news/2026-04-15_wweek_pps-introduces-another-metric-inform-school-closures.txt) | Portland Public Schools began its community engagement process on school closures with an April 11 forum at Kellogg Middle School. |
| 2026-04-17 | KATU | Parents push back on PPS plan to close neighborhood schools at packed listening session | [2026-04-17_katu_parents-push-back-pps-plan-close-neighborhood.txt](news/2026-04-17_katu_parents-push-back-pps-plan-close-neighborhood.txt) | Next week, Portland Public Schools (PPS) will hear from families about its plan to close between five and 10 schools. |
| 2026-04-17 | KGW | PPS parents at Title I schools create coalition to keep schools open | [2026-04-17_kgw_pps-parents-title-i-schools-create-coalition.txt](news/2026-04-17_kgw_pps-parents-title-i-schools-create-coalition.txt) | Across the Pacific Northwest school districts are dealing with budget cuts and falling enrollment. |
| 2026-04-20 | KPTV | Portland Public Schools seeks community input on proposed school closures | [2026-04-20_kptv_portland-public-schools-seeks-community-input-proposed.txt](news/2026-04-20_kptv_portland-public-schools-seeks-community-input-proposed.txt) | Portland Public Schools is asking for community input ahead of a proposed plan to consolidate and close several schools. |
| 2026-04-20 | The Oregonian/OregonLive | Readers respond: Build a school district that families choose | [2026-04-20_oregonian_readers-respond-build-school-district-families-choose.txt](news/2026-04-20_oregonian_readers-respond-build-school-district-families-choose.txt) | Letter: PPS should build a district families choose rather than only cutting. |
| 2026-04-22 | KATU | PPS starts district ‘rightsizing’ amid budget gap, declining enrollment, aging buildings | [2026-04-22_katu_pps-starts-district-rightsizing-amid-budget-gap.txt](news/2026-04-22_katu_pps-starts-district-rightsizing-amid-budget-gap.txt) | The Portland Public Schools Board is hearing from families and staff as it looks to reorganize the district amid a multi-million dollar budget deficit and declining enrollment. |
| 2026-04-22 | Portland Mercury | With Portland Public Schools’ Budget in Peril, All Eyes Are on State Leaders - Portland Mercury | [2026-04-22_mercury_portland-public-schools-budget-peril-all-eyes.txt](news/2026-04-22_mercury_portland-public-schools-budget-peril-all-eyes.txt) | PPS budget crisis: parents and PAT look to Gov. Kotek/Legislature and the Education Stability Fund; Kotek office declines. |
| 2026-04-22 | Willamette Week | What PPS Loses if It Closes a Title I School | [2026-04-22_wweek_pps-loses-if-closes-title-i-school.txt](news/2026-04-22_wweek_pps-loses-if-closes-title-i-school.txt) | What closing a Title I school costs a neighborhood; parent coalition of Title I schools forms; Chase-Miller on resource risks. |
| 2026-04-23 | KPTV | Portland parents air concerns to board over potential school closures | [2026-04-23_kptv_portland-parents-air-concerns-board-over-potential.txt](news/2026-04-23_kptv_portland-parents-air-concerns-board-over-potential.txt) | Parents air concerns at a board community session about potential closures. |
| 2026-04-23 | OPB | Portland Public Schools wants to know: What should be considered when closing schools? | [2026-04-23_opb_portland-public-schools-wants-know-should-considered.txt](news/2026-04-23_opb_portland-public-schools-wants-know-should-considered.txt) | At an engagement session PPS asks what to weigh when closing schools (up to ~12 of 81); Wang describes "properly resourced" goal. |
| 2026-04-26 | Citizen Portal (AI meeting summaries) | Portland Public Schools holds rightsizing listening session as district faces enrollment decline and $50 million shortfall (partial: login wall) | [2026-04-26_citizenportal_portland-public-schools-holds-rightsizing-listening-session.txt](news/2026-04-26_citizenportal_portland-public-schools-holds-rightsizing-listening-session.txt) | Portland Public Schools holds rightsizing listening session as district faces enrollment decline and $50 million shortfall |
| 2026-04-27 | KATU | PPS holds final community meeting as it considers 'right-sizing,' school closures | [2026-04-27_katu_pps-holds-final-community-meeting-considers-right.txt](news/2026-04-27_katu_pps-holds-final-community-meeting-considers-right.txt) | Portland Public Schools families can gather to ask questions and voice concerns about the district's pending "right-sizing," which could include closing up to a dozen elementary and middle schools. |
| 2026-04-28 | KATU | Today on ARC PDX / April 28, 2026 / Portland Public Schools continue 'right-sizing' talks | [2026-04-28_katu_today-arc-pdx-april-28-2026-portland.txt](news/2026-04-28_katu_today-arc-pdx-april-28-2026-portland.txt) | KATU morning rundown; item on PPS continuing "right-sizing" talks. |
| 2026-04-29 | Axios Portland | Portland schools brace for cuts amid $56M deficit | [2026-04-29_axios_portland-schools-brace-cuts-amid-56m-deficit.txt](news/2026-04-29_axios_portland-schools-brace-cuts-amid-56m-deficit.txt) | State of play: Superintendent Kimberlee Armstrong presented her $2.7 billion budget proposal for the 2026-27 school year to the school board this week. |
| 2026-04-29 | KGW | Portland Public Schools leaders propose more than $50 million in budget cuts | [2026-04-29_kgw_portland-public-schools-leaders-propose-more-than.txt](news/2026-04-29_kgw_portland-public-schools-leaders-propose-more-than.txt) | Portland Public Schools is facing down a looming $56 million budget gap, and officials say that the cuts they have to make will be "devastating" to the district. |
| 2026-04-29 | OPB | Another year of cuts: Portland Public Schools presents $2.77 billion budget | [2026-04-29_opb_another-year-cuts-portland-public-schools-presents.txt](news/2026-04-29_opb_another-year-cuts-portland-public-schools-presents.txt) | Deep cuts to schools, central office services and specialized programs were among the features of Portland Public Schools’ $2.77 billion budget for the 2026-27 school year, presented by Superintendent Kimberlee… |
| 2026-04-30 | KPTV | Portland Public Schools now to cut over 300 jobs next year and may close schools | [2026-04-30_kptv_portland-public-schools-now-cut-over-300.txt](news/2026-04-30_kptv_portland-public-schools-now-cut-over-300.txt) | The Portland Public Schools superintendent said on Wednesday that the district is considering cutting more than 300 jobs next year as major budget deficits continue. |
| 2026-05-01 | North Peninsula Review | Portland Public School closures? Not so fast - North Peninsula Review | [2026-05-01_northpeninsulareview_portland-public-school-closures-not-so-fast.txt](news/2026-05-01_northpeninsulareview_portland-public-school-closures-not-so-fast.txt) | Guest column questioning whether closing ~10 elementary schools would actually save money. |
| 2026-05-13 | The Oregonian/OregonLive | Community panel warns that baked-in assumptions in PPS budget may worsen its deficit | [2026-05-13_oregonian_community-panel-warns-baked-assumptions-pps-budget.txt](news/2026-05-13_oregonian_community-panel-warns-baked-assumptions-pps-budget.txt) | Community budget review committee warns PPS budget assumptions may worsen its deficit. |
| 2026-05-17 | The Oregonian/OregonLive | Readers respond: A better PPS budget strategy | [2026-05-17_oregonian_readers-respond-better-pps-budget-strategy.txt](news/2026-05-17_oregonian_readers-respond-better-pps-budget-strategy.txt) | Letter: PPS should not spend billions renovating high schools as child population dwindles. |
| 2026-05-26 | Citizen Portal (AI meeting summaries) | Board adopts guiding principles for 'right‑sizing' process; public engagement and equity lens prioritized (partial: login wall) | [2026-05-26_citizenportal_board-adopts-guiding-principles-right-sizing-process.txt](news/2026-05-26_citizenportal_board-adopts-guiding-principles-right-sizing-process.txt) | Board adopts guiding principles for 'right‑sizing' process; public engagement and equity lens prioritized |
| 2026-05-26 | Citizen Portal (AI meeting summaries) | Portland board adopts guiding principles for 'right‑sizing' schools, launches public scenario process (partial: login wall) | [2026-05-26_citizenportal_portland-board-adopts-guiding-principles-right-sizing.txt](news/2026-05-26_citizenportal_portland-board-adopts-guiding-principles-right-sizing.txt) | Portland board adopts guiding principles for 'right‑sizing' schools, launches public scenario process |
| 2026-05-27 | Willamette Week | Equity and Resource Distribution Top of Mind as Portland School Board Tackles School Closures | [2026-05-27_wweek_equity-resource-distribution-top-mind-portland-school.txt](news/2026-05-27_wweek_equity-resource-distribution-top-mind-portland-school.txt) | The Portland School Board voted unanimously Tuesday night to adopt a resolution that outlines the clearest guiding principles and work plan yet for Portland Public Schools’ school closure process. |
| 2026-06-09 | OPB | As Portland teachers receive layoff notices, union raises objections | [2026-06-09_opb_portland-teachers-receive-layoff-notices-union-raises.txt](news/2026-06-09_opb_portland-teachers-receive-layoff-notices-union-raises.txt) | As more than 40,000 Portland Public Schools students head into summer break, a number of their teachers are getting layoff notices. |
| 2026-06-10 | KGW | PPS employees push back against possible layoffs at Portland school board meeting | [2026-06-10_kgw_pps-employees-push-back-against-possible-layoffs.txt](news/2026-06-10_kgw_pps-employees-push-back-against-possible-layoffs.txt) | Employees and union leaders voiced concerns about layoffs and staffing reductions during a Portland Public Schools board meeting Tuesday night, warning that the cuts could worsen existing challenges across the district. |
| 2026-06-18 | OPB | OPB’s First Look: The small school downtown | [2026-06-18_opb_opbs-first-look-small-school-downtown.txt](news/2026-06-18_opb_opbs-first-look-small-school-downtown.txt) | OPB newsletter: profile of MLC, the district's only K-12 school, after its high school grades were cut. |
| 2026-06-23 | KATU | PPS considers last-second measure to restore cut positions | [2026-06-23_katu_pps-considers-last-second-measure-restore-cut.txt](news/2026-06-23_katu_pps-considers-last-second-measure-restore-cut.txt) | The board of Portland Public Schools is set to approve its 2026-2027 budget at its meeting on Tuesday night, ahead of the start of the fiscal year on July 1. |
| 2026-06-24 | KOIN | Portland Public Schools board adopts new budget with 320 layoffs | [2026-06-24_koin_portland-public-schools-board-adopts-new-budget.txt](news/2026-06-24_koin_portland-public-schools-board-adopts-new-budget.txt) | Portland Public Schools has adopted a new budget for its upcoming school year, and layoffs are underway for hundreds of staff positions. |
| 2026-06-24 | KPTV | Portland Public Schools adopts budget for 2026-27 school year after months of debate | [2026-06-24_kptv_portland-public-schools-adopts-budget-2026-27.txt](news/2026-06-24_kptv_portland-public-schools-adopts-budget-2026-27.txt) | Oregon’s largest school district has adopted a budget for the 2026-27 school year after months of debate over a $50 million shortfall. |
| 2026-06-24 | The Oregonian/OregonLive | As enrollment falls, mixed grades become new normal at Portland elementary schools | [2026-06-24_oregonian_enrollment-falls-mixed-grades-become-new-normal.txt](news/2026-06-24_oregonian_enrollment-falls-mixed-grades-become-new-normal.txt) | Blended/multi-grade classrooms spread as enrollment falls at Portland elementary schools. |
| 2026-06-24 | The Oregonian/OregonLive | At Portland Public Schools, a joyless march to a final budget no one much likes | [2026-06-24_oregonian_portland-public-schools-joyless-march-final-budget.txt](news/2026-06-24_oregonian_portland-public-schools-joyless-march-final-budget.txt) | The seven members of the Portland Public Schools board tried desperately to avoid signing off on a months-in-the-making $1.09 billion operating budget for the upcoming school year, before reluctantly casting their… |
| 2026-06-25 | OPB | Portland Public Schools board passes painful $2.77 billion budget | [2026-06-25_opb_portland-public-schools-board-passes-painful-2.txt](news/2026-06-25_opb_portland-public-schools-board-passes-painful-2.txt) | Board passes $2.77B 2026-27 budget after midnight; Engelsman abstains; failed amendments to restore $13.1M of positions. |
| 2026-06-28 | The Oregonian/OregonLive | Editorial: Portland Public Schools’ narrow escape from budget myopia | [2026-06-28_oregonian_editorial-portland-public-schools-narrow-escape-budget.txt](news/2026-06-28_oregonian_editorial-portland-public-schools-narrow-escape-budget.txt) | Editorial: board was right to reject last-minute amendments (Engelsman, Chase-Miller, La Forte) to restore $13M via reserves. |
| 2026-06-30 | Willamette Week | A Tense PPS Budget Approval Has Divided the District—and Could Alter the School Board | [2026-06-30_wweek_tense-pps-budget-approval-has-divided-district.txt](news/2026-06-30_wweek_tense-pps-budget-approval-has-divided-district.txt) | Analysis: 6-1 rejection of Engelsman's $13.2M amendment splits board from PAT, which eyes 2027 board races. |
| 2026-07-08 | Axios Portland | Portland's shrinking child population could reshape its economy | [2026-07-08_axios_portlands-shrinking-child-population-reshape-economy.txt](news/2026-07-08_axios_portlands-shrinking-child-population-reshape-economy.txt) | Census data: Western under-18 population fell 5.7% 2020-25; implications for Portland schools. |
| 2026-07-31 | Willamette Week | Ahead of PPS School Consolidations, a Report Offers Lessons From Its Most Recent Enrollment Balancing Attempt | [2026-07-31_wweek_ahead-pps-school-consolidations-report-offers-lessons.txt](news/2026-07-31_wweek_ahead-pps-school-consolidations-report-offers-lessons.txt) | PPS-commissioned 150-page evaluation of the Southeast Guiding Coalition rebalancing offers lessons ahead of closures. |
| 2026-08-26 | KATU | Up to 20 Portland schools could face consolidation or closure due to growing budget crunch | [2026-08-26_katu_20-portland-schools-face-consolidation-or-closure.txt](news/2026-08-26_katu_20-portland-schools-face-consolidation-or-closure.txt) | Portland Public Schools (PPS) leaders kicked off the new school year at Rosa Parks Elementary School on Wednesday while warning that another difficult budget season could bring additional layoffs, school closures and… |
| 2026-08-26 | KGW | Portland Public Schools superintendent says up to 20 schools could face closure: 'This year will be even harder' | [2026-08-26_kgw_portland-public-schools-superintendent-says-20-schools.txt](news/2026-08-26_kgw_portland-public-schools-superintendent-says-20-schools.txt) | Amid all the excitement of back to school this week, a sort of "budgetary black cloud" hangs over Portland Public Schools. |
| 2026-08-26 | The Oregonian/OregonLive | As Portland Public Schools weighs sweeping closures, parents wonder which schools will be left standing | [2026-08-26_oregonian_portland-public-schools-weighs-sweeping-closures-parents.txt](news/2026-08-26_oregonian_portland-public-schools-weighs-sweeping-closures-parents.txt) | As PPS weighs sweeping closures, parents at small schools wonder which will survive; unanswered questions on layoffs and savings. |
| 2026-08-26 | Willamette Week | PPS Superintendent Says District Could Close Up to 20 Schools | [2026-08-26_wweek_pps-superintendent-says-district-close-20-schools.txt](news/2026-08-26_wweek_pps-superintendent-says-district-close-20-schools.txt) | Armstrong says closures could total 10-20 schools (up from 5-10); draft list to board in November. |
| 2026-08-27 | KATU | Portland Association of Teachers president fears more cuts could strain classrooms | [2026-08-27_katu_portland-association-teachers-president-fears-more-cuts.txt](news/2026-08-27_katu_portland-association-teachers-president-fears-more-cuts.txt) | Alisha Chavez, president of the Portland Association of Teachers (PAT), said she learned on the first day of school that Portland Public Schools may need to make further cuts. |
| 2026-08-27 | Portland Mercury | Good Morning, News: Iconic Actor and Most Flamboyant Man Tim Curry Has Died, Make Every Factory Juantonio’s, and PPS Weighs School Downsizing - Portland Mercury | [2026-08-27_mercury_good-morning-news-iconic-actor-most-flamboyant.txt](news/2026-08-27_mercury_good-morning-news-iconic-actor-most-flamboyant.txt) | Mercury morning roundup; item: PPS weighs school downsizing of up to 20 schools. |
| 2026-08-27 | The Oregonian/OregonLive | Which Portland Public Schools buildings could be candidates for closure? Early clues are emerging | [2026-08-27_oregonian_which-portland-public-schools-buildings-candidates-closure.txt](news/2026-08-27_oregonian_which-portland-public-schools-buildings-candidates-closure.txt) | Early clues on which buildings could be closure candidates; board principles say no corner of the district is off-limits. |
| 2026-08-28 | Willamette Week | PPS Model Shows District Must Close 15 Elementary Schools to Reach Robust Enrollment Thresholds | [2026-08-28_wweek_pps-model-shows-district-must-close-15.txt](news/2026-08-28_wweek_pps-model-shows-district-must-close-15.txt) | District model: closing 15 of 45 elementaries would put all remaining at the 360-student QEM threshold by 2031-32. |
| 2026-08-30 | The Oregonian/OregonLive | Editorial: PPS enters the minefield of school closings | [2026-08-30_oregonian_editorial-pps-enters-minefield-school-closings.txt](news/2026-08-30_oregonian_editorial-pps-enters-minefield-school-closings.txt) | Editorial: closures are unavoidable but perilous; urges a careful, transparent process and constructive role for officials; notes PAT petition. |
| 2026-08-31 | KATU | Portland Public Schools to discuss closing 15 elementary schools Tuesday | [2026-08-31_katu_portland-public-schools-discuss-closing-15-elementary.txt](news/2026-08-31_katu_portland-public-schools-discuss-closing-15-elementary.txt) | Portland Public Schools officials are set to present a series of charts to the Portland School Board that lay out, in stark terms, why Superintendent Armstrong recently raised her estimate of how many schools the… |
| 2026-09-01 | KATU | Portland Public Schools board has 'sobering' conversation about school closure priorities | [2026-09-01_katu_portland-public-schools-board-has-sobering-conversation.txt](news/2026-09-01_katu_portland-public-schools-board-has-sobering-conversation.txt) | Superintendent Kimberlee Armstrong opened up Tuesday night's conversation about Rightsizing, the district's plan to close or consolidate schools to adjust for drops in enrollment that are projected to continue for… |
| 2026-09-01 | KATU | Portland Public Schools board to discuss 15 potential elementary school closures | [2026-09-01_katu_portland-public-schools-board-discuss-15-potential.txt](news/2026-09-01_katu_portland-public-schools-board-discuss-15-potential.txt) | The Portland Public Schools Board is set to discuss the potential closure of 15 elementary schools Tuesday night as Oregon’s largest school district considers major cuts amid declining enrollment. |
| 2026-09-01 | KATU | Today on ARC PDX / September 1, 2026 / Portland Public Schools could close 15 schools | [2026-09-01_katu_today-arc-pdx-september-1-2026-portland.txt](news/2026-09-01_katu_today-arc-pdx-september-1-2026-portland.txt) | KATU morning rundown; item on PPS possibly closing 15 schools. |
| 2026-09-01 | KGW | PPS could close up to 20 schools in controversial 'rightsizing' plan | [2026-09-01_kgw_pps-close-20-schools-controversial-rightsizing-plan.txt](news/2026-09-01_kgw_pps-close-20-schools-controversial-rightsizing-plan.txt) | Preview of Sept. 1 board meeting on rightsizing that could close up to 20 schools. |
| 2026-09-01 | North Peninsula Review | PPS Superintendent joins students on first day at Rosa Parks Elementary School - North Peninsula Review | [2026-09-01_northpeninsulareview_pps-superintendent-joins-students-first-day-rosa.txt](news/2026-09-01_northpeninsulareview_pps-superintendent-joins-students-first-day-rosa.txt) | Armstrong opens the school year at Rosa Parks Elementary; DePass and Chase-Miller attend. |
| 2026-09-01 | The Oregonian/OregonLive | Portland Public Schools weighs raise for its superintendent as it faces budget cuts, school closures | [2026-09-01_oregonian_portland-public-schools-weighs-raise-superintendent-faces.txt](news/2026-09-01_oregonian_portland-public-schools-weighs-raise-superintendent-faces.txt) | Portland Public School board members will consider giving Superintendent Kimberlee Armstrong a raise and three-year contract extension during a Tuesday evening meeting at Grant High School. |
| 2026-09-01 | Willamette Week | Portland School Board Will Weigh Contract Extension for Its Superintendent That Includes a Raise | [2026-09-01_wweek_portland-school-board-weigh-contract-extension-superintendent.txt](news/2026-09-01_wweek_portland-school-board-weigh-contract-extension-superintendent.txt) | The Portland School Board on Tuesday night will consider a contract extension with its superintendent. |
| 2026-09-02 | Citizen Portal (AI meeting summaries) | Board approves superintendent contract extension 5-2 after contentious public comment (partial: login wall) | [2026-09-02_citizenportal_board-approves-superintendent-contract-extension-5-2.txt](news/2026-09-02_citizenportal_board-approves-superintendent-contract-extension-5-2.txt) | The board approved resolution 7371 authorizing a multi-year extension of Superintendent Armstrong's contract by a 5-2 vote after extended public comment and debate about timing, retention, and pay amid budget cuts… |
| 2026-09-02 | Citizen Portal (AI meeting summaries) | Board asks how facilities and deferred maintenance will factor into rightsizing; staff point to operations workgroups (partial: login wall) | [2026-09-02_citizenportal_board-asks-how-facilities-deferred-maintenance-factor.txt](news/2026-09-02_citizenportal_board-asks-how-facilities-deferred-maintenance-factor.txt) | Board asks how facilities and deferred maintenance will factor into rightsizing; staff point to operations workgroups |
| 2026-09-02 | Citizen Portal (AI meeting summaries) | Board presses staff on layoffs, split staffing and arts positions; staff say rightsizing aims for more stable staffing (partial: login wall) | [2026-09-02_citizenportal_board-presses-staff-layoffs-split-staffing-arts.txt](news/2026-09-02_citizenportal_board-presses-staff-layoffs-split-staffing-arts.txt) | Board presses staff on layoffs, split staffing and arts positions; staff say rightsizing aims for more stable staffing |
| 2026-09-02 | Citizen Portal (AI meeting summaries) | District staff lay out 'well‑resourced' school framework as rightsizing begins (partial: login wall) | [2026-09-02_citizenportal_district-staff-lay-out-well-resourced-school.txt](news/2026-09-02_citizenportal_district-staff-lay-out-well-resourced-school.txt) | District staff told the Board's Teaching, Learning & Enrollment committee that declining enrollment—more than 6,000 students since 2018–19 and another projected 3,400 by 2031–32—has stretched resources and that a… |
| 2026-09-02 | Citizen Portal (AI meeting summaries) | Portland school board agrees to develop multiple "rightsizing" scenarios after heated debate (partial: login wall) | [2026-09-02_citizenportal_portland-school-board-agrees-develop-multiple-rightsizing.txt](news/2026-09-02_citizenportal_portland-school-board-agrees-develop-multiple-rightsizing.txt) | Portland school board agrees to develop multiple "rightsizing" scenarios after heated debate |
| 2026-09-02 | KATU | Today on ARC PDX / September 2, 2026 / Portland Public Schools 'sobering conversation' | [2026-09-02_katu_today-arc-pdx-september-2-2026-portland.txt](news/2026-09-02_katu_today-arc-pdx-september-2-2026-portland.txt) | KATU morning rundown; item on board's "sobering conversation" about closures. |
| 2026-09-02 | KGW | 'Absolutely shocking': Portland Public Schools parents react to plan to close up to 18 schools | [2026-09-02_kgw_absolutely-shocking-portland-public-schools-parents-react.txt](news/2026-09-02_kgw_absolutely-shocking-portland-public-schools-parents-react.txt) | Portland Public Schools is weighing the closure of 15 elementary schools and three middle schools as district leaders confront declining enrollment and a projected $50 million budget shortfall. |
| 2026-09-02 | KPTV | Portland Public Schools board weighs plan to close up to 20 schools | [2026-09-02_kptv_portland-public-schools-board-weighs-plan-close.txt](news/2026-09-02_kptv_portland-public-schools-board-weighs-plan-close.txt) | As Portland Public Schools faces a major budget deficit, the board weighed closing up to 20 schools in the district on Tuesday. |
| 2026-09-02 | OPB | Portland Public Schools says ‘rightsizing’ plan to close schools aims to standardize educational experience across the district | [2026-09-02_opb_portland-public-schools-says-rightsizing-plan-close.txt](news/2026-09-02_opb_portland-public-schools-says-rightsizing-plan-close.txt) | Oregon’s largest school district has lost 6,086 students since 2018. |
| 2026-09-02 | The Oregonian/OregonLive | Portland Public Schools board approves raise, contract extension for its superintendent | [2026-09-02_oregonian_portland-public-schools-board-approves-raise-contract.txt](news/2026-09-02_oregonian_portland-public-schools-board-approves-raise-contract.txt) | Portland Public Schools board members voted 5-2 in favor of giving Superintendent Kimberlee Armstrong a raise and three-year contract extension during a Tuesday evening meeting at Grant High School. |
| 2026-09-02 | The Oregonian/OregonLive | Portland school board backs planning for up to 20 school closures | [2026-09-02_oregonian_portland-school-board-backs-planning-20-school.txt](news/2026-09-02_oregonian_portland-school-board-backs-planning-20-school.txt) | Five of the seven Portland Public Schools board members directed the district Tuesday night to continue working on scenarios that could close up to 20 schools. |
| 2026-09-02 | Willamette Week | Portland School Board Approves Contract Extension for Its Superintendent | [2026-09-02_wweek_portland-school-board-approves-contract-extension-superintendent.txt](news/2026-09-02_wweek_portland-school-board-approves-contract-extension-superintendent.txt) | Board approves Armstrong contract extension 5-2 (La Forte, Engelsman no); Wang and Splitt explain timing. |
| 2026-09-03 | K-12 Dive | Portland Public Schools ponders up to 18 school closures | [2026-09-03_k12dive_portland-public-schools-ponders-18-school-closures.txt](news/2026-09-03_k12dive_portland-public-schools-ponders-18-school-closures.txt) | K-12 Dive: PPS presentation says 15 elementary and 3 middle schools would need to close for sustainable enrollment. |
| 2026-09-03 | KPTV | Portland school board approves pay raise for superintendent amid closure talks | [2026-09-03_kptv_portland-school-board-approves-pay-raise-superintendent.txt](news/2026-09-03_kptv_portland-school-board-approves-pay-raise-superintendent.txt) | Board approves superintendent pay raise/extension amid closure talks; Councilor Koyama Lane objects. |
| 2026-09-03 | Willamette Week | Here’s Where Every PPS Board Member Stands on School Closures | [2026-09-03_wweek_heres-where-every-pps-board-member-stands.txt](news/2026-09-03_wweek_heres-where-every-pps-board-member-stands.txt) | Rundown of where each of the seven directors stood on closures after the Sept. 1 meeting. |
| 2026-09-09 | Willamette Week | To Close Schools, Portland Public Schools Must Overcome Fierce Pushback From the Teachers Union | [2026-09-09_wweek_close-schools-portland-public-schools-must-overcome.txt](news/2026-09-09_wweek_close-schools-portland-public-schools-must-overcome.txt) | PAT, furious over the superintendent contract and closures, signals it will fight consolidation and remember votes at bargaining. |
| 2026-09-11 | KATU | Oregon Public Schools are getting smaller and more school closures could follow | [2026-09-11_katu_oregon-public-schools-getting-smaller-more-school.txt](news/2026-09-11_katu_oregon-public-schools-getting-smaller-more-school.txt) | Statewide enrollment fell 9,000+ in 2025-26; more Oregon school closures likely. |
| 2026-09-14 | The Oregonian/OregonLive | Readers respond: False justification for closing schools | [2026-09-14_oregonian_readers-respond-false-justification-closing-schools.txt](news/2026-09-14_oregonian_readers-respond-false-justification-closing-schools.txt) | Letter: the 360/500 enrollment thresholds are a false justification for closing 15-20 schools. |
| 2026-09-16 | Willamette Week | Murmurs: Fancy Mental Health Care Tracker Underwhelms Key Lawmaker | [2026-09-16_wweek_murmurs-fancy-mental-health-care-tracker-underwhelms.txt](news/2026-09-16_wweek_murmurs-fancy-mental-health-care-tracker-underwhelms.txt) | Murmurs item: PPS data shows Title I schools disproportionately underenrolled; Title I parent coalition responds. |
| 2026-09-16 | Willamette Week | What Will Happen to the School Buildings the District Closes? | [2026-09-16_wweek_happen-school-buildings-district-closes.txt](news/2026-09-16_wweek_happen-school-buildings-district-closes.txt) | What happens to closed buildings: leasing, sale, housing ideas; Chase-Miller floats Austin-style housing conversions. |
| 2026-09-17 | Citizen Portal (AI meeting summaries) | Board puts rightsizing, facilities and community engagement on the evaluation calendar (partial: login wall) | [2026-09-17_citizenportal_board-puts-rightsizing-facilities-community-engagement-evaluation.txt](news/2026-09-17_citizenportal_board-puts-rightsizing-facilities-community-engagement-evaluation.txt) | Board sets rightsizing, facilities and community engagement as annual focus areas (Citizen Portal AI summary; partial). |
| 2026-09-17 | Willamette Week | Former School Board Member Files Petition to Recall PPS Board Chair | [2026-09-17_wweek_former-school-board-member-files-petition-recall.txt](news/2026-09-17_wweek_former-school-board-member-files-petition-recall.txt) | On Tuesday, former School Board member Mike Rosen, a school advocate who held the Zone 7 seat from 2015 to 2019, filed a prospective recall petition with the Multnomah County Elections Division, seeking to remove… |
| 2026-09-18 | KATU | Leaked copy of damning audit prompts effort to recall PPS board president | [2026-09-18_katu_leaked-copy-damning-audit-prompts-effort-recall.txt](news/2026-09-18_katu_leaked-copy-damning-audit-prompts-effort-recall.txt) | A leaked draft of a damning independent audit into a Texas contractor hired to oversee over a billion dollars’ worth of construction for Portland Public Schools has prompted an effort to recall Board Chair Eddie Wang. |
| 2026-09-19 | Willamette Week | PPS Finds Title I Schools Underenrolled Compared to Peers | [2026-09-19_wweek_pps-finds-title-i-schools-underenrolled-compared.txt](news/2026-09-19_wweek_pps-finds-title-i-schools-underenrolled-compared.txt) | As the Portland School Board considers closing as many as 20 elementary, K-8 and middle schools, each of its seven members has asked Portland Public Schools to consider various factors as it determines which… |
| 2026-09-20 | KOIN | ‘Big upheaval’: PPS families, leaders hold discussions as dozens of schools may close | [2026-09-20_koin_big-upheaval-pps-families-leaders-hold-discussions.txt](news/2026-09-20_koin_big-upheaval-pps-families-leaders-hold-discussions.txt) | KOIN: families and leaders discuss the "big upheaval" as dozens of PPS schools may close. |
| 2026-09-21 | The Oregonian/OregonLive | In 2 weeks, Portland Public Schools will unveil school closure scenarios. Some parents are already taking sides | [2026-09-21_oregonian_2-weeks-portland-public-schools-unveil-school.txt](news/2026-09-21_oregonian_2-weeks-portland-public-schools-unveil-school.txt) | In two weeks time, staff at Portland Public Schools will unveil their long-awaited scenarios for which combination of K-5, K-8 and middle schools they will recommend for closure. |
| 2026-09-23 | K-12 Dive | More school closure decisions likely ahead for the 2026-27 school year | [2026-09-23_k12dive_more-school-closure-decisions-likely-ahead-2026.txt](news/2026-09-23_k12dive_more-school-closure-decisions-likely-ahead-2026.txt) | National roundup: more districts (incl. Portland) face closure decisions in 2026-27. |
| 2026-09-27 | Save PDX Schools (parent group) | PPS Rightsizing: What the Evidence Shows ("Rightsizing" Response for PTAs) | [2026-09-27_savepdxschools_pps-rightsizing-what-evidence-shows.txt](news/2026-09-27_savepdxschools_pps-rightsizing-what-evidence-shows.txt) | Save PDX Schools evidence deck for PTAs: closures save little (<$1M/building net) and harm students. |
| 2026-09-30 | Willamette Week | A Controversial Bond Management Contract Continues to Divide the Portland School Board | [2026-09-30_wweek_controversial-bond-management-contract-continues-divide-portland.txt](news/2026-09-30_wweek_controversial-bond-management-contract-continues-divide-portland.txt) | Draft bond audit of Procedeo keeps the board divided; members restate their Dec. 2025 votes (context for recall effort). |
| 2026-10-01 | KOIN | Parents brace for potential Portland Public Schools closures | [2026-10-01_koin_parents-brace-potential-portland-public-schools-closures.txt](news/2026-10-01_koin_parents-brace-potential-portland-public-schools-closures.txt) | Portland Public Schools is set to release its first draft for possible school closures and other changes next Monday. |
| 2026-10-04 | The Oregonian/OregonLive | Readers respond: All Portlanders affected by school closures | [2026-10-04_oregonian_readers-respond-all-portlanders-affected-school-closures.txt](news/2026-10-04_oregonian_readers-respond-all-portlanders-affected-school-closures.txt) | Letter: closing up to 20 schools affects all Portlanders, not just families. |
| 2026-10-05 | KATU | PPS is closing schools but may not see a big budget payoff. Here's why. | [2026-10-05_katu_pps-closing-schools-but-not-see-big.txt](news/2026-10-05_katu_pps-closing-schools-but-not-see-big.txt) | When the school bell rings for the new school year in the fall of 2027, hundreds of Portland Public Schools (PPS) elementary and middle school students may find themselves at a new school. |
| 2026-10-05 | KATU | Portland Public Schools proposes closing up to 14 schools amid declining enrollment | [2026-10-05_katu_portland-public-schools-proposes-closing-14-schools.txt](news/2026-10-05_katu_portland-public-schools-proposes-closing-14-schools.txt) | Portland Public Schools released two scenarios on Monday night that it says will address declining enrollment in the district. |
| 2026-10-05 | KGW | PPS is moving forward with its 'rightsizing' plan. These are the schools that could close | [2026-10-05_kgw_pps-moving-forward-rightsizing-plan-these-schools.txt](news/2026-10-05_kgw_pps-moving-forward-rightsizing-plan-these-schools.txt) | Portland Public Schools on Monday evening released a list of schools that it's considering shutting down as it weighs how to address declining enrollment and rising costs. |
| 2026-10-05 | KPTV | Full: PPS superintendent talks school closures, $65M shortfall (video page) | [2026-10-05_kptv_full-pps-superintendent-talks-school-closures-65m.txt](news/2026-10-05_kptv_full-pps-superintendent-talks-school-closures-65m.txt) | Video: full Armstrong interview on closures and the $65M shortfall. |
| 2026-10-05 | KPTV | PPS to name schools that could close Monday | [2026-10-05_kptv_pps-name-schools-close-monday.txt](news/2026-10-05_kptv_pps-name-schools-close-monday.txt) | Portland Public Schools families are waiting to learn which schools could close as the district prepares to release the first list under its controversial downsizing plan Monday. |
| 2026-10-05 | OPB | Up to 14 schools closing in Portland Public Schools ‘rightsizing’ scenarios | [2026-10-05_opb_14-schools-closing-portland-public-schools-rightsizing.txt](news/2026-10-05_opb_14-schools-closing-portland-public-schools-rightsizing.txt) | Portland Public Schools announced two scenarios Monday evening that would result in massive changes for Portland’s elementary, middle and K-8 schools, including building closures, program consolidations and changes… |
| 2026-10-05 | The Oregonian/OregonLive | Portland Public Schools will reveal school closure proposals Monday evening. Parents, teachers and school staff are on pins and needles | [2026-10-05_oregonian_portland-public-schools-reveal-school-closure-proposals.txt](news/2026-10-05_oregonian_portland-public-schools-reveal-school-closure-proposals.txt) | Staff at Portland Public Schools will go public with their long-awaited scenarios for which combination of K-5, K-8 and middle schools they are recommending for closures, attendance boundary adjustments and program… |
| 2026-10-05 | Willamette Week | Portland Public Schools Releases Two School Closure Scenarios to School Board | [2026-10-05_wweek_portland-public-schools-releases-two-school-closure.txt](news/2026-10-05_wweek_portland-public-schools-releases-two-school-closure.txt) | Portland Public Schools released two consolidation scenarios Monday night for the Portland School Board to consider. |
| 2026-10-06 | Axios Portland | These Portland schools face possible closure | [2026-10-06_axios_these-portland-schools-face-possible-closure.txt](news/2026-10-06_axios_these-portland-schools-face-possible-closure.txt) | Axios list of the 14 schools in Scenario A; list is not final, board votes in December. |
| 2026-10-06 | KATU | PPS plans would close six schools serving more low-income families | [2026-10-06_katu_pps-plans-would-close-six-schools-serving.txt](news/2026-10-06_katu_pps-plans-would-close-six-schools-serving.txt) | Portland Public Schools is weighing two closure plans, but both would shut the same six Title I schools. |
| 2026-10-06 | KATU | Parents and teachers cram into PPS board meeting, calling for delay on closures | [2026-10-06_katu_parents-teachers-cram-into-pps-board-meeting.txt](news/2026-10-06_katu_parents-teachers-cram-into-pps-board-meeting.txt) | Parents and teachers crowded a Portland Public Schools board meeting Tuesday night to urge the district to pause its school closure proposal. |
| 2026-10-06 | KGW | Portland Public Schools parents prepare to speak out over possible school closures | [2026-10-06_kgw_portland-public-schools-parents-prepare-speak-out.txt](news/2026-10-06_kgw_portland-public-schools-parents-prepare-speak-out.txt) | Portland Public Schools parents are preparing to voice their concerns Tuesday as the school board discusses the district's proposed "rightsizing" plan, which includes scenarios that could close up to 14 schools. |
| 2026-10-06 | KGW | Portland Public Schools weighs closing 14 schools as parents brace for major changes | [2026-10-06_kgw_portland-public-schools-weighs-closing-14-schools.txt](news/2026-10-06_kgw_portland-public-schools-weighs-closing-14-schools.txt) | Portland Public Schools leaders will take the first step Tuesday evening in talking about plans to potentially close 14 schools, cuts that the district says are needed to close a massive budget deficit caused by… |
| 2026-10-06 | KOIN | ‘I thought we would be safe’: Community responds after PPS proposes closing 14 schools | [2026-10-06_koin_i-thought-we-would-safe-community-responds.txt](news/2026-10-06_koin_i-thought-we-would-safe-community-responds.txt) | Portland Public Schools announced Monday evening the 14 schools they are considering closing. |
| 2026-10-06 | KPTV | Interview with PPS Superintendent Dr. Kimberlee Armstrong on school closures (video page) | [2026-10-06_kptv_interview-pps-superintendent-dr-kimberlee-armstrong-school.txt](news/2026-10-06_kptv_interview-pps-superintendent-dr-kimberlee-armstrong-school.txt) | Video: KPTV interview with Armstrong on the closure plan. |
| 2026-10-06 | KPTV | PPS proposes closing up to 14 schools as district faces $65M shortfall | [2026-10-06_kptv_pps-proposes-closing-14-schools-district-faces.txt](news/2026-10-06_kptv_pps-proposes-closing-14-schools-district-faces.txt) | Portland Public Schools is proposing two scenarios that would close up to 14 schools, as the district faces a $65 million shortfall. |
| 2026-10-06 | KXL | Portland Public Schools Proposes Up to 14 School Closures in Major Restructuring Plan | [2026-10-06_kxl_portland-public-schools-proposes-14-school-closures.txt](news/2026-10-06_kxl_portland-public-schools-proposes-14-school-closures.txt) | Portland Public Schools officials presented sweeping “rightsizing” proposals to the Board of Education, outlining plans to close up to 14 schools, adjust dozens of attendance boundaries, and overhaul specialized… |
| 2026-10-06 | North Peninsula Review | Can PPS School closures be stopped? - North Peninsula Review | [2026-10-06_northpeninsulareview_can-pps-school-closures-stopped-north-peninsula.txt](news/2026-10-06_northpeninsulareview_can-pps-school-closures-stopped-north-peninsula.txt) | Former board members predict a parent/teacher coalition could stop closures; Councilor Dan Ryan says closures affect whole city. |
| 2026-10-06 | OPB | Hundreds of students, parents, staff ask Portland to pause school closures | [2026-10-06_opb_hundreds-students-parents-staff-ask-portland-pause.txt](news/2026-10-06_opb_hundreds-students-parents-staff-ask-portland-pause.txt) | Students, staff, and parents representing over a dozen Portland schools, crowded the Portland Public Schools headquarters building Tuesday to protest newly released plans to “rightsize” the district by closing… |
| 2026-10-06 | OPB | OPB’s First Look: Closing Portland schools? | [2026-10-06_opb_opbs-first-look-closing-portland-schools.txt](news/2026-10-06_opb_opbs-first-look-closing-portland-schools.txt) | OPB newsletter summary of the closure proposals. |
| 2026-10-06 | Portland Mercury | Good Morning, News: Portland Public Schools on the Chopping Block, a "White Supremacist" Brunch, and Bad News for Senate Republicans (Hee-hee-hee) - Portland Mercury | [2026-10-06_mercury_good-morning-news-portland-public-schools-chopping.txt](news/2026-10-06_mercury_good-morning-news-portland-public-schools-chopping.txt) | Mercury morning roundup; lead item on PPS releasing 14-school closure scenarios. |
| 2026-10-06 | Portland Tribune | Portland Public Schools proposes closing up to 14 schools in 'rightsizing' plan | [2026-10-06_portlandtribune_portland-public-schools-proposes-closing-14-schools.txt](news/2026-10-06_portlandtribune_portland-public-schools-proposes-closing-14-schools.txt) | Scenario A closes 14, B closes 11, C defers; PAT petition demands boundary changes, central-office cuts, sale of HQ. |
| 2026-10-06 | The Oregonian/OregonLive | It’s not just closed schools: See how Portland Public Schools’ proposals could reshape your school | [2026-10-06_oregonian_not-just-closed-schools-see-how-portland.txt](news/2026-10-06_oregonian_not-just-closed-schools-see-how-portland.txt) | Leaders at Portland Public Schools will make their case for why they identified 14 schools across the city as potential candidates for closure during what is expected to be a standing-room-only school board meeting… |
| 2026-10-06 | The Oregonian/OregonLive | These 14 Portland schools could close under district's consolidation plan | [2026-10-06_oregonian_these-14-portland-schools-close-under-districts.txt](news/2026-10-06_oregonian_these-14-portland-schools-close-under-districts.txt) | Portland Public Schools on Monday unveiled two potential scenarios for a wave of school closures, boundary changes and program shifts that would fundamentally reshape the district, directly impacting students,… |
| 2026-10-06 | Willamette Week | Movement Swells to Protest PPS School Closure Proposals | [2026-10-06_wweek_movement-swells-protest-pps-school-closure-proposals.txt](news/2026-10-06_wweek_movement-swells-protest-pps-school-closure-proposals.txt) | In March, Portland School Board chair Eddie Wang told WW that while school closure conversations are difficult, he felt that the public recognized Portland Public Schools had reached hard times. |
| 2026-10-07 | Grants Pass Tribune | Oregon’s Shrinking Enrollment Puts Neighborhood Schools on the Closure List | [2026-10-07_grantspasstribune_oregons-shrinking-enrollment-puts-neighborhood-schools-closure.txt](news/2026-10-07_grantspasstribune_oregons-shrinking-enrollment-puts-neighborhood-schools-closure.txt) | Portland and Salem-Keizer are moving toward decisions that could reshape their public school systems in 2027, with proposed closures, attendance boundary changes and program relocations affecting families well beyond… |
| 2026-10-07 | KOIN | ‘Want to do everything we can’: PPS defends reasoning for proposed closures | [2026-10-07_koin_want-do-everything-we-can-pps-defends.txt](news/2026-10-07_koin_want-do-everything-we-can-pps-defends.txt) | Portland Public Schools is considering school closures and other changes as the district works to address declining enrollment and a projected $65 million budget deficit. |
| 2026-10-07 | KOIN | ‘We can’t let this happen’: Parents push back against proposed school closures at PPS meeting | [2026-10-07_koin_we-cant-let-happen-parents-push-back.txt](news/2026-10-07_koin_we-cant-let-happen-parents-push-back.txt) | It was a big night for many Portland Public School families, as the district officially outlined why they have certain schools on the potential chopping block during a packed public comment hearing on Tuesday. |
| 2026-10-07 | KPTV | PPS board member, parents react to controversial school closure plan | [2026-10-07_kptv_pps-board-member-parents-react-controversial-school.txt](news/2026-10-07_kptv_pps-board-member-parents-react-controversial-school.txt) | La Forte says some schools must close but she is still weighing the proposal; parents at James John react. |
| 2026-10-07 | KPTV | ‘It’s a betrayal’: Parents push back against potential PPS school closures at board meeting | [2026-10-07_kptv_betrayal-parents-push-back-against-potential-pps.txt](news/2026-10-07_kptv_betrayal-parents-push-back-against-potential-pps.txt) | Parents call the proposal "a betrayal" at the Oct. 6 board meeting; PAT president asks how closures help students. |
| 2026-10-07 | Portland Public Schools (official) | Board Members | [2026-10-07_pps_board-members.txt](news/2026-10-07_pps_board-members.txt) | PPS official roster page (zones, terms, student representative). |
| 2026-10-07 | Portland Public Schools (official) | Frequently Asked Questions | [2026-10-07_pps_frequently-asked-questions.txt](news/2026-10-07_pps_frequently-asked-questions.txt) | PPS rightsizing FAQ (official). |
| 2026-10-07 | Portland Public Schools (official) | Rightsize, Right Supports, Right for Students | [2026-10-07_pps_rightsize-right-supports-right-students.txt](news/2026-10-07_pps_rightsize-right-supports-right-students.txt) | PPS rightsizing landing page (official): engagement sessions, scenarios, feedback channels. |
| 2026-10-07 | Portland Public Schools (official) | Timeline | [2026-10-07_pps_timeline.txt](news/2026-10-07_pps_timeline.txt) | PPS rightsizing timeline page (official): phases and milestones. |
| 2026-10-07 | Save PDX Schools (parent group) | About — Save PDX Schools | [2026-10-07_savepdxschools_about-save-pdx-schools.txt](news/2026-10-07_savepdxschools_about-save-pdx-schools.txt) | Save PDX Schools "About" page (parent-run). |
| 2026-10-07 | Save PDX Schools (parent group) | Write PPS and Salem about school “right-sizing” | [2026-10-07_savepdxschools_write-pps-salem-about-school-right-sizing.txt](news/2026-10-07_savepdxschools_write-pps-salem-about-school-right-sizing.txt) | Save PDX Schools letter-writing tool to the board, legislators, governor (not used). |
| 2026-10-07 | Save PDX Schools (parent group) | “Rightsizing” is wrong for Portland. — Save PDX Schools | [2026-10-07_savepdxschools_rightsizing-wrong-portland-save-pdx-schools.txt](news/2026-10-07_savepdxschools_rightsizing-wrong-portland-save-pdx-schools.txt) | Save PDX Schools main page: "Rightsizing is wrong for Portland" - evidence summary, action steps. |
| 2026-10-07 | The Oregonian/OregonLive | At raucous rally, Portland parents, teachers and students protest school closures | [2026-10-07_oregonian_raucous-rally-portland-parents-teachers-students-protest.txt](news/2026-10-07_oregonian_raucous-rally-portland-parents-teachers-students-protest.txt) | Hundreds of infuriated parents and staff members descended on Portland Public Schools’ headquarters Tuesday night to protest far-reaching proposals to close up to 14 schools, shift grade configurations and programs… |
| 2026-10-07 | ppsclosures.info (independent data site) | Portland Public Schools Data Explorer | [2026-10-07_ppsclosures_portland-public-schools-data-explorer.txt](news/2026-10-07_ppsclosures_portland-public-schools-data-explorer.txt) | Independent data explorer for all 74 in-scope schools, incl. parsed Oct. 2026 scenarios. |

---

## 1. Timeline of rightsizing

Built from the coverage above. Where the board's own records add precision, they are cited from the sibling `boardbook/` folder.

### Background (2025)

- **2025-01-23**: A Portland State University forecast projects PPS enrollment will fall about 15% over the next decade. (`news/2025-01-23_wweek_preliminary-enrollment-forecasts-show-steeper-decline-come`)
- **Apr 2025**: Armstrong's 2025-26 budget cuts about $40M, the third straight deficit year. (`2025-04-22_opb_…`, `2025-04-23_oregonian_…`, `2025-04-23_yahoo_…`)
- **2025-05-20**: Board election.
  - Splitt is retained in Zone 1. Chase-Miller unseats Greene in Zone 4.
  - La Forte (Zone 5) and Engelsman (Zone 6) win open seats.
  - Voters also pass the $1.83B bond.
  - The new members are seated in July 2025.
  - (`2025-05-21_oregonian_…`, `2025-05-02_kgw_…`, `2025-05-12_axios_…`)
- **2025-08-26**: On the first day of school, Armstrong names enrollment and "optimizing" schools as a top priority, likely including consolidating schools, perhaps instead of seismic retrofits. A PAT video decries "false promises of 'consolidation.'" (`2025-08-27_wweek_murmurs-…`)
- **Sep 2025**: Some parents petition PPS to close Access Academy (the TAG school) first, to shore up underenrolled neighborhood schools. (`2025-09-03_oregonian_…`, `2025-09-15_oregonian_readers-respond-…`)
- **Sep 2025**: The new board leadership (Chair Wang and then-Vice Chair DePass) wants "big-picture," superintendent-supportive governance. La Forte and Engelsman push back on "unity" as a goal. (`2025-09-17_wweek_…`)
- **2025-10-08**: At the Facilities committee, staff say they don't want to spend millions on seismic retrofits at schools that may be "right-sized." The term "right-sized" enters the PPS vocabulary. More than 20 elementaries enroll only 200–300 students. (`2025-10-13_oregonian_…`)
- **Dec 2025**: The board approves a $61.5M Procedeo bond-management contract, 5–2 (La Forte and Engelsman no). This later fuels a recall effort against Wang. (`2026-09-30_wweek_…`, `2026-09-17_wweek_…`)

### Budget squeeze and launch (Jan–Apr 2026)

- **2026-01-13**: The board votes 6–1 (Engelsman no) to redraw NE Portland high school boundaries and shift students to Jefferson. This is an enrollment-balancing precursor. (`2026-01-14_oregonian_…`, `2026-01-14_axios_…`)
- **Jan 2026**: PPS floats cutting about 300 positions to close a $50M gap for 2026-27. PAT blames administrative growth and state funding. (`2026-01-21_kgw_…`, `2026-01-21_oregonian_…`, `2026-01-24_oregonian_…`)
- **Feb 2026**: PPS abruptly ends the high school grades at Metropolitan Learning Center (MLC). The board debates the process (2/24 meeting), and this becomes a preview of the closure fights. (`2026-02-19_oregonian_fury-…`, `2026-02-24_wweek_…`, `2026-02-25_wweek_…`)
  - In the same period, an unexpected midyear gap of $10M grows to $14M. (`2026-02-24_opb_…`, `2026-02-24_oregonian_…`, `2026-03-07_oregonian_…`)
- **2026-03-10**: Armstrong holds a press conference. PPS may close **5–10 of 74** elementary, K-8, middle and alternative schools by fall 2027, with a recommendation in late fall and a board decision by the end of 2026.
  - The board unanimously agrees to launch a nine-month review.
  - Armstrong: "in the end I want to call it what it is, which will be a recommendation to close a subset of schools."
  - (`2026-03-10_wweek_…`, `2026-03-12_oregonian_…`, `2026-03-13_opb_…`, `2026-03-18_wweek_…`)
- **2026-03-20/31**: PAT ratifies four furlough days, 85% in favor. The board approves the furlough MOUs 6–0 (Splitt absent), and the school year ends June 5. (`2026-03-21_kgw_…`, `2026-04-01_wweek_…`, `2026-03-25_axios_…`)
- **2026-04-11 to 04-27**: Rightsizing community engagement sessions run on Apr 11 (Kellogg), Apr 20, 22, 25 and 27. PPS introduces a "utilization" metric, and Armstrong floats a range of "one to 12" schools. (`2026-04-15_wweek_…`, `2026-04-13_oregonian_…`, `2026-04-22_katu_…`, `2026-04-23_opb_…`, `2026-04-27_katu_…`)
- **2026-04-14**: **Resolution 7296**, "Direct the Superintendent to Begin a Rightsizing Process," passes **5–2**.
  - Yes: Wang, DePass, Chase-Miller, Splitt, Sullivan. No: **Engelsman, La Forte**. Student rep Ritorto voted no (unofficial).
  - Sources: the Citizen Portal lede (`2026-04-15_citizenportal_…`) and the draft minutes at `boardbook/2026-06-09_Regular_Meeting_749359/2026_04_14_Draft_Meeting_Minutes_3997322.txt`.
  - Several amendments were voted on that night, including Splitt's amendment that the process "will include school and program closures, consolidations, or boundary changes," which passed 6–0–1 (Wang abstained).
  - Engelsman and Sullivan moved to soften "will" to "may"; that failed 2–5.
  - La Forte's package of added recitals (equity impact, financial transparency, etc.) is recorded as "passed 4–3," but the listed roll call shows 3 yes and 4 no. This is an internal inconsistency in the draft minutes.
  - Note: Oregonian 10/5–10/6 says "all seven members voted last spring to direct district staff to research closure scenarios." That probably refers to the unanimous May 26 Resolution 7307, not to Resolution 7296.
- **2026-04-17 to 04-22**: Parents at Title I schools begin forming a coalition. (`2026-04-17_kgw_…`, `2026-04-22_wweek_…`)
- **2026-04-28/29**: Armstrong presents a $2.77B 2026-27 budget with a $56M deficit and 300+ positions cut. She projects a further **$65M deficit for 2027-28**.
  - Gov. Kotek has ordered that furlough days can no longer be used.
  - (`2026-04-29_opb_…`, `2026-04-29_axios_…`, `2026-04-29_kgw_…`, `2026-04-30_kptv_…`, `2026-04-22_mercury_…`)

### Framework and budget (May–Jul 2026)

- **2026-05-26**: The board **unanimously** adopts **Resolution 7307**, the rightsizing guiding principles and workplan.
  - The four principles: well-resourced schools; safe and healthy environments; neighborhood schools plus choice; and an equity lens for "focal" students.
  - It also requires an equity impact analysis and a data-driven analysis.
  - (`2026-05-27_wweek_…`, `2026-05-26_citizenportal_…`; the resolution text is in `boardbook/2026-05-26_Special_Meeting_746944/`)
- **2026-06-23/24**: The 2026-27 budget is adopted 6–0 with **Engelsman abstaining**. 87 educators are laid off.
  - Engelsman's amendment to restore $13.2M for student-facing positions fails 1–6.
  - Chase-Miller's proposal to tap reserves and La Forte's half-reserves variant also fail.
  - La Forte's freeze on board and leadership travel passes.
  - (`2026-06-24_oregonian_…joyless…`, `2026-06-25_opb_…`, `2026-06-30_wweek_…`, `2026-06-28_oregonian_editorial-…`)
- **2026-07-31 / Aug 4**: A PPS-commissioned 150-page evaluation of the 2021–24 Southeast Guiding Coalition rebalancing is presented as lessons for closures. (`2026-07-31_wweek_…`)

### Scale jumps (Aug–Sep 2026)

- **2026-08-26**: On the first day of school, Armstrong says closures could total **10–20** schools, up from 5–10, with a draft list due in November. (`2026-08-26_wweek_…`, `2026-08-26_katu_…`, `2026-08-26_kgw_…`, `2026-08-26_oregonian_…`)
- **2026-08-28**: The district model shows that closing **15 of 45 elementaries** would put every remaining elementary at or above the 360-student threshold in the Quality Education Model (QEM) by 2031-32. Three middle-school closures still leave four middle schools below the 500 threshold. (`2026-08-28_wweek_…`, `2026-09-03_k12dive_…`)
- **2026-08-30**: An Oregonian editorial ("PPS enters the minefield") calls closures unavoidable but urges care. It notes PAT's petition. (`2026-08-30_oregonian_editorial-…`)
- **2026-08-31**: The "Right-Sizing the Right Way" parent coalition launches a petition to prioritize neighborhood schools. (`2026-08-31_katu_…`)
- **2026-09-01**: Regular meeting at Grant HS, with two items:
  - **(a) Rightsizing direction.** Five directors are willing to let staff keep modeling **up to 20** closures: Wang, Chase-Miller, DePass, La Forte, Sullivan. **Splitt and Engelsman** express discomfort with the magnitude. This was a direction or consensus, not a formal resolution.
  - **(b) Resolution 7371**, a superintendent contract extension through June 2029 with a raise, passes **5–2** (La Forte, Engelsman no).
  - PAT President Alisha Chavez attacks both items.
  - (`2026-09-02_oregonian_…backs-planning…`, `2026-09-03_wweek_heres-where-every…`, `2026-09-02_opb_…`, `2026-09-01_katu_…sobering…`, `2026-09-02_wweek_…`, `2026-09-02_oregonian_…approves-raise…`, `2026-09-09_wweek_…`)
- **2026-09-15**: Data at the regular meeting shows Title I schools are disproportionately under the enrollment thresholds. In the 2025-26 school year, 18% of Title I elementaries met the threshold versus 35% of non-Title I elementaries. (`2026-09-19_wweek_…`, `2026-09-16_wweek_murmurs-…`)
- **2026-09-15/18**: Former director Mike Rosen files a prospective recall petition against Chair Wang. He cites a leaked draft audit of Procedeo, and closures as a further concern. (`2026-09-17_wweek_…`, `2026-09-18_katu_…`)
- **2026-09-16**: Board retreat. WW reports on what happens to closed buildings (lease, sale, housing). (`2026-09-16_wweek_happen-…`)
- **2026-09-19**: The Faubion community listening session is attended by La Forte and Engelsman. Parent groups (Save PDX Schools and others) are organizing. (`2026-09-21_oregonian_…`)
- **2026-09-29**: Board special meeting (virtual). The agenda covered Resolution 7382, the board's responses to the draft bond-program (Procedeo) audit, not rightsizing. On several amendments, a 4-3 bloc (Splitt, Sullivan, La Forte and Engelsman) prevailed over board leadership, for example striking a budget-availability caveat. An "additional auditor" recommendation passed 5-2. Sources: `boardbook/2026-09-29_Special_Meeting_769094/`, transcript `transcripts/text/2026-09-29_Board_of_Education_Special_Meeting__SPwXuNlwP_U.txt`, vote details in `BOARD_PROFILES.md`.

### Scenarios released (Oct 2026)

- **2026-10-04**: PAT publicly releases its petition. It asks PPS to:
  - redraw boundaries;
  - return central-office staffing to pre-2019 levels (PAT claims 79 administrators have been added since 2019);
  - sell or repurpose the Portland Education Center;
  - grow enrollment.
  - (`2026-10-05_wweek_…`, `2026-10-06_portlandtribune_…`)
- **2026-10-05**: PPS releases its scenarios:
  - **Scenario A** closes 14: 13 elementaries (Maplewood, Stephenson, Irvington, Rose City Park, Buckman, Creston, Marysville, Woodmere, Lewis, Beach, James John, Peninsula, Sabin) plus Sellwood MS, with 38 boundary changes.
  - **Scenario B** closes 11: the same list minus Stephenson, Rose City Park and Lewis, with 34 boundary changes.
  - **Scenario C** keeps the status quo / defers.
  - Both A and B convert 7 K-8s to K-5 (Beverly Cleary, Laurelhurst, Sunnyside, Bridger, César Chávez, Faubion, Vernon).
  - Both end Sunnyside's environmental focus and Buckman's arts focus, move Odyssey to MLC (closing MLC's high school), and relocate or combine dual-language immersion programs.
  - Six of the ten schools on both lists are Title I schools.
  - About 7,981 (A) or 6,988 (B) K-8 students would move.
  - (`2026-10-05_opb_…`, `2026-10-06_oregonian_these-14-…`, `2026-10-05_wweek_…`, `2026-10-06_katu_pps-plans-…`, `2026-10-06_portlandtribune_…`, `2026-10-07_ppsclosures_…`)
- **2026-10-06**: Regular board meeting.
  - A PAT rally beforehand draws 500+ people by Chavez's estimate. The petition has about 3,600–4,000 signatures.
  - The crowd forces its way in, and Wang threatens to move the meeting.
  - Engelsman calls the plan "mayhem." Chase-Miller asks for clear answers on what "well-resourced" means.
  - Rep. Thuy Tran testifies that PPS had assured Rose City Park in Jan 2026 it was not a closure candidate.
  - (`2026-10-06_opb_hundreds-…`, `2026-10-06_wweek_movement-…`, `2026-10-07_oregonian_raucous-…`, `2026-10-06_katu_parents-teachers-…`, `2026-10-07_koin_…`, `2026-10-07_kptv_…`)

### Next steps (as reported)

- Community feedback runs through November.
- **Armstrong's formal recommendation comes in mid-November.** One web-search summary said Nov. 17; this is not confirmed in the saved text.
- **The board votes in December 2026.**
- Changes take effect in **fall 2027**.
- The $65M 2027-28 deficit remains regardless. PPS says closing schools is "not a money-saving exercise." Savings come mainly from principal and office staffing.
- PAT contract bargaining starts in January 2027. Board elections are in May 2027, with the seats held by Wang, DePass, Sullivan and Splitt on the ballot.
- (`2026-10-06_oregonian_these-14-…`, `2026-10-05_katu_pps-closing-schools-…`, `2026-06-30_wweek_…`)

---

## 2. Board member statements

Statements are quoted or closely paraphrased from the cited files, in date order within each director. A vote table follows the directors.

### Eddie Wang (Zone 7, Chair): the strongest proponent of large-scale change

- **2025-09-17** (`2025-09-17_wweek_…`): Wants a board that sets goals and backs the superintendent rather than "nitpicking every contract." He said boards "supportive of their superintendent see outcomes."
- **2026-02-05** (`2026-02-05_kptv_…`): Called the cuts "an emergency." He urged the state to use the Education Stability Fund, saying morale is "at an all time low."
- **2026-02-24** (`2026-02-25_wweek_…`): On MLC, opposed bending policy when "certain communities come out in full force." He said that "leads places that serve historically disadvantaged families feeling unheard and unseen."
- **2026-03-10/12** (`2026-03-12_oregonian_…`):
  - Called the closure question fundamentally "an engineering problem" where urgency matters.
  - Said the process will try to keep upheaval from falling disproportionately on poorer areas.
  - Defended hiring outside consultants: "Right-sizing is not something we do every day."
- **2026-03-18** (`2026-03-18_wweek_…`):
  - "We literally have 6,000 students less than we did in 2018… That's, like, 30 elementary schools' worth."
  - "The basis of having everything on the table is already the start of equity in the process."
- **2026-04-15** (`2026-04-15_wweek_…`): Cautioned that a low utilization rate "does not automatically mean that the lower-enrolled one will be closed."
- **2026-04-23** (`2026-04-23_opb_…`): The goal is that "all of our schools… are properly resourced," for example a full-time librarian and a special-education teacher at every elementary.
- **2026-04-29** (`2026-04-29_kgw_…`): "There's no more fat to cut… we are into the bone."
- **2026-06-23** (`2026-06-25_opb_…`, `2026-06-30_wweek_…`):
  - Voted against Engelsman's $13.2M amendment: "The way I voted was not just looking at this year, but looking at future years."
  - Compared the moment to 2010: "That was cake compared to this."
- **2026-09-01** (`2026-09-03_wweek_…`): Among the most open to dramatic change, he doesn't want to keep "dragging its feet." If equity is centered and the remaining schools are better resourced: "I am for going for as much as needed."
- **2026-09-01** (`2026-09-01_oregonian_…`, `2026-09-02_wweek_…`): Argued for Resolution 7371 on compensation-comparables grounds and voted yes.
- **2026-09-15** (`2026-09-19_wweek_…`): "If we do nothing, our Title I schools will be in an even worse position than they are today… this is also an opportunity to do something new."
- **2026-09-17/18** (`2026-09-17_wweek_…`, `2026-09-18_katu_…`): Responding to the recall petition, he called its allegations "unsubstantiated" and said "fear of change" is behind it.
- **2026-10-06** (`2026-10-06_opb_hundreds-…`): Threatened to move the meeting after repeated interruptions. WW (`2026-10-06_wweek_…`) contrasts this with his March remark that "people understand [school closures] more so than probably in the past."

### Rashelle Chase-Miller (Zone 4, Vice Chair per Sep–Oct 2026 coverage): supports the process with an equity framing; wants answers before committing

- **2026-02-18** (`2026-02-18_wweek_…`): "Historically, the district has listened to the more affluent schools, the predominantly white schools… So it's the kids from low-income communities or from Black and brown schools that are forced to move."
- **2026-02-24** (`2026-02-25_wweek_…`): On MLC: "we're at a point where we don't have options." She also asked for the cost analysis required by policy.
- **2026-03-10** (`2026-03-12_oregonian_…`): "Everything should be on the table… I don't think kids should have to go to a special school, or a school out of their neighborhood, to have an amazing experience."
- **2026-04-14**: Voted **yes** on Resolution 7296 and seconded it (minutes).
- **2026-04-22** (`2026-04-22_wweek_pps-loses-…`): "Reducing Title I schools really just means that there will be fewer resources for the kids that really need them."
- **2026-06-23** (`2026-06-25_opb_…`, `2026-06-28_oregonian_editorial-…`): Proposed tapping reserves to restore positions. The proposal failed.
- **2026-09-01** (`2026-09-01_katu_…discuss-15…`, `2026-09-03_wweek_…`, `2026-09-02_oregonian_…backs-planning…`):
  - "We're already a school district stretched thin… exacerbated as time goes on if we don't make any changes."
  - Wants a plan that guarantees a full-time librarian, art teachers, counselors and social workers "for as many students as possible."
  - Voted to keep modeling up to 20 closures "because she wanted more information." She confirmed with Armstrong that the board could still "hit the brakes."
  - Voted **yes** on Resolution 7371.
- **2026-09-16** (`2026-09-16_wweek_happen-…`): Suggests that closed buildings could become affordable or educator housing (the Austin ISD model), or be leased to community partners.
- **2026-09-18 / 09-30** (`2026-09-18_katu_…`, `2026-09-30_wweek_…`): Defends her Procedeo vote and Chair Wang, calling the recall "a distraction and misguided."
- **2026-10-06** (`2026-10-06_wweek_movement-…`): "I do really hope that really soon the public has some really clear answers about what well-resourced schools look like… perhaps some massaging of the scenarios."

### Michelle DePass (Zone 2): favors going "big" and fast

- **2025-09-02** (`2025-09-02_northpeninsulareview_…`): "These conversations cannot happen in a vacuum." Enrollment, seismic needs and community voices all factor in.
- **2025-09-17** (`2025-09-17_wweek_…`): "We need to move forward… we need to get the job done."
- **2026-03-10/18** (`2026-03-12_oregonian_…`, `2026-03-18_wweek_…`): Supported more feedback on equity: "This is a process that the entire PPS family should bear the brunt of and be part of."
- **2026-04-14**: Moved adoption of Resolution 7296 and voted **yes** (minutes).
- **2026-06-23** (`2026-06-24_oregonian_…joyless…`, `2026-06-30_wweek_…`): "Sometimes we need to display courage and do hard things… We can't say yes to everything that comes across our desk." She opposed last-minute amendments.
- **2026-09-01** (`2026-09-03_wweek_…`, `2026-09-02_oregonian_…backs-planning…`):
  - "If it takes a greater magnitude of rightsizing to get to the outcome… I'd say go big."
  - Prefers a "rip the Band-Aid off" approach to a piecemeal one.
  - Voted **yes** on Resolution 7371.
- **2026-09-30**: Declined WW's request for comment on Procedeo (`2026-09-30_wweek_…`).

### Christy Splitt (Zone 1): from supportive to "scalpel, not hammer"

- **2026-03-12** (`2026-03-18_wweek_…`): "If there are buildings that we should just not be investing any more money in, then that would be to me a good building to consider letting go of."
- **2026-04-14**: Voted **yes** on Resolution 7296. Her amendment making closures, consolidations or boundary changes explicit passed. She voted no on softening "will" to "may" (minutes).
- **2026-04-27** (`2026-04-27_katu_…`): "If you're not pissed off at the state Legislature and our governor right now, you're not paying attention."
- **2026-06-23** (`2026-06-25_opb_…`): Spoke emotionally about the layoffs while voting for the budget.
- **2026-09-01** (`2026-09-01_katu_…sobering…`, `2026-09-02_opb_…`, `2026-09-03_wweek_…`, `2026-09-09_wweek_…`):
  - "So the Duniways and Alamadas [sic] get protected just because they're big? That doesn't seem very fair."
  - "I worry that a 'hammer' approach, where we're closing a quarter of our schools… [is] possibly doing more damage than we're meaning to. So count me in as being more skeptical now than I was a week ago."
  - "I think we probably do need to close some schools, but one quarter of the schools just really shook me… I would much prefer a scalpel approach."
  - Wants to hear teacher voices.
- **2026-09-01** (`2026-09-02_wweek_…`): Voted **yes** on Resolution 7371. She said the timing slip was "the product of board inaction."
- **2026-10-05/06** (`2026-10-05_oregonian_…`, `2026-10-06_oregonian_these-14-…`): Named alongside Engelsman as having "expressed qualms about the scope and magnitude."

### Patte Sullivan (Zone 3): committed to continuing, wants many voices heard

- **2026-02-24** (`2026-02-25_wweek_…`): Asked whether MLC could recruit more students instead of closing its high school.
- **2026-04-14**: Voted **yes** on Resolution 7296. She seconded Engelsman's "will" to "may" amendment (which failed) and suggested bringing La Forte's amendments back in two weeks (minutes).
- **2026-06-23** (`2026-06-25_opb_…`): "Maybe Salem is looking at this board meeting."
- **2026-09-01** (`2026-09-01_katu_…sobering…`, `2026-09-03_wweek_…`, `2026-09-02_oregonian_…backs-planning…`):
  - "It's important to me that they all look good. If that means we have to do some Rightsizing, then I'm really wanting to look at it."
  - "If rightsizing means… 'increased stability and improved student earning [sic] and experience across the system and in every school'… I'm for it."
  - Stressed the many unanswered questions on savings, layoffs and building disposition.
  - Voted **yes** on Resolution 7371.
- **2026-09-30** (`2026-09-30_wweek_…`): Stands by her Procedeo vote.

### Virginia La Forte (Zone 5): favors consolidating "at scale" in principle, but votes against process and timing; worries about "school deserts"

- **2025-09-17** (`2025-09-17_wweek_…`): "A unified board is not the goal; it's a possible outcome." She regrets her earlier Procedeo vote.
- **2026-02-24** (`2026-02-25_wweek_…`): Would have voted no on the MLC closure as a stand-alone item: "I feel like we're way outside of [the spirit of our board resolution]."
- **2026-03-10** (`2026-03-12_oregonian_…`, `2026-03-18_wweek_…`):
  - Said 5–10 schools could be **too low**, and suggested phasing out K-8s.
  - "Consolidating at scale would allow more significant upgrades to a smaller number of schools."
  - "We need more students learning together in the buildings we operate."
- **2026-03-31** (`2026-04-01_wweek_…`): On the furloughs: "devastating and nauseating."
- **2026-04-11** (`2026-04-13_oregonian_…`): Asked the forum crowd, "What are the things that keep you up at night so we can take them into account?"
- **2026-04-14**: Voted **no** on Resolution 7296. Earlier that night she moved a package of added recitals on decision criteria, equity impact, community engagement, timeline, financial transparency and policy alignment. The draft minutes record its outcome inconsistently (minutes).
- **2026-06-23** (`2026-06-25_opb_…`): Her travel-freeze amendment passed: "If it's five dollars, it's worth passing." She also floated a half-reserves amendment, which failed.
- **2026-09-01** (`2026-09-03_wweek_…`, `2026-09-02_oregonian_…approves-raise…`):
  - "It does feel like we're at a tipping point… We may need to make some big swings." She wants attention to transition grades and to the K-8 vs. middle-school question.
  - Voted **no** on Resolution 7371 because of timing amid the budget crisis.
- **2026-09-19** (`2026-09-21_oregonian_…`): "Everyone wants their school to stay, but the reality is that it isn't going to happen. I want to make sure that there is still a strong school at the center of our communities."
- **2026-10-02** (`2026-10-05_opb_…`): Video message: "It's weighing heavy on all of us."
- **2026-10-06/07** (`2026-10-06_kgw_…weighs-closing-14…`, `2026-10-07_kptv_pps-board-member-…`):
  - "I want to make sure we don't have areas of the city that we are leaving as essentially school deserts."
  - "I think we are going to have to take some action. Definitely. What that will look like? That's what the next two months are for."
  - She has not yet decided on the scenarios.

### Stephanie Engelsman (Zone 6): the most consistent skeptic; wants boundaries first and answers before closures

- **2025-09-17** (`2025-09-17_wweek_…`): The only no vote on the Sept 2025 Procedeo extension. "We do not have to be unified in our decisions."
- **2026-01-13** (`2026-01-14_oregonian_…`): The only no vote on the HS boundaries. She preferred an alternative that "strengthened all of our high schools."
- **2026-02-24** (`2026-02-25_wweek_…`): On MLC: "we owe that to our constituents… to make this a process that they understand… [so] they don't feel like rugs are being pulled out."
- **2026-03-10** (`2026-03-10_katu_…board-mulls…`, `2026-03-18_wweek_…`):
  - "At what point in this parallel right-sizing, seismic conversation, do we then say this school is staying open?"
  - Cites the Bridger merger as a cautionary tale: its combined enrollment fell from 752 to 446.
- **2026-04-14**: Voted **no** on Resolution 7296. She moved several amendments: adding "boundary changes" passed; "will" to "may" failed (minutes).
- **2026-06-23** (`2026-06-30_wweek_…`, `2026-06-25_opb_…`):
  - Moved to restore $13.2M for student-facing positions: "it's not my job, or our job, to come up with finding the money… We cannot balance another budget on the backs of our students." It failed 1–6.
  - **Abstained** on the budget.
- **2026-09-01** (`2026-09-01_katu_…sobering…`, `2026-09-03_wweek_…`, `2026-09-02_oregonian_…backs-planning…`, `2026-09-02_wweek_…`):
  - Asked what each closure would save, how many layoffs there would be, and whether families leave PPS after closures.
  - "If drawing boundaries and realigning boundaries is sufficient, then I think that's a great place to start… I don't know that I share the same readiness to go forward."
  - Voted **no** on Resolution 7371: "It seemed so tone-deaf given the magnitude of the budget crisis."
- **2026-09-30** (`2026-09-30_wweek_…`): Worried Procedeo has not delivered Jefferson "faster or cheaper." She would vote no again.
- **2026-10-06** (`2026-10-06_katu_parents-teachers-…`, `2026-10-06_opb_hundreds-…`):
  - "To me, this plan is mayhem."
  - "It's gonna take these kids a very long time to get home, which is frankly widening an equity gap."
  - Objects to ending Sunnyside's environmental focus and Buckman's arts focus.
  - To staff: "I'm recommending you do the work."

### Student representatives

- **Ian Ritorto** (2025–26): Said he would have voted no on the MLC closure as a stand-alone item (`2026-02-25_wweek_…`). Cast an unofficial no on Resolution 7296 (minutes).
- **Rose Sandell** (2026–27): No statements found in the coverage.

### Board votes related to rightsizing

| Date | Item | Result | No / abstain | Sources |
|---|---|---|---|---|
| Sep 2025 | Procedeo contract extension (context) | 6–1 | No: Engelsman | `2025-09-17_wweek_…` |
| Dec 2025 | Procedeo $61.5M bond-management contract (context; recall trigger) | 5–2 | No: La Forte, Engelsman | `2026-09-30_wweek_…` |
| 2026-01-13 | NE Portland HS boundary change (Jefferson) | 6–1 | No: Engelsman | `2026-01-14_oregonian_…` |
| 2026-03-10 | Launch of nine-month closure review | Unanimous agreement (reported; may have been consensus rather than a resolution) | — | `2026-03-12_oregonian_…` |
| 2026-03-31 | Furlough MOUs and calendar change | 6–0 | Splitt absent | `2026-04-01_wweek_…` |
| **2026-04-14** | **Res. 7296: begin rightsizing process** | **5–2** | **No: Engelsman, La Forte** (Ritorto unofficial no) | `2026-04-15_citizenportal_…`; boardbook draft minutes |
| **2026-05-26** | **Res. 7307: guiding principles and workplan** | **Unanimous** | — | `2026-05-27_wweek_…` |
| 2026-06-23 | Engelsman amendment to restore $13.2M | Failed 1–6 | Only Engelsman yes | `2026-06-30_wweek_…` |
| 2026-06-23 | 2026-27 budget adoption | Passed 6–0–1 | Abstain: Engelsman | `2026-06-25_opb_…` |
| **2026-09-01** | **Direction to keep modeling up to 20 closures** | 5 supportive / 2 reluctant (not a formal vote) | Reluctant: Splitt, Engelsman | `2026-09-02_oregonian_…backs-planning…` |
| **2026-09-01** | **Res. 7371: superintendent contract extension and raise** | **5–2** | **No: La Forte, Engelsman** | `2026-09-02_oregonian_…approves-raise…`, `2026-09-02_wweek_…` |
| Dec 2026 (scheduled) | Final rightsizing plan | — | — | — |

---

## 3. Stakeholder positions

### Labor

- **Portland Association of Teachers (PAT)**: the main organized opposition.
  - **Under President Angela Bonilla** (through spring 2026):
    - Blamed administrative growth and the state for the cuts. Asked Gov. Kotek to tap the $1B Education Stability Fund and called the cuts "Kotek Cuts."
    - Ran a forensic look at PPS finances. Filed a layoff grievance.
    - (`2026-01-21_oregonian_…`, `2026-03-13_opb_…superintendent…`, `2026-04-30_kptv_…`, `2026-06-09_opb_…`)
    - Its 2025 video warned of "false promises of 'consolidation'" (`2025-08-27_wweek_…`).
  - **Under President Alisha Chavez** (from summer 2026):
    - "You cannot close schools without increasing the pressure on the schools that remain." (`2026-09-02_oregonian_…backs-planning…`)
    - Warned the board "We will remember the choices you make when we sit across the bargaining table." (`2026-09-01_wweek_…`)
    - "Closing schools is not a plan, it's a reaction… We ask that the district exhaust every available option it has before considering closing schools." (`2026-10-05_kgw_…`, `2026-10-05_wweek_…`)
    - "We are not rightsizing education, we are reducing it." (`2026-10-07_oregonian_raucous-…`)
  - **PAT petition demands:** redraw boundaries; cut the central office to pre-2019 levels (it claims 79 added administrators); sell or repurpose the Portland Education Center; evaluate vacant properties; move staff into underused schools; grow enrollment, including social-housing partnerships. (`2026-10-06_portlandtribune_…`, `2026-10-06_oregonian_these-14-…`)
  - **Politics:** PAT is signalling it will recruit and fund challengers in the May 2027 board races (`2026-06-30_wweek_…`).
- **SEIU 503 Local 140, Portland Federation of School Professionals, ATU**: Raised concerns about budget cuts and took furlough days (`2026-01-21_kgw_…`, `2026-04-01_wweek_…`). No separate closure statements found.

### Parent and community groups

- **Save PDX Schools**, a parent coalition ("'Rightsizing' is wrong for Portland"):
  - Argues closures save little (net savings under $1M per building) and harm students, citing research from Chicago and Philadelphia.
  - Calls for alternatives, a student-centered plan and state funding.
  - Provides letter-writing tools aimed at the board, legislators and the governor.
  - Also hosts independent automated transcripts of PPS meetings, in a JS app that was not scraped.
  - (`news/2026-10-07_savepdxschools_*`, `2026-09-27_savepdxschools_…`, `2026-10-06_opb_hundreds-…`, `2026-09-21_oregonian_…`)
- **Title I school parent coalition**, formed in April 2026 around Lee, Lent, Jason Lee and other schools:
  - Wants equity to be the "north star" and Title I communities "the last to bear the burden."
  - Says low enrollment reflects "underinvestment, redlining, and special exceptions that have privileged better-off communities."
  - Called the October scenarios "disappointing."
  - (`2026-04-17_kgw_…`, `2026-04-22_wweek_…`, `2026-04-14_katu_…`, `2026-09-19_wweek_…`, `2026-10-05_wweek_…`)
- **"Right-Sizing the Right Way"** coalition (launched Aug 2026): Petitions PPS to prioritize neighborhood schools over focus-option programs, which it says serve a more privileged population (`2026-08-31_katu_…`).
- **Cesar Chavez K-8 parents** (Mar 2026): Open letter criticizing the "absence of equity in the selection process" and the opaque seismic and closure lists (`2026-03-12_oregonian_…`).
- **Community and Parents for Public Schools (CPPS)**: Puts responsibility on the state. Hosted a funding forum with the Ways & Means co-chairs, Sen. Kate Lieber and Rep. Tawna Sanchez (`2026-04-22_mercury_…`, `2026-04-23_opb_…`).
- **PTAs at individual schools**: James John, Sellwood MS, Arleta/Marysville, Lee, Rieke and others testified or organized to oppose closure of their schools or to demand that PPS "show their work." (`2026-04-13_oregonian_…`, `2026-10-06_koin_…`, `2026-10-07_kptv_…`)
- **Access Academy petition parents** (Sep 2025): Proposed closing the TAG school first (`2025-09-03_oregonian_…`).
- **MLC community**: Petition with more than 1,500–2,000 signatures against ending the high school (`2026-02-19_oregonian_readers-respond-…`, `2026-02-24_wweek_…`).
- **ppsclosures.info**, an independent data explorer: A neutral data resource covering the 74 in-scope schools and the parsed scenarios (`2026-10-07_ppsclosures_…`).
- **PPS Community Budget Review Committee**: Warned that the budget's baked-in assumptions may worsen the deficit (`2026-05-13_oregonian_…`).

### Elected officials and others

- **Gov. Tina Kotek**:
  - Declined to tap the Education Stability Fund. Her spokesperson said school funding was "prioritized and protected."
  - Issued an executive order barring instructional-day cuts.
  - Has not spoken publicly on PPS closures, per Save PDX Schools.
  - (`2026-04-22_mercury_…`, `2026-04-29_opb_…`, `2026-10-07_savepdxschools_write-…`)
- **State Rep. Thuy Tran (D-Portland)**: Told the board on 10/6 that district officials had assured Rose City Park in Jan 2026 it was not a closure candidate because of its seismic priority (`2026-10-06_opb_hundreds-…`).
- **State Sen. Lew Frederick (D-Portland)**: Warned in Feb 2026 that dissolving MLC's high school was a first step toward closing the building (`2026-02-19_oregonian_fury-…`).
- **City Councilor Tiffany Koyama Lane**:
  - At the June budget vote: "I know you all are in an impossible position" (`2026-06-25_opb_…`); she also pressed the board to find money to restore positions (`2026-06-30_wweek_…`).
  - Opposed the timing of the superintendent's raise (`2026-09-02_oregonian_…approves-raise…`, `2026-09-03_kptv_…`).
- **City Councilor Dan Ryan**: "The city's in charge of the infrastructure surrounding these schools and we have a big responsibility for families and safety." (`2026-10-06_northpeninsulareview_…`)
- **Mayor Keith Wilson**: No statement on closures found.
- **Former board members**:
  - Mike Rosen filed a prospective recall of Wang over Procedeo and doubts about "their capacity to do this" (`2026-09-17_wweek_…`, `2026-09-18_katu_…`).
  - Paul Anthony and Steve Buel predict a parent and union coalition could stop closures (`2026-10-06_northpeninsulareview_…`).
  - Andrew Scott says the budget crunch was predictable (`2026-04-22_mercury_…`).
- **The Oregonian editorial board**: Supports closures as necessary but urges a careful, transparent process. Praised the board for rejecting unfunded amendments in June. (`2026-08-30_oregonian_editorial-…`, `2026-06-28_oregonian_editorial-…`)
- **Letters to The Oregonian**: For and against closures; see the letter items from 2025-08 through 2026-10 in the table.

---

## 4. Needs browser fetch / not obtained

| URL / source | Status | What's needed |
|---|---|---|
| citizenportal.ai: 11 PPS rightsizing summaries (URLs in `news/raw/fetch_log.tsv`, files `news/*_citizenportal_*`) | Sign-up wall; only ledes saved | Full text requires a free account (not created). These are AI summaries, so the boardbook minutes and videos are better primary sources. |
| https://www.theskanner.com/news/newsbriefs/26544-portland-public-school-closures | HTTP 526 (site down). The Skanner ceased publication in Feb 2026, per OPB. | Probably an old pre-2025 brief anyway. |
| The Portland Observer | Nothing found. A New Pittsburgh Courier item (Apr 2026, 403) reports two legacy Black newspapers closing. | Confirm whether the Observer is still publishing. https://newpittsburghcourier.com/2026/04/08/two-legacy-black-newspapers-close-citing-financial-pressures/ |
| https://www.schooldecision.com/newsroom/portland-public-schools-sweeping-closure-plan | HTTP 410 Gone | — |
| Reddit r/portland | Requires login; web search cannot index Reddit | Search r/portland manually for threads with substantive reporting. |
| PAT closure petition (Action Network or similar) | URL not located; PAT's website news page is stale (last item May 2025) | Find the petition URL linked from PAT social media. |
| "Right-Sizing the Right Way" and Title I coalition petitions | URLs not located | Same as above. |
| savepdxschools.org/schools/ and /transcripts/ | JavaScript (Supabase) apps; static HTML is empty | Render in a browser if the school list or transcripts are needed. |
| KPTV video pages (3) | Video only, no transcript | Watch or transcribe if Armstrong's interview statements are needed. |
| SunshinePPS wiki (wiki.sunshinepps.org) | Reachable, but **no rightsizing pages exist**; the last edit was Sept 2025 | Nothing to save. |
| Street Roots, Chalkbeat | Searched (Street Roots via its WP API); **no PPS rightsizing coverage found** | — |
| OregonLive (27 news items + 11 editorials/letters) | Retrieved via browser (curl gets 403); full text present | Optional re-check: OregonLive is metered, but the HTML contained full text. |
| KGW (12 items), Axios (6) | Retrieved via browser (curl gets 403) | — |
| 2026-09-29 board special meeting | No news coverage found | RESOLVED: full transcript at `transcripts/text/2026-09-29_Board_of_Education_Special_Meeting__SPwXuNlwP_U.txt` (bond-audit responses, not rightsizing). |
| 2026-10-06 board meeting minutes, and votes/remarks from 9/1 and 10/6 | Minutes not yet posted | RESOLVED for remarks: full transcripts `transcripts/text/2026-09-01_…__5RMfvT-sAPU.txt` and `transcripts/text/2026-10-06_…__zOUH2Jq7Owo.txt`; per-director excerpts in `board-members/<slug>/*_transcript_excerpts_*.txt`. Formal minutes are still pending. |
