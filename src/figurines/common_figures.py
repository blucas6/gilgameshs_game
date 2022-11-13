import pygame
import pygame.math

from config import *
from figurines.figurine import Figurine, State, Team
from utilities import *
from colors import *

class Soldier(Figurine):
    def __init__(self, game, stx_board, sty_board, team_side):
        self.g = game
        self.img_file = "../sprites/soldier.png"
        self.img = pygame.image.load(self.img_file).convert_alpha()
        self.w = TILESIZE_W
        self.h = TILESIZE_H
        self._layer = FIGURINE_LAYER
        groups = self.g.all_sprites_group
        stx = stx_board
        sty = sty_board
        side = team_side

        Figurine.__init__(self, self.g, self.w, self.h, self.img, groups, stx, sty, side)

    def Moving(self):
        self.move()

    def Idle(self):
        print(self.Energy)
        if self.Energy > FIGURINE_MOVE_ENERGY:
            self.Energy = 0
            self.state = self.ChangeState(State.MOVING)