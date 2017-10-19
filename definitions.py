"""
Some things are constant. They belong here.
Colours are constant.
Screen size is NOT constant.
All other modules that rely on this module require pygame.
"""

import pygame
from mainScript import *

# Define some colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

fs = True
fs = False

objectSize = 4

WIDTH = 320  # Actual Width of the screen - only used by screen surface and for screen scaling.
HEIGHT = 240
resoScale = 4.5  # The scale up from the base resolution. Multiply every size/speed by this!!!
BASEWIDTH = WIDTH * resoScale  # Width determined by resolution - use this to draw objects to main surface.
BASEHEIGHT = HEIGHT * resoScale

# Set the width and height of the screen [width, height]
if fs:
    objectSize = 10  # Change this to change the resolution of the game screen.
else:
    objectSize = 4
if fs:
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

main_surf = pygame.Surface([BASEWIDTH, BASEHEIGHT])

fps = 60  # Tasty
clock = pygame.time.Clock()
dt = 0  # Used to count a second, leave it
