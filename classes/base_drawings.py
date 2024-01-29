# PyGame Imports
import pygame as pg

class Drawing(pg.sprite.Sprite):
    """Basic rectangle drawing sprite
    
    Arguments:
    shape {tuple} -- Two integers defining the rectangle shape
    pos {tuple} -- Two integers defining the position
    color {str} -- Filling color (default 'black')

    Instance Variables:
    image {pg.Surface} -- PyGame Surface
    rect {pg.Rect} -- PyGame rectangle
    """

    def __init__(self, shape:tuple, pos:tuple, color:str='black'):
        super().__init__()
        self.image = pg.Surface(shape)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

class GroupedDrawings(pg.sprite.Sprite):
    """Group of basic rectangle drawing sprites

    Arguments:
    sprites {list} -- List of sprites to group

    Instance Variables:
    image {pg.Surface} -- PyGame Surface
    rect {pg.Rect} -- PyGame rectangle
    """

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
