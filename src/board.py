import pygame
from config import *

class Board:
    def __init__(self, game, num):
        self.game = game
        self.boardNum = num
        self.drawBoard()

    def drawBoard(self):
        for x in range(self.boardNum):
            for y in range(self.boardNum):
                Tile(self.game, x * TILESIZE_W, y * TILESIZE_H)


class Tile (pygame.sprite.Sprite):
    def __init__(self, g, x, y):
        pygame.sprite.Sprite.__init__(self, g.all_sprites_group)
        self.img_file = "../sprites/board_tileset.png"
        self.image = pygame.image.load(self.img_file).convert_alpha()
        self.game = g
        self.width = TILESIZE_W
        self.height = TILESIZE_H
        self._layer = BOARD_TILE_LAYER
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

