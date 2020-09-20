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


#--------------------------------------------------------------------------------------------------------
# draw window
# update the game logic
# handle input
# use the data to draw graphics

# clear the screen
# update the game
# draw the game

# 1) Behavior
# 2) constants
# 3) Data Definitions
# 4) functions

###############
# Software Architecture

#    Behaviors:
#       Game Over:
#            - snake hits the edge of the screen
#            - snake touches itself
#       Snake Movement:
#            - body trails its head
#       Snake:
#            - Eats an apple, grows by open
#       Score:
#           - How much food has been eaten
#       Menu Screen:
#           - Shows one time ath the beginning
#       Game Over:
#           - Displays when snake hits wall or eats itself
#           - will go back to a new game on any keypress
#       key input:
#           - arrow keys and ways to change snake direction
###############