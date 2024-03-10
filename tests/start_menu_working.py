# Trying to create a working starup menu

# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import GroupedDrawings, Drawing
from classes.menu import MainMenu, Menu, Button
from classes.logo import Logo
from classes.crosshair import CrossHair

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Working Startup Menu')
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
menu = MainMenu(size=size)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    screen.fill('grey')
    
    menu.update()

    spr_tup = (menu, ch)
    sprites = pg.sprite.RenderPlain(spr_tup)
    ch.update()
    sprites.draw(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()