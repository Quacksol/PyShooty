import random
import math
from definitions import *
import fadeStuff


class Bullet(fadeStuff.drawObject):
    """
    Abstract class for bullets. Each one disappears at a different rate, has different shape, colour, etc
    Each bullet decides itself where it moves, depeding on its starting conditions
    """
    timeToLive = 0  # Frames until bullet dies
    angle = 0  # Angle being shot at
    speed = 0  # Speed travelling at
    speedDecay = 0  # Rate of decay of speed, unique and constant for bullet type
    colour = None   # Main colour

    def __init__(self, position, direction, speed):
        self.x = position[0]
        self.y = position[1]
        self.angle = 90 * direction
        self.speed = speed

    def move(self):
        """
        Default movement for most bullet types
        :return: None
        """
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.speed -= self.speedDecay


class Gun:
    """
    Generic abstract class for guns. Recharge is same for everything, at least
    No gun object will ever be made, so the following variables are set to 0 lol
    """
    ammo = 0  # Absolute amount of Ammo you have
    maxAmmo = 100  # Max ammo, constant for all TODO (make a macro)
    depletionRate = 0  # Rate at which ammo depletes/is consumed
    rechargeRate = 0  # Rate at which amm recharges
    chargedTimer = 0  # Used to make the ammo bar flash a bit when fully charged, same for all guns
    shot = False  # Did the gun JUST shoot? If so, don't recharge for this frame.

    bullet = None  # Bullet class allocated to this gun. Objects of this class will be mde when shooting
    angle = 0

    #  Should recharge rate or max ammo be constant? Only one needs to be

    def __init__(self, direction):
        self.angle = 90 * direction
        self.ammo = self.maxAmmo

    def shoot(self, position, speed):
        """
        When a button is pressed, player gets the gun object attached to that button
        Then the gun object makes the bullets, sets variables, etc
        Direction will be needed as an input
        :param direction: 0-3, specifies the direction the bullet will go, rotation, etc
        :return: None, but inside the function the bullet is added to a list?
        """
        newBullet = None
        if self.ammo >= self.depletionRate+1:
            self.shot = True
            self.ammo -= self.depletionRate
            #newBullet = self.bullet(position, self.angle, speed)  # Make a bullet object with direction TODO actually implement bullet lol
        return newBullet

    def recharge(self):
        """
        Every frame, each gun recharges its supply.
        :return:
        """
        if not self.shot:  # Not sure about this
            if not self.ammo >= self.maxAmmo:
                self.ammo += self.rechargeRate
                if self.ammo >= self.maxAmmo:
                    self.chargedTimer = 15
            if self.chargedTimer > 0:
                self.chargedTimer -= 1
        else:
            self.shot = False

# --------------------------------------------------------------------------------------------------------------------


class SprayGunBullet(Bullet):
    def __init__(self, position, direction, speed):
        super(SprayGunBullet, self).__init__(position, direction, speed)
        self.timeToLive = 300
        self.speed = speed + random.randint(-5, 5)      # todo change
        self.angle = 90 * direction                     # todo change
        self.speedDecay = 10
        self.colour = WHITE

    def draw(self, position):
        super(SprayGunBullet, self).draw(position)
        pygame.draw.circle(screen, self.colour, [int(self.x), int(self.y)], 30, 0)


class SprayGun(Gun):
    def __init__(self, direction):
        super(SprayGun, self).__init__(direction)
        self.depletionRate = 1
        self.rechargeRate = 2
        self.bullet = SprayGunBullet
        self.direction = direction


