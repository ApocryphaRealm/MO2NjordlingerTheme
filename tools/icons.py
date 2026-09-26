r"""Line icons for MO2's smaller buttons in the Njordlinger theme - 24x24, one-unit strokes at 87% opacity, which is the
weight and bone grey of Njordlinger's toolbar set (src\toolbar\, about 2 px lines of #dbd6cd at 48 px). Drawn for this
theme (no third-party icon art). {i} = icon colour, {a} = accent colour."""

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" '
        'stroke="{i}" stroke-opacity="0.87" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">')
TAIL = "</svg>"

ICONS = {
    # change game / instance: two stacked panels
    "instances": '<rect x="3" y="7" width="13" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-3" stroke="{a}"/>',
    # install a mod from an archive: a chest with an arrow into it
    "install": '<path d="M4 11h16v8a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/><path d="M4 11l2-4h12l2 4" stroke="{a}"/><path d="M12 2v7M9 6l3 3 3-3"/>',
    # browse Nexus: a cloud with a down arrow
    "nexus": '<path d="M7 18a4 4 0 0 1-.6-7.95A6 6 0 0 1 18 9a4 4 0 0 1-1 8.9"/><path d="M12 12v8M9 17l3 3 3-3" stroke="{a}"/>',
    # the mod's web page: a globe
    "modpage": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18" stroke="{a}"/>',
    # profiles: two figures
    "profiles": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6" stroke="{a}"/>',
    # refresh: two arrows chasing
    "refresh": '<path d="M20 11A8 8 0 0 0 5.6 6.2L3 9"/><path d="M3 4v5h5" stroke="{a}"/><path d="M4 13a8 8 0 0 0 14.4 4.8L21 15"/><path d="M21 20v-5h-5" stroke="{a}"/>',
    # executables: a window with a run triangle
    "executables": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8h18" stroke="{a}"/><path d="M10 11.5v5l4.5-2.5z"/>',
    # tools: a wrench
    "tools": '<path d="M14.7 6.3a4 4 0 0 0 5 5L21 13a6 6 0 0 1-7.6 1.4L6 21.8a2.1 2.1 0 0 1-3-3l7.4-7.4A6 6 0 0 1 11.8 3.8z"/><circle cx="5.2" cy="18.8" r=".6" stroke="{a}"/>',
    # settings: a cog
    "settings": '<circle cx="12" cy="12" r="3" stroke="{a}"/><path d="M12 2.5l1.6 2.4 2.8-.6.6 2.8 2.4 1.6-1.2 2.6 1.2 2.6-2.4 1.6-.6 2.8-2.8-.6L12 21.5l-1.6-2.4-2.8.6-.6-2.8-2.4-1.6 1.2-2.6-1.2-2.6 2.4-1.6.6-2.8 2.8.6z"/>',
    # endorse: a heart
    "endorse": '<path d="M12 20s-7.5-4.6-9-9.3A4.6 4.6 0 0 1 12 7a4.6 4.6 0 0 1 9 3.7C19.5 15.4 12 20 12 20z"/><path d="M8.5 10.5l2 2 4-4" stroke="{a}"/>',
    # notifications / problems: a warning triangle
    "problems": '<path d="M10.3 3.9L2.4 18a2 2 0 0 0 1.7 3h15.8a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z" fill="#000000" fill-opacity="1"/><path d="M12 9v5M12 17.5v.01" stroke="{a}"/>',
    # update: an arrow up out of a circle
    "update": '<circle cx="12" cy="12" r="9"/><path d="M12 16.5v-9M8 11l4-4 4 4" stroke="{a}"/>',
    # help: a question mark in a circle
    "help": '<circle cx="12" cy="12" r="9"/><path d="M9.3 9a2.8 2.8 0 0 1 5.4 1c0 1.9-2.7 2.5-2.7 4" stroke="{a}"/><path d="M12 17.5v.01" stroke="{a}"/>',
    # list options: three dots
    "dots": '<circle cx="5" cy="12" r="1.3"/><circle cx="12" cy="12" r="1.3" stroke="{a}"/><circle cx="19" cy="12" r="1.3"/>',
    # open folder menu
    "folder": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M3 10h18" stroke="{a}"/>',
    # back up the list: a floppy-style save
    "backup": '<path d="M5 4h11l3 3v12a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1z"/><path d="M8 4v5h7V4" stroke="{a}"/><path d="M8 20v-6h8v6" stroke="{a}"/>',
    # restore a backup: an arrow turning back round a clock hand
    "restore": '<path d="M4 12a8 8 0 1 0 2.4-5.7L4 8.6"/><path d="M4 4v4.6h4.6" stroke="{a}"/><path d="M12 8v4l3 2" stroke="{a}"/>',
    # clear / close
    "cross": '<path d="M6 6l12 12M18 6L6 18"/>',
    # sort
    "sort": '<path d="M7 4v16M4 7l3-3 3 3"/><path d="M17 20V4M14 17l3 3 3-3" stroke="{a}"/>',
    "minus": '<path d="M5 12h14"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    # run
    "play": '<path d="M7 4.5v15l12-7.5z"/>',
    # create a shortcut
    "shortcut": '<path d="M14 4h6v6"/><path d="M20 4l-9 9" stroke="{a}"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    # track a mod
    "pin": '<path d="M9 3h6l-1 6 4 4H6l4-4z"/><path d="M12 13v8" stroke="{a}"/>',
    # the plugin's own button: a brush over a palette
    "theme": '<path d="M12 3a9 9 0 1 0 0 18c1.2 0 1.6-.9 1.3-1.8-.4-1.1.3-2.2 1.5-2.2H17a4 4 0 0 0 4-4c0-5.5-4-10-9-10z"/><circle cx="7.5" cy="11" r="1.2" stroke="{a}"/><circle cx="10" cy="7" r="1.2" stroke="{a}"/><circle cx="14.5" cy="7" r="1.2" stroke="{a}"/>',
}


def svg(name, icon, accent):
    return HEAD.replace("{i}", icon) + ICONS[name].replace("{a}", accent).replace("{i}", icon) + TAIL
