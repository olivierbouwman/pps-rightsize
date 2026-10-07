#!/usr/bin/env python3
"""Summarize ORESTAR transaction exports in board-members/_campaign_finance.
Institutional contributors and political giving out are listed by name;
individual contributors are aggregated (no addresses) with only the largest named."""
import collections, glob, os
import openpyxl

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "board-members", "_campaign_finance")
CONTRIB = {"Cash Contribution", "In-Kind Contribution", "Loan Received (Non-Exempt)", "Pledge of Cash", "Pledge of In-Kind"}
GIVE_OUT_TYPES = {"Political Committee", "Political Party Committee", "Labor Organization", "Other"}
VENDOR_OTHER = ("Secretary of State", "Elections", "DMV", "Postal", "ODOT")


def money(x):
    return f"${x:,.0f}"


def summarize(path):
    ws = openpyxl.load_workbook(path, read_only=True).active
    rows = list(ws.iter_rows(values_only=True))
    hdr, data = rows[0], [dict(zip(rows[0], r)) for r in rows[1:]]
    data = [d for d in data if d["Tran Status"] != "Deleted"]
    filer = data[0]["Filer"] if data else "?"
    by_year = collections.defaultdict(lambda: collections.Counter())
    inst = collections.defaultdict(float)
    indiv = collections.defaultdict(lambda: [0.0, ""])
    misc_small = 0.0
    out = collections.defaultdict(float)
    for d in data:
        amt, yr, st, bt = d["Amount"] or 0, (d["Tran Date"] or "")[-4:], d["Sub Type"], d["Book Type"] or ""
        name = d["Contributor/Payee"]
        if st in CONTRIB:
            by_year[yr]["raised"] += amt
            if name.startswith("Miscellaneous"):
                misc_small += amt
                by_year[yr]["small"] += amt
            elif bt == "Individual":
                indiv[name][0] += amt
                indiv[name][1] = ", ".join(x for x in (d["Occptn Txt"], d["Emp Name"]) if x)
                by_year[yr]["individual"] += amt
            elif "Immediate Family" in bt:
                inst["Candidate self/immediate-family funding (names omitted)"] += amt
                by_year[yr]["institutional"] += amt
            else:
                inst[f"{name} [{bt or 'type n/a'}]"] += amt
                by_year[yr]["institutional"] += amt
        elif st in ("Cash Expenditure", "Personal Expenditure for Reimbursement") and (bt in GIVE_OUT_TYPES or d["Contributor/Payee Committee ID"]) \
                and not any(v in name for v in VENDOR_OTHER):
            out[f"{name} [{bt or 'committee'}]"] += amt
    total = sum(v["raised"] for v in by_year.values())
    lines = [f"## {filer} — `board-members/_campaign_finance/{os.path.basename(path)}`", "",
             f"Total contributions recorded: **{money(total)}** "
             f"(institutional/self {money(sum(inst.values()))}, individuals {money(sum(v[0] for v in indiv.values()))} from {len(indiv)} named donors, "
             f"small-dollar aggregated {money(misc_small)})", "",
             "| Year | Raised | Institutional | Individual | Small (<$100 aggregated) |", "|---|---|---|---|---|"]
    for y in sorted(by_year):
        c = by_year[y]
        lines.append(f"| {y} | {money(c['raised'])} | {money(c['institutional'])} | {money(c['individual'])} | {money(c['small'])} |")
    lines += ["", "**Institutional contributors (unions, PACs, parties, businesses, committees) and self-funding:**", ""]
    lines += [f"- {k}: {money(v)}" for k, v in sorted(inst.items(), key=lambda kv: -kv[1])] or ["- none"]
    top = sorted(indiv.items(), key=lambda kv: -kv[1][0])[:10]
    lines += ["", "**Largest individual contributors (top 10; occupation/employer as reported):**", ""]
    lines += [f"- {k}: {money(v[0])}" + (f" — {v[1]}" if v[1] else "") for k, v in top] or ["- none"]
    lines += ["", "**Money given to other campaigns, parties and organizations (vendors excluded; signals alignment):**", ""]
    lines += [f"- {k}: {money(v)}" for k, v in sorted(out.items(), key=lambda kv: -kv[1]) if v >= 100] or ["- none"]
    return "\n".join(lines) + "\n"


def main():
    parts = ["# Campaign finance summary (ORESTAR exports, pulled 2026-10-07)", "",
             "Source: Oregon SoS ORESTAR transaction search, export per committee. Deleted transactions excluded. "
             "Patte Sullivan has no ORESTAR committee (consistent with reports she raised/spent under the $750 filing threshold). "
             "Michelle DePass's committee 19811 also covers her 2024 Portland City Council race.", ""]
    for p in sorted(glob.glob(os.path.join(DIR, "orestar_*.xlsx"))):
        parts.append(summarize(p))
    open(os.path.join(DIR, "..", "..", "CAMPAIGN_FINANCE.md"), "w").write("\n".join(parts))
    print("\n".join(parts))


if __name__ == "__main__":
    main()
