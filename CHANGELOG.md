# Changelog - Njordlinger (MO2 theme)

Versions are issued by the project's version gate. Written as the change happens (rule 61).

## 1.0.0 - 2026-09-26

First packaged version. The owner: *"i want it packeged with the button faces and icons, the separator and mod colors
and exports that apply to other plugins"*, then *"they just tell you to past the files into the stylesheets folder so
we should do that instead"*.

* Installs like any MO2 theme: `Njordlinger.qss` and the `Njordlinger\` folder into `<MO2>\stylesheets\`.
* Built from one palette (`src\palette.json`, 29 colour roles) by `tools\build_theme.py`. With the shipped palette the
  sheet is token for token the Njordlinger sheet it replaces.
* Separators and mods are coloured separately by the stylesheet itself: separators black (palette `separator`,
  `::item:has-children` - with collapsible separators MO2's separators are the tree's parent rows), mods the dark row
  grey (`mod_row`), with MO2's conflict highlight on mods untouched (the owner: *"make sure the stylesheet in our theme
  mod changes the separator and mod colors separatly"*).
* Button faces and widget art: 35 images, tinted from the palette.
* Toolbar icons: Njordlinger's own set on 12 toolbar actions; the notifications button is a warning triangle filled black
  (the owner: *"i like the warning triangle in black more than the bell"*). MO2's smaller buttons reuse those images
  or get line icons drawn in the same grey and weight.
* `Njordlinger\theme.json` for **MO2 Theme Framework**: black separators, MO2's conflict colours, the palette for other
  plugins, and the Plugin Browser's hard-coded colours mapped onto the palette. Without the framework the theme still
  works as a plain stylesheet.