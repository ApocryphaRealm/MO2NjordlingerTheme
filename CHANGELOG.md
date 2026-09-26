# Changelog - Njordlinger (MO2 theme)

Versions are issued by the project's version gate. Written as the change happens (rule 61).

## 1.0.0 - 2026-09-26

First packaged version. The owner: *"i want it packeged with the button faces and icons, the separator and mod colors
and exports that apply to other plugins"*, then *"they just tell you to past the files into the stylesheets folder so
we should do that instead"*.

* Installs like any MO2 theme: `Njordlinger.qss` and the `Njordlinger\` folder into `<MO2>\stylesheets\`.
* Built from one palette (`src\palette.json`, 29 colour roles) by `tools\build_theme.py`. With the shipped palette the
  sheet is token for token the Njordlinger sheet it replaces.
* Button faces and widget art: 35 images, tinted from the palette.
* 24 icons drawn for the theme, on all 13 toolbar actions and MO2's own buttons (list options, open folder, backup /
  restore, clear filters, sort, refresh, run, shortcut, enable / disable all plugins, Nexus, track, endorse).
* `Njordlinger\theme.json` for **MO2 Theme Framework**: black separators, MO2's conflict colours, the palette for other
  plugins, and the Plugin Browser's hard-coded colours mapped onto the palette. Without the framework the theme still
  works as a plain stylesheet.