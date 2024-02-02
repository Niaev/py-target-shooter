# Trying to create targets

# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import GroupedDrawings, Drawing

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Targets Drawing')
clock = pg.time.Clock()
run = True

class Target(GroupedDrawings):
    def __init__(self, center:tuple, layers: int, size:tuple, colors:list):
        x = center[0]
        y = center[1]

        layer_thicness = size[0] / layers

        sprites = []
        old_size = ()
        curr_size = size

        for layer in range(layers):
            color_idx = layer % 2
            color = colors[color_idx]

            if layer == 0:
                offset_x = size[0]/2
                offset_y = size[1]/2
                old_size = size
            else:
                curr_x = old_size[0] - layer_thicness
                curr_y = old_size[1] - layer_thicness
                curr_size = (curr_x, curr_y)
                offset_x = curr_size[0]/2
                offset_y = curr_size[1]/2
                old_size = curr_size

            sprite = Drawing(curr_size, (x-offset_x, y-offset_y), color=color)
            sprites.append(sprite)

        super().__init__(sprites)

class BigTarget(Target):
    def __init__(self, center:tuple):
        super().__init__(
            center, 
            5, 
            (60, 60),
            ['#7B0828', 'white']
        )

class MediumTarget(Target):
    def __init__(self, center:tuple):
        super().__init__(
            center, 
            5, 
            (50, 50),
            ['#0A2342', 'white']
        )

class SmallTarget(Target):
    def __init__(self, center:tuple):
        super().__init__(
            center, 
            3, 
            (36, 36),
            ['#FFF275', 'white']
        )

class SuperSmallTarget(Target):
    def __init__(self, center:tuple):
        super().__init__(
            center, 
            3, 
            (18, 18),
            ['#FFDAC6', 'white']
        )

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill('grey')

    bt = BigTarget((36, height/2))
    mt = MediumTarget((width/3, height/2))
    st = SmallTarget((width/3*2, height/2))
    sst = SuperSmallTarget((width-24, height/2))
    sprites = pg.sprite.RenderPlain((bt, mt, st, sst))
    sprites.draw(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()