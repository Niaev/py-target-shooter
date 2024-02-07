# PyGame imports
import pygame as pg

# Project imports
from classes.crosshair import CrossHair
from classes.targets import Target

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

class CHPopUp(PopUp):
    """PopUp that shows with cross hair actions
    
    Arguments:
    ch {CrossHair} -- User cursor crosshair
    target {Target|None} -- Target that got shot or None when nothing 
                            was shot
    """

    def __init__(self, ch:CrossHair, target:Target|None, max_width:int=600):
        # Getting x position to be a little bit to the side of the 
        # CrossHair
        ch_x = ch.rect.x + ch.rect.size[0] * 1.75
        # Determine which side it will be
        if ch_x > max_width:
            # Left if crosshair is near screen end
            x = ch.rect.x - (ch.rect.size[0])
        else:
            # Right if crosshair is anywhere else
            x = ch.rect.x + (ch.rect.size[0])
        # Place somewhere (this works for the console font only)
        y = ch.rect.y + 10

        # Determine text to be displayed based on target
        if target:
            text = f'+{target.points}'
        else:
            text = 'miss!'

        # Make it a real PopUp now
        super().__init__((x,y), text)

class TPopUp(PopUp):
    """PopUp that shows when targets hide

    Arguments:
    target {Target} -- Target that will be hidden
    """

    def __init__(self, target:Target):
        # Bank of texts
        texts = [
            'L!',
            'oof!',
            'loss',
            'lost',
            'loser',
            'ow',
            'ouch' 
        ]
        # Random text index
        rng = randint(0, len(texts)-1)

        # Position of the text based on the target
        x = target.center[0]
        y = target.center[1]

        # Make it a real PopUp now
        super().__init__((x,y), texts[rng])