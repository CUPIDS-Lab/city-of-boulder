# Working in this repository

Instructions for coding agents (Claude Code, Codex, and others) and for people
who work here. Each talk or project has its own folder, such as
`2026-10-21-ett/`, with a `README.md` that says what it is and how to build it.

## Slide decks

- **No speaker notes.** Decks carry no `\note{...}`, and the repository holds
  no notes PDF. What a speaker would say lives in the speaker, not the file.
  When you edit a deck, don't add notes; if you find one, remove it.
  (Decided 2026-10-21.)
- **No section dividers, and no `block` environments.** A frame defaults to
  plain text and carries at most one `alertblock`. (Decided 2026-10-20.)
- **Text lines up at the margins.** Decks load beamer's `onlytextwidth` class
  option, so column text starts where text outside columns does. A list that
  sits under a heading uses `\flushitems` (in the deck's preamble) so its
  bullets align with the heading.
- **Build it before you push it.** The instructor edits in Overleaf, which
  pushes to `main`, sometimes with errors in it. After any change, build with
  `latexmk -pdf` from the deck's folder and read the log for `!` errors,
  `Overfull` boxes, and `Missing character` warnings: a missing character
  prints nothing on the slide and raises no error. Commit the rebuilt deck
  PDF.

## Figures

- **White or transparent backgrounds**, always. Re-export a chart from the
  code that draws it; don't patch an exported file. (Decided 2026-10-20.)
- **City of Boulder brand identity** for charts and diagrams: colors from the
  city's "City Colors" palette (bouldercolorado.gov/brand) and Assistant, the
  brand's named alternative to Adelle Sans. Check a categorical palette for
  contrast on white and for color-vision deficiency before using it.
  (Decided 2026-10-20.)
- Each image gets a row in its folder's `img/IMAGES.md`: what it is, how it
  was made, and its source.

## Branches and pull requests

- Start each change from a fresh `origin/main`: Overleaf pushes to `main`
  without warning, and when it can't merge it opens an `overleaf-*` branch
  and pull request instead.
- One pull request per change. Merge only when the instructor asks, with a
  merge commit and the expected head SHA. Don't rebase or force-push a branch
  someone may have seen.
- A pull request description says what changed, why, what you checked, and
  what you left alone on purpose.
