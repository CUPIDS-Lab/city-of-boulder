# Long Data: Emerging Technologies Taskforce, October 21, 2026

Brian Keegan's talk to the City of Boulder's Emerging Technologies Taskforce
(October 21, 2026, 4:00–5:30pm, virtual), on "Emerging technology for improved
access to and use of historic documentation." The slot is up to 15 minutes, and
the audience is general: taskforce members, city staff, and residents.

| File | What it is |
|---|---|
| `2026-10-21-ett.tex` | The deck source (Beamer) |
| `2026-10-21-ett.pdf` | The deck: 21 numbered frames and 4 appendix frames |
| `2026-10-21-ett-notes.pdf` | The same deck with a page of speaker notes after each frame |
| `common/` | The INFO 4617 course's Gotham theme and preamble, copied (see below) |
| `img/` | The figures and memes the deck shows; `img/IMAGES.md` says where each came from |
| `code/` | `long-data-analysis.ipynb`, which makes the hotline and budget charts; the hotline labels it saves; the Assistant font; and the script that captions the one new meme |

## Building

From this folder, with TeX Live (the packages the course's CI installs:
`texlive-latex-extra`, `texlive-fonts-extra`, and `latexmk`):

```bash
latexmk -pdf 2026-10-21-ett.tex
latexmk -pdf -jobname=2026-10-21-ett-notes -usepretex='\def\shownotes{}' 2026-10-21-ett.tex
```

The build needs no biber: sources are cited in each frame's bottom line.

## Format

The deck uses the INFO 4617 theme and preamble
([`cuinfoscience/INFO4617-Fall2026`](https://github.com/cuinfoscience/INFO4617-Fall2026),
`slides/common/`), copied into `common/` without biblatex and the `\cupids`
logo macro. Three rules of its own:

- No section dividers.
- No `block` environments. A frame defaults to plain text and carries at most
  one `alertblock`; most carry none.
- The outlook and risk frames put the argument in a left column and a meme in
  the right.

## The story

The council hotline opens the talk with a question (could the city's own
records answer council's questions, and could a machine find them?), and the
rest of the deck answers it:

1. **Terms.** Long data; document understanding, defined and scoped; data
   liberation, defined, with precedents and possible uses for the city.
2. **What we know today.** Two liberation sprints, then *Web Data Science*
   chapter 9's revenue-report case study: the records portal's folder
   listing, one report's totals row and its check, and the 2017–2024 chart.
   Nothing new was requested from the city's server for this talk.
3. **The hotline case study.** The data and method (moved from the appendix),
   what council asks about, what the answers needed, and what to liberate
   first.
4. **Obligations.** Accessibility law, the Colorado Open Records Act, and the
   city's Sustainability, Equity and Resilience Framework.
5. **Outlook and risks.** What happens next, why I might be wrong, records
   that shouldn't become data, and who bears the cost. The hotline returns in
   each.

The deck calls the city's document system "the city's records portal" and
never names its software, as the taskforce asked. The appendix code leaves the
portal's addresses to chapter 9. The source URLs in `img/IMAGES.md` are the
city's own addresses and appear only there.

## Where each taskforce prompt is answered

Each frame's speaker note starts with the prompt it answers. Frame numbers are
the ones in each slide's footer; the title page is not counted.

| Taskforce prompt | Frames |
|---|---|
| Overview of the topic, technology, or trend | 1 The council hotline; 2 Long data; 3 Document understanding |
| What do we know today? | 2 Long data; 6 Two liberation sprints; 7–9 the revenue-report demo; 10 The hotline data |
| What do we think will happen? Why might we be wrong? | 17 What happens next; 18 Why I might be wrong |
| Relevant examples, kept general | 4 Data liberation |
| Potential implications for the city | 5 What liberation could do for the city; 11 What council asks about; 12 What the answers needed; 13 What to liberate first |
| Key opportunities and risks in adoption | 5; 13; 14 Accessibility; 15 The Colorado Open Records Act; 16 Community values; 19 Some records shouldn't become data |
| Would impacts be disproportionately felt in our community? | 20 Who bears the cost |
| What would the city need to do to mitigate impacts? | 16 Community values; 19; 20; 21 Key takeaways |

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
   Charting Boulder budget-history folder (`BUDGET_CSV`).

Charts use the City of Boulder's brand colors and Assistant, the brand's
alternative typeface (`code/fonts/`, SIL Open Font License), on white.

The hand-coded sample of 40 staff responses was drawn from messages through
September 15, 2026, and the notebook draws the same sample. The coding sheet
itself (`hotline-sample-coding.csv`) is not in this folder yet.
