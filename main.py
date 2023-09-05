import pygame as py

# =============================================

import settings as sett
import functions as fun
import sprites as spr

# ======================================================================================================================

window = py.display.set_mode([sett.WIDTH, sett.HEIGHT])

time = py.time.Clock()

# ======================================================================================================================


# ======================================================================================================================

while_number = False

while while_number == 0:
    window.fill("#000000")

    # ===================================================================
    py.display.update()
    events = py.event.get()
    for f in events:
        if f.type == py.QUIT:
            while_number += 1

    time.tick(60)