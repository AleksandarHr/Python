import pygame, sys
from pygame.locals import *

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 900
CELL_GRID_SIZE = 15

X_DIM = WINDOW_WIDTH / CELL_GRID_SIZE
Y_DIM = WINDOW_HEIGHT / CELL_GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (60, 60, 60)

def drawGrid():
    for x in range(0, WINDOW_WIDTH, CELL_GRID_SIZE):
        pygame.draw.line(DISPLAYSURF, GREY, (x, 0), (x, WINDOW_HEIGHT))

    for y in range (0, WINDOW_HEIGHT, CELL_GRID_SIZE):
        pygame.draw.line(DISPLAYSURF, GREY, (0, y), (WINDOW_WIDTH, y))

def main():
    pygame.init()
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Hello World Display')
    DISPLAYSURF.fill(WHITE)
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

