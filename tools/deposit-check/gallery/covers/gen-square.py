#!/usr/bin/env python3
"""Square 1200x1200 adaptation of the chosen donut cover for Gumroad's Thumbnail field."""
from PIL import Image, ImageDraw, ImageFont
OUT = '/home/hatch/workspace/glenerds-microsite/tools/deposit-check/gallery/covers/clean-1-donut-square.png'
W = H = 1200
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
def ctr(d, cx, y, text, f, fill):
    d.text((cx - d.textlength(text, font=f)/2, y), text, font=f, fill=fill)

img = Image.new('RGB', (W, H), (16, 60, 44))
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / (H - 1)
    d.line([(0, y), (W, y)], fill=(int(16-8*t), int(60-30*t), int(44-20*t)))

# brand row, centered
s = 96
d.rounded_rectangle([W/2-260, 60, W/2-260+s, 60+s], radius=21, fill='#0f9d58')
m = s/32; x0, y0 = W/2-260, 60
d.line([(x0+9*m,y0+22*m),(x0+13*m,y0+13*m),(x0+16*m,y0+18*m),(x0+18*m,y0+15*m),(x0+23*m,y0+22*m)],
       fill='white', width=7, joint='curve')
d.line([(x0+9*m,y0+22*m),(x0+23*m,y0+22*m)], fill='white', width=7)
f = fit(d, 'DepositCheck', 420, 64, True)
d.text((x0+s+18, 68), 'DepositCheck', font=f, fill='white')

f2 = fit(d, 'Was your deposit fairly deducted?', 980, 62, True)
ctr(d, W/2, 210, 'Was your deposit fairly deducted?', f2, 'white')
f3 = font(34)
ctr(d, W/2, 292, 'Audit every charge. Dispute what\'s unfair.', f3, '#bfe3cf')

# donut center
cx, cy, R, wdt = W/2, 660, 260, 110
d.arc([cx-R, cy-R, cx+R, cy+R], start=0, end=360, fill='#234034', width=wdt)
d.arc([cx-R, cy-R, cx+R, cy+R], start=-90, end=-90+252, fill='#e5484d', width=wdt)
d.arc([cx-R, cy-R, cx+R, cy+R], start=-90+252, end=-90+360, fill='#4fd18a', width=wdt)
fc = fit(d, '$1,050', 330, 92, True)
ctr(d, cx, cy-72, '$1,050', fc, 'white')
f5 = font(38)
ctr(d, cx, cy+34, 'overcharged', f5, '#ffb4ab')

# legend
f6 = font(30)
lab1, lab2 = 'Overcharged $1,050', 'Fair $450'
w1 = 30 + 16 + d.textlength(lab1, font=f6)
w2 = 30 + 16 + d.textlength(lab2, font=f6)
x0 = cx - (w1 + 60 + w2)/2
d.rectangle([x0, 1000, x0+30, 1030], fill='#e5484d')
d.text((x0+46, 998), lab1, font=f6, fill='#cfe0d6')
x1 = x0 + w1 + 60
d.rectangle([x1, 1000, x1+30, 1030], fill='#4fd18a')
d.text((x1+46, 998), lab2, font=f6, fill='#cfe0d6')
f7 = font(26)
ctr(d, cx, 1060, 'Sample audit: $2,000 deposit, $1,000 withheld.', f7, '#7d938a')

img.save(OUT)
print('saved', OUT)
