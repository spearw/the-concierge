"""Generate a print-ready 'scan me' card (poker size, 2.5 x 3.5in) as a PDF.

Vector QR is baked into the PDF via reportlab, so it stays crisp at any size.
Run:  uv run --with reportlab --python 3.12 python card_gen.py
"""
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

URL = "https://spearw.github.io/the-concierge/"
OUT = r"D:\dev\the-concierge\card.pdf"

W, H = 2.5 * inch, 3.5 * inch
NAVY = HexColor("#0a0c12")
GOLD = HexColor("#c9a24b")
GOLD_SOFT = HexColor("#a98c44")
CREAM = HexColor("#f3ecda")
WHITE = HexColor("#ffffff")

c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle("The Parlour - invitation")
cx = W / 2.0

# background
c.setFillColor(NAVY)
c.rect(0, 0, W, H, fill=1, stroke=0)

# double border (cut guide)
c.setStrokeColor(GOLD); c.setLineWidth(1)
c.rect(8, 8, W - 16, H - 16, fill=0, stroke=1)
c.setStrokeColor(GOLD_SOFT); c.setLineWidth(0.4)
c.rect(11.5, 11.5, W - 23, H - 23, fill=0, stroke=1)


def caps(cx, y, text, font, size, color, track):
    c.setFont(font, size); c.setFillColor(color)
    widths = [c.stringWidth(ch, font, size) for ch in text]
    total = sum(widths) + track * (len(text) - 1)
    x = cx - total / 2.0
    for ch, wch in zip(text, widths):
        c.drawString(x, y, ch)
        x += wch + track


# wordmark
caps(cx, H - 28, "THE PARLOUR", "Helvetica-Bold", 9, GOLD, 2.3)
caps(cx, H - 39, "A PRIVATE GAMES CONCIERGE", "Helvetica", 5.5, GOLD_SOFT, 1.3)
c.setStrokeColor(GOLD_SOFT); c.setLineWidth(0.5)
c.line(cx - 26, H - 47, cx + 26, H - 47)

# monogram
mc_y = H - 72
c.setStrokeColor(GOLD); c.setLineWidth(1)
c.circle(cx, mc_y, 16, stroke=1, fill=0)
c.setFont("Times-Roman", 21); c.setFillColor(GOLD)
c.drawCentredString(cx, mc_y - 7.5, "P")

# deadpan line
c.setFillColor(CREAM)
c.setFont("Times-Italic", 10.5)
c.drawCentredString(cx, H - 104, "An acquisition awaits the")
c.drawCentredString(cx, H - 118, "attention of Raymond.")

# QR tile (white so it scans)
T = 96.0
tile_x = cx - T / 2.0
tile_y = 28.0
c.setFillColor(WHITE)
c.roundRect(tile_x, tile_y, T, T, 6, fill=1, stroke=0)

# vector QR
qr_margin = 9.0
qs = T - 2 * qr_margin
qrw = QrCodeWidget(URL)
qrw.barLevel = "H"
qrw.barBorder = 0
qrw.barFillColor = NAVY
b = qrw.getBounds()
bw, bh = b[2] - b[0], b[3] - b[1]
d = Drawing(qs, qs, transform=[qs / bw, 0, 0, qs / bh, -b[0] * qs / bw, -b[1] * qs / bh])
d.add(qrw)
renderPDF.draw(d, c, tile_x + qr_margin, tile_y + qr_margin)

# instruction
caps(cx, 18, "SCAN TO RECEIVE YOUR DOSSIER", "Helvetica", 6, GOLD, 1.2)

c.showPage()
c.save()
print("wrote", OUT)
