import pygame

from config import *
from colors import *

class Figurine(pygame.sprite.Sprite):
    def __init__(self, game, width, height, img, groups):
        pygame.sprite.Sprite.__init__(self, groups)
        self.game = game
        self.width = width
        self.height = height
        self.image = img
        self._layer = FIGURINE_LAYER
        self.rect = self.image.get_rect()
        self.rect.x = 100

