# General imports
from datetime import datetime

# PyGame imports
import pygame as pg

# Project Imports
from classes.base_drawings import GroupedDrawings, Drawing

class Target(GroupedDrawings):
    """Target to shoot!
    
    Arguments:
    center {tuple} -- Position that defines the initial center of the 
                      sprite
    layers {int} -- Number of stripe layers of the target drawing
    size {tuple} -- Defines the size of the target 
    color {list} -- Contains two strings with the color codes
    seconds {int} -- Number of seconds target needs to be up

    Instance Variables:
    start {datetime} -- Date and time of the startup of the object
    image {pg.Surface} -- PyGame Surface
    rect {pg.Rect} -- PyGame rectangle
    seconds {int} -- Number of seconds target needs to be up
    """

    def __init__(self, center:tuple, layers: int, size:tuple, colors:list, seconds:int):
        self.start = datetime.now()
        self.seconds = seconds

        x = center[0]
        y = center[1]

        # Layer thickness is the difference between subsequent layers
        # When divided by 2 it gives us the width of the layer stripe!
        layer_thickness = size[0] / layers

        # For every layer, draw it
        sprites = []
        old_size = ()
        curr_size = size
        for layer in range(layers):
            # Getting the color
            color_idx = layer % 2
            color = colors[color_idx]

            if layer == 0:
                # First layer is always the same size as the whole
                # Target
                offset_x = size[0]/2
                offset_y = size[1]/2
                old_size = size
            else:
                # Other layers have its sizes and positions defined by
                # The difference between the previous layer size and
                # Layer thickness!
                curr_x = old_size[0] - layer_thickness
                curr_y = old_size[1] - layer_thickness
                curr_size = (curr_x, curr_y)
                offset_x = curr_size[0]/2
                offset_y = curr_size[1]/2
                old_size = curr_size

            # Draw the layer with the given position, size and color
            sprite = Drawing(curr_size, (x-offset_x, y-offset_y), color=color)
            sprites.append(sprite)

        # Transform everything on a single object
        super().__init__(sprites)

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

        co = self.rect.colliderect(obj.rect)
        return bool(co)

class BigTarget(Target):
    """Bigger, default target!
    
    Arguments:
    center {tuple} -- Position that defines the initial center of the 
                      sprite
    
    Instance Variables:
    center {tuple} -- Same as the argument
    size {tuple} -- Size of the target and also its hit box
    points {int} -- Amount of points earned from hitting it
    """

    def __init__(self, center:tuple):
        self.center = center
        self.size = (60, 60)

        super().__init__(
            self.center, 
            5, 
            self.size,
            ['#AD0B39', 'white'],
            10
        )

        self.points = 1

class MediumTarget(Target):
    """Medium target!
    
    Arguments:
    center {tuple} -- Position that defines the initial center of the 
                      sprite
    
    Instance Variables:
    center {tuple} -- Same as the argument
    size {tuple} -- Size of the target and also its hit box
    points {int} -- Amount of points earned from hitting it
    """

    def __init__(self, center:tuple):
        self.center = center
        self.size = (50, 50)

        super().__init__(
            self.center, 
            5, 
            self.size,
            ['#10396A', 'white'],
            7
        )

        self.points = 5

class SmallTarget(Target):
    """Small target!
    
    Arguments:
    center {tuple} -- Position that defines the initial center of the 
                      sprite
    
    Instance Variables:
    center {tuple} -- Same as the argument
    size {tuple} -- Size of the target and also its hit box
    points {int} -- Amount of points earned from hitting it
    """

    def __init__(self, center:tuple):
        self.center = center
        self.size = (36, 36)

        super().__init__(
            self.center, 
            3, 
            self.size,
            ['#F7B226', 'white'],
            5
        )

        self.points = 20

class SuperSmallTarget(Target):
    """Super small target! The hardest one!
    
    Arguments:
    center {tuple} -- Position that defines the initial center of the 
                      sprite
    
    Instance Variables:
    center {tuple} -- Same as the argument
    size {tuple} -- Size of the target and also its hit box
    points {int} -- Amount of points earned from hitting it
    """

    def __init__(self, center:tuple):
        self.center = center
        self.size = (18, 18)

        super().__init__(
            self.center, 
            3, 
            self.size,
            ['#CE2791', 'white'],
            3
        )

        self.points = 50