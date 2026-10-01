#!/usr/bin/env python3
"""5 clean cover styles for DepositCheck — NO app UI.
1 donut (existing) · 2 shield · 3 dollar · 4 magnifier · 5 scales. 1280x720."""
import math
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

def logo(d, x, y, s):
    d.rounded_rectangle([x, y, x + s, y + s], radius=int(s * 0.22), fill='#0f9d58')
    m = s / 32
    d.line([(x + 9*m, y + 22*m), (x + 13*m, y + 13*m), (x + 16*m, y + 18*m),
            (x + 18*m, y + 15*m), (x + 23*m, y + 22*m)], fill='white',
           width=max(2, int(2.2*m)), joint='curve')
    d.line([(x + 9*m, y + 22*m), (x + 23*m, y + 22*m)], fill='white', width=max(2, int(2.2*m)))

def pills(d, x, y, items, bg, fg):
    px = x
    for t in items:
        f = font(20)
        tw = d.textlength(t, font=f)
        pw, ph = tw + 36, 48
        d.rounded_rectangle([px, y, px + pw, y + ph], radius=24, fill=bg)
        d.text((px + 18, y + 13), t, font=f, fill=fg)
        px += pw + 14

# ============ 2 · SHIELD (navy, centered) ============
img, d = base((18, 30, 54), (8, 14, 28))
logo(d, W//2 - 48, 64, 96)
f = fit(d, 'DepositCheck', 560, 76, True); tw = d.textlength('DepositCheck', font=f)
d.text((W//2 - tw/2, 180), 'DepositCheck', font=f, fill='white')
# shield
sx, sy, ss = W//2, 400, 120
shield = [(sx - ss, sy - ss*0.7), (sx + ss, sy - ss*0.7), (sx + ss, sy + ss*0.1),
          (sx, sy + ss*0.95), (sx - ss, sy + ss*0.1)]
d.polygon(shield, outline='#e8b64c', width=10)
d.line([(sx - 52, sy + 5), (sx - 12, sy + 48), (sx + 58, sy - 42)], fill='white', width=16, joint='curve')
f2 = fit(d, "Keep what's yours.", 800, 58, True); tw2 = d.textlength("Keep what's yours.", font=f2)
d.text((W//2 - tw2/2, 548), "Keep what's yours.", font=f2, fill='white')
f3 = font(27); sub = 'Audit every deduction before you accept it.'
tw3 = d.textlength(sub, font=f3)
d.text((W//2 - tw3/2, 622), sub, font=f3, fill='#9fb0c8')
img.save(OUTD + 'clean-2-shield.png')

# ============ 3 · DOLLAR (cream, split) ============
img, d = base((250, 244, 232), (233, 223, 205))
logo(d, 90, 120, 96)
f = fit(d, 'DepositCheck', 470, 76, True)
d.text((204, 126), 'DepositCheck', font=f, fill='#14332a')
f2 = fit(d, 'Get your deposit back.', 480, 52, True)
d.text((90, 268), 'Get your', font=f2, fill='#14332a')
d.text((90, 330), 'deposit back.', font=f2, fill='#14332a')
f3 = font(27)
d.text((90, 420), 'Find every dollar they owe you.', font=f3, fill='#3d5a4e')
pills(d, 90, 490, ['Offline', 'No subscription', 'Dispute letter'], '#0f9d58', 'white')
# big dollar coin right
cx, cy, R = 950, 360, 185
d.ellipse([cx - R, cy - R, cx + R, cy + R], fill='#0f9d58')
d.ellipse([cx - R + 14, cy - R + 14, cx + R - 14, cy + R - 14], outline='#ffffff', width=5)
f4 = fit(d, '$1,050', 280, 92, True); tw4 = d.textlength('$1,050', font=f4)
d.text((cx - tw4/2, cy - 78), '$1,050', font=f4, fill='white')
f5 = font(30); t5 = 'overcharged'
d.text((cx - d.textlength(t5, font=f5)/2, cy + 18), t5, font=f5, fill='#d7efe2')
f6 = font(21); cap = 'Sample audit: $2,000 deposit, $1,000 withheld.'
d.text((cx - d.textlength(cap, font=f6)/2, cy + R + 28), cap, font=f6, fill='#6b7f74')
img.save(OUTD + 'clean-3-dollar.png')

# ============ 4 · MAGNIFIER (paper, graphic left / text right) ============
img, d = base((242, 245, 242), (226, 232, 228))
# magnifier
cx, cy, R = 330, 350, 165
d.ellipse([cx - R, cy - R, cx + R, cy + R], outline='#14332a', width=26)
hx, hy = cx + R*0.72, cy + R*0.72
d.line([(hx, hy), (hx + 130, hy + 130)], fill='#14332a', width=30)
# inside the lens: audited charge
f4 = fit(d, '$1,200', 220, 52, True); tw4 = d.textlength('$1,200', font=f4)
d.text((cx - tw4/2, cy - 78), '$1,200', font=f4, fill='#8a978f')
d.line([(cx - tw4/2 - 8, cy - 50), (cx + tw4/2 + 8, cy - 50)], fill='#e5484d', width=7)
f5 = fit(d, '$250 fair', 230, 58, True); tw5 = d.textlength('$250 fair', font=f5)
d.text((cx - tw5/2, cy - 6), '$250 fair', font=f5, fill='#0f9d58')
# text right
logo(d, 640, 130, 92)
f = fit(d, 'DepositCheck', 500, 72, True)
d.text((750, 136), 'DepositCheck', font=f, fill='#14332a')
f2 = fit(d, 'Every charge, audited.', 540, 50, True)
d.text((640, 280), 'Every charge,', font=f2, fill='#14332a')
d.text((640, 340), 'audited.', font=f2, fill='#14332a')
f3 = font(26)
d.text((640, 424), 'Useful-life depreciation math', font=f3, fill='#3d5a4e')
d.text((640, 460), 'on each line item.', font=f3, fill='#3d5a4e')
pills(d, 640, 530, ['Offline', 'No subscription'], '#0f9d58', 'white')
img.save(OUTD + 'clean-4-magnifier.png')

# ============ 5 · SCALES (dark teal, split) ============
img, d = base((13, 34, 44), (6, 18, 26))
logo(d, 90, 120, 96)
f = fit(d, 'DepositCheck', 470, 76, True)
d.text((204, 126), 'DepositCheck', font=f, fill='white')
f2 = fit(d, 'The math is', 480, 52, True)
d.text((90, 268), 'The math is', font=f2, fill='white')
d.text((90, 330), 'on your side.', font=f2, fill='white')
f3 = font(26)
d.text((90, 420), 'Depreciation tables for carpet,', font=f3, fill='#9fd8b8')
d.text((90, 456), 'paint, appliances & more.', font=f3, fill='#9fd8b8')
pills(d, 90, 530, ['Offline', 'No subscription', 'Dispute letter'], '#0f9d58', 'white')
# balance scale, beam tipped: landlord side heavier (lower)
sx = 950
d.line([(sx, 170), (sx, 560)], fill='#e8b64c', width=10)          # post
d.line([(sx - 60, 560), (sx + 60, 560)], fill='#e8b64c', width=10) # foot
d.line([(sx - 200, 250), (sx + 200, 330)], fill='#e8b64c', width=8) # beam
d.ellipse([sx - 14, 262, sx + 14, 290], fill='#e8b64c')            # pivot
for ex, ey, drop, label, sub2, col in [
        (sx - 200, 250, 150, '$1,000', 'withheld', '#ff8a80'),
        (sx + 200, 330, 110, '$450', 'fair share', '#4fd18a')]:
    d.line([(ex, ey), (ex, ey + drop)], fill='#c8ccd4', width=5)
    d.line([(ex - 70, ey + drop), (ex + 70, ey + drop)], fill='#c8ccd4', width=8)
    fl = fit(d, label, 150, 34, True); twl = d.textlength(label, font=fl)
    d.text((ex - twl/2, ey + drop + 16), label, font=fl, fill=col)
    fs = font(21); tws = d.textlength(sub2, font=fs)
    d.text((ex - tws/2, ey + drop + 56), sub2, font=fs, fill='#9fb3a8')
img.save(OUTD + 'clean-5-scales.png')

print('saved 4 new clean covers')
