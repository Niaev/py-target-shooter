# Trying to make a counter that increases for every click

# General Imports
from datetime import datetime

# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import Drawing, GroupedDrawings
from classes.crosshair import CrossHair

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Click Counter')
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
class Hud(GroupedDrawings):
    def __init__(self, width:int=600, height:int=48, pos:tuple=(0,0)):
        self.start = datetime.now()

        self.width = width
        self.height = height
        
        self.x = pos[0]
        self.y = pos[1]

        self.font = pg.font.SysFont('Console', 48)
        self.time = self.font.render('00:00', True, (0,0,0))
        self.score = self.font.render('0', True, (0,0,0))

        self.amount = 0

    def draw_time(self, screen):
        time_pos = self.time.get_rect(x=self.x-2, y=self.y-15)
        screen.blit(self.time, time_pos)

    def draw_score(self, screen):
        score_rect = self.score.get_rect(x=-50, y=-50)
        score_size = score_rect.size
        score_width = score_size[0]+1
        score_pos = self.score.get_rect(x=self.width-score_width, y=self.y-15)
        screen.blit(self.score, score_pos)

    def draw(self, screen):
        self.draw_time(screen)
        self.draw_score(screen)

    def update_time(self, screen):
        now = datetime.now()

        diff = now - self.start

        _secs = diff.seconds
        nmins = _secs // 60
        try:
            nsecs = _secs % (nmins * 60)
        except ZeroDivisionError:
            nsecs = _secs % 60

        mins = '%02d' % nmins
        secs = '%02d' % nsecs

        self.time = self.font.render(f'{mins}:{secs}', True, (0,0,0))
        
        self.draw_time(screen)

    def update_score(self, screen, points=1):
        self.amount += points
        self.score = self.font.render(str(self.amount), True, (0,0,0))

        self.draw_score(screen)

ch = CrossHair((0,0))
hud = Hud()

hud_already_loaded = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_presses = pg.mouse.get_pressed()
            if mouse_presses[0]:
                hud.update_score(screen)

    screen.fill('grey')
    if not hud_already_loaded:
        hud.draw(screen)

    sprites = pg.sprite.RenderPlain((ch))
    ch.update()
    sprites.draw(screen)

    hud.update_time(screen)
    
    pg.display.flip()
    
    clock.tick(60)

pg.quit()