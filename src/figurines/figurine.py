import pygame
from enum import Enum
from copy import deepcopy

from config import *
from colors import *
from utilities import *
from colors import *

class State(Enum):
    IDLE = 1
    MOVING = 2
    ATTACK = 3
    ULTI = 4
    DEATH = 5

class Team(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2

class Figurine(pygame.sprite.Sprite):
    def __init__(self, game, width, height, img, groups, stx_board, sty_board, team):
        pygame.sprite.Sprite.__init__(self, groups)
        self.team = team
        self.game = game
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(img, (0,0), (0,0,self.width, self.height))
        self.image.set_colorkey(VOID)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = BoardToPixel(stx_board, sty_board)

        self.current_pos_board = [stx_board,sty_board]
        self.board_src = [stx_board,sty_board]
        self.board_dest = [stx_board,sty_board]

        self.state = State.IDLE

        self.Energy = 0

    def update(self, board_turn):
        self.Energy += board_turn
        if self.state == State.IDLE:
            self.Idle()
        elif self.state == State.MOVING:
            self.Moving()

    def ChangeState(self, state):
        if state != self.state:
            if state == State.MOVING:
                self.board_dest[0], self.board_dest[1] = self.NextDestination()
                self.board_src = deepcopy(self.current_pos_board)
            return state

    def move(self):
        if self.board_dest == self.current_pos_board:
            self.state = self.ChangeState(State.IDLE)
        else:
            cx = self.board_dest[0] - self.board_src[0]
            cy = self.board_dest[1] - self.board_src[1]
            if cx > 0:
                self.rect.x += FIGURINE_MOVE_SPEED
                self.current_pos_board[0] += FIGURINE_MOVE_SPEED / TILESIZE_W
            if cx < 0:
                self.rect.x -= FIGURINE_MOVE_SPEED
                self.current_pos_board[0] -= FIGURINE_MOVE_SPEED / TILESIZE_W
            if cy > 0:
                self.rect.y += FIGURINE_MOVE_SPEED
                self.current_pos_board[1] += FIGURINE_MOVE_SPEED / TILESIZE_H
            if cy < 0:
                self.rect.y -= FIGURINE_MOVE_SPEED
                self.current_pos_board[1] -= FIGURINE_MOVE_SPEED / TILESIZE_H

    def Idle(self):
        pass

    def Moving(self):
        pass

    def NextDestination(self):
        path = aStar([int(self.current_pos_board[0]),int(self.current_pos_board[1])], [4,4], 5, 5, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        if path == -1:
            print("Error: A* failure")
        # else:
        #     print(path[1])  # A* returns a list - first coordinate is the current pos, second is the next dest
        return path[1]



