# Trying to create a working set of buttons

# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import GroupedDrawings, Drawing
from classes.crosshair import CrossHair
from classes.menu import Button

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Multiple Buttons')
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
start_btn = Button(
    'start',
    (width/2, height/2 - 80),
    (200, 50)
)
opt_btn = Button(
    'options',
    (width/2, height/2),
    (200, 50)
)
cred_btn = Button(
    'credits',
    (width/2, height/2 + 80),
    (200, 50)
)
ch = CrossHair((0,0))

btns = {
    'start': start_btn,
    'opt': opt_btn,
    'cred': cred_btn
}
l_maker = lambda d: [d[k] for k in d]

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_presses = pg.mouse.get_pressed()
            if mouse_presses[0]:
                for k in btns:
                    b = btns[k]
                    if b.rect.collidepoint(pg.mouse.get_pos()):
                        print(k)
    
    screen.fill('grey')

    for k in btns:
        b = btns[k]
        if b.rect.collidepoint(pg.mouse.get_pos()) and b.mode == 'normal':
            btns[k] = Button(
                b.label,
                (b.x, b.y),
                (b.width, b.height),
                mode='hover',
            )
        elif not b.rect.collidepoint(pg.mouse.get_pos()) and b.mode == 'hover':
            btns[k] = Button(
                b.label,
                (b.x, b.y),
                (b.width, b.height),
            )

    l_btns = l_maker(btns)
    spr_tup = (*l_btns, ch)
    sprites = pg.sprite.RenderPlain(spr_tup)
    ch.update()
    sprites.draw(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()