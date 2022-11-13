import pygame
import pygame.math

from config import *
from figurines.figurine import Figurine, State
from utilities import *
from colors import *

class Soldier(Figurine):
    def __init__(self, game, stx_board, sty_board):
        self.g = game
        self.img_file = "../sprites/soldier.png"
        self.img = pygame.image.load(self.img_file).convert_alpha()
        self.w = TILESIZE_W
        self.h = TILESIZE_H
        self._layer = FIGURINE_LAYER
        groups = self.g.all_sprites_group
        stx = stx_board
        sty = sty_board

        Figurine.__init__(self, self.g, self.w, self.h, self.img, groups, stx, sty)

    def Moving(self):
        self.move()

    def Idle(self):
        pass