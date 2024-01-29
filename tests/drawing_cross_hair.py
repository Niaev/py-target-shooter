# Trying to create a cross hair with no image

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

# Set system cursor as transparent
pg.mouse.set_cursor(
    (8,8),
    (0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0)
)

class Drawing(pg.sprite.Sprite):
    def __init__(self, shape: tuple, pos: tuple, color:str='black'):
        super().__init__()
        self.image = pg.Surface(shape)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

class GroupedDrawings(pg.sprite.Sprite):
    def __init__(self, sprites):
        super().__init__()
        self.rect = sprites[0].rect.copy()
        for sprite in sprites[1:]:
            self.rect.union_ip(sprite.rect)
        
        self.image = pg.Surface(self.rect.size, pg.SRCALPHA)
        for sprite in sprites:
            self.image.blit(
                sprite.image,
                (
                    sprite.rect.x-self.rect.left,
                    sprite.rect.y-self.rect.top
            ))

        self.offset = (-self.rect.size[0]/2,-self.rect.size[1]/2)

    def update(self):
        """Moves with the mouse"""

        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.offset)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill('grey')

    ## Drawing cross hair -- doing it poorly
    #ch_reference = pg.draw.rect(screen, 'blue', (ch_pos.x-30, ch_pos.y-30, 60, 60))
    #ch_top = pg.draw.rect(screen, 'black', (ch_pos.x-3, ch_pos.y-30, 6, 20))
    #ch_left = pg.draw.rect(screen, 'black', (ch_pos.x+10, ch_pos.y-3, 20, 6))
    #ch_bottom = pg.draw.rect(screen, 'black', (ch_pos.x-3, ch_pos.y+10, 6, 20))
    #ch_right = pg.draw.rect(screen, 'black', (ch_pos.x-30, ch_pos.y-3, 20, 6))

    # Drawing cross hair parts
    ch_top = Drawing((6, 20), (ch_pos.x-3, ch_pos.y-30))
    ch_left = Drawing((20, 6), (ch_pos.x+10, ch_pos.y-3))
    ch_bottom = Drawing((6, 20), (ch_pos.x-3, ch_pos.y+10))
    ch_right = Drawing((20, 6), (ch_pos.x-30, ch_pos.y-3))
    # Grouping to cross hair parts
    all_draws = pg.sprite.Group(ch_top, ch_left, ch_bottom, ch_right)
    sprites = [sprite for sprite in all_draws]
    group = GroupedDrawings(sprites)
    # Draw
    #pg.draw.rect(screen, 'black', group.rect, 1) # For some reason,
    #                                             # This draws just a
    #                                             # Black square
    #for sprite in sprites: # This draws the crosshair correctly
    #    pg.draw.rect(screen, 'black', sprite.rect) # ,1) # Using this 
    #                                                     # Width parameter 
    #                                                     # Makes it cooler!!
    ## This works!!
    sps = pg.sprite.RenderPlain((group))
    sps.update()
    sps.draw(screen)
    
    pg.display.flip()
    
    clock.tick(60)

pg.quit()