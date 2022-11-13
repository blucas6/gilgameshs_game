import pygame

from config import *
from colors import *
from figurines.common_figures import *
from board import Board

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.playing = True

        self.frames = 0

    def load(self):
        self.all_sprites_group = pygame.sprite.LayeredUpdates()   # all sprites in the game
        self.piece = Soldier(self, 2, 2, Team.PLAYER_1)
        self.piece2 = Soldier(self, 1, 0, Team.PLAYER_2)
        self.Board = Board(self, 5, BOARD_POS[0], BOARD_POS[1])

    def main(self):
        self.load()
        while self.playing:
            self.event()
            self.update()
            self.render()
            pygame.display.update()
            self.clock.tick(FPS)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
    
    def update(self):
        self.frames += 1
        if self.frames > BOARD_TURN_SPEED:
            self.frames = 0
            self.Board.Board_Turn += 1
        self.Board.update()
        self.all_sprites_group.update(self.Board.Board_Turn)

    def render(self):
        self.screen.fill(CLOUDBLUE)
        self.all_sprites_group.draw(self.screen)