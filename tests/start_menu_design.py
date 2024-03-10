# Trying to create a working starup menu

# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import GroupedDrawings, Drawing
from classes.menu import Button
from classes.logo import Logo
from classes.crosshair import CrossHair

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Startup Menu')
clock = pg.time.Clock()
run = True

class StartMenu(GroupedDrawings):
    def __init__(self, size:tuple):
        self.logo = Logo()
        self.logo.center((size[0]/2, 125))

        self.start = Button(
            'start',
            (size[0]/2, size[1]/2),
            (200, 50)
        )

        self.options = Button(
            'options',
            (size[0]/2, size[1]/2 + 80),
            (200, 50)
        )

        self.credits = Button(
            'credits',
            (size[0]/2, size[1]/2 + 160),
            (200, 50)
        )

        #self.items = [self.logo]
        sprites = [
            self.logo,
            self.start,
            self.options,
            self.credits
        ]
        super().__init__(sprites)

# Set system cursor as transparent
pg.mouse.set_cursor(
    (8,8),
    (0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0)
)

# Game Entities
ch = CrossHair((0,0))
menu = StartMenu(size=size)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    screen.fill('grey')

    spr_tup = (menu, ch)
    sprites = pg.sprite.RenderPlain(spr_tup)
    ch.update()
    sprites.draw(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()