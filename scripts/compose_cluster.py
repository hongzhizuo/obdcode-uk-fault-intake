#!/usr/bin/env python3
"""Rasterize vector lamps and build per-fuel cluster PNGs.

Sources live in assets/svg/. The owner sees one numbered dashboard for
the fuel of this car. Lamp numbers stay global (9 is always DPF).
"""
from __future__ import annotations

import math
import re
from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SVG_DIR = ASSETS / "svg"

LAMPS = [
    (1, "01-oil-pressure", "lamp-01-oil-pressure.png", "red"),
    (2, "02-coolant-temp", "lamp-02-coolant-temp.png", "red"),
    (3, "03-brake-system", "lamp-03-brake-system.png", "red"),
    (4, "04-airbag-srs", "lamp-04-airbag-srs.png", "red"),
    (5, "05-power-steering", "lamp-05-power-steering.png", "red"),
    (8, "08-battery-charging", "lamp-08-battery-charging.png", "red"),
    (6, "06-engine-steady", "lamp-06-engine-steady.png", "amber"),
    (7, "07-engine-flashing", "lamp-07-engine-flashing.png", "amber"),
    (9, "09-dpf", "lamp-09-dpf.png", "amber"),
    (10, "10-tyre-pressure", "lamp-10-tyre-pressure.png", "amber"),
    (11, "11-abs", "lamp-11-abs.png", "amber"),
    (12, "12-esc-traction", "lamp-12-esc-traction.png", "amber"),
    (13, "13-glow-plug", "lamp-13-glow-plug.png", "amber"),
]
BY_N = {row[0]: row for row in LAMPS}

# Layout numbers stay global. 7 is not drawn: one engine cell (6), flashing is spoken.
# Ghost slots keep omitted numbers in place so people do not count cells.
BOARDS = {
    "unknown": {
        "file": "cluster.png",
        "tag": "Use the circled number. Do not count 1, 2, 3.",
        "left": "RPM",
        "red": [1, 2, 3, 4, 5, 8],
        "amber": [6, 9, 10, 11, 12, 13],
    },
    "petrol": {
        "file": "cluster-petrol.png",
        "tag": "Petrol. Empty slots are not on this car. Exhaust-dots: say GPF, not 9.",
        "left": "RPM",
        "red": [1, 2, 3, 4, 5, 8],
        "amber": [6, "ghost-9", 10, 11, 12, "ghost-13"],
    },
    "diesel": {
        "file": "cluster-diesel.png",
        "tag": "Diesel. 9 is DPF. 13 is a fault only if it stays on or flashes after start. AdBlue: say AdBlue.",
        "left": "RPM",
        "red": [1, 2, 3, 4, 5, 8],
        "amber": [6, 9, 10, 11, 12, 13],
    },
    "hybrid": {
        "file": "cluster-hybrid.png",
        "tag": "Hybrid. Engine and 12V still apply. Empty slots are not on this car.",
        "left": "RPM",
        "red": [1, 2, 3, 4, 5, 8],
        "amber": [6, "ghost-9", 10, 11, 12, "ghost-13"],
    },
    "electric": {
        "file": "cluster-electric.png",
        "tag": "Electric. 8 is the 12V rectangle only. Turtle / car-with-! / plug: say none of these.",
        "left": "PWR",
        "red": ["ghost-1", 2, 3, 4, 5, 8],
        "amber": ["ghost-6", "ghost-9", 10, 11, 12, "ghost-13"],
    },
}

RED = (255, 56, 56, 255)
AMBER = (255, 176, 32, 255)
RED_HEX = "#ff3838"
AMBER_HEX = "#ffb020"
WHITE = (236, 236, 240, 255)
MUTED = (150, 152, 160, 255)
BEZEL = (48, 50, 56, 255)
WELL = (10, 10, 12, 255)
BG = (18, 18, 22, 255)

W, H = 1760, 960
CELL = 164
ICON = 100
GAP = 12
LAMP_PNG = 256


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def rounded_rect(draw: ImageDraw.ImageDraw, box, fill, radius: int, outline=None, width: int = 1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def colorize_svg(svg: str, hex_color: str) -> str:
    svg = svg.replace("currentColor", hex_color)
    root = re.search(r"<svg\b[^>]*>", svg)
    root_fill = root.group(0) if root else ""
    if "fill=" not in root_fill:
        svg = svg.replace("<svg ", f'<svg fill="{hex_color}" ', 1)
    if 'fill="none"' not in root_fill:
        svg = re.sub(r"<path(?![^>]*\bfill=)", f'<path fill="{hex_color}"', svg)
    return svg


def raster_svg(svg_stem: str, kind: str) -> Image.Image:
    hex_color = RED_HEX if kind == "red" else AMBER_HEX
    svg = (SVG_DIR / f"{svg_stem}.svg").read_text()
    svg = colorize_svg(svg, hex_color)
    inner = 184
    png = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=inner, output_height=inner)
    icon = Image.open(BytesIO(png)).convert("RGBA")
    canvas = Image.new("RGBA", (LAMP_PNG, LAMP_PNG), (0, 0, 0, 255))
    glow = icon.filter(ImageFilter.GaussianBlur(5))
    glow = ImageEnhance.Brightness(glow).enhance(1.7)
    ox = (LAMP_PNG - inner) // 2
    canvas.alpha_composite(glow, (ox, ox))
    canvas.alpha_composite(icon, (ox, ox))
    return canvas


def draw_gauge(img: Image.Image, cx: int, cy: int, r: int, label: str) -> None:
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.ellipse((cx - r - 10, cy - r - 10, cx + r + 10, cy + r + 10), fill=(28, 28, 32, 255), outline=BEZEL, width=10)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(8, 8, 10, 255), outline=(70, 72, 80, 255), width=3)
    for i in range(13):
        ang = math.radians(220 - i * (220 - 40) / 12)
        inner, outer = r - (22 if i % 2 == 0 else 14), r - 6
        x1, y1 = cx + inner * math.cos(ang), cy - inner * math.sin(ang)
        x2, y2 = cx + outer * math.cos(ang), cy - outer * math.sin(ang)
        d.line((x1, y1, x2, y2), fill=(90, 92, 100, 255), width=3 if i % 2 == 0 else 2)
    rest = math.radians(220)
    nx = cx + (r - 36) * math.cos(rest)
    ny = cy - (r - 36) * math.sin(rest)
    d.line((cx, cy, nx, ny), fill=(200, 40, 40, 255), width=4)
    d.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=(180, 40, 40, 255))
    f = font(18, bold=True)
    bbox = d.textbbox((0, 0), label, font=f)
    tw = bbox[2] - bbox[0]
    d.text((cx - tw / 2, cy + r * 0.28), label, font=f, fill=MUTED)
    img.alpha_composite(overlay)


def stamp_number(cell: Image.Image, n: int, colour: tuple[int, int, int, int]) -> None:
    d = ImageDraw.Draw(cell)
    f = font(20, bold=True)
    cx, cy = CELL / 2, CELL - 22
    d.ellipse((cx - 16, cy - 16, cx + 16, cy + 16), fill=(0, 0, 0, 230), outline=colour, width=3)
    text = str(n)
    bbox = d.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((cx - tw / 2, cy - th / 2 - 1), text, font=f, fill=WHITE)


def caption(cell: Image.Image, text: str, colour: tuple[int, int, int, int]) -> None:
    d = ImageDraw.Draw(cell)
    f = font(11, bold=True)
    bbox = d.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    d.text(((CELL - tw) / 2, CELL - 52), text, font=f, fill=colour)


def make_cell(n: int, png_name: str, kind: str) -> Image.Image:
    colour = RED if kind == "red" else AMBER
    cell = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    d = ImageDraw.Draw(cell)
    rounded_rect(d, (0, 0, CELL - 1, CELL - 1), WELL, 16, outline=colour, width=2)
    icon = Image.open(ASSETS / png_name).convert("RGBA").resize((ICON, ICON), Image.Resampling.LANCZOS)
    ox = (CELL - ICON) // 2
    oy = 6
    cell.alpha_composite(icon, (ox, oy))
    if n == 6:
        caption(cell, "FLASHING = 7", AMBER)
    elif n == 13:
        caption(cell, "START-UP OK", AMBER)
    stamp_number(cell, n, colour)
    return cell


def make_ghost(n: int, kind: str) -> Image.Image:
    colour = RED if kind == "red" else AMBER
    cell = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    d = ImageDraw.Draw(cell)
    d.rounded_rectangle((0, 0, CELL - 1, CELL - 1), radius=16, outline=(70, 72, 80, 255), width=2)
    f = font(11, bold=True)
    t = "NOT THIS CAR"
    bbox = d.textbbox((0, 0), t, font=f)
    tw = bbox[2] - bbox[0]
    d.text(((CELL - tw) / 2, CELL / 2 - 18), t, font=f, fill=MUTED)
    stamp_number(cell, n, colour)
    return cell


def layout_cell(slot) -> Image.Image:
    if isinstance(slot, str) and slot.startswith("ghost-"):
        n = int(slot.split("-", 1)[1])
        kind = BY_N[n][3]
        return make_ghost(n, kind)
    n_id, _svg, png_name, kind = BY_N[int(slot)]
    return make_cell(n_id, png_name, kind)


def row_of(slots: list) -> Image.Image:
    n = len(slots)
    w = n * CELL + (n - 1) * GAP
    row = Image.new("RGBA", (w, CELL), (0, 0, 0, 0))
    x = 0
    for slot in slots:
        row.alpha_composite(layout_cell(slot), (x, 0))
        x += CELL + GAP
    return row


def render_lamp_pngs() -> None:
    for _n, stem, png_name, kind in LAMPS:
        im = raster_svg(stem, kind)
        path = ASSETS / png_name
        im.convert("RGB").save(path, "PNG", optimize=True)
        print(f"wrote {path.name} ({path.stat().st_size} bytes)")


def compose_cluster(board_id: str, spec: dict) -> None:
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    rounded_rect(d, (24, 24, W - 25, H - 25), (22, 22, 26, 255), 36, outline=BEZEL, width=6)
    rounded_rect(d, (40, 40, W - 41, H - 41), (16, 16, 20, 255), 28)

    title = font(28, bold=True)
    t = "YOUR DASHBOARD"
    bbox = d.textbbox((0, 0), t, font=title)
    d.text(((W - (bbox[2] - bbox[0])) / 2, 56), t, font=title, fill=WHITE)

    sub = font(16)
    s = spec["tag"] + " If it flashes, say flashing."
    bbox = d.textbbox((0, 0), s, font=sub)
    d.text(((W - (bbox[2] - bbox[0])) / 2, 94), s, font=sub, fill=MUTED)

    draw_gauge(img, 148, 470, 100, spec["left"])
    draw_gauge(img, W - 148, 470, 100, "SPEED")

    red_row = row_of(spec["red"])
    amber_row = row_of(spec["amber"])

    well_w = max(red_row.width, amber_row.width) + 48
    well_h = red_row.height + amber_row.height + GAP + 88
    well_x = (W - well_w) // 2
    well_y = 150
    rounded_rect(
        d,
        (well_x, well_y, well_x + well_w, well_y + well_h),
        (8, 8, 10, 255),
        20,
        outline=(40, 42, 48, 255),
        width=2,
    )

    label_f = font(14, bold=True)
    d.text((well_x + 24, well_y + 16), "STOP IF LIT  ·  red", font=label_f, fill=RED)
    d.text((well_x + 24, well_y + 48 + CELL + 8), "CHECK  ·  amber", font=label_f, fill=AMBER)

    img.alpha_composite(red_row, (well_x + (well_w - red_row.width) // 2, well_y + 40))
    img.alpha_composite(amber_row, (well_x + (well_w - amber_row.width) // 2, well_y + 40 + CELL + 36))

    foot = font(15)
    ftxt = "Circled number, not a count. Blue/green are not faults. If none of these shapes match, say none."
    bbox = d.textbbox((0, 0), ftxt, font=foot)
    d.text(((W - (bbox[2] - bbox[0])) / 2, H - 72), ftxt, font=foot, fill=MUTED)

    out = ASSETS / spec["file"]
    img.convert("RGB").save(out, "PNG", optimize=True)
    print(f"wrote {out.name} ({out.stat().st_size} bytes) [{board_id}]")


def main() -> None:
    render_lamp_pngs()
    for board_id, spec in BOARDS.items():
        compose_cluster(board_id, spec)


if __name__ == "__main__":
    main()
