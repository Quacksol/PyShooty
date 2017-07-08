import pygame

# Define some colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

# Set the width and height of the screen [width, height]
resoChange = 4  # Change this to change the size of the game screen.
WIDTH = 192 * resoChange
HEIGHT = 108 * resoChange
size = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(size)

