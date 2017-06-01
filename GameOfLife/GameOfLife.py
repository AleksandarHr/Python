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

def drawGrid():
    for x in range(0, WINDOW_WIDTH, CELL_GRID_SIZE):
        pygame.draw.line(DISPLAYSURF, GREY, (x, 0), (x, WINDOW_HEIGHT))

    for y in range (0, WINDOW_HEIGHT, CELL_GRID_SIZE):
        pygame.draw.line(DISPLAYSURF, GREY, (0, y), (WINDOW_WIDTH, y))

def blankGrid():
    cellsDict = {}
    for x in range (X_DIM):
        for y in range (Y_DIM):
            cellsDict[x,y] = 0; #the cell is dead
    return cellsDict

def randomStartingGrid(lifeDict):
    for cell in lifeDict:
        lifeDict[cell] = random.randint(0,1)
    return lifeDict

def colourCell(item, lifeDict):
    x_coord = item[0]
    y_coord = item[1]
    cell_x = x_coord * CELL_GRID_SIZE
    cell_y = y_coord * CELL_GRID_SIZE
    #draw dead cells
    if lifeDict[item] == 0:
        pygame.draw.rect(DISPLAYSURF, WHITE, (cell_x, cell_y, CELL_GRID_SIZE, CELL_GRID_SIZE))
    #draw alive cells
    else:
        pygame.draw.rect(DISPLAYSURF, RED, (cell_x, cell_y, CELL_GRID_SIZE, CELL_GRID_SIZE))

    return None

def main():
    pygame.init()
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Hello World Display')
    DISPLAYSURF.fill(WHITE)

    lifeDict = blankGrid()
    lifeDict = randomStartingGrid(lifeDict)
    for cell in lifeDict:
        colourCell(cell, lifeDict)

    drawGrid()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            drawGrid()
            pygame.display.update()

if __name__ == '__main__':
    main()

