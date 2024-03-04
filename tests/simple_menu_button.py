# Trying to create a working simple button

# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import GroupedDrawings, Drawing

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Simple Button')
clock = pg.time.Clock()
run = True

class Button():
    def __init__(self):
        return

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill('grey')

    sprites = pg.sprite.RenderPlain(())
    sprites.draw(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()