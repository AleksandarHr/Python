import pygame, sys, random
from pygame.locals import *

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 900
CELL_GRID_SIZE = 15

X_DIM = WINDOW_WIDTH / CELL_GRID_SIZE
Y_DIM = WINDOW_HEIGHT / CELL_GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (60, 60, 60)
RED = (255, 0, 0)

FPS = 10

#draws initial grid
def drawGrid():
    for x in range(0, WINDOW_WIDTH, CELL_GRID_SIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, GREY, (x,0),(x,WINDOW_HEIGHT))
    for y in range (0, WINDOW_HEIGHT, CELL_GRID_SIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, GREY, (0,y), (WINDOW_WIDTH, y))

    # colors cells which contain a 1 instead of a 0 (the alive cells)
def colourCell(item, lifeDict):
    x_coord = item[0]
    y_coord = item[1]
    cell_x = x_coord * CELL_GRID_SIZE
    cell_y = y_coord * CELL_GRID_SIZE
    # draw dead cells
    if lifeDict[item] == 0:
        pygame.draw.rect(DISPLAYSURF, WHITE, (cell_x, cell_y, CELL_GRID_SIZE, CELL_GRID_SIZE))
    # draw alive cells
    else:
        pygame.draw.rect(DISPLAYSURF, RED, (cell_x, cell_y, CELL_GRID_SIZE, CELL_GRID_SIZE))
    return None

#saves grid numbers of a blank grid into a dictionary
def blankGrid():
    cellsDict = {}
    for x in range (X_DIM):
        for y in range (Y_DIM):
            cellsDict[x,y] = 0; #the cell is dead
    return cellsDict

# sets random cells to 1
def randomStartingGrid(lifeDict):
    for cell in lifeDict:
        lifeDict[cell] = random.randint(0,1)
    return lifeDict



# count neighbours of a cell
def countNeighbours(cell, lifeDict):
    neighbours = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            currCell = (cell[0] + x, cell[1] + y)
            if currCell[0] < X_DIM and currCell[0] >= 0:
                if currCell[1] < Y_DIM and currCell[1] >= 0:
                    if lifeDict[currCell] == 1:
                        if x == 0 and y == 0:
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

#1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#2. Any live cell with two or three live neighbours lives on to the next generation.
#3. Any live cell with more than three live neighbours dies, as if by overcrowding.
#4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def nextGen(lifeDict):
    nextGeneration = {}
    for cell in lifeDict:
        neighbours = countNeighbours(cell, lifeDict)
        if lifeDict[cell] == 1:
            if neighbours < 2:
                nextGeneration[cell] = 0
            elif neighbours > 3:
                nextGeneration[cell] = 0
            else:
                nextGeneration[cell] = 1
        elif lifeDict[cell] == 0:
            if neighbours == 3:
                nextGeneration[cell] = 1
            else:
                nextGeneration[cell] = 0
    return nextGeneration

def startWithRpentomino(lifeDict):
    #R-pentomino
    lifeDict[48,32] = 1
    lifeDict[49,32] = 1
    lifeDict[47,33] = 1
    lifeDict[48,33] = 1
    lifeDict[48,34] = 1
    return lifeDict


def main():
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Game of Life Display')
    DISPLAYSURF.fill(WHITE)

    lifeDict = blankGrid()
    lifeDict = startWithRpentomino(lifeDict)

    for cell in lifeDict:
        colourCell(cell, lifeDict)

    drawGrid()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        lifeDict = nextGen(lifeDict)

        for cell in lifeDict:
            colourCell(cell, lifeDict)

        drawGrid()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
