# Trying to implement targets alongside with crosshair

# PyGame Imports
import pygame as pg

# Project Imports
from classes.targets import BigTarget, MediumTarget, SmallTarget, SuperSmallTarget
from classes.crosshair import CrossHair

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Cross Hair Drawing')
clock = pg.time.Clock()
run = True

# Set system cursor as transparent
pg.mouse.set_cursor(
    (8,8),
    (0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0)
)

# Game entities
ch = CrossHair((0,0))
bt = BigTarget((width/3, height/3))
mt = MediumTarget((width/3*2, height/3))
st = SmallTarget((width/3, height/3*2))
sst = SuperSmallTarget((width/3*2, height/3*2))

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill('grey')

    sprites = pg.sprite.RenderPlain((bt, mt, st, sst, ch))
    ch.update()
    sprites.draw(screen)
    
    pg.display.flip()
    
    clock.tick(60)

pg.quit()