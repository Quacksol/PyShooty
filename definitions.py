import pygame

fs = True
fs = False

# Define some colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

# Set the width and height of the screen [width, height]
if fs:
    resoChange = 10  # Change this to change the resolution of the game screen.
else:
    resoChange = 4
WIDTH = 192 * resoChange
HEIGHT = 108 * resoChange
if fs:
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

fps = 60  # Tasty
clock = pygame.time.Clock()
dt = 0  # Used to count a second, leave it


def change_resolution(direction):
    """
    Change the resolution. Only do this in the menu, too much effort to change the sizes of everything in-game.
    :param direction: Increase or decrease reso.
    :return: None
    """
    global resoChange, HEIGHT, WIDTH, screen
    if direction == 0:
        # Reduce resolution
        resoChange -= 1
    if direction == 1:
        # Increase resolution
        resoChange += 1
    if direction == 2:
        # Change fullscreen
        pass

    WIDTH = 192 * resoChange
    HEIGHT = 108 * resoChange
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

