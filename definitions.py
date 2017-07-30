import pygame

# Define some colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

# Set the width and height of the screen [width, height]
resoChange = 8  # Change this to change the resolution of the game screen.
WIDTH = 192 * resoChange
HEIGHT = 108 * resoChange

screen = pygame.display.set_mode((WIDTH, HEIGHT))#, pygame.FULLSCREEN)

fps = 60  # Tasty
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

