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
        self.angle = math.radians(90) * direction
        self.speed = speed

    def move(self):
        """
        Default movement for most bullet types
        :return: None
        """
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.speed -= self.speedDecay

    def update(self):
        self.do_fader()


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

    #  Should recharge rate or max ammo be constant? Only one needs to be

    def __init__(self, direction):
        self.direction = direction - 1
        self.ammo = self.maxAmmo

    def shoot(self, position, speed):
        """
        When a button is pressed, player gets the gun object attached to that button
        Then the gun object makes the bullets, sets variables, etc
        :param position: The player's location
        :return: Newly made bullet object
        """
        newBullet = None
        if self.ammo >= self.depletionRate+1:
            self.shot = True
            self.ammo -= self.depletionRate
            newBullet = self.bullet(position, self.direction, speed)  # Make a bullet object with direction TODO actually implement bullet lol
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
        self.speed = math.fabs(speed) + random.randrange(0, 20, 1)/10 + 1  # todo if shooting the opposite direction of movement, it still goes faster
        self.angle = direction * math.radians(90) + math.radians(random.randrange(-10, 10, 1))          # todo change
        self.speedDecay = 10
        self.colour = WHITE

        size = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([size*2, size*2])
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.colour, (size, size), size, 0)
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        self.rect = [self.x, self.y]


class SprayGun(Gun):
    def __init__(self, direction):
        super(SprayGun, self).__init__(direction)
        self.depletionRate = 2
        self.rechargeRate = 1
        self.bullet = SprayGunBullet


