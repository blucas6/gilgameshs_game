import pygame

from config import *
from figurines.figurine import Figurine

class Soldier(Figurine):
    def __init__(self, game):
        self.g = game
        self.img_file = "../sprites/soldier.png"
        self.img = pygame.image.load(self.img_file).convert_alpha()
        self.w = TILESIZE_W
        self.h = TILESIZE_W

        Figurine.__init__(self, self.g, self.w, self.h, self.img, self.g.all_sprites_group)

    def update(self):
        pass