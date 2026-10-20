# Images

Where each image in the deck came from. None is a screenshot: three are charts
drawn from the city's open data, one is a chart from the textbook, and four are
memes for the outlook and risk frames.

| File | Frame | Kind | Made | Source |
|---|---|---|---|---|
| `deck-themes-by-quarter.pdf` | 11 What council asks about | chart | by Brian Keegan with `code/hotline_themes.py`, from data through September 15, 2026 | City of Boulder open data, "Emails to the City Council Hotline" (CC0) |
| `deck-records-needed.pdf` | 12 What the answers needed | chart | as above | as above |
| `hotline-theme-by-records.pdf` | Appendix: which records each theme depends on | chart | as above | as above |
| `sales-use-tax.png` | 9 Eight years of sales and use tax | chart (render) | 2026-10-12, matplotlib from pdfplumber readings, by the textbook's `tools/shots/renders/ch-09.py` | `cuinfoscience/Web-Data-Science-Book`, `images/ch-09/sales-use-tax.png`, copied unchanged on 2026-10-20 |
| `drake-hotline.png` | 17 What happens next | meme | 2026-10-20, captioned by `code/make_memes.py` | imgflip template "Drake Hotline Bling" (181913649), https://i.imgflip.com/30b1gx.jpg |
| `this-is-fine.jpg` | 18 Why I might be wrong | meme | copied unchanged on 2026-10-20 | `cuinfoscience/INFO4617-Fall2026`, `slides/week-02/img/this-is-fine.jpg` (K. C. Green's "This is fine"), the instructor's pick |
| `ben-parker.jpg` | 19 Some records shouldn't become data | meme | copied unchanged on 2026-10-20 | `cuinfoscience/INFO4617-Fall2026`, `slides/week-02/img/ben-parker.jpg` (Uncle Ben, *Spider-Man*, 2002), the instructor's pick |
| `archives-are-incomplete.jpg` | 20 Who bears the cost | meme | copied unchanged on 2026-10-20 | `cuinfoscience/INFO4617-Fall2026`, `slides/week-07/img/archives-are-incomplete.jpg` (*Star Wars: Episode II*, "Perhaps the archives are incomplete"), the instructor's pick |

## Notes

- The three hotline charts came with the talk's original upload. The script
  that draws them is in `code/`; the data layer is
  `https://services.arcgis.com/ePKBjXrBZ2vEEgWd/arcgis/rest/services/Emails_to_the_City_Council_Hotline/FeatureServer/0`.
- `sales-use-tax.png` (SHA-256 `e7121ed3ffb7ec72f353b9bd01841970748a28a095f509844b2299688e52797f`)
  is drawn from the textbook's saved copies of seven year-end revenue reports,
  retrieved from the city's records portal on October 6, 2026. The folder is
  `https://documents.bouldercolorado.gov/WebLink/Browse.aspx?id=194345&dbid=0&repo=LF8PROD2`;
  the textbook's `data/ch-09/manifest.csv` lists each file's URL, size, and
  checksum. To refresh the chart, retake it in the textbook and copy it here
  again. The textbook's `tools/shots/run sync` writes to the course repository,
  so this copy was made by hand.
- The program output on frames 7 and 8 is set as text, not as an image. It is
  what chapter 9's code prints, copied from `ch-09-pdfs.qmd`.
