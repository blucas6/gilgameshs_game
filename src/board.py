import pygame
#img = "../sprites/board_tileset.png"
#board class
class Board:
    def __init__(self, game, num, tile):
        self.game = game
        self.boardNum = num
        self.boardTile = tile


class Tile (pygame.sprite.Sprite):
    def __init__(self, pos, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.position = [pos[0],pos[1]]
        #draw the sprite at position

