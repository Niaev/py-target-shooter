# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import Drawing, GroupedDrawings

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

        self.shooting = False
        #self.rotation = 0

    def update(self):
        """Moves with the mouse"""

        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.offset)

    def shoot(self, target):
        """Close the cross hair"""
        return None