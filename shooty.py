"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import math

import fadeStuff
import guns
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
            nodes.append([i*(WIDTH/xNodes)+(WIDTH/xNodes)/2, j*(HEIGHT/yNodes)+(HEIGHT/yNodes)/2])
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
        self.image = pygame.Surface([self.radius*2, self.radius*2])
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, self.colour, (self.radius, self.radius), self.radius, 1)

        self.node = [math.ceil(xNodes / 2), math.ceil(yNodes / 2)]
        xy = get_node_pos(self.node)
        self.x = xy[0]
        self.y = xy[1]
        self.destX = self.x
        self.destY = self.y

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

    def update_pos(self):
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
        #self.x = math.floor(self.x)
        #self.y = math.floor(self.y)
        self.speed = speed

    def shoot(self, dr):
        bullet = self.equippedGuns[dr].shoot([self.x, self.y], self.speed)
        if bullet:
            bulletList.append(bullet)

    def draw(self, position):
        super(Player, self).draw([int(position[0]), int(position[1])])
        for item in self.drawList:
            pygame.draw.circle(screen, item.colour, [int(item.position[0]), int(item.position[1])], player.radius, 1)



# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Game stuff -------
drawList = []
bulletList = []

# 15:9 is a good ratio
xNodes = 15
yNodes = 9
playerNodes = setup_nodes()

player = Player()
drawList.append(player)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
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
        pass

    # --- Game logic should go here
    if player.r == 255:
        if not player.b == 0:
            player.b -= player.colourChangeRate
        else:
            player.g += player.colourChangeRate
    if player.g == 255:
        if not player.r == 0:
            player.r -= player.colourChangeRate
        else:
            player.b += player.colourChangeRate
    if player.b == 255:
        if not player.g == 0:
            player.g -= player.colourChangeRate
        else:
            player.r += player.colourChangeRate

    player.colour = pygame.Color(player.r, player.g, player.b)
    player.update_pos()
    for gun in player.equippedGuns:
        gun.recharge()

    # --- Drawing code should go here
    screen.fill(BLACK)

    i = 0
    for gun in player.equippedGuns:
        i += 20
        b = (gun.ammo/gun.maxAmmo)
        a = (WIDTH - 100) + b * 90
        pygame.draw.line(screen, WHITE, [WIDTH - 100, HEIGHT - 20 - i], [a, HEIGHT - 20 - i], 4)

    for pos in playerNodes:
        pygame.draw.line(screen, WHITE, pos, pos, 1)

    for thing in drawList:
        thing.draw([thing.x, thing.y])
    for thing in bulletList:
        thing.timeToLive -= 1
        if thing.timeToLive <= 0:
            bulletList.remove(thing)
        else:
            thing.draw([thing.x, thing.y])
    # As the player moves so fast, there are gaps between where the player moved from.
    # Looks kinda naff
    # Draw line from where player was last to where is now?
    # Fade depending on distance to player/object who made trace?

    #circList.append([player.x, player.y, player.radius, pygame.Color(player.r, player.g, player.b, 100)])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    # print(clock.get_fps())

# Close the window and quit.
pygame.quit()
