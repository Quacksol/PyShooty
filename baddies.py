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
    dead = None  # TODO if an enemy is dead, it shouldn't know it's dead- it's dead
    colour = WHITE

    radius = 0 * resoChange

    # example position -> [0, 1]
    def __init__(self, position, radius):
        self.x = position[0]
        self.y = position[1]
        self.radius = radius * resoChange

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.rect = self.image.get_rect()

    def move(self, dest):
        self.destX = dest[0]
        self.destY = dest[1]

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

        self.rect.x = self.x
        self.rect.y = self.y

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
    def __init__(self, position):
        self.radius = 4  # increase size of enemy
        super(Fodder, self).__init__(position, self.radius)

        x = self.x
        y = self.y
        h = self.radius
        self.rect = pygame.Rect(x - h / 2, y - h / 2, h, h)
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        # Draw triangle from three pointsS
        pygame.draw.polygon(self.image, self.colour, [[x, y + h / 2], [x - h / 2, y - h / 2], [x + h / 2, y - h / 2]], 1)
        self.image.set_colorkey(BLACK)

        self.health = 10
        self.maxHealth = self.health
        self.speed = 1.5
        self.dead = False

    def update(self):
        x = self.x
        y = self.y
        h = self.radius
        self.rect.center = (x, y)
        # next - draw collision rectangle from bottom left corner of triangle - #
        if 1:   # fixme This code is bad unfortunately, the drawing should br done by the group.draw() function. But that doesn't work >:(
            self.rect = pygame.Rect(x - h / 2, y - h / 2, h, h)
            self.image = pygame.Surface([self.radius * 2, self.radius * 2])
            # Draw triangle from three pointsS
            pygame.draw.polygon(screen, self.colour, [[x, y + h / 2], [x - h / 2, y - h / 2], [x + h / 2, y - h / 2]], 1)
            self.image.set_colorkey(BLACK)
        # next - draw lifebar
        self.lifebar()

    def act(self, position):
        self.do_fader()

        # all enemies will have one - perform next actions
        if not self.dead:
            self.move(position)
            # Enemies that can fire guns would have a 'def shoot' method, called in 'def act'


            # Further enemies that fire bullets might require a rework of the 'guns' script.
            # Curently (09/07/2017) it assumes that bullets are always friendly.
