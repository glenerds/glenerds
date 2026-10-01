#!/usr/bin/env python3
"""Option 6: clean cover — no app UI. Large text + donut graphic (real sample numbers)."""
from PIL import Image, ImageDraw, ImageFont
import math

OUT = '/home/hatch/workspace/glenerds-microsite/tools/deposit-check/gallery/covers/cover-6-clean.png'
W, H = 1280, 720
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FBB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(sz, bold=False): return ImageFont.truetype(FBB if bold else FB, sz)
def fit(d, text, max_w, start, bold=False):
    sz = start
    while sz > 10:
        f = font(sz, bold)
        if d.textlength(text, font=f) <= max_w: return f
        sz -= 2
    return font(10, bold)

img = Image.new('RGB', (W, H), (16, 60, 44))
d = ImageDraw.Draw(img)
for y in range(H):  # subtle vertical gradient
    t = y / (H - 1)
    d.line([(0, y), (W, y)], fill=(int(16-8*t), int(60-30*t), int(44-20*t)))

def rounded(box, r, fill):
    d.rounded_rectangle(box, radius=r, fill=fill)

# ---- left: brand block ----
def logo(x, y, s):
    rounded([x, y, x+s, y+s], s*0.22, '#0f9d58')
    m = s/32
    d.line([(x+9*m,y+22*m),(x+13*m,y+13*m),(x+16*m,y+18*m),(x+18*m,y+15*m),(x+23*m,y+22*m)],
           fill='white', width=max(2,int(2.2*m)), joint='curve')
    d.line([(x+9*m,y+22*m),(x+23*m,y+22*m)], fill='white', width=max(2,int(2.2*m)))
logo(90, 120, 96)
f = fit(d, 'DepositCheck', 460, 84, True)
d.text((204, 128), 'DepositCheck', font=f, fill='white')
f2 = fit(d, 'Was your deposit', 460, 44, True)
d.text((90, 268), 'Was your deposit', font=f2, fill='white')
d.text((90, 322), 'fairly deducted?', font=f2, fill='white')
f3 = font(27)
d.text((90, 396), 'Audit every charge.', font=f3, fill='#bfe3cf')
d.text((90, 434), "Dispute what's unfair.", font=f3, fill='#bfe3cf')
px = 90
for t in ['Offline', 'No subscription', 'Dispute letter']:
    f4 = font(20)
    tw = d.textlength(t, font=f4)
    pw, ph = tw + 36, 48
    rounded([px, 500, px+pw, 500+ph], 24, '#0f9d58')
    d.text((px+18, 513), t, font=f4, fill='white')
    px += pw + 14

# ---- right: donut of the sample audit ----
cx, cy, R, wdt = 950, 340, 200, 84
# track
d.arc([cx-R, cy-R, cx+R, cy+R], start=0, end=360, fill='#234034', width=wdt)
# overcharged 70% red, fair 30% green — real sample numbers ($1050 / $1500)
d.arc([cx-R, cy-R, cx+R, cy+R], start=-90, end=-90+252, fill='#e5484d', width=wdt)
d.arc([cx-R, cy-R, cx+R, cy+R], start=-90+252, end=-90+360, fill='#4fd18a', width=wdt)
# center label: hole diameter = 2*(R-wdt/2) = 232; keep text well inside
fc = fit(d, '$1,050', 200, 64, True)
twc = d.textlength('$1,050', font=fc)
d.text((cx-twc/2, cy-52), '$1,050', font=fc, fill='white')
f5 = font(26)
tw5 = d.textlength('overcharged', font=f5)
d.text((cx-tw5/2, cy+22), 'overcharged', font=f5, fill='#ffb4ab')
# legend — measured, centered as a group so labels never collide
f6 = font(22)
lab1, lab2 = 'Overcharged $1,050', 'Fair $450'
w1 = 22 + 12 + d.textlength(lab1, font=f6)
w2 = 22 + 12 + d.textlength(lab2, font=f6)
x0 = cx - (w1 + 48 + w2) / 2
d.rectangle([x0, 590, x0+22, 612], fill='#e5484d')
d.text((x0+34, 588), lab1, font=f6, fill='#cfe0d6')
x1 = x0 + w1 + 48
d.rectangle([x1, 590, x1+22, 612], fill='#4fd18a')
d.text((x1+34, 588), lab2, font=f6, fill='#cfe0d6')
f7 = font(20)
cap = 'Sample audit: $2,000 deposit, $1,000 withheld.'
tw7 = d.textlength(cap, font=f7)
d.text((cx-tw7/2, 630), cap, font=f7, fill='#7d938a')

img.save(OUT)
print('saved', OUT)
