# Images

Where each image in the deck came from, by the title of the frame that shows
it. Frames are named rather than numbered, because numbers shift as frames are
added. Four images are charts drawn from data; the rest are a screenshot, a
table crop, and memes added in Overleaf, whose sources are still to be
recorded.

| File | Frame | Kind | Made | Source |
|---|---|---|---|---|
| `datalab.png` | Document understanding | screenshot | added in Overleaf on 2026-10-20 (commit `818d68a`) | not yet recorded: the page it shows, its URL, and the capture date |
| `budget-index.png` | Twenty-two years of the city's budget | chart | 2026-10-20, matplotlib, by `code/long-data-analysis.ipynb` | `budget-history-wide.csv` in the Charting Boulder budget-history folder (`brianckeegan/charting-boulder-private`, `2027-XX-budget-history/`, commit `a0e3825`), which transcribes the city's budget books and annual financial reports. Staffing, sales and use tax, property tax, and the capital budget, 2005–2026, each indexed to 2005 = 100, with the dollar series in constant 2005 dollars (BLS CPI-U, Denver–Aurora–Lakewood, saved as `code/denver-cpi.csv`) |
| `revenue.png` | Teaching with the city's records portal | table crop | added in Overleaf on 2026-10-20 (commit `1b32e7c`) | appears to be "Table 1 - Sales and Use Tax" from the city's 2018 year-end revenue report; page and crop still to be recorded |
| `sales-use-tax.png` | Teaching with the city's records portal | chart (render) | 2026-10-12, matplotlib from pdfplumber readings, by the textbook's `tools/shots/renders/ch-09.py` | `cuinfoscience/Web-Data-Science-Book`, `images/ch-09/sales-use-tax.png`, copied unchanged on 2026-10-20 |
| `deck-themes-by-quarter.pdf` | Analyzing hotline: questions from council | chart | 2026-10-20, matplotlib, by `code/long-data-analysis.ipynb`, from messages through October 15, 2026 (complete quarters shown) | City of Boulder open data, "Emails to the City Council Hotline" (CC0) |
| `deck-records-needed.pdf` | Analyzing hotline: answers from staff | chart | as above | as above |
| `responsive.jpg` | Accessibility and CORA/FOIA | meme | added in Overleaf on 2026-10-20 (commit `5b6e796`) | not yet recorded: the template and where it came from |
| `iceberg.jpg` | Community values | meme | added in Overleaf on 2026-10-20 (commit `8ba9e26`) | not yet recorded |
| `georgi.jpg` | What happens next | meme | added in Overleaf on 2026-10-20 (commit `1eb238b`) | not yet recorded |
| `chart.jpg` | Why I might be wrong | meme | added in Overleaf on 2026-10-20 (commit `1eb238b`) | not yet recorded |
| `ignoring.jpg` | Other risks | meme | added in Overleaf on 2026-10-20 (commit `1eb238b`) | not yet recorded |
| `hotline-theme-by-records.pdf` | Appendix: which records each theme depends on | chart | 2026-10-20, matplotlib, by `code/long-data-analysis.ipynb` | as `deck-themes-by-quarter.pdf` |

## Notes

- The hotline charts' data layer is
  `https://services.arcgis.com/ePKBjXrBZ2vEEgWd/arcgis/rest/services/Emails_to_the_City_Council_Hotline/FeatureServer/0`.
- `sales-use-tax.png` (SHA-256 `e7121ed3ffb7ec72f353b9bd01841970748a28a095f509844b2299688e52797f`)
  is drawn from the textbook's saved copies of seven year-end revenue reports,
  retrieved from the city's records portal on October 6, 2026. The folder is
  `https://documents.bouldercolorado.gov/WebLink/Browse.aspx?id=194345&dbid=0&repo=LF8PROD2`;
  the textbook's `data/ch-09/manifest.csv` lists each file's URL, size, and
  checksum. To refresh the chart, retake it in the textbook and copy it here
  again. The textbook's `tools/shots/run sync` writes to the course repository,
  so this copy was made by hand.
- Every chart from data is drawn by `code/long-data-analysis.ipynb` on a white
  background, in the City of Boulder's brand colors ("City Colors",
  bouldercolorado.gov/brand) and Assistant, the brand's alternative typeface.
  The heat maps run from Glacier Blue to Winter Night; bars are Boulder Blue.
  The budget chart's four lines (Winter Night, Buffalo Bronze, Boulder Blue,
  Red Rocks Rust) each reach 4.5:1 on white and stay at least 22 apart in
  CIELAB under simulated deutan, protan and tritan vision. On 2026-10-20 the
  three hotline charts were redrawn this way, replacing the original deck's
  cream-background versions.
- `budget-index.png` is 1920 x 1080 pixels (16:9). Capital starts in 2005, so
  every series is indexed to 2005 rather than 2002. The capital line is the
  adopted capital budget, a plan rather than actual spending.
  Since 2026-10-21 the three dollar series are deflated to constant 2005
  dollars by the Denver–Aurora–Lakewood CPI-U: annual averages from BLS's
  semiannual series (`CUUSS48BSA0`, `S03`), and for 2026, which has no annual
  average yet, the mean of its bimonthly readings through September
  (`CUURS48BSA0`). Prices rose about 82% over the period.
- `sales-use-tax.png` is the textbook's figure, copied unchanged, so it keeps
  the textbook's colors.
