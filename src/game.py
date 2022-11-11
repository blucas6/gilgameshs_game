import pygame

from config import *
from colors import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.playing = True


    def main(self):
        while self.playing:
            self.event()
            self.render()
            pygame.display.update()
            self.clock.tick(FPS)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def render(self):
        self.screen.fill(CLOUDBLUE)