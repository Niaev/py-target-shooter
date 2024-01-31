# My first attempt on making a real game with PyGame
# It should be just a shooter like Duck Hunt but even more simple
# Counting points and with a cronometer running on the corner
# Just that
# This code is based on multiple PyGame website tutorials and
# Specially the Chimp one:
# https://www.pygame.org/docs/tut/ChimpLineByLine.html

# PyGame Imports
import pygame as pg

# Project Imports
from classes.crosshair import CrossHair
from classes.hud import Hud

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game')
clock = pg.time.Clock()
run = True

# Set system cursor as transparent
pg.mouse.set_cursor(
    (8,8),
    (0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0)
)

# Game Entities
ch = CrossHair((0,0))
hud = Hud()

hud_already_loaded = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill('grey')
    if not hud_already_loaded:
        hud.draw(screen)

    # Load crosshair and make it follow the mouse
    ss = pg.sprite.RenderPlain((ch))
    ss.update()
    ss.draw(screen)

    hud.update_time(screen)

    pg.display.flip()

    clock.tick(60)

pg.quit()