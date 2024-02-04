# Trying to make targets appear on random positions without colliding 
# with each other

# General imports
from datetime import datetime
from random import randint

# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import GroupedDrawings, Drawing
from classes.targets import Target
from classes.hud import Hud

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game - Targets on random positions')
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

    def shoot(self, targets:list) -> Target | None:
        """Verify if it was hit and return corresponding score"""

        hitbox = self.rect.inflate(-50, -50)

        target_hit = None
        for target in targets:
            hit = hitbox.colliderect(target.rect)
            if hit: 
                target_hit = target
                break

        if target_hit:
            return target_hit
        else:
            return None

class BigTarget(Target):
    """Bigger, default target!
    
    Arguments:
    center {tuple} -- Position that defines the initial center of the 
                      sprite
    
    Instance Variables:
    start {datetime} -- Date and time of the startup of the object
    center {tuple} -- Same as the argument
    size {tuple} -- Size of the target and also its hit box
    points {int} -- Amount of points earned from hitting it
    seconds {int} -- Number of seconds target needs to be up
    """

    def __init__(self, center:tuple):
        # Time target was created
        self.start = datetime.now()

        self.center = center
        self.size = (60, 60)

        super().__init__(
            self.center, 
            5, 
            self.size,
            ['#7B0828', 'white']
        )

        self.points = 1
        self.seconds = 10

    def time_over(self) -> bool:
        """Check if target time is over"""

        # Current time
        now = datetime.now()
        # Difference between start and current time
        diff = now - self.start

        # Return if the time is over
        if self.seconds <= diff.seconds:
            return True
        return False
    
    def collide(self, obj: 'pg.Surface') -> bool:
        """Verify if given object collides with target"""

        hitbox = self.rect
        co = hitbox.colliderect(obj.rect)
        return bool(co)

hud = Hud()
ch = CrossHair((0,0))

hud_already_loaded = 0
targets_on_screen = []
screen_limits = [(30, width-30), (78, height-30)]

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Check Mouse Button 1 click
            mouse_presses = pg.mouse.get_pressed()
            if mouse_presses[0]:
                target = ch.shoot(targets_on_screen)
                if target: # Check if a Target is shot
                    # Update points and remove target from screen
                    hud.update_score(screen, target.points)
                    targets_on_screen.remove(target)
    
    # Filling the screen with up to 10 targets
    if len(targets_on_screen) < 10:
        # Make sure a new target won't collide with an existing target
        perfect = False
        while not perfect:
            x = randint(*screen_limits[0])
            y = randint(*screen_limits[1])
            t = BigTarget((x, y))

            collisions = 0
            for target in targets_on_screen:
                co = target.collide(t)
                if co:
                    collisions += 1
            
            if collisions == 0:
                perfect = True
        
        # If it is ok, we have a new target
        targets_on_screen.append(t)

    # Check if any target time on screen is over
    for target in targets_on_screen:
        if target.time_over():
            targets_on_screen.remove(target)

    # Initiate screen
    screen.fill('grey')
    # Show Hud
    if not hud_already_loaded:
        hud.draw(screen)

    # Display all objects on screen
    spr_tup = (*targets_on_screen, ch)
    sprites = pg.sprite.RenderPlain(spr_tup)
    ch.update()
    sprites.draw(screen)
    
    # Update hud time
    hud.update_time(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()