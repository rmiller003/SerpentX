# This is my 4th attempt at the classic Python Snake Game...

import pygame, sys

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))
#BASICFONT = pygame.font.Font('freesansbold.ttf')
CLOCK = pygame.time.Clock()
pygame.display.set_caption('SerpentX')

while True: #main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((255,255,255))
    pygame.display.update()
    CLOCK.tick(60)



