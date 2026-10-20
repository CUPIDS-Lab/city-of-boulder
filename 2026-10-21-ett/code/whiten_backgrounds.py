"""Turn the cream background (#FAF8F5) of the hotline charts' PDFs white.

The three hotline charts in img/ were drawn by matplotlib with the original deck's "paper" color as their background. Their plotting code is not in this folder, so instead of redrawing them, this script rewrites each page's content stream, replacing that one fill color with white. Nothing else in the chart changes.

Run from this talk's folder: python3 code/whiten_backgrounds.py
"""
import re

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, NameObject

FILES = ["img/deck-themes-by-quarter.pdf", "img/deck-records-needed.pdf", "img/hotline-theme-by-records.pdf"]
# #FAF8F5 as matplotlib writes an RGB fill: each channel over 255, to ten decimals, sometimes broken across lines
CREAM = re.compile(rb"0\.9803921569\s+0\.9725490196\s+0\.9607843137\s+rg")
WHITE = b"1 1 1 rg"

for path in FILES:
    reader = PdfReader(path)
    writer = PdfWriter(clone_from=reader)
    replaced = 0
    for page in writer.pages:
        data = page.get_contents().get_data()
        data, count = CREAM.subn(WHITE, data)
        replaced += count
        stream = ContentStream(None, writer)
        stream.set_data(data)
        page[NameObject("/Contents")] = writer._add_object(stream)
    writer.write(path)
    print(path, "fills replaced:", replaced)
