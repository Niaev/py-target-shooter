# PyGame Imports
import pygame as pg

# Project Imports
from classes.base_drawings import Drawing, GroupedDrawings

class Logo(GroupedDrawings):
    def __init__(self, targets:int=2):
        color = 'black'
        target1_color = '#AD0B39'
        target2_color = '#10396A'

        # CrossHair T letter
        ch_T = [
            # Top line
            Drawing((6,18), (24,0), color=color),
            # Left Line
            Drawing((18,6), (0,24), color=color),
            # Right Line
            Drawing((18,6), (36,24), color=color),
            # Bottom Line
            Drawing((6,42), (24,36), color=color),
        ]

        # "Target" A letter
        tg_A = [
            Drawing((24,6), (42,48), color=color),
            Drawing((6,18), (60,54), color=color),
            Drawing((18,6), (42,60), color=color),
            Drawing((6,6), (42,66), color=color),
            Drawing((18,6), (42,72), color=color),
            Drawing((6,6), (66,72), color=color),
        ]

        # "Target" R letter
        tg_R = [
            Drawing((6,30), (78,48), color=color),
            Drawing((6,6), (84,54), color=color),
            Drawing((12,6), (90,48), color=color),
        ]

        # "Target" G letter
        tg_G = [
            # Top circle
            Drawing((30,6), (108,48), color=color),
            Drawing((6,18), (108,54), color=color),
            Drawing((6,12), (132,54), color=color),
            Drawing((18,6), (114,66), color=color),
            # Bottom circle
            Drawing((6,24), (132,72), color=color),
            Drawing((30,6), (102,84), color=color),
            Drawing((6,18), (102,90), color=color),
            Drawing((18,6), (108,102), color=color),
            Drawing((6,6), (126,96), color=color),
        ]

        # "Target" E letter
        tg_E = [
            Drawing((30,6), (144,48), color=color),
            Drawing((6,24), (144,54), color=color),
            Drawing((6,12), (168,54), color=color),
            Drawing((18,6), (150,60), color=color),
            Drawing((24,6), (150,72), color=color),
        ]

        # "Target" T letter
        tg_T = [
            Drawing((30,6), (174,36), color=color),
            Drawing((6,42), (186,30), color=color),
            Drawing((12,6), (192,72), color=color),
        ]

        # Middle Line
        ml = [
            Drawing((48,6), (0,102), color=color),
            Drawing((162,6), (138,102), color=color)
        ]

        # "Shooter" S letter
        sh_S = [
            Drawing((36,6), (60,102), color=color),
            Drawing((6,18), (54,108), color=color),
            Drawing((36,6), (60,126), color=color),
            Drawing((6,24), (96,132), color=color),
            Drawing((42,6), (54,156), color=color),
        ]

        # "Shooter" H letter
        sh_H = [
            Drawing((6,48), (108,114), color=color),
            Drawing((18,6), (114,132), color=color),
            Drawing((6,24), (126,138), color=color),
        ]

        if targets == 2:
            # Red Target
            red_tg = [
                Drawing((30,30), (138,132), color=target1_color),
                Drawing((18,18), (144,138), color='white'),
                Drawing((6,6), (150,144), color=target1_color),
            ]
        else:
            red_tg = []

        if targets > 0:
            # Blue Target
            blu_tg = [
                Drawing((30,30), (174,132), color=target2_color),
                Drawing((18,18), (180,138), color='white'),
                Drawing((6,6), (186,144), color=target2_color),
            ]
        else:
            blu_tg = []

        # "Shooter" T letter
        sh_T = [
            Drawing((30,6), (204,120), color=color),
            Drawing((6,42), (216,114), color=color),
            Drawing((12,6), (222,156), color=color),
        ]

        # "Shooter" E letter
        sh_E = [
            Drawing((30,6), (240,132), color=color),
            Drawing((6,24), (240,138), color=color),
            Drawing((6,12), (264,138), color=color),
            Drawing((18,6), (246,144), color=color),
            Drawing((24,6), (246,156), color=color),
        ]

        # "Shooter" R letter
        sh_R = [
            Drawing((6,30), (276,132), color=color),
            Drawing((6,6), (282,138), color=color),
            Drawing((12,6), (288,132), color=color),
        ]

        sprites = [
            *ch_T, 
            *tg_A, 
            *tg_R,
            *tg_G,
            *tg_E,
            *tg_T,
            *ml,
            *sh_S,
            *sh_H,
            *red_tg,
            *blu_tg,
            *sh_T,
            *sh_E,
            *sh_R
        ]
        super().__init__(sprites)

    def move(self, pos:tuple):
        self.rect.topleft = pos

    def center(self, size:tuple):
        self.rect.center = (size[0]/2, size[1]/2)