from enum import Enum

from config import *

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

def BoardToPixel(posx_board, posy_board):
    return BOARD_POS[0] + FIGURINE_SHIFT_X + (posx_board * TILESIZE_W), BOARD_POS[1] + FIGURINE_SHIFT_Y + (posy_board * TILESIZE_H)
