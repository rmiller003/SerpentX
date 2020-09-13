
import pygame
import sys
import random

class snake(object):
    def_init_(self):
    self.length = 1
    self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
    self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    self.color = (0, 0, 255)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get.head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        pass


class food(object):
    def_init_(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass

    def drawGrid(surface):
        for y in range(0, int(GRID_HEIGHT)):
            for x in range(0, int(GRID_WIDTH)):
                if (x + y) % 2 ==0:
                    r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                    pygame.draw.rect(surface, (93, 216, 228), r)
                else:
                    rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), GRIDSIZE, GRIDSIZE))
                    pygame.draw.rect(surface, (84, 194, 205), rr)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get.size())
    surface = surface.convert()
    drawGrid(surface)

    snake = snake()
    food = food()

    score = 0
    while (True):
        clock.tick(10)
    # handle events

    screen.blit(surfaced, (0, 0))
    pygame.display.update()

main()

