#!/usr/bin/env python3
"""5 NEW clean covers, thumbnail-first: giant type, one idea each, no app UI. 1280x720."""
from PIL import Image, ImageDraw, ImageFont

OUTD = '/home/hatch/workspace/glenerds-microsite/tools/deposit-check/gallery/covers/'
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

def base(top, bot):
    img = Image.new('RGB', (W, H), top)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    return img, d

def brand(d, light=True):
    fg = 'white' if light else '#14332a'
    d.rounded_rectangle([60, 48, 124, 112], radius=14, fill='#0f9d58')
    m = 64 / 32
    d.line([(60+9*m, 48+22*m), (60+13*m, 48+13*m), (60+16*m, 48+18*m),
            (60+18*m, 48+15*m), (60+23*m, 48+22*m)], fill='white', width=5, joint='curve')
    d.line([(60+9*m, 48+22*m), (60+23*m, 48+22*m)], fill='white', width=5)
    f = font(40, True)
    d.text((140, 58), 'DepositCheck', font=f, fill=fg)

def centered(d, cx, y, text, f, fill):
    d.text((cx - d.textlength(text, font=f)/2, y), text, font=f, fill=fill)

# ============ T1 · the number (dark green, centered) ============
img, d = base((13, 59, 46), (6, 30, 24))
brand(d)
f1 = fit(d, '$1,050', 900, 230, True)
centered(d, W/2, 200, '$1,050', f1, 'white')
f2 = fit(d, 'OVERCHARGED?', 900, 96, True)
centered(d, W/2, 440, 'OVERCHARGED?', f2, '#ff6b6b')
f3 = font(34)
centered(d, W/2, 580, 'Was your deposit fairly deducted?', f3, '#9fc4ae')
img.save(OUTD + 't1-number.png')

# ============ T2 · the percent (navy, centered) ============
img, d = base((16, 28, 51), (8, 15, 32))
brand(d)
f1 = fit(d, '70%', 800, 260, True)
centered(d, W/2, 190, '70%', f1, 'white')
f2 = fit(d, 'OF CHARGES ARE UNFAIR', 1000, 76, True)
centered(d, W/2, 460, 'OF CHARGES ARE UNFAIR', f2, '#e8b64c')
f3 = font(32)
centered(d, W/2, 590, 'Sample audit: $1,050 overcharged of $1,500 billed.', f3, '#8fa0bd')
img.save(OUTD + 't2-percent.png')

# ============ T3 · receipt with red X (maroon, split) ============
img, d = base((74, 20, 32), (44, 11, 19))
brand(d)
f1 = fit(d, 'REJECT', 560, 120, True)
d.text((80, 190), 'REJECT', font=f1, fill='white')
f1b = fit(d, 'UNFAIR CHARGES', 560, 84, True)
d.text((80, 320), 'UNFAIR', font=f1b, fill='white')
d.text((80, 410), 'CHARGES', font=f1b, fill='white')
f3 = font(32)
d.text((80, 540), 'Audit before you accept.', font=f3, fill='#d8a0a8')
# receipt card
rx, ry, rw, rh = 800, 170, 360, 400
d.rounded_rectangle([rx, ry, rx+rw, ry+rh], radius=18, fill='#f7f4ec')
fr = font(24, True)
centered(d, rx+rw/2, ry+22, 'DEPOSIT DEDUCTIONS', fr, '#5a5348')
rows = [('Carpet', '$1,200'), ('Cleaning', '$200'), ('Paint', '$100')]
fy = ry + 80
for name, amt in rows:
    d.text((rx+36, fy), name, font=font(26), fill='#3a352d')
    fa = font(26, True); tw = d.textlength(amt, font=fa)
    d.text((rx+rw-36-tw, fy), amt, font=fa, fill='#3a352d')
    fy += 56
d.line([(rx+30, fy+6), (rx+rw-30, fy+6)], fill='#c9c2b2', width=3)
# red X badge stamping the card's bottom-right corner — clear of all row text
ccx, ccy, cr = rx+rw-20, ry+rh-20, 82
d.ellipse([ccx-cr, ccy-cr, ccx+cr, ccy+cr], fill='#e5484d')
d.line([(ccx-40, ccy-40), (ccx+40, ccy+40)], fill='white', width=20)
d.line([(ccx-40, ccy+40), (ccx+40, ccy-40)], fill='white', width=20)
img.save(OUTD + 't3-receipt.png')

# ============ T4 · dispute letter (teal, split) ============
img, d = base((14, 58, 63), (7, 32, 37))
brand(d)
f1 = fit(d, 'DISPUTE IT', 560, 116, True)
d.text((80, 190), 'DISPUTE IT', font=f1, fill='white')
f1b = fit(d, 'IN WRITING', 560, 116, True)
d.text((80, 316), 'IN WRITING', font=f1b, fill='#7fe0c3')
f3 = font(32)
d.text((80, 500), 'Generates your dispute letter.', font=f3, fill='#9fc4bb')
# envelope graphic
ex, ey, ew, eh = 800, 230, 380, 260
d.rounded_rectangle([ex, ey-70, ex+ew, ey+120], radius=10, fill='white')   # letter peeking
for ly in range(ey-40, ey+90, 26):
    d.line([(ex+40, ly), (ex+ew-40, ly)], fill='#c9d4d0', width=6)
d.rounded_rectangle([ex, ey, ex+ew, ey+eh], radius=14, fill='#14957f')     # envelope body
d.polygon([(ex, ey), (ex+ew, ey), (ex+ew/2, ey+110)], fill='#0e7a68')      # flap
d.line([(ex, ey+eh), (ex+ew/2, ey+120)], fill='#0b5f53', width=8)
d.line([(ex+ew, ey+eh), (ex+ew/2, ey+120)], fill='#0b5f53', width=8)
img.save(OUTD + 't4-letter.png')

# ============ T5 · moving out key (charcoal, split) ============
img, d = base((30, 36, 48), (17, 21, 30))
brand(d)
f1 = fit(d, 'MOVING OUT?', 560, 112, True)
d.text((80, 190), 'MOVING OUT?', font=f1, fill='#e8b64c')
f1b = fit(d, 'CHECK FIRST.', 560, 112, True)
d.text((80, 316), 'CHECK FIRST.', font=f1b, fill='white')
f3 = font(32)
d.text((80, 500), 'Audit your deposit deductions.', font=f3, fill='#9aa3b5')
# big key, right side
kx, ky = 950, 380
d.ellipse([kx-95, ky-160, kx+95, ky+30], outline='#e8b64c', width=34)  # bow
d.line([(kx, ky+30), (kx, ky+210)], fill='#e8b64c', width=34)          # shaft
d.line([(kx, ky+130), (kx+80, ky+130)], fill='#e8b64c', width=30)      # tooth 1
d.line([(kx, ky+185), (kx+62, ky+185)], fill='#e8b64c', width=30)      # tooth 2
img.save(OUTD + 't5-key.png')

# thumbnails for readability check
for n in ['t1-number', 't2-percent', 't3-receipt', 't4-letter', 't5-key']:
    im = Image.open(OUTD + n + '.png')
    im.resize((240, 135)).save(OUTD + n + '-thumb.png')
print('saved 5 covers + thumbs')
