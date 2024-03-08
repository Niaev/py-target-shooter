# Trying to create a working simple button

# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import GroupedDrawings, Drawing
from classes.crosshair import CrossHair

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Simple Button')
clock = pg.time.Clock()
run = True

class Button(GroupedDrawings):
    def __init__(self, center:tuple, size:tuple, mode:str='normal'):
        self.x, self.y = center
        self.width, self.height = size

        self.sprites = []
        self.font = pg.font.Font('data/fonts/console/pixeldroidConsoleRegular.ttf', 48)

        self.offset_x = self.width / 2
        self.offset_y = self.height / 2

        if mode == 'normal':
            border_text_color = 'black' # #000000
            bg_color = 'grey' # #bebebe
        elif mode == 'hover':
            border_text_color = 'black' #'#444444'
            bg_color = '#999999'

        self.background = Drawing(
            (self.width, self.height), 
            (self.x-self.offset_x, self.y-self.offset_y), 
            color=bg_color
        )

        self.bd_top = Drawing(
            (self.width, 6), 
            (self.x-self.offset_x, self.y-self.offset_y-6),
            color=border_text_color
        )

        self.bd_right = Drawing(
            (6, self.height), 
            (self.x+self.offset_x, self.y-self.offset_y),
            color=border_text_color
        )

        self.bd_bottom = Drawing(
            (self.width, 6), 
            (self.x-self.offset_x, self.y+self.offset_y),
            color=border_text_color
        )

        self.bd_left = Drawing(
            (6, self.height), 
            (self.x-self.offset_x-6, self.y-self.offset_y),
            color=border_text_color
        )

        self.sprites = [
            self.background,
            self.bd_top,
            self.bd_right,
            self.bd_bottom,
            self.bd_left
        ]

        super().__init__(self.sprites)

        self.text = self.font.render('Ok', True, border_text_color)
    
        text_pos = self.text.get_rect(x=self.width/2-11, y=self.height/2-17)
        self.image.blit(self.text, text_pos)

        self.mode = mode
        
# Set system cursor as transparent
pg.mouse.set_cursor(
    (8,8),
    (0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0)
)

# Game Entities
btn = Button(
    (width/2, height/2),
    (100, 50)
)
ch = CrossHair((0,0))

btns = {
    'Ok': btn
}
l_maker = lambda d: [d[k] for k in d]

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    screen.fill('grey')

    for k in btns:
        b = btns[k]
        if b.rect.collidepoint(pg.mouse.get_pos()) and b.mode == 'normal':
            btns[k] = Button(
                (width/2, height/2),
                (100, 50),
                mode='hover',
            )
        elif not b.rect.collidepoint(pg.mouse.get_pos()) and b.mode == 'hover':
            btns[k] = Button(
                (width/2, height/2),
                (100, 50),
            )

    l_btns = l_maker(btns)
    spr_tup = (*l_btns, ch)
    sprites = pg.sprite.RenderPlain(spr_tup)
    ch.update()
    sprites.draw(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()