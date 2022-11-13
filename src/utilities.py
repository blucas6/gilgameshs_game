from enum import Enum
import math

from config import *

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

def BoardToPixel(posx_board, posy_board):
    return BOARD_POS[0] + FIGURINE_SHIFT_X + (posx_board * TILESIZE_W), BOARD_POS[1] + FIGURINE_SHIFT_Y + (posy_board * TILESIZE_H)

class Cell:
    def __init__(self):
        self.parent = [-1, -1]
        self.f = -1
        self.g = -1
        self.h = -1
        self.m = -1
        self.mdir = "none"
    
def isValid(point, width, height):
    if point[0] >= 0 and point[0] < width and point[1] >= 0 and point[1] < height:
        return True
    return False

def isUnblocked(point, grid, gridw, gridh):
    # 0 is open cell
    return isValid(point, gridw, gridh) and grid[point[1]][point[0]] == 0

def isDestination(pos, dest):
    return pos == dest

def calculateHValue(src, dest):
    return math.sqrt(((src[0] - dest[0])*(src[0] - dest[0])) + ((src[1] - dest[1])*(src[1] - dest[1])))

def tracePath(cellDetails, dest):
    path = []

    row = dest[1]
    col = dest[0]

    while True:
        path.append([col, row])
        next_node = cellDetails[row][col].parent
        row = next_node[1]
        col = next_node[0]

        if cellDetails[row][col].parent == next_node:
            break

    path.append([col, row])
    path.reverse()
    return path

def aStar(src, dest, gridw, gridh, grid):
    if not isValid(src, gridw, gridh):
        print("ERROR: Astar - invalid src")
        return -1
    
    if not isValid(dest, gridw, gridh):
        print("ERROR: Astar - invalid dest")
        return -1

    if not isUnblocked(src, grid, gridw, gridh) or not isUnblocked(dest, grid, gridw, gridh):
        print("ERROR: Astar - src or dest blocked")
        return -1
    
    if isDestination(src, dest):
        print("NOTE: src at dest")
        return -1

    # closed list boolean 2d array showing that no cell is included
    closed_list = []
    for j in range(gridh):
        row = []
        for i in range(gridw):
            row.append(False)
        closed_list.append(row)

    # 2d array to hold cell info
    cellDetails = []
    for r in range(gridh):
        row = []
        for c in range(gridw):
            row.append(Cell())
        cellDetails.append(row)

    # starting node
    i = src[0]
    j = src[1]
    cellDetails[j][i].f = 0.0
    cellDetails[j][i].g = 0.0
    cellDetails[j][i].h = 0.0
    cellDetails[j][i].m = 0.0
    cellDetails[j][i].parent = [i, j]

    # open list [ f, [i,j] ]    f = g + h 
    # add starting cell
    open_list = []
    open_list.append([0.0, [i, j]])

    while open_list:
        # find min f value
        p = open_list.pop(open_list.index(min(open_list)))
        i = p[1][0]
        j = p[1][1]

        closed_list[j][i] = True

        # gen successors
        for addx in range(-1, 2, 1):
            for addy in range(-1, 2, 1):
                if (addx==0 and addy==-1) or (addx==1 and addy==0) or (addx==0 and addy==1) or (addx==-1 and addy==0):
                    neighbour = [i + addx, j + addy]
                    # check if valid
                    if isValid(neighbour, gridw, gridh):
                        # check if dest
                        if isDestination(neighbour, dest):
                            cellDetails[neighbour[1]][neighbour[0]].parent = [i, j]
                            return tracePath(cellDetails, dest)
                            
                        # check if on closed list or blocked
                        elif not closed_list[neighbour[1]][neighbour[0]] and isUnblocked(neighbour, grid, gridw, gridh):
                            gnew = cellDetails[j][i].g + 1
                            hnew = calculateHValue(neighbour, dest)
                            fnew = gnew + hnew

                            # dir
                            if addx==0 and addy==-1:       #up
                                mdirNew = "top" 
                            elif addx==0 and addy==1:       #down
                                mdirNew = "down"
                            elif addx==1 and addy==0:       #right
                                mdirNew = "right"
                            elif addx==-1 and addy==0:       #left
                                mdirNew = "left"
                            if cellDetails[j][i].mdir == mdirNew:
                                mnew = cellDetails[j][i].m + 1.0
                            else:
                                mnew = 0.0

                            # if not on open list add it and add info 
                            # or check if the cost is better
                            if cellDetails[neighbour[1]][neighbour[0]].f == -1 or cellDetails[neighbour[1]][neighbour[0]].f > fnew:
                                open_list.append([fnew, [neighbour[0],neighbour[1]]])
                                cellDetails[neighbour[1]][neighbour[0]].f = fnew
                                cellDetails[neighbour[1]][neighbour[0]].g = gnew
                                cellDetails[neighbour[1]][neighbour[0]].h = hnew
                                cellDetails[neighbour[1]][neighbour[0]].m = mnew
                                cellDetails[neighbour[1]][neighbour[0]].mdir = mdirNew
                                cellDetails[neighbour[1]][neighbour[0]].parent = [i, j]

    print("ERROR: Astar - failed to find path")