"""Draw the deck's one captioned meme, img/drake-hotline.png.

The template is imgflip's "Drake Hotline Bling" (template 181913649), a 1200 x 1200 image whose right half is two white panels. This script writes a caption into each panel, so the meme can be redrawn with new wording.

Run from this talk's folder: python3 code/make_memes.py
"""
import io
import textwrap
import urllib.request

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "https://i.imgflip.com/30b1gx.jpg"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
# The two captions: the top panel is the one Drake waves away, the bottom the one he points at
CAPTIONS = ["Buying a chatbot to answer council's questions",
            "Publishing the records its answers would cite"]


def draw_caption(draw, box, text, font):
    """Center text, wrapped to fit, inside box = (left, top, right, bottom)."""
    left, top, right, bottom = box
    lines = textwrap.wrap(text, width=14)
    heights = [draw.textbbox((0, 0), line, font=font)[3] for line in lines]
    y = top + (bottom - top - sum(heights) - 12 * (len(lines) - 1)) / 2
    for line, height in zip(lines, heights):
        width = draw.textlength(line, font=font)
        draw.text((left + (right - left - width) / 2, y), line, fill="black", font=font)
        y += height + 12


request = urllib.request.Request(TEMPLATE, headers={"User-Agent": "WebDataScience/1.0 (brian.keegan@colorado.edu)"})
image = Image.open(io.BytesIO(urllib.request.urlopen(request, timeout=60).read())).convert("RGB")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(FONT, 58)
half = image.height // 2
draw_caption(draw, (620, 20, 1180, half - 20), CAPTIONS[0], font)
draw_caption(draw, (620, half + 20, 1180, image.height - 20), CAPTIONS[1], font)
image.save("img/drake-hotline.png")
print("wrote img/drake-hotline.png", image.size)
