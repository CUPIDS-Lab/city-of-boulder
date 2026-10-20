# Long Data: Emerging Technologies Taskforce, October 21, 2026

Brian Keegan's talk to the City of Boulder's Emerging Technologies Taskforce
(October 21, 2026, 4:00–5:30pm, virtual), on "Emerging technology for improved
access to and use of historic documentation." The slot is up to 15 minutes.

| File | What it is |
|---|---|
| `2026-10-21-ett.tex` | The deck source (Beamer) |
| `2026-10-21-ett.pdf` | The deck: 22 numbered frames, 5 section dividers, 5 appendix frames |
| `2026-10-21-ett-notes.pdf` | The same deck with a page of speaker notes after each frame |
| `common/` | The INFO 4617 course's Gotham theme and preamble, copied (see below) |
| `img/` | The figures the deck shows; `img/IMAGES.md` says where each came from |
| `code/` | The hotline scripts and their labeled output |

## Building

From this folder, with TeX Live (the packages the course's CI installs:
`texlive-latex-extra`, `texlive-fonts-extra`, and `latexmk`):

```bash
latexmk -pdf 2026-10-21-ett.tex
latexmk -pdf -jobname=2026-10-21-ett-notes -usepretex='\def\shownotes{}' 2026-10-21-ett.tex
```

The build needs no biber: sources are cited in each frame's bottom line.

## Format

The deck follows the INFO 4617 slide format
([`cuinfoscience/INFO4617-Fall2026`](https://github.com/cuinfoscience/INFO4617-Fall2026),
`slides/common/AUTHORING.md`):

- `common/` holds copies of the course's Gotham theme files, unchanged, and of
  its `preamble.tex`, without biblatex and the `\cupids` logo macro.
- Frame titles are bare and factual. A frame's so-what sits in a
  `Consequences` block at the bottom, in place of the original's red one-line
  closers.
- There are no `[standout]` frames. The last frame is "Key takeaways."
- Sources go in `\bottomcite` lines.

The deck keeps the original's order of frames. The original source, as
uploaded, is in this folder's git history (the first commit).

## The demo

Frames 7–9 are the revenue-report case study from chapter 9 of *Web Data
Science* ([`cuinfoscience/Web-Data-Science-Book`](https://github.com/cuinfoscience/Web-Data-Science-Book),
`ch-09-pdfs.qmd`, "Getting the Files" and "Case Study: Boulder Revenue
Reports"). They show the chapter's printed output and its chart, unchanged.
Nothing new was requested from the city's server for this talk. The code is in
the last two appendix frames, condensed from the chapter.

The taskforce asked speakers not to comment on specific providers, so the deck
calls the city's document system "the city's records portal" and never names
its software. That includes the appendix code, which leaves the portal's
addresses to chapter 9. The source URLs in `img/IMAGES.md` are the city's own
addresses and appear only there.

## Where each taskforce prompt is answered

Each frame's speaker note starts with the prompt it answers.

| Taskforce prompt | Frames |
|---|---|
| Overview of the topic, technology, or trend | 1 Long data; 2 Retrieval fits long data; 3 Erosion, enclosure, exemption |
| What do we know today? | 4 The city charter; 5 What the city holds; 6 Two liberation sprints; 7–9 the revenue-report demo |
| What do we think will happen? Why might we be wrong? | 18 What happens next, and why I might be wrong |
| Relevant examples, kept general | 4 The city charter; 17 Examples from other sectors |
| Potential implications for the city | 11 What council asks about; 12 The council hotline; 13 What to liberate first |
| Key opportunities and risks in adoption | 14 Accessibility remediation; 16 Community capacity; 19 Three kinds of holdings; 20 Shouldn't become data |
| Would impacts be disproportionately felt in our community? | 21 Would impacts fall unevenly in our community? |
| What would the city need to do to mitigate impacts? | 10 Archive, derived, and retrieval layers; 15 Vendor lock-in; 19–20; 22 Key takeaways |

(Frame numbers are the ones in each slide's footer; the title page and the
section dividers are not counted.)

## The hotline scripts

`code/hotline_provocation.py` pulls every record from the city's open data
layer "Emails to the City Council Hotline" (CC0) and sorts list traffic by
author and function. `code/hotline_themes.py` labels each message by policy
theme and by the records an answer would need; `code/hotline-labels-all.csv`
is its output for the 779 hotline-list messages. The hand-coded sample of 40
staff responses (`hotline-sample-coding.csv`, named in
`hotline_provocation.py`) is not in this folder yet.
