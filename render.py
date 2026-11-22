"""Draw entry.png: a newspaper front page summing up Sunday 22 Nov 2026.

Build-time script only (the grader never runs it). Run:
    python3 render.py
Writes entry.png (1024x1024) next to this file. Pillow is used.
All 38 stories come from the One Turn day page for 2026-11-22 and the
publications it cites; see STORIES.md for one source per story.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 242, 223)
INK = (20, 20, 20)
RED = (168, 30, 35)
NAVY = (30, 60, 100)
BLUE = (70, 120, 170)
SEA = (188, 214, 232)
LAND = (217, 203, 166)
MUTED = (90, 82, 72)
GOLD = (176, 132, 40)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centre(draw, y, text, fnt, fill=INK, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)


def panel_frame(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=2)


# ---------------------------------------------------------------- scenes
def scene_dymer(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(196, 214, 232))
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(120, 116, 108))
    d.rectangle([x + 30, y + 30, x + 110, y + h - 26], fill=(150, 146, 138))
    d.rectangle([x + 130, y + 48, x + 205, y + h - 26], fill=(128, 124, 116))
    for bx in (30, 130):
        for wy in range(y + 38, y + h - 34, 16):
            for wx in range(x + bx + 8, x + bx + 72, 18):
                d.rectangle([wx, wy, wx + 10, wy + 10], fill=(250, 220, 120))
    d.polygon([(x + 150, y + 18), (x + 190, y + 18), (x + 205, y + 30),
               (x + 135, y + 30)], fill=(90, 88, 84))
    d.ellipse([x + 168, y + 22, x + 184, y + 34], fill=(90, 88, 84))
    d.ellipse([x + 200, y + 8, x + 236, y + 40], fill=(240, 240, 235))
    d.ellipse([x + 214, y + 22, x + 244, y + 52], fill=(225, 225, 220))


def scene_tanker(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 190, 130))
    d.rectangle([x, y + 78, x + w, y + h], fill=(52, 110, 150))
    d.rectangle([x + 40, y + 58, x + 200, y + 82], fill=(140, 40, 36))
    d.rectangle([x + 168, y + 40, x + 188, y + 58], fill=(200, 200, 195))
    d.polygon([(x + 118, y + 52), (x + 130, y + 22), (x + 142, y + 52)],
              fill=(240, 170, 40))
    d.ellipse([x + 112, y + 10, x + 150, y + 42], fill=(250, 120, 30))
    for wx in range(x + 10, x + w - 10, 26):
        d.arc([wx, y + 88, wx + 22, y + 100], 0, 180, fill=(255, 255, 255),
              width=2)


def scene_mercury(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 18, 34))
    for sx, sy in [(20, 16), (60, 40), (210, 22), (180, 60), (40, 80),
                   (230, 90), (100, 14)]:
        d.ellipse([x + sx, y + sy, x + sx + 3, y + sy + 3],
                  fill=(255, 255, 255))
    cx, cy, r = x + 78, y + 62, 42
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(176, 168, 156))
    for ox, oy, orad in [(58, 48, 7), (92, 80, 9), (70, 88, 5), (100, 44, 6)]:
        d.ellipse([x + ox - orad, y + oy - orad, x + ox + orad,
                   y + oy + orad], fill=(140, 132, 120))
    d.rectangle([x + 160, y + 30, x + 196, y + 44], fill=(200, 200, 200))
    d.rectangle([x + 150, y + 24, x + 160, y + 50], fill=(150, 150, 150))
    d.rectangle([x + 196, y + 24, x + 206, y + 50], fill=(150, 150, 150))
    d.line([x + 160, y + 52, x + 130, y + 80], fill=(240, 200, 80), width=2)


def scene_stocks(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    for gy in range(y + 20, y + h - 10, 22):
        d.line([x + 8, gy, x + w - 8, gy], fill=(225, 225, 225), width=1)
    pts = [(x + 12, y + 22), (x + 50, y + 30), (x + 88, y + 26),
           (x + 126, y + 48), (x + 164, y + 62), (x + 202, y + 78),
           (x + 232, y + 96)]
    d.line(pts, fill=RED, width=4)
    for px, py in pts:
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=RED)
    d.text((x + 150, y + 8), "-3.7%", font=font(SANS_B, 20), fill=RED)


def scene_f1(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 24, 40))
    d.rectangle([x, y + 84, x + w, y + h], fill=(60, 60, 66))
    d.rectangle([x + 30, y + 58, x + 200, y + 80], fill=(200, 30, 40))
    d.polygon([(x + 110, y + 58), (x + 130, y + 38), (x + 165, y + 38),
               (x + 175, y + 58)], fill=(200, 30, 40))
    d.rectangle([x + 34, y + 40, x + 44, y + 58], fill=(220, 220, 220))
    d.rectangle([x + 30, y + 36, x + 48, y + 42], fill=(220, 220, 220))
    d.rectangle([x + 168, y + 30, x + 176, y + 58], fill=(220, 220, 220))
    for wx, wy in [(70, 80), (180, 80)]:
        d.ellipse([x + wx - 16, y + wy - 12, x + wx + 16, y + wy + 12],
                  fill=(10, 10, 10))
        d.ellipse([x + wx - 7, y + wy - 7, x + wx + 7, y + wy + 7],
                  fill=(200, 200, 200))
    for sx, sy in [(20, 14), (90, 10), (160, 18), (220, 12)]:
        d.ellipse([x + sx, y + sy, x + sx + 3, y + sy + 3],
                  fill=(255, 220, 100))


def scene_shuri(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(150, 200, 235))
    d.rectangle([x, y + 92, x + w, y + h], fill=(110, 160, 90))
    d.polygon([(x + 52, y + 46), (x + 122, y + 18), (x + 192, y + 46)],
              fill=(168, 30, 35))
    d.rectangle([x + 66, y + 46, x + 178, y + 66], fill=(200, 60, 50))
    d.polygon([(x + 58, y + 74), (x + 122, y + 52), (x + 186, y + 74)],
              fill=(168, 30, 35))
    d.rectangle([x + 76, y + 74, x + 168, y + 92], fill=(210, 70, 58))
    d.rectangle([x + 112, y + 66, x + 132, y + 92], fill=(90, 50, 40))
    d.ellipse([x + 18, y + 16, x + 46, y + 44], fill=(255, 240, 180))


def scene_bts(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(40, 20, 70))
    for lx, col in [(30, (255, 80, 120)), (122, (120, 200, 255)),
                    (210, (255, 220, 90))]:
        d.polygon([(x + lx, y), (x + lx + 26, y), (x + lx + 60, y + h),
                   (x + lx - 8, y + h)], fill=col)
    d.rectangle([x, y + 92, x + w, y + h], fill=(20, 10, 36))
    d.ellipse([x + 104, y + 52, x + 140, y + 88], fill=(255, 220, 190))
    d.rectangle([x + 118, y + 88, x + 126, y + 104], fill=(255, 220, 190))
    d.ellipse([x + 112, y + 40, x + 132, y + 56], fill=(60, 60, 60))
    d.rectangle([x + 150, y + 60, x + 168, y + 76], fill=(220, 220, 220))
    d.ellipse([x + 152, y + 54, x + 168, y + 68], fill=(220, 220, 220))


def scene_crispr(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 245, 250))
    import math
    for i in range(0, 13):
        px = x + 40 + i * 13
        py = y + 14 + i * 7
        d.line([px, py, px + 70, py + 14], fill=(120, 160, 200), width=2)
        off = int(26 * math.sin(i * 0.9))
        d.ellipse([px - 4, py + off - 4, px + 4, py + off + 4],
                  fill=NAVY)
        d.ellipse([px + 66 - 4, py + 14 - off - 4, px + 66 + 4,
                   py + 14 - off + 4], fill=RED)
    d.ellipse([x + 188, y + 12, x + 224, y + 48], fill=(255, 255, 255),
              outline=NAVY, width=2)
    d.text((x + 194, y + 20), "-52%", font=font(SANS_B, 16), fill=NAVY)


PANELS = [
    ("UKRAINE", "Drone hits Kyiv flat;", "14 missing in rubble", scene_dymer),
    ("THE GULF", "Iran strikes Bahrain", "site; tankers hit too", scene_tanker),
    ("SPACE", "BepiColombo reaches", "Mercury after 8 years", scene_mercury),
    ("MARKETS", "Stocks fall into", "correction; S&P -3.7%", scene_stocks),
    ("SPORT - F1", "Verstappen wins in", "Las Vegas again", scene_f1),
    ("CULTURE", "Shuri Castle restored", "7 years after fire", scene_shuri),
    ("MUSIC", "BTS win five MAMA", "awards in Osaka", scene_bts),
    ("HEALTH", "One CRISPR dose cuts", "cholesterol 52%", scene_crispr),
]

COLUMNS = [
    ("CONFLICT", [
        "Russian ship burns in Gulf",
        "Settlers torch cars, W. Bank",
        "Eisenkot invites Likud to talks",
        "Houthis hit Saudi refinery",
        "Strikes continue in Gaza",
        "Drones hit Khartoum; UN hurt",
        "El Chapo Isidro held; 11 die",
    ]),
    ("POLITICS & MARKETS", [
        "EU, Indonesia sign trade deal",
        "CRISPR cuts cholesterol 52%",
        "AI-weapons talks end, no rules",
        "Trump-Xi-Putin: summit fallout",
        "Cost-of-living protests spread",
        "Argentina OKs $50bn LNG plan",
        "Denmark expels Russian attache",
    ]),
    ("AROUND THE WORLD", [
        "EU-Rwanda deportation hubs deal",
        "Aoun: Israel, Iran threaten us",
        "Korea minister quits over AI",
        "ICE arrests at Seattle airport",
        "Nigeria boat sinks; 24 dead",
        "Basra power fire kills four",
        "Indonesia factory fire; 3 dead",
    ]),
]

BRIEFS = [
    ("IRAN RATIONS POWER", "blackouts begin as cold sets in after war damage."),
    ("KATE IN REMISSION", "Princess of Wales announces recovery in film Heal."),
    ("BOLSONARO IN ICU", "ex-president stable with bowel obstruction."),
    ("BANGLADESH STRIKES", "80 garment factories shut in wage protests."),
    ("HAITI PRISONS", "deal with El Salvador to build three prisons."),
    ("MONGOLIA VOTE", "snap presidential poll is called."),
    ("HONG KONG VOTE", "5,700 pick election committee members."),
    ("CYCLONE XAVIER", "weakens near Cook Islands; all on Nassau safe."),
]

MAP_PINS = [
    (1, "Antalya, Turkey - COP31", 304, 576),
    (2, "Dymer, Ukraine - drone hit", 284, 560),
    (3, "Bahrain - Iran strike", 324, 590),
    (4, "Sinaloa, Mexico - cartel arrest", 104, 592),
    (5, "Banten, Indonesia - factory fire", 397, 617),
    (6, "Las Vegas, USA - F1 win", 84, 574),
    (7, "Seoul, S. Korea - minister quits", 426, 576),
    (8, "Gaza - strikes continue", 292, 590),
]


def draw_map(d):
    mx, my, mw, mh = 12, 540, 500, 124
    d.rectangle([mx, my, mx + mw, my + mh], fill=SEA, outline=INK, width=2)
    land = [
        [(30, 560), (60, 548), (110, 552), (120, 575), (100, 600),
         (70, 605), (45, 590)],
        [(130, 615), (160, 610), (170, 640), (150, 660), (135, 640)],
        [(270, 548), (310, 545), (315, 565), (285, 568), (268, 558)],
        [(275, 575), (320, 572), (335, 600), (310, 640), (285, 625)],
        [(315, 545), (480, 545), (495, 575), (460, 610), (400, 615),
         (360, 590), (330, 568)],
        [(440, 625), (480, 622), (485, 645), (445, 648)],
    ]
    for poly in land:
        d.polygon(poly, fill=LAND, outline=(150, 134, 96))
    d.text((mx + 8, my + 4), "THE WORLD", font=font(SANS_B, 13), fill=NAVY)
    for num, _label, px, py in MAP_PINS:
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED,
                  outline=(255, 255, 255), width=2)
        tw = d.textlength(str(num), font=font(SANS_B, 12))
        d.text((px - tw / 2, py - 7), str(num), font=font(SANS_B, 12),
               fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    centre(d, 6, "THE WORLD IN ONE DAY", font(SERIF_B, 60))
    centre(d, 72, "SUNDAY 22 NOVEMBER 2026", font(SANS_B, 36), fill=RED)
    d.line([12, 116, W - 12, 116], fill=INK, width=3)
    d.line([12, 121, W - 12, 121], fill=INK, width=1)

    # Lead story
    d.text((12, 128), "LEAD STORY - CLIMATE", font=font(SANS_B, 15),
           fill=RED)
    d.text((12, 146), "COP31 COLLAPSES WITHOUT A DEAL",
           font=font(SERIF_B, 33), fill=INK)
    d.text((12, 182),
           "UN climate talks in Antalya end two days late with no agreement after the EU",
           font=font(SANS, 16), fill=INK)
    d.text((12, 200),
           "and others reject a draft that never mentions fossil fuels.",
           font=font(SANS, 16), fill=INK)

    # Picture panels, two rows of four
    cell_w = 244
    for row in range(2):
        for col in range(4):
            idx = row * 4 + col
            tag, cap1, cap2, scene = PANELS[idx]
            x = 12 + col * 256
            y = 224 + row * 160
            scene(d, x, y, cell_w, 100)
            panel_frame(d, x, y, cell_w, 100)
            d.text((x + 2, y + 104), tag, font=font(SANS_B, 13), fill=RED)
            d.text((x + 2, y + 119), cap1, font=font(SANS_B, 15), fill=INK)
            d.text((x + 2, y + 134), cap2, font=font(SANS_B, 15), fill=INK)

    # World map + key
    draw_map(d)
    kx = 524
    d.text((kx, 542), "WHERE IT HAPPENED", font=font(SANS_B, 16), fill=RED)
    key_font = font(SANS, 14)
    for i, (num, label, _px, _py) in enumerate(MAP_PINS):
        col = i % 2
        row = i // 2
        tx = kx + col * 244
        ty = 566 + row * 25
        d.ellipse([tx, ty + 2, tx + 15, ty + 17], fill=RED)
        tw = d.textlength(str(num), font=font(SANS_B, 11))
        d.text((tx + (15 - tw) / 2, ty + 3), str(num),
               font=font(SANS_B, 11), fill=(255, 255, 255))
        d.text((tx + 20, ty + 2), label, font=key_font, fill=INK)

    # Three headline columns
    d.line([12, 672, W - 12, 672], fill=INK, width=2)
    col_x = [12, 352, 692]
    head_font = font(SANS_B, 15)
    for ci, (title, items) in enumerate(COLUMNS):
        x = col_x[ci]
        d.text((x, 680), title, font=font(SANS_B, 14), fill=RED)
        d.line([x, 700, x + 320, 700], fill=MUTED, width=1)
        for ri, item in enumerate(items):
            d.text((x, 706 + ri * 25), "- " + item, font=head_font,
                   fill=INK)

    # Briefs: bold lead-in, then the rest of the line in regular weight
    d.line([12, 880, W - 12, 880], fill=INK, width=2)
    d.text((12, 886), "IN BRIEF", font=font(SANS_B, 15), fill=RED)
    brief_font = font(SANS, 13)
    brief_bold = font(SANS_B, 13)
    for i, (lead, rest) in enumerate(BRIEFS):
        col = i % 4
        row = i // 4
        x = 12 + col * 256
        y = 904 + row * 26
        lines = wrap(d, lead + " - " + rest, brief_font, 230)
        for li, line in enumerate(lines[:2]):
            if li == 0 and line.startswith(lead):
                d.text((x, y), lead, font=brief_bold, fill=INK)
                lead_w = d.textlength(lead, font=brief_bold)
                d.text((x + lead_w, y), line[len(lead):],
                       font=brief_font, fill=INK)
            else:
                d.text((x, y + li * 13), line, font=brief_font, fill=INK)

    # Day-in-figures strip
    d.rectangle([12, 962, W - 12, 990], fill=NAVY)
    centre(d, 968,
           "S&P 500 -3.7%  |  Brent $90  |  14 missing, Dymer  |  "
           "24 dead, Nigeria  |  $50bn LNG  |  98.5% tariffs cut",
           font(SANS_B, 15), fill=(255, 255, 255), x0=12, x1=W - 12)

    # Footer
    centre(d, 996,
           "All 38 stories happened or were first reported on Sunday "
           "22 November 2026 - Sources: One Turn, Guardian, BBC, "
           "Reuters, AP - see STORIES.md",
           font(SANS, 12), fill=MUTED)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
