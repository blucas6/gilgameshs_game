import pygame
from config import *

class Board:
    def __init__(self, game, num, stx, sty):
        self.game = game
        self.boardNum = num
        self.startx = stx
        self.starty = sty
        self.Board_Turn = 0
        self.Playing = False
        self.drawBoard()

    def drawBoard(self):
        for x in range(self.boardNum):
            for y in range(self.boardNum):
                Tile(self.game, self.startx + x * TILESIZE_W, self.starty + y * TILESIZE_H)

    def NewBoardGame(self):
        self.Board_Turn = 0
        self.Playing = True

    def update(self):
        if self.Playing:
            self.Board_Turn += 1

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

