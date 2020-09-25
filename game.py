from config import Config
from snake import Snake
from apple import Apple
import pygame, sys


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('SerpentX')
        self.apple = Apple()
        self.snake = Snake()

    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def gameLoop(self):
        while True:  # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)

            self.snake.update(self.apple)
            self.draw()
            if self.isGameOver():
                break
