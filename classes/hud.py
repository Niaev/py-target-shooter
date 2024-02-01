# General Imports
from datetime import datetime

# PyGame Imports
import pygame as pg

class Hud():
    """Player Hud cointaining time spent and total score

    Arguments:
    width {int} -- Total width. Should be the same as screen width
                   (default 600)
    height {int} -- Total height. Should be the same as screen height
                   (default 600)
    pos {tuple} -- Containing x and y of the position. Should be (0,0).

    Instance Variables:
    start {datetime} -- Date and time of the startup of the object
    width {int}
    height {int}
    x {int}
    y {int}
    font {pg.Font} -- Default font for the hud
    time {pg.Surface} -- Time counter
    score {pg.Surface} -- Points counter
    amount {int} -- Total amount of points
    """

    def __init__(self, width:int=600, height:int=48, pos:tuple=(0,0)):
        # Time object with the moment the hud was built
        self.start = datetime.now()

        self.width = width
        self.height = height
        
        self.x = pos[0]
        self.y = pos[1]

        # Set font family and size
        self.font = pg.font.SysFont('Console', 48)
        # Set initial time count
        self.time = self.font.render('00:00', True, (0,0,0))
        # Set initial score count
        self.score = self.font.render('0', True, (0,0,0))

        # Set initial amount of points
        self.amount = 0

    def draw_time(self, screen: 'pg.Surface'):
        """Draw self.time Sprite on top left of the screen

        Arguments:
        screen {pg.Surface} -- Game display
        """

        time_pos = self.time.get_rect(x=self.x-2, y=self.y-15)
        screen.blit(self.time, time_pos)

    def draw_score(self, screen: 'pg.Surface'):
        """Draw self.score Sprite on top right of the screen

        Arguments:
        screen {pg.Surface} -- Game display
        """

        score_rect = self.score.get_rect(x=-50, y=-50)
        score_size = score_rect.size
        score_width = score_size[0]+1
        score_pos = self.score.get_rect(x=self.width-score_width, y=self.y-15)
        screen.blit(self.score, score_pos)

    def draw(self, screen: 'pg.Surface'):
        """Draw all hud content

        Arguments:
        screen {pg.Surface} -- Game display
        """
        
        self.draw_time(screen)
        self.draw_score(screen)

    def update_time(self, screen: 'pg.Surface'):
        """Update time counter on the screen

        Arguments:
        screen {pg.Surface} -- Game display
        """

        # Current time
        now = datetime.now()
        # Difference between start and current time
        diff = now - self.start

        # Calculate minutes and seconds of the difference
        _secs = diff.seconds
        nmins = _secs // 60
        try:
            nsecs = _secs % (nmins * 60)
        except ZeroDivisionError:
            nsecs = _secs % 60
        # Getting string values for minutes and seconds with two digits
        mins = '%02d' % nmins
        secs = '%02d' % nsecs

        # Rewrite time counter
        self.time = self.font.render(f'{mins}:{secs}', True, (0,0,0))
        # Update the screen
        self.draw_time(screen)

    def update_score(self, screen: 'pg.Surface', points:int=1):
        """Update points counter on the screen

        Arguments:
        screen {pg.Surface} -- Game display
        points {int} -- Points to increase to the amount (default 1)
        """

        # Increase amount
        self.amount += points
        # Rewrite score countes
        self.score = self.font.render(str(self.amount), True, (0,0,0))
        # Update the screen
        self.draw_score(screen)