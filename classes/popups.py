# PyGame imports
import pygame as pg

class PopUp():
    """Pop text up on screen and fade out quickly

    Arguments:
    pos {tuple} -- Position that defines x and y of the text
    text {str} -- Text to show up

    Instance Variables:
    pos {tuple} -- Position that defines x and y of the text
    text {str} -- Text to show up
    alpha {int} -- 0 to 255, defines transparency
    font {pg.Font} -- Console font from pixeldroid, 32px
    label {pg.Surface} -- Text surface
    """

    def __init__(self, pos:tuple, text:str):
        # Base instance variables
        self.pos = pos
        self.text = text

        # Transparency
        self.alpha = 255

        # Set font family and size
        self.font = pg.font.Font('data/fonts/console/pixeldroidConsoleRegular.ttf', 32)
        self.label = self.font.render(self.text, True, (0,0,0))

    def draw(self, screen:'pg.Surface'):
        """Determine if the popup need to be drawn and handles alpha channel
        
        Arguments:
        screen {pg.Surface} -- Game display

        Returns:
        {bool} -- If the text will be drawn or not
        """

        # If font is already completely transparent
        if self.alpha < 0:
            # Do not draw
            return False

        # Determine new position (always going up)
        x = self.pos[0]
        y = self.pos[1] - 1

        # Write text again with updated alpha channel
        self.label = self.font.render(self.text, True, (0,0,0))
        self.label.set_alpha(self.alpha)

        # Draw text again
        label_pos = self.label.get_rect(x=x, y=y)
        screen.blit(self.label, label_pos)

        # Update position and alpha channel
        self.pos = (x,y)
        self.alpha -= 17

        # Say that the object was drawn
        return True