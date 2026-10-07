#!/usr/bin/env python3
"""Build the chronological markdown table for NEWS_COVERAGE.md from raw/manifest.tsv (+ extra docs)."""
import csv, re, os, glob
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'news')
rows = list(csv.reader(open(f'{BASE}/raw/manifest.tsv'), delimiter='\t'))[1:]
# add hand-made txt files not in manifest (e.g. PDF extraction)
known = {r[3] for r in rows}
for f in glob.glob(f'{BASE}/*.txt'):
    b = os.path.basename(f)
    if b not in known:
        h = dict(l.split(': ', 1) for l in open(f).read().split('\n\n', 1)[0].splitlines() if ': ' in l)
        rows.append([h.get('Date', ''), h.get('Outlet', ''), h.get('Title', ''), b, h.get('URL', ''), h.get('Author', ''), '', h.get('Note', '')])
rows.sort(key=lambda r: (r[0], r[1], r[2]))

OVR = {
 '2026-09-17_citizenportal': 'Board sets rightsizing, facilities and community engagement as annual focus areas (Citizen Portal AI summary; partial).',
 '2026-04-20_oregonian_readers': 'Letter: PPS should build a district families choose rather than only cutting.',
 '2026-03-22_oregonian_readers': 'Letter: PPS erodes trust by dismissing public concerns (MLC/budget context).',
 '2026-02-19_oregonian_readers': 'Letter from an MLC parent urging PPS to keep the MLC high school open; petition >1,500 signatures.',
 '2026-01-21_oregonian': 'PPS floats shedding ~300 positions to close a $50M gap; PAT blames admin growth and state funding.',
 '2026-08-30_oregonian_editorial': 'Editorial: closures are unavoidable but perilous; urges a careful, transparent process and constructive role for officials; notes PAT petition.',
 '2026-06-28_oregonian_editorial': 'Editorial: board was right to reject last-minute amendments (Engelsman, Chase-Miller, La Forte) to restore $13M via reserves.',
 '2026-09-09_wweek': 'PAT, furious over the superintendent contract and closures, signals it will fight consolidation and remember votes at bargaining.',
 '2026-09-30_wweek': 'Draft bond audit of Procedeo keeps the board divided; members restate their Dec. 2025 votes (context for recall effort).',
 '2026-09-20_koin': 'KOIN: families and leaders discuss the "big upheaval" as dozens of PPS schools may close.',
 '2026-09-23_k12dive': 'National roundup: more districts (incl. Portland) face closure decisions in 2026-27.',
 '2026-10-06_axios': 'Axios list of the 14 schools in Scenario A; list is not final, board votes in December.',
 '2026-09-03_k12dive': 'K-12 Dive: PPS presentation says 15 elementary and 3 middle schools would need to close for sustainable enrollment.',
 '2026-03-10_kptv_superintendent-portland': 'Video: Armstrong says 5-10 schools may close next year; central-office furloughs to address deficit.',
 '2026-05-17_oregonian_readers': 'Letter: PPS should not spend billions renovating high schools as child population dwindles.',
 '2025-08-01_oregonian_readers': 'Letter: new board should boost enrollment with focus-area programs.',
 '2025-09-15_oregonian_readers': 'Letter: Access Academy (TAG school) contradicts PPS equity commitment amid consolidation talk.',
 '2026-09-14_oregonian_readers': 'Letter: the 360/500 enrollment thresholds are a false justification for closing 15-20 schools.',
 '2026-10-04_oregonian_readers': 'Letter: closing up to 20 schools affects all Portlanders, not just families.',
 '2026-06-18_opb': 'OPB newsletter: profile of MLC, the district\'s only K-12 school, after its high school grades were cut.',
 '2026-10-06_opb_opbs-first-look': 'OPB newsletter summary of the closure proposals.',
 '2026-05-13_oregonian': 'Community budget review committee warns PPS budget assumptions may worsen its deficit.',
 '2026-07-31_wweek': 'PPS-commissioned 150-page evaluation of the Southeast Guiding Coalition rebalancing offers lessons ahead of closures.',
 '2026-08-27_oregonian': 'Early clues on which buildings could be closure candidates; board principles say no corner of the district is off-limits.',
 '2025-04-23_yahoo': 'KOIN (syndicated): Armstrong presents 2025-26 budget with hundreds of position cuts amid a ~$40M deficit, third straight deficit year.',
 '2025-04-27_oregonian_editorial-endorsement': 'Oregonian editorial board endorses Splitt (Z1), Greene (Z4), La Forte (Z5), Engelsman (Z6); candidate profiles.',
 '2025-05-02_kgw': 'Candidate guide for the May 2025 PPS board races (Zones 1, 4, 5, 6) incl. endorsements by sitting board members, PAT, councilors.',
 '2025-08-27_wweek_murmurs': 'Armstrong, on first day of school, says a top 2025-26 priority is tackling enrollment and likely consolidating schools; PAT video decries "false promises of consolidation".',
 '2026-01-14_axios': 'Board-approved NE Portland high school boundary change shifts students to Jefferson (enrollment balancing precursor).',
 '2026-02-05_kptv': 'PPS leaders warn lawmakers a $50M cut could eliminate ~300 jobs and close a school; Chair Wang calls it an emergency.',
 '2026-02-18_wweek': 'Seismic-retrofit prioritization collides with looming closures; Chase-Miller warns past closure decisions favored affluent, white schools.',
 '2026-02-24_wweek': 'PPS abruptly closes MLC high school grades; families question process (preview of districtwide closure fights).',
 '2026-03-10_katu_portland-public-schools-board-mulls': 'Board discusses possible closures alongside seismic priorities; Engelsman asks when a school would be declared "staying open".',
 '2026-03-13_opb_portland-public-schools-now': 'OPB interview: Armstrong says 5-10 of 74 schools may close by fall 2027; budget hole deepens; PAT criticizes admin staffing.',
 '2026-03-13_opb_portland-public-schools-superintendent': 'Armstrong defends budget approach as PAT blames administrators and calls for systemic change.',
 '2026-03-10_wweek': 'Armstrong: PPS could close 5-10 of its 74 elementary/K-8/middle/alternative schools by fall 2027; recommendation due late fall 2026.',
 '2026-04-22_mercury': 'PPS budget crisis: parents and PAT look to Gov. Kotek/Legislature and the Education Stability Fund; Kotek office declines.',
 '2026-04-22_wweek': 'What closing a Title I school costs a neighborhood; parent coalition of Title I schools forms; Chase-Miller on resource risks.',
 '2026-04-23_kptv': 'Parents air concerns at a board community session about potential closures.',
 '2026-04-23_opb': 'At an engagement session PPS asks what to weigh when closing schools (up to ~12 of 81); Wang describes "properly resourced" goal.',
 '2026-04-28_katu': 'KATU morning rundown; item on PPS continuing "right-sizing" talks.',
 '2026-05-01_northpeninsulareview': 'Guest column questioning whether closing ~10 elementary schools would actually save money.',
 '2026-06-24_oregonian_enrollment-falls': 'Blended/multi-grade classrooms spread as enrollment falls at Portland elementary schools.',
 '2026-06-25_opb': 'Board passes $2.77B 2026-27 budget after midnight; Engelsman abstains; failed amendments to restore $13.1M of positions.',
 '2026-07-08_axios': 'Census data: Western under-18 population fell 5.7% 2020-25; implications for Portland schools.',
 '2026-08-26_oregonian': 'As PPS weighs sweeping closures, parents at small schools wonder which will survive; unanswered questions on layoffs and savings.',
 '2026-08-26_wweek': 'Armstrong says closures could total 10-20 schools (up from 5-10); draft list to board in November.',
 '2026-08-27_mercury': 'Mercury morning roundup; item: PPS weighs school downsizing of up to 20 schools.',
 '2026-08-28_wweek': 'District model: closing 15 of 45 elementaries would put all remaining at the 360-student QEM threshold by 2031-32.',
 '2026-09-01_katu_today': 'KATU morning rundown; item on PPS possibly closing 15 schools.',
 '2026-09-01_northpeninsulareview': 'Armstrong opens the school year at Rosa Parks Elementary; DePass and Chase-Miller attend.',
 '2026-09-01_kgw': 'Preview of Sept. 1 board meeting on rightsizing that could close up to 20 schools.',
 '2026-09-02_katu_today': 'KATU morning rundown; item on board\'s "sobering conversation" about closures.',
 '2026-09-02_wweek': 'Board approves Armstrong contract extension 5-2 (La Forte, Engelsman no); Wang and Splitt explain timing.',
 '2026-09-03_kptv': 'Board approves superintendent pay raise/extension amid closure talks; Councilor Koyama Lane objects.',
 '2026-09-03_wweek': 'Rundown of where each of the seven directors stood on closures after the Sept. 1 meeting.',
 '2026-09-16_wweek_murmurs': 'Murmurs item: PPS data shows Title I schools disproportionately underenrolled; Title I parent coalition responds.',
 '2026-09-16_wweek_happen': 'What happens to closed buildings: leasing, sale, housing ideas; Chase-Miller floats Austin-style housing conversions.',
 '2026-10-05_kptv_full': 'Video: full Armstrong interview on closures and the $65M shortfall.',
 '2026-10-06_kptv_interview': 'Video: KPTV interview with Armstrong on the closure plan.',
 '2026-10-06_mercury': 'Mercury morning roundup; lead item on PPS releasing 14-school closure scenarios.',
 '2026-10-06_portlandtribune': 'Scenario A closes 14, B closes 11, C defers; PAT petition demands boundary changes, central-office cuts, sale of HQ.',
 '2026-10-07_kptv_pps-board-member': 'La Forte says some schools must close but she is still weighing the proposal; parents at James John react.',
 '2026-10-07_kptv_betrayal': 'Parents call the proposal "a betrayal" at the Oct. 6 board meeting; PAT president asks how closures help students.',
 '2026-10-07_pps_board-members': 'PPS official roster page (zones, terms, student representative).',
 '2026-10-07_pps_frequently': 'PPS rightsizing FAQ (official).',
 '2026-10-07_pps_rightsize': 'PPS rightsizing landing page (official): engagement sessions, scenarios, feedback channels.',
 '2026-10-07_pps_timeline': 'PPS rightsizing timeline page (official): phases and milestones.',
 '2026-10-07_savepdxschools_about': 'Save PDX Schools "About" page (parent-run).',
 '2026-10-07_savepdxschools_rightsizing': 'Save PDX Schools main page: "Rightsizing is wrong for Portland" - evidence summary, action steps.',
 '2026-10-07_savepdxschools_write': 'Save PDX Schools letter-writing tool to the board, legislators, governor (not used).',
 '2026-10-07_ppsclosures': 'Independent data explorer for all 74 in-scope schools, incl. parsed Oct. 2026 scenarios.',
 '2026-09-27_savepdxschools': 'Save PDX Schools evidence deck for PTAs: closures save little (<$1M/building net) and harm students.',
 '2025-09-17_wweek': 'New board leadership (Wang, DePass) wants "big-picture" governance; La Forte and Engelsman push back on unity framing.',
 '2026-02-25_wweek': 'Board grapples with abrupt MLC high school closure; La Forte, Engelsman, Sullivan, Chase-Miller question process; Wang, DePass back staff.',
 '2026-10-06_northpeninsulareview': 'Former board members predict a parent/teacher coalition could stop closures; Councilor Dan Ryan says closures affect whole city.',
 '2026-09-11_katu': 'Statewide enrollment fell 9,000+ in 2025-26; more Oregon school closures likely.',
 '2026-06-30_wweek': 'Analysis: 6-1 rejection of Engelsman\'s $13.2M amendment splits board from PAT, which eyes 2027 board races.',
}
def gist_for(file):
    for k, v in OVR.items():
        if file.startswith(k): return v
    t = open(f'{BASE}/{file}').read().split('\n\n', 1)
    body = t[1] if len(t) > 1 else ''
    paras = [p.strip() for p in body.split('\n') if len(p.strip()) > 90]
    lede = paras[0] if paras else ''
    lede = re.sub(r'^PORTLAND,? (Ore\.?|Oregon)\s*(\([A-Za-z ]*\))?\s*[—–-]+\s*', '', lede)
    lede = re.sub(r'\b(Dr|Ore|St|Sen|Rep|Gov|Jan|Feb|Aug|Sept|Oct|Nov|Dec|No)\.', r'\1<DOT>', lede)
    s = re.split(r'(?<=[.!?])\s+(?=[A-Z“"])', lede)[0].replace('<DOT>', '.')
    if len(s) > 220: s = s[:217].rsplit(' ', 1)[0] + '…'
    return s
out = ['| Date | Outlet | Title | File | Gist |', '|---|---|---|---|---|']
for r in rows:
    date, outlet, title, file = r[0], r[1], r[2], r[3]
    note = r[7] if len(r) > 7 else ''
    flag = ''
    if note.startswith('PARTIAL'): flag = ' (partial: login wall)'
    elif 'VIDEO' in open(f'{BASE}/{file}').read()[:2000]: flag = ' (video page)'
    g = gist_for(file).replace('|', '/')
    t = title.replace('|', '/')
    out.append(f'| {date} | {outlet} | {t}{flag} | [{file}]({file}) | {g} |')
open(f'{BASE}/raw/table.md', 'w').write('\n'.join(out) + '\n')
print(len(rows))
