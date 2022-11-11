import pygame

from config import *

class Figurine(pygame.sprite.Sprite):
    def __init__(self, game, width, height, img, groups):
        pygame.sprite.Sprite.__init__(self, groups)
        self.game = game
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(self.img, (0,0), (0, 0, self.width, self.height))
        self.image = img
        self._layer = FIGURINE_LAYER

        self.pos_in_window = (0,0)
        self.rect = self.image.get_rect()

