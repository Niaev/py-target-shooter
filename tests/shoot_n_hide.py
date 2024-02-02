# Trying to make a target be shot and hide in sequence

# PyGame Imports
import pygame as pg

# Project Imports
from classes.targets import BigTarget
from classes.crosshair import CrossHair
from classes.hud import Hud

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Shoot and Hide')
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
hud = Hud()
ch = CrossHair((0,0))

hud_already_loaded = 0
targets_on_screen = []
position_handler = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_presses = pg.mouse.get_pressed()
            if mouse_presses[0]:
                points = ch.shoot(targets_on_screen)
                hud.update_score(screen, points)

                if points > 0:
                    position_handler += 1
                    if position_handler == 4: position_handler = 0
                    targets_on_screen = []
    
    if len(targets_on_screen) == 0:
        if position_handler == 0:
            t = BigTarget((width/3, height/3))
        elif position_handler == 1:
            t = BigTarget((width/3, height/3*2))
        elif position_handler == 2:
            t = BigTarget((width/3*2, height/3*2))
        elif position_handler == 3:
            t = BigTarget((width/3*2, height/3))    
        targets_on_screen.append(t)

    screen.fill('grey')
    if not hud_already_loaded:
        hud.draw(screen)

    spr_tup = (*targets_on_screen, ch)
    sprites = pg.sprite.RenderPlain(spr_tup)
    ch.update()
    sprites.draw(screen)
    
    hud.update_time(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()