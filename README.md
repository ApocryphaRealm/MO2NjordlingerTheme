# Njordlinger - a Mod Organizer 2 theme

The dark, Nordic-grey theme of the Njordlinger modlist: Skyrim-style button faces and widget art, its own toolbar and
button icons, dark mod rows with black separators.

## Install

1. Copy `stylesheets\Njordlinger.qss` and the `stylesheets\Njordlinger\` folder into `<MO2>\stylesheets\`.
2. In MO2: Settings > General > Style > **Njordlinger**.

**Recommended: MO2 Theme Framework.** A stylesheet alone cannot colour separators, the mod list's conflict
highlights, or plugin windows that hard-code their colours (the Plugin Browser, for one). With MO2 Theme Framework
installed, the theme's `Njordlinger\theme.json` takes care of those too - and switching to another theme puts your own
colours back.

## Changing the colours

Edit `src\palette.json` and run `python tools\build_theme.py` (Python 3 with Pillow). The sheet, the tinted art, the
icons and `theme.json` are all rebuilt from the palette.

Licence: GPL-3.0-or-later (`LICENSE`, `NOTICE.md`), built on chintsu_kun's GPL-3.0 Skyrim theme (`THIRD_PARTY_NOTICES.md`).