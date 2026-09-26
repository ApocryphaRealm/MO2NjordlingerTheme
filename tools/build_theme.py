"""Builds the Njordlinger MO2 theme as plain files, the way MO2 themes are installed - paste into <MO2>\\stylesheets:

    stylesheets\\Njordlinger.qss              the theme
    stylesheets\\Njordlinger\\*.png            widget art and button faces (tinted from the palette)
    stylesheets\\Njordlinger\\icons\\*.png      the 13 toolbar icons - Njordlinger's own set (src\\toolbar\\)
    stylesheets\\Njordlinger\\icons\\*.svg      line icons for MO2's smaller buttons (tools\\icons.py, in the same grey and weight)

Inputs: src\\theme.qss.in ({{role}} placeholders), src\\palette.json (role -> colour), src\\base\\*.png, tools\\icons.py.
Run from the repo root:  python tools\\build_theme.py
"""
import json
import os
import re
import shutil
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import icons  # noqa: E402

THEME = "Njordlinger"
OUT = os.path.join(ROOT, "stylesheets")
THEME_DIR = os.path.join(OUT, THEME)

def argb(text):
    """(a, r, g, b) from #RRGGBB, #AARRGGBB or rgba(r, g, b, a<=1)."""
    t = text.strip()
    m = re.match(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)$", t)
    if m:
        a = 1.0 if m.group(4) is None else float(m.group(4))
        return (round(a * 255) if a <= 1 else int(a), int(m.group(1)), int(m.group(2)), int(m.group(3)))
    h = t.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) == 6:
        return (255, int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
    if len(h) == 8:
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16))
    raise ValueError("not a colour: " + text)


def css(text):
    a, r, g, b = argb(text)
    if a == 255:
        return "#%02x%02x%02x" % (r, g, b)
    return "rgba(%d, %d, %d, %s)" % (r, g, b, ("%.2f" % (a / 255)).rstrip("0").rstrip("."))


def main():
    pal = json.load(open(os.path.join(ROOT, "src", "palette.json"), encoding="utf-8"))["roles"]
    version = open(os.path.join(ROOT, "VERSION"), encoding="utf-8").read().strip()   # issued by the version gate
    if os.path.isdir(THEME_DIR):
        shutil.rmtree(THEME_DIR)
    os.makedirs(os.path.join(THEME_DIR, "icons"))

    # the sheet
    template = open(os.path.join(ROOT, "src", "theme.qss.in"), encoding="utf-8").read()
    missing = set()

    def sub(m):
        role = m.group(1)
        if role not in pal or not pal[role]:
            missing.add(role)
            return "#ff00ff"
        return css(pal[role])
    sheet = re.sub(r"\{\{([a-z_]+)\}\}", sub, template)
    if missing:
        raise SystemExit("palette has no colour for: " + ", ".join(sorted(missing)))
    sheet = sheet.replace("TEMPLATE: tools\\build_theme.py fills each double-braced role from", "Version " + version + ". BUILT by tools\\build_theme.py from")
    open(os.path.join(OUT, THEME + ".qss"), "w", encoding="utf-8", newline="\n").write(sheet)

    # art, tinted
    _, tr, tg, tb = argb(pal.get("art_tint", "#ffffff"))
    base = os.path.join(ROOT, "src", "base")
    n_art = 0
    for name in sorted(os.listdir(base)):
        if not name.lower().endswith(".png"):
            continue
        im = Image.open(os.path.join(base, name)).convert("RGBA")
        if (tr, tg, tb) != (255, 255, 255):
            px = im.load()
            for y in range(im.height):
                for x in range(im.width):
                    r, g, b, a = px[x, y]
                    if a:
                        px[x, y] = (r * tr // 255, g * tg // 255, b * tb // 255, a)
        im.save(os.path.join(THEME_DIR, name))
        n_art += 1

    # toolbar icons - Njordlinger's own set, copied as they are
    for name in sorted(os.listdir(os.path.join(ROOT, "src", "toolbar"))):
        if name.lower().endswith(".png"):
            shutil.copy2(os.path.join(ROOT, "src", "toolbar", name), os.path.join(THEME_DIR, "icons", name))
    missing_png = [n for n in set(re.findall(r"icons/(\w+)\.png", sheet)) if not os.path.isfile(os.path.join(THEME_DIR, "icons", n + ".png"))]
    if missing_png:
        raise SystemExit("the sheet names toolbar images src\\toolbar does not have: " + ", ".join(sorted(missing_png)))
    # line icons for the smaller buttons - every one the sheet names
    wanted = sorted(set(re.findall(r"icons/(\w+)\.svg", sheet)))
    ic, ac = css(pal["icon"]), css(pal["icon_accent"])
    for name in wanted:
        if name not in icons.ICONS:
            raise SystemExit("the sheet names an icon icons.py does not draw: " + name)
        open(os.path.join(THEME_DIR, "icons", name + ".svg"), "w", encoding="utf-8").write(icons.svg(name, ic, ac))

    print("built %s.qss (%d bytes), %d art images, %d toolbar images, %d line icons" % (THEME, len(sheet), n_art, len(os.listdir(os.path.join(ROOT, "src", "toolbar"))), len(wanted)))


if __name__ == "__main__":
    main()
