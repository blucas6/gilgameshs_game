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

    def load(self):
        self.all_sprites_group = pygame.sprite.LayeredUpdates()   # all sprites in the game
        self.piece = Soldier(self)
        self.board = Board(self, 3)

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
        self.all_sprites_group.update()

    def render(self):
        self.screen.fill(CLOUDBLUE)
        self.all_sprites_group.draw(self.screen)