import random
import time
import math
from definitions import *
import fadeStuff


class Enemy(fadeStuff.drawObject):
    """
    Abstract class for enemies. Each enemy has a position and health.
    """

    destX = 0.0
    destY = 0.0

    health = 0
    maxHealth = 0

    # for lifebar 'counter'
    elaTime = 0

    speed = 0
    dead = None
    colour = WHITE

    radius = 0 * resoChange

    # example position -> [0, 1]
    def __init__(self, position, radius):
        super(Enemy, self).__init__()
        self.x = position[0]
        self.y = position[1]
        self.radius = radius * resoChange

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()

    def move(self, position):
        self.destX = position[0]
        self.destY = position[1]

        # move in straight line towards target

        # direction (rough maths incoming)
        xMove = self.destX - self.x
        yMove = self.destY - self.y

        # self.x += speed/xMove
        # self.y += speed/yMove

        # exhibits weird behaviour
        # self.x += xMove/(xMove+yMove) * self.speed
        # self.y += yMove/(xMove+yMove) * self.speed

        # y = mx + c
        # y2 - y1 / x2 - x1 = gradient

        hyp = math.sqrt((xMove ** 2) + (yMove ** 2))
        self.x += xMove / (hyp) * self.speed
        self.y += yMove / (hyp) * self.speed

    def lifebar(self):
        # take_damage will reset lifebar elapse time

        curTime = int(round(time.time() * 1000))  # time in milliseconds

        # I should use an asyncronous timer as a countdown for the lifebar
        # But using time should work for now

        if curTime <= self.elaTime:
            healthLeft = self.health / self.maxHealth

            barColour = WHITE

            if healthLeft <= 0.2:
                barColour = RED

            # below is a complete mess
            # pygame.draw.line(screen, WHITE, [self.x - self.radius, self.y - self.radius], [self.x + self.radius, self.y - self.radius], barWidth)
            pygame.draw.line(screen, barColour, [self.x - self.radius, self.y - self.radius],
                             [(self.x + self.radius) - (self.radius * 2 * (1 - healthLeft)), self.y - self.radius], 2)

    def take_damage(self, damage):
        self.health -= damage

        # for lifebar - reset elapse time
        curTime = int(round(time.time() * 1000))
        self.elaTime = curTime + 2000  # elapse time is set for 2 seconds (2000 milliseconds) from now

        self.check_death()

    def check_death(self):
        if self.health <= 0:
            self.death()

    def death(self):
        # explosion effect
        self.colour = RED  # - temp for explosion
        self.dead = True

    # delete instance


class Fodder(Enemy):
    radius = 4  # increase size of enemy

    def __init__(self, position):
        super(Fodder, self).__init__(position, self.radius)
        self.health = 10
        self.maxHealth = self.health
        self.speed = 1.5
        self.dead = False

    def update(self):
        x = self.x
        y = self.y
        h = self.radius

        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.image.fill(BLACK)
        # next - draw triangle from three points
        pygame.draw.polygon(screen, self.colour, [[x, y + h / 2], [x - h / 2, y - h / 2], [x + h / 2, y - h / 2]], 1)
        self.image.set_colorkey(BLACK)
        self.rect.center = (x, y)
        # next - draw collision rectange from bottom left corner of triangle
        self.rect = pygame.Rect(x - h / 2, y - h / 2, h, h)
        # next - draw lifebar
        self.lifebar()

    def act(self, position):
        self.do_fader()

        # all enemies will have one - perform next actions
        if self.dead == False:
            self.move(position)
            # Enemies that can fire guns would have a 'def shoot' method, called in 'def act'


            # Further enemies that fire bullets might require a rework of the 'guns' script.
            # Curently (09/07/2017) it assumes that bullets are always friendly.
