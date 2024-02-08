# My first attempt on making a real game with PyGame
# It should be just a shooter like Duck Hunt but even more simple
# Counting points and with a cronometer running on the corner
# Just that
# This code is based on multiple PyGame website tutorials and
# Specially the Chimp one:
# https://www.pygame.org/docs/tut/ChimpLineByLine.html

# General Imports
from random import randint

# PyGame Imports
import pygame as pg

# Project Imports
from classes.crosshair import CrossHair
from classes.hud import Hud
from classes.targets import BigTarget, MediumTarget, SmallTarget, SuperSmallTarget
from classes.popups import CHPopUp, TPopUp

# Setup game
pg.init()
## Setting game screen to be 600x600 pixels
size = width, height = 600, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('Target Shooter: The Game')
pg.display.set_icon(pg.image.load('data/imgs/icon.png'))
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
ch = CrossHair((0,0))
hud = Hud()

# Initialization stuff
hud_already_loaded = 0

# Objects that variate to show up on the screen
targets_on_screen = []
popups = []

# Some configuration stuff idk
screen_limits = [(30, width-30), (78, height-30)]
rng_t = [1,1,1,1,2,2,2,3,3,4]
targets_handler = {
    '1': BigTarget,
    '2': MediumTarget,
    '3': SmallTarget,
    '4': SuperSmallTarget
}

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

                # Create new popup
                popup = CHPopUp(ch, target)
                popups.append(popup)

    # Filling the screen with up to 10 targets
    if len(targets_on_screen) < 2:
        rng = rng_t[randint(0, len(rng_t)-1)]
        ChosenTarget = targets_handler[str(rng)]

        # Make sure a new target won't collide with an existing target
        perfect = False
        while not perfect:
            x = randint(*screen_limits[0])
            y = randint(*screen_limits[1])
            t = ChosenTarget((x, y))

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
            # Create new popup
            popup = TPopUp(target)
            popups.append(popup)
            # Remove target
            targets_on_screen.remove(target)

    # Initiate screen
    screen.fill('grey')
    # Show Hud
    if not hud_already_loaded:
        hud.draw(screen)

    # Check and draw all popups
    for popup in popups:
        r = popup.draw(screen)
        if not r:
            popups.remove(popup)

    # Load crosshair and targets
    ss = pg.sprite.RenderPlain((*targets_on_screen, ch))
    ss.update()
    ss.draw(screen)

    # Update hud time counter
    hud.update_time(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()