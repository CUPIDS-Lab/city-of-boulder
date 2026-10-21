# Long Data: Emerging Technologies Taskforce, October 21, 2026

Brian Keegan's talk to the City of Boulder's Emerging Technologies Taskforce
(October 21, 2026, 4:00–5:30pm, virtual), on "Emerging technology for improved
access to and use of historic documentation." The slot is up to 15 minutes, and
the audience is general: taskforce members, city staff, and residents.

| File | What it is |
|---|---|
| `2026-10-21-ett.tex` | The deck source (Beamer) |
| `2026-10-21-ett.pdf` | The deck: a title page, 19 numbered frames, and 2 appendix frames |
| `common/` | The INFO 4617 course's Gotham theme and preamble, copied (see below) |
| `img/` | The figures and memes the deck shows, and nothing it doesn't; `img/IMAGES.md` says where each came from |
| `code/` | `long-data-analysis.ipynb`, which makes the hotline and budget charts; the hotline labels and price index it saves; and the Assistant font |

## Building

From this folder, with TeX Live (the packages the course's CI installs:
`texlive-latex-extra`, `texlive-fonts-extra`, and `latexmk`):

```bash
latexmk -pdf 2026-10-21-ett.tex
```

The build needs no biber: sources are cited in each frame's bottom line.

## Format

The deck uses the INFO 4617 theme and preamble
([`cuinfoscience/INFO4617-Fall2026`](https://github.com/cuinfoscience/INFO4617-Fall2026),
`slides/common/`), copied into `common/` without biblatex and the `\cupids`
logo macro. Its own rules (the repository's `AGENTS.md` has the reasons):

- No section dividers.
- No `block` environments. A frame defaults to plain text and carries at most
  one `alertblock`; most carry none.
- The outlook and risk frames put the argument in a left column and a meme in
  the right.
- No speaker notes, and no notes PDF.
- Figures use a white or transparent background, and charts and diagrams use
  the City of Boulder's brand colors.

## The story

1. **Terms** (frames 1–4). Long data; document understanding; data
   liberation and rescue, with precedents; and uses for the city.
2. **What we know today** (5–7). Two liberation sprints, the budget index, and
   *Web Data Science* chapter 9's lesson on the city's revenue reports.
3. **The council hotline** (8–11). What council asks, what staff answers
   need, and what to liberate first.
4. **A proposed pipeline** (12). Sources, capture, document understanding, a
   privacy screen, a data lake, and access for agents (MCP) and the public,
   with the points where people check the work. It names no products.
5. **Obligations and values** (13–14). Accessibility law and CORA, and the
   city's Sustainability, Equity and Resilience Framework.
6. **Outlook and risks** (15–19). What happens next, why I might be wrong,
   other risks, key takeaways.

## Where each taskforce prompt is answered

Frame numbers are the ones in each slide's footer; the title page is not
counted.

| Taskforce prompt | Frames |
|---|---|
| Overview of the topic, technology, or trend | 1 Long data; 2 Document understanding; 3 Data liberation and rescue |
| What do we know today? | 5 Two data liberation sprints; 6 Twenty-two years of the city's budget; 7 Teaching with city's records portal; 8–10 the hotline |
| What do we think will happen? Why might we be wrong? | 15 What happens next; 16 Why I might be wrong |
| Relevant examples, kept general | 3 Data liberation and rescue |
| Potential implications for the city | 4 Data liberation for the City of Boulder; 9–10 the hotline analysis; 11 What to liberate first |
| Key opportunities and risks in adoption | 12 A proposed pipeline; 13 Accessibility and CORA/FOIA; 14 Community values; 17 Other risks |
| Would impacts be disproportionately felt in our community? | 17 Other risks |
| What would the city need to do to mitigate impacts? | 12 A proposed pipeline; 14 Community values; 18 Key takeaways |

## The analysis notebook

`code/long-data-analysis.ipynb` makes every chart in the deck that comes from
data, with a Markdown cell before each step. Run it from `code/`.

1. It pulls every record from the city's open data layer "Emails to the City
   Council Hotline" (CC0), keeps messages received through October 15, 2026,
   and sorts the hotline-list traffic by author and function.
2. It labels each message by policy theme and by the kinds of records an
   answer would need, with short keyword dictionaries, and saves the labels
   to `code/hotline-labels-all.csv`. Set `PULL_LIVE = False` to redraw from
   that file without the network.
3. It draws the three hotline charts and prints every hotline number the
   slides quote.
4. It draws the budget index chart from `budget-history-wide.csv` in the
   Charting Boulder budget-history folder (`BUDGET_CSV`), with the dollar
   series deflated to constant 2005 dollars by the Denver–Aurora–Lakewood
   consumer price index, which it downloads from BLS and saves to
   `code/denver-cpi.csv`.

Charts use the City of Boulder's brand colors and Assistant, the brand's
alternative typeface (`code/fonts/`, SIL Open Font License), on white.

The hand-coded sample of 40 staff responses was drawn from messages through
September 15, 2026, and the notebook draws the same sample. The coding sheet
itself (`hotline-sample-coding.csv`) is not in this folder yet.
