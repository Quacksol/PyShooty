"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import math

import random

import fadeStuff
import guns
import baddies
from definitions import *

pygame.init()

GUI = pygame.Surface(size)
GUI.set_colorkey(BLACK)
screen.fill(BLACK)  # Make screen black to start off

pygame.display.set_caption("Real Life Video Game")


def setup_nodes():
    """
    Returns the positions of the nodes the player moves between
    :return: nodes
    """
    nodes = []
    for j in range(yNodes):
        for i in range(xNodes):
            nodes.append([i * (WIDTH / xNodes) + (WIDTH / xNodes) / 2, j * (HEIGHT / yNodes) + (HEIGHT / yNodes) / 2])
    return nodes


def get_node_pos(node):
    """
    Gets the absolute position when given a node index
    :param node: tuple, containing a node position
    :return: tuple holding x and y coords
    """
    index = (node[1] - 1) * xNodes + (node[0] - 1)
    coords = playerNodes[index]
    return coords


class Player(fadeStuff.drawObject):
    # Player Node
    node = []
    # Absolute Position
    x = 0.0
    y = 0.0
    # Destination position
    destX = x
    destY = y
    speed = 0  # When moving, we need bullets to take current speed into account.
    # Colour stuff
    r = 255
    g = 255
    b = 255
    colourChangeRate = 3
    radius = 3 * resoChange
    # Other attributes
    moveSpeed = 0.075

    equippedGuns = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.radius * 2, self.radius * 2])

        # Modification for collision detection

        self.rect = self.image.get_rect()

        self.node = [math.ceil(xNodes / 2), math.ceil(yNodes / 2)]
        xy = get_node_pos(self.node)
        self.x = xy[0]
        self.y = xy[1]
        self.destX = self.x
        self.destY = self.y

        # Modification for collision detection

        h = self.radius
        self.rect = pygame.Rect(self.x - h / 2, self.y - h / 2, h * 2, h * 2)

        for i in range(4):
            self.equippedGuns.append(guns.SprayGun(i))

    def move(self, dr):
        if dr == 0:
            # Try to go up
            if self.node[1] - 1 > 0:
                self.node[1] -= 1
                self.destY = get_node_pos(self.node)[1]
        elif dr == 1:
            # Try to go right
            if self.node[0] + 1 <= xNodes:
                self.node[0] += 1
                self.destX = get_node_pos(self.node)[0]
        elif dr == 2:
            # Try to go down
            if self.node[1] + 1 <= yNodes:
                self.node[1] += 1
                self.destY = get_node_pos(self.node)[1]
        elif dr == 3:
            # Try to go left
            if self.node[0] - 1 > 0:
                self.node[0] -= 1
                self.destX = get_node_pos(self.node)[0]
                # print(self.node)

    def update(self):
        speed = 0
        if not self.x == self.destX:
            diff = self.destX - self.x
            if abs(diff) > 1:
                speed = diff * self.moveSpeed
                self.x += speed
            else:
                self.x = self.destX
        if not self.y == self.destY:
            diff = self.destY - self.y
            if abs(diff) > 1:
                speed = diff * self.moveSpeed
                self.y += speed
            else:
                self.y = self.destY

        self.image = pygame.Surface([self.radius * 2, self.radius * 2])
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, self.colour, (self.radius, self.radius), self.radius, 1)
        self.image.set_colorkey(BLACK)

        # Modification for collision detection

        h = self.radius

        self.rect = pygame.Rect(self.x - h / 2, self.y - h / 2, h * 2, h * 2)

        # -----------------------------------

        self.rect.center = (self.x, self.y)
        # self.x = math.floor(self.x)
        # self.y = math.floor(self.y)
        self.speed = speed

        self.do_fader()
        self.draw_ammo()

        # Cool colour stuff, probably won't stay
        if self.r == 255:
            if not self.b == 0:
                self.b -= self.colourChangeRate
            else:
                self.g += self.colourChangeRate
        if self.g == 255:
            if not self.r == 0:
                self.r -= self.colourChangeRate
            else:
                self.b += self.colourChangeRate
        if self.b == 255:
            if not self.g == 0:
                self.g -= self.colourChangeRate
            else:
                self.r += self.colourChangeRate

        self.colour = pygame.Color(self.r, self.g, self.b)
        pygame.draw.circle(self.image, self.colour, (self.radius, self.radius), self.radius, 1)

    def shoot(self, dr):
        bullet = self.equippedGuns[dr].shoot([self.x, self.y], self.speed)
        if bullet:
            bulletList.add(bullet)

    def draw_ammo(self):  # TODO rename variables, tidy up a bit - no 'a' or 'b' stuff, give real names.
        ammoBarPositionModifier = 0
        for gun in self.equippedGuns:
            ammoBarPositionModifier += 20
            b = (gun.ammo / gun.maxAmmo)
            a = (WIDTH - 100) + b * 90

            barWidth = (WIDTH - 100) + 90  # For getting a constant bar width ~ Dylan

            w = 4  # So I don't have to keep typing 4 ~ Dylan

            # ADDITION #1 - 'Running out of ammo' change

            c = WHITE

            if b < 0.2:
                c = RED  # If low % of ammo remaining, change bar to red ~ Dylan

            # ////////////////////////////////////////////

            # (location, colour, pointA, pointB, line thickness) - points as X, Y
            # point defined as (X, Y)

            pygame.draw.line(screen, c, [WIDTH - 100, HEIGHT - 20 - ammoBarPositionModifier],
                             [a, HEIGHT - 20 - ammoBarPositionModifier], w)  # TODO The ammo bars are backwards

            # ADDITION #2  - Simple ammo counter

            lineWidth = barWidth - (WIDTH - 100)  # how long is the ammo bar? ~ Dylan

            ammoCount = 3  # would get from gun.maxAmmo if ammunition differed between weapons.
            # ammoCounts of 1 to ~50 show well, beyond that it becomes hard to read ~ Dylan

            increment = lineWidth / ammoCount  # how many pieces to split the ammo bar into ~ Dylan

            j = 0
            while j < ammoCount:
                offset = j * increment
                pygame.draw.line(screen, BLACK, [WIDTH - 100 + offset, HEIGHT - 20 - ammoBarPositionModifier - 3],
                                 [WIDTH - 100 + offset, HEIGHT - 20 - ammoBarPositionModifier + 3], 1)
                j += 1

                # Take max ammo, divide length of bar by amount of bullets
                # Add lines at increments of the bar.

                # If the ammo bars are going to have outlines, we could just blit the outline over the coloured bar.


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Game stuff -------
allSprites = pygame.sprite.Group()
bulletList = pygame.sprite.Group()
enemyList = pygame.sprite.Group()

# 15:9 is a good ratio
xNodes = 15
yNodes = 9
playerNodes = setup_nodes()

player = Player()
allSprites.add(player)

enemy = baddies.Fodder([random.randint(40, 700), random.randint(40, 700)])  # - for testing
enemyList.add(enemy)

# -------- Main Program Loop -----------
while not done:
    # --- Input logic here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move(0)
            if event.key == pygame.K_s:
                player.move(2)
            if event.key == pygame.K_a:
                player.move(3)
            if event.key == pygame.K_d:
                player.move(1)

            if event.key == pygame.K_r:
                screen.fill(BLACK)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.shoot(0)
    if keys[pygame.K_DOWN]:
        player.shoot(2)
    if keys[pygame.K_LEFT]:
        player.shoot(3)
    if keys[pygame.K_RIGHT]:
        player.shoot(1)

    if keys[pygame.K_SPACE]:
        enemy = baddies.Fodder([random.randint(40, 700), random.randint(40, 700)])  # - for testing
        enemyList.add(enemy)
        allSprites.add(enemy)
        pass

        # --- Game logic should go here

    # enemy behaviour
    # (apologies - this is a mess. We'll have to consider if another class is required for this)

    maxEnemies = 2  # maxEnemies on screen at once: increase this for crazy results

    if 1:  # Set to 0 to turn off random enemy spawning
        while len(enemyList) < maxEnemies:
            # We'll need more sophisticated code for finding spawn positions just outside of the screen border
            # Right now an enemy can spawn in the middle of the screen
            enemy = baddies.Fodder([random.randint(40, 700), random.randint(40, 700)])  # - for testing
            enemyList.add(enemy)

        if enemy.dead:
            enemyList.remove(enemy)

        # -------------------------------------- (It's a mess - sorry) -----------------

    for gun in player.equippedGuns:  # FIXME should be a player function
        gun.recharge()

    # collision check
    for bullet in bulletList:  # TODO I think there's a much less intensive collision method, which asks if members of a group collided, then checks what the collider was. I did it before, I'll try and find it
        for enemy in enemyList:
            if bullet.rect.colliderect(enemy.rect):
                enemy.take_damage(bullet.damage)
                bullet.destroy()

            # (Crude player death script - disappearing = death)
    for enemy in enemyList:
        if enemy.rect.colliderect(player.rect):
            allSprites.remove(player)  # TODO player take damage/death animation, respawning.

            # (Experiment code: you can get enemies to crash into each-other)
        for enemy2 in enemyList:
            if enemy != enemy2:
                if enemy.rect.colliderect(enemy2.rect):
                    enemy.death()
                    enemy2.death()

                # 'BALANCED' ALTERNATIVE TO ABOVE 'CRASH' CODE - DOESN'T WORK - UNSURE WHY
                #  IDEA: Take the health of the other ship in the collision, treat it as damage to this ship
    # for enemy2 in enemyList:
    #        if enemy.rect.colliderect(enemy2.rect):
    #            if enemy != enemy2:
    #                health1 = enemy.health
    #                health2 = enemy2.health
    #                
    #                enemy.take_damage(health2)
    #                enemy2.take_damage(health1)

    for thing in bulletList:  # FIXME add to player's new function to do gun stuff
        thing.timeToLive -= 10
        if thing.timeToLive <= 0:
            bulletList.remove(thing)

    # --- Drawing code should go here
    screen.fill(BLACK)

    for pos in playerNodes:
        pygame.draw.line(screen, WHITE, pos, pos, 1)

    # allSprites.clear(screen, background) # Don't think this is required
    allSprites.update()
    allSprites.draw(screen)

    bulletList.update()
    bulletList.draw(screen)

    enemyList.update()
    for enemy in enemyList:
        enemy.act([player.x, player.y])  # take action based on the player's position
    enemyList.draw(screen)

    fadeStuff.FM.do_fading()
    fadeStuff.FM.drawList.draw(screen)

    # As the player moves so fast, there are gaps between where the player moved from.
    # Looks kinda naff
    # Draw line from where player was last to where is now?
    # Fade depending on distance to player/object who made trace?

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(fps)
    dt += 1
    if dt == fps:
        dt = 0
    # print(clock.get_fps())

# Close the window and quit.
pygame.quit()
