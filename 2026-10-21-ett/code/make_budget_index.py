"""Draw img/budget-index.png: staffing, sales and use tax, property tax, and the capital budget, 2005-2026, each indexed to 2005 = 100.

The data is budget-history-wide.csv from the budget-history folder of the Charting Boulder project (brianckeegan/charting-boulder-private, 2027-XX-budget-history/), which transcribes the city's budget books and annual financial reports. That folder is not public yet, so this script reads the CSV from a path you give it and this repository keeps only the chart.

Series and bases, as the wide file picks them (see that folder's data dictionary):
- staffing_fte: adopted full-time-equivalent positions
- salesuse_total, property_tax_revenue: audited collections through 2025, the adopted budget for 2026
- budget_capital: the adopted capital budget, which starts in 2005; it is a plan, not actual capital spending

2005 is the base year because it is the first year with all four series. Money is in nominal dollars, not adjusted for inflation.

Run from this talk's folder:
    python3 code/make_budget_index.py PATH/TO/budget-history-wide.csv
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE_YEAR, LAST_YEAR = 2005, 2026
# Column in the wide file, label on the chart, and color (the deck's Tableau colors, in the preamble's tab-* order)
SERIES = [
    ("budget_capital", "Capital budget", "#E15759"),
    ("property_tax_revenue", "Property tax", "#59A14F"),
    ("salesuse_total", "Sales and use tax", "#F28E2B"),
    ("staffing_fte", "Staff (FTE)", "#4E79A7"),
]

wide = pd.read_csv(sys.argv[1]).set_index("year").loc[BASE_YEAR:LAST_YEAR]

# 16:9 at 200 dpi: 1920 x 1080 pixels, on a white background
fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=200, facecolor="white")
ax.set_facecolor("white")
for column, label, color in SERIES:
    values = wide[column]
    assert values.notna().all(), f"{column} has a gap between {BASE_YEAR} and {LAST_YEAR}"
    index = values / values.loc[BASE_YEAR] * 100
    # A year whose value is a budget rather than a collection gets a dashed segment and an open marker
    basis = wide[column + "_basis"]
    closed = basis == "actual" if (basis == "actual").any() else basis.notna()
    ax.plot(index.index[closed], index[closed], color=color, linewidth=2.6, solid_capstyle="round")
    if not closed.all():
        start = index.index[closed][-1]
        ax.plot(index.loc[start:].index, index.loc[start:], color=color, linewidth=2.6, linestyle=(0, (2, 1.5)))
        ax.plot(index.index[~closed], index[~closed], "o", color=color, markerfacecolor="white", markersize=6, markeredgewidth=2)
    # Label each line at its right end, with its 2026 value
    ax.annotate(f"{label}  {index.iloc[-1]:.0f}", (index.index[-1], index.iloc[-1]), xytext=(8, 0), textcoords="offset points",
                va="center", fontsize=13, color=color, fontweight="bold")
    print(f"{label}: {values.loc[BASE_YEAR]:.2f} in {BASE_YEAR}, {values.iloc[-1]:.2f} in {LAST_YEAR}, index {index.iloc[-1]:.1f}; peak {index.max():.0f} in {index.idxmax()}")

ax.axhline(100, color="#BAB0AC", linewidth=1, zorder=0)
ax.set_xlim(BASE_YEAR - 0.3, LAST_YEAR + 0.3)
ax.set_xticks(range(BASE_YEAR, LAST_YEAR + 1, 3))
ax.set_ylabel(f"Index, {BASE_YEAR} = 100", fontsize=13)
ax.tick_params(labelsize=12, length=0)
ax.grid(axis="y", color="#E6E6E6", linewidth=0.8)
ax.set_axisbelow(True)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("#BAB0AC")
# No footnote in the image: the slide states the bases and the source, at a size the room can read
fig.subplots_adjust(left=0.08, right=0.78, top=0.96, bottom=0.08)
fig.savefig("img/budget-index.png", facecolor="white")
print("wrote img/budget-index.png")
