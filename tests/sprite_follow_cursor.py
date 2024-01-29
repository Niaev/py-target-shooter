# Trying to create a cursor following simple sprite

# PyGame Imports
import pygame as pg

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Cross Hair Drawing')
clock = pg.time.Clock()
run = True

# Game Entities
## Cross Hair position
ch_pos = pg.Vector2(width / 2, height / 2)

class Cursor(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((10, 10))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft=(10, 10))
        self.offset = (0, 0)

    def update(self):
        """Moves with the mouse"""

        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.offset)

# Set system cursor as transparent
pg.mouse.set_cursor(
    (8,8),
    (0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0)
)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill('grey')

    c = Cursor()
    sprites = pg.sprite.RenderPlain((c))
    sprites.update()
    sprites.draw(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()