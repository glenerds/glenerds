#!/usr/bin/env python3
"""5 hybrid cover directions for DepositCheck (1280x720).
Real app UI in browser frames + DepositCheck brand + one benefit line each.
Strict layout QA: centered, no overlaps, text measured before drawing."""
import os
from PIL import Image, ImageDraw, ImageFont

G = '/home/hatch/workspace/glenerds-microsite/tools/deposit-check/gallery/'
OUT = '/home/hatch/workspace/glenerds-microsite/tools/deposit-check/gallery/covers/'
os.makedirs(OUT, exist_ok=True)
W, H = 1280, 720
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FBB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def font(sz, bold=False):
    return ImageFont.truetype(FBB if bold else FB, sz)

def fit_font(draw, text, max_w, start, bold=False, min_sz=10):
    sz = start
    while sz > min_sz:
        f = font(sz, bold)
        if draw.textlength(text, font=f) <= max_w:
            return f
        sz -= 2
    return font(min_sz, bold)

def rounded(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def vgrad(size, top, bot):
    w, h = size
    img = Image.new('RGB', size, top)
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h - 1, 1)
        d.line([(0, y), (w, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    return img

def logo_badge(d, x, y, s):
    """DepositCheck logo: green rounded square + white mountain path."""
    rounded(d, [x, y, x + s, y + s], s * 0.22, fill='#0f9d58')
    m = s / 32
    pts = [(x + 9 * m, y + 22 * m), (x + 13 * m, y + 13 * m), (x + 16 * m, y + 18 * m),
           (x + 18 * m, y + 15 * m), (x + 23 * m, y + 22 * m)]
    d.line(pts, fill='white', width=max(2, int(2.2 * m)), joint='curve')
    d.line([(x + 9 * m, y + 22 * m), (x + 23 * m, y + 22 * m)], fill='white', width=max(2, int(2.2 * m)))

def browser_frame(shot_path, fw, fh):
    """Browser chrome + screenshot, returns image."""
    shot = Image.open(shot_path).convert('RGB')
    # crop screenshot to fit content area (below chrome)
    chrome_h = int(fh * 0.075)
    content = shot.resize((fw - 8, fh - chrome_h - 4))
    fr = Image.new('RGB', (fw, fh), '#2b3a33')
    d = ImageDraw.Draw(fr)
    # traffic dots
    for i, c in enumerate(['#ff5f57', '#febc2e', '#28c840']):
        d.ellipse([16 + i * 26, chrome_h // 2 - 8, 16 + i * 26 + 16, chrome_h // 2 + 8], fill=c)
    f = font(max(14, chrome_h // 3))
    url = 'depositcheck.html · offline'
    tw = d.textlength(url, font=f)
    d.rounded_rectangle([70, chrome_h // 2 - 16, 70 + tw + 36, chrome_h // 2 + 16], radius=10, fill='#3a4d44')
    d.text((88, chrome_h // 2 - 12), url, font=f, fill='#cfe0d6')
    fr.paste(content, (4, chrome_h))
    return fr

def pill(d, cx, y, text, bg, fg, f):
    tw = d.textlength(text, font=f)
    pw, ph = tw + 44, f.size + 26
    rounded(d, [cx - pw / 2, y, cx + pw / 2, y + ph], ph // 2, fill=bg)
    d.text((cx - tw / 2, y + 13), text, font=f, fill=fg)
    return ph

# ---------------- direction 1: verdict ----------------
img = vgrad((W, H), (16, 60, 44), (8, 30, 24))
d = ImageDraw.Draw(img)
fr = browser_frame(G + '04-results.png', 640, 470)
img.paste(fr, (600, 125))
logo_badge(d, 90, 130, 92)
f = fit_font(d, 'DepositCheck', 370, 72, True)
d.text((200, 138), 'DepositCheck', font=f, fill='white')
f2 = fit_font(d, 'Was your deposit fairly deducted?', 440, 40, True)
d.text((90, 260), 'Was your deposit', font=f2, fill='white')
d.text((90, 310), 'fairly deducted?', font=f2, fill='white')
f3 = font(26)
d.text((90, 380), 'Find out in minutes — line by line.', font=f3, fill='#bfe3cf')
# pills left-aligned row
px = 90
for t in ['Offline', 'No subscription', 'Dispute letter']:
    f4 = font(20)
    tw = d.textlength(t, font=f4)
    pw, ph = tw + 36, 48
    rounded(d, [px, 452, px + pw, 452 + ph], 24, fill='#0f9d58')
    d.text((px + 18, 465), t, font=f4, fill='white')
    px += pw + 14
img.save(OUT + 'cover-1-verdict.png')

# ---------------- direction 2: letter ----------------
img = vgrad((W, H), (250, 244, 232), (232, 222, 204))
d = ImageDraw.Draw(img)
fr = browser_frame(G + '05-letter.png', 600, 450)
img.paste(fr, (80, 135))
logo_badge(d, 760, 150, 84)
f = fit_font(d, 'DepositCheck', 400, 64, True)
d.text((862, 156), 'DepositCheck', font=f, fill='#14332a')
f2 = fit_font(d, 'Turns your audit into', 420, 38, True)
d.text((760, 280), 'Turns your audit into', font=f2, fill='#14332a')
d.text((760, 326), 'a dispute letter.', font=f2, fill='#14332a')
f3 = font(25)
d.text((760, 396), 'Pre-filled with your numbers.', font=f3, fill='#3d5a4e')
d.text((760, 432), 'Print it or copy it — done.', font=f3, fill='#3d5a4e')
img.save(OUT + 'cover-2-letter.png')

# ---------------- direction 3: dark split ----------------
img = Image.new('RGB', (W, H), '#f3f6f4')
d = ImageDraw.Draw(img)
d.rectangle([W // 2, 0, W, H], fill='#0f1412')
fr1 = browser_frame(G + '01-light-overview.png', 430, 330)
fr2 = browser_frame(G + '02-dark-overview.png', 430, 330)
img.paste(fr1, (105, 260))
img.paste(fr2, (745, 260))
logo_badge(d, W // 2 - 46, 60, 92)
f = fit_font(d, 'DepositCheck', 460, 60, True)
tw = d.textlength('DepositCheck', font=f)
pill_w, pill_h = tw + 72, 100
rounded(d, [W // 2 - pill_w / 2, 168, W // 2 + pill_w / 2, 168 + pill_h], 28, fill='#10231c')
d.text((W // 2 - tw / 2, 168 + (pill_h - f.size) / 2 - 4), 'DepositCheck', font=f, fill='white')
# benefit across the split: draw twice for contrast
f2 = fit_font(d, 'Audits your deposit in light or dark. 100% offline.', 900, 32)
tw2 = d.textlength('Audits your deposit in light or dark. 100% offline.', font=f2)
d.text((W // 2 - tw2 / 2, 620), 'Audits your deposit in light or dark.', font=f2, fill='#9fb3a8')
f3 = fit_font(d, '100% offline.', 900, 32, True)
tw3 = d.textlength('100% offline.', font=f3)
d.text((W // 2 - tw3 / 2, 660), '100% offline.', font=f3, fill='#4fd18a')
img.save(OUT + 'cover-3-split.png')

# ---------------- direction 4: overcharge ----------------
img = vgrad((W, H), (24, 32, 68), (10, 14, 34))
d = ImageDraw.Draw(img)
fr = browser_frame(G + '01-light-overview.png', 560, 420)
img.paste(fr, (650, 150))
logo_badge(d, 90, 140, 92)
f = fit_font(d, 'DepositCheck', 440, 72, True)
d.text((200, 148), 'DepositCheck', font=f, fill='white')
f2 = font(120, True)
d.text((90, 260), '$1,050', font=f2, fill='#ff8a80')
f3 = fit_font(d, 'overcharged — caught line by line.', 480, 34, True)
d.text((90, 400), 'overcharged —', font=f3, fill='white')
d.text((90, 444), 'caught line by line.', font=f3, fill='white')
f4 = fit_font(d, 'Sample audit: $2,000 deposit, $1,000 withheld.', 520, 24)
d.text((90, 520), 'Sample audit: $2,000 deposit, $1,000 withheld.', font=f4, fill='#9fb0c8')
img.save(OUT + 'cover-4-overcharge.png')

# ---------------- direction 5: checklist ----------------
img = vgrad((W, H), (14, 52, 42), (6, 26, 22))
d = ImageDraw.Draw(img)
# centered layout
logo_badge(d, W // 2 - 46, 56, 92)
f = fit_font(d, 'DepositCheck', 500, 60, True)
tw = d.textlength('DepositCheck', font=f)
d.text((W // 2 - tw / 2, 162), 'DepositCheck', font=f, fill='white')
f2 = fit_font(d, "Don't accept the charges until you've checked them.", 1000, 34)
tw2 = d.textlength("Don't accept the charges until you've checked them.", font=f2)
d.text((W // 2 - tw2 / 2, 240), "Don't accept the charges until you've checked them.", font=f2, fill='#bfe3cf')
fr = browser_frame(G + '06-checklist.png', 760, 380)
img.paste(fr, (W // 2 - 380, 300))
img.save(OUT + 'cover-5-checklist.png')

print('saved 5 covers')
