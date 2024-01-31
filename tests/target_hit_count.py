# Trying to implement targets alongside with crosshair

# PyGame Imports
import pygame as pg

# Project Imports
from classes.targets import BigTarget, MediumTarget, SmallTarget, SuperSmallTarget
from classes.base_drawings import Drawing, GroupedDrawings
from classes.hud import Hud

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
class CrossHair(GroupedDrawings):
    """CrossHair that moves with the user mouse
    
    Arguments:
    center {tuple} -- Position that defines the initial center of the
                      sprite
    size {tuple} -- Defines the size of each crosshair part 
                    (default (6, 20))]
    color {str} -- Filling color (default 'black')

    Instance Variables:
    image {pg.Surface} -- PyGame Surface
    rect {pg.Rect} -- PyGame rectangle
    offset {tuple} -- Two integers defining the sprite offset related
                      to the mouse cursor
    shooting {bool} -- Defines if the user is shooting or not
    """

    def __init__(self, center:tuple, size:tuple=(6,20), color:str='black'):
        x = center[0]
        y = center[1]

        # Drawing cross hair parts separately
        top = Drawing(size, (x-3, y-30), color=color)
        left = Drawing(size[::-1], (x+10, y-3), color=color)
        bottom = Drawing(size, (x-3, y+10), color=color)
        right = Drawing(size[::-1], (x-30, y-3), color=color)

        # Initialize grouped sprite
        sprites = [top, left, bottom, right]
        super().__init__(sprites)

        # Defining sprite offset related to the cursor
        size = self.rect.size
        offset_x = -size[0]/2
        offset_y = -size[1]/2
        self.offset = (offset_x, offset_y)

    def update(self):
        """Moves with the mouse"""

        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.offset)

    def shoot(self, targets:list) -> int:
        """Verify if it was hit and return corresponding score"""

        hitbox = self.rect.inflate(-50, -50)

        target_hit = None
        for target in targets:
            hit = hitbox.colliderect(target.rect)
            if hit: 
                target_hit = target
                break

        if target_hit:
            return target_hit.points
        else:
            return 0

hud = Hud()
ch = CrossHair((0,0))
bt = BigTarget((width/3, height/3))
mt = MediumTarget((width/3*2, height/3))
st = SmallTarget((width/3, height/3*2))
sst = SuperSmallTarget((width/3*2, height/3*2))

hud_already_loaded = 0
targets_on_screen = [bt, mt, st, sst]

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_presses = pg.mouse.get_pressed()
            if mouse_presses[0]:
                points = ch.shoot(targets_on_screen)
                hud.update_score(screen, points)

    screen.fill('grey')
    if not hud_already_loaded:
        hud.draw(screen)

    sprites = pg.sprite.RenderPlain((bt, mt, st, sst, ch))
    ch.update()
    sprites.draw(screen)
    
    hud.update_time(screen)

    pg.display.flip()
    
    clock.tick(60)

pg.quit()