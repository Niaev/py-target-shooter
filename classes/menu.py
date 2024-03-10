# PyGame imports
import pygame as pg

# Project imports
from classes.base_drawings import GroupedDrawings, Drawing

class Button(GroupedDrawings):
    def __init__(self, label:str, center:tuple, size:tuple, mode:str='normal'):
        self.label = label
        
        self.x, self.y = center
        self.width, self.height = size

        self.sprites = []
        self.font = pg.font.Font('data/fonts/console/pixeldroidConsoleRegular.ttf', 48)

        self.offset_x = self.width / 2
        self.offset_y = self.height / 2

        if mode == 'normal':
            border_text_color = 'black' # #000000
            bg_color = 'grey' # #bebebe
        elif mode == 'hover':
            border_text_color = 'black' #'#444444'
            bg_color = '#999999'

        self.background = Drawing(
            (self.width, self.height), 
            (self.x-self.offset_x, self.y-self.offset_y), 
            color=bg_color
        )

        self.bd_top = Drawing(
            (self.width, 6), 
            (self.x-self.offset_x, self.y-self.offset_y-6),
            color=border_text_color
        )

        self.bd_right = Drawing(
            (6, self.height), 
            (self.x+self.offset_x, self.y-self.offset_y),
            color=border_text_color
        )

        self.bd_bottom = Drawing(
            (self.width, 6), 
            (self.x-self.offset_x, self.y+self.offset_y),
            color=border_text_color
        )

        self.bd_left = Drawing(
            (6, self.height), 
            (self.x-self.offset_x-6, self.y-self.offset_y),
            color=border_text_color
        )

        self.sprites = [
            self.background,
            self.bd_top,
            self.bd_right,
            self.bd_bottom,
            self.bd_left
        ]

        super().__init__(self.sprites)

        self.text = self.font.render(self.label, True, border_text_color)
    
        text_pos = self.text.get_rect(centerx=self.width/2, centery=self.height/2)
        self.image.blit(self.text, text_pos)

        self.mode = mode

class Menu(GroupedDrawings):
    def __init__(self, buttons:dict, sprites:list):
        self.buttons = buttons
        self.sprites = sprites

        super().__init__(self.sprites)

    def hover_buttons(self):
        for k in self.buttons:
            button = self.buttons[k]
            hover = button.rect.collidepoint(pg.mouse.get_pos())

            if hover and button.mode == 'normal':
                self.buttons[k] = Button(
                    button.label,
                    (button.x, button.y),
                    (button.width, button.height),
                    mode='hover'
                )
            if not hover and button.mode == 'hover':
                self.buttons[k] = Button(
                    button.label,
                    (button.x, button.y),
                    (button.width, button.height),
                    mode='normal'
                )