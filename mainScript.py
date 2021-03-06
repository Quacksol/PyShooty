"""
This script is the main thing that is called. It initialises pygame and all that, then goes to the menu.
It basically is the menu. This while loop does the menu stuff,
and when the game starts exits that loops and goes into the game loop enters another loop.
"""

if __name__ == '__main__':
    from definitions import *
    import fileReader

    fileReader.read_game_settings()
    # setup stuff
    pygame.display.set_caption("Real Life Video Game")
    pygame.init()

    pygame.font.init()
    titleFont = pygame.font.SysFont("calibri", int(8*2*resoScale))
    submenuFont = pygame.font.SysFont("calibri", int(5*2*resoScale))

    quitGame = False

    # Define stuff that is for both menu and in-game
    def change_resolution(width, height):
        """
        Change the resolution. Only do this in the menu, too much effort to change the sizes of everything in-game.
        :param height: New screen height
        :param width: New screen width
        :return: None
        """
        global screen, HEIGHT, WIDTH
        WIDTH = width
        HEIGHT = height
        screen = pygame.Surface([WIDTH, WIDTH])
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    def change_fullscreen():
        """
        Changes the game from windowed to fullscreen, and vice-versa, depending on current state.
        :return: None
        """
        global fullscreen, screen
        fullscreen = not fullscreen
        if fullscreen:
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            # Set to windowed based on saved reso settings


    while not quitGame:
        inMenu = True
        gameStart = False
        if inMenu:
            menuTable = [[[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6]],  # Main menu
                         [[1, 0], [0, 0]],                                  # Level Select
                         [[2, 0], [0, 0]],                                  # Endless
                         [[3, 0], [3, 0], [0, 0]],                          # Options
                         [[4, 0], [0, 0]],                                  # Progress
                         [[5, 0], [0, 0]],                                  # Credits
                         [[7, 0], [0, 0]],                                  # Exit confirmation
                         []]                                                # Actually exit
            # Up, down, left, right
            cursorTable = [[[5, 1, 0, 0], [0, 2, 1, 1], [1, 3, 2, 2], [2, 4, 3, 3], [3, 5, 4, 4], [4, 0, 5, 5]],
                           [[0, 1, 0, 0], [0, 1, 0, 0]],
                           [[0, 1, 0, 0], [0, 1, 0, 0]],
                           [[0, 1, 0, 0], [0, 2, 0, 0], [1, 3, 0, 0]],
                           [[0, 1, 0, 0], [0, 1, 0, 0]],
                           [[0, 1, 0, 0], [0, 1, 0, 0]],
                           [[0, 0, 0, 1], [0, 0, 0, 1]]

                           ]
            cursorState = 0  # Position of the menu cursor
            menuState = 0  # Which state we are in the menu. See menu doc for info

            titleSurface = titleFont.render('The best game ever made in the world ever', False, WHITE)
            levelSelectSurface = titleFont.render('Level Select', False, WHITE)
            endlessSurface = titleFont.render('Endless Mode options', False, WHITE)
            optionsSurface = titleFont.render('Options', False, WHITE)
            progressSurface = titleFont.render('Progress n stuff', False, WHITE)
            creditsSurface = titleFont.render('Credits', False, WHITE)
            exitSurface = titleFont.render('Are you 100% sure you want to quit?', False, WHITE)
            displaySurface = None  # Start at none, define later properly.

            drawList = []


            def move_cursor(direction):
                """
                Judges if the cursor can move to the requested position,
                which depends on the current position and which menu we're in.
                :return: None
                """
                global cursorState
                cursorState = cursorTable[menuState][cursorState][direction]


            def draw_menu():
                """
                'Move' to the menu, depending on the global menuState.
                Also do any computing for any state change.

                :return: None
                """
                global menuState
                if menuState == 0:
                    make_main_menu()
                elif menuState == 1:
                    make_level_select()
                elif menuState == 2:
                    make_endless_menu()
                elif menuState == 3:
                    make_options_menu()
                elif menuState == 4:
                    make_progress_menu()
                elif menuState == 5:
                    make_credits_screen()
                elif menuState == 6:
                    make_exit_screen()

            def move_menu(direction):
                """
                Changes the menu state, depending on current menu state and cursor selection.
                Calls move_menu with no parameters, after changing the menuState.
                :return: None
                """
                # TODO Screen transitions won't be immediate as they are now.
                global menuState, cursorState, displaySurface
                menuState = menuTable[menuState][cursorState][direction]
                cursorState = 0
                draw_menu()

            def do_menu(direction):
                """
                Do a menu action, whether that be a special function or generic menu change.
                Determined by the current menu state + direction.
                :param direction: 0 for up, 1 for down a menu.
                :return: None
                """
                global menuState, cursorState
                special = False
                if direction == 1:
                    # Just change menu down, esc never does a special function.
                    move_menu(direction)
                else:
                    if menuState == 0:  # Main menu
                        pass
                    elif menuState == 1:  # Level select
                        pass  # TODO Choose a particular level
                    elif menuState == 2:  # Endless
                        pass
                    elif menuState == 3:  # Options
                        pass  # FIXME Change resolutions
                        if cursorState == 0:
                            change_fullscreen()
                            special = True

                if not special:  # :'(
                    move_menu(direction)


            class MenuOption:
                """
                Class for the options that appear in each menu.
                Comes with the text it is to display as str and image, and its position to appear on the screen.
                """
                def __init__(self, text, position):
                    self.text = text  # TODO You might not need this
                    self.image = submenuFont.render(text, False, WHITE)
                    self.position = [position[0], position[1]]


            def make_main_menu():
                global displaySurface, drawList
                displaySurface = titleSurface
                drawList = []
                mainMode = MenuOption('Main mode', [2*(BASEWIDTH/10), 3 * (BASEHEIGHT / 10)])
                drawList.append(mainMode)
                endlessMode = MenuOption('Endless mode', [2*(BASEWIDTH/10), 4 * (BASEHEIGHT / 10)])
                drawList.append(endlessMode)
                optionsScreen = MenuOption('Options', [2*(BASEWIDTH/10), 5 * (BASEHEIGHT / 10)])
                drawList.append(optionsScreen)
                progressScreen = MenuOption('Unlockables', [2*(BASEWIDTH/10), 6 * (BASEHEIGHT / 10)])
                drawList.append(progressScreen)
                creditsScreen = MenuOption('Credits', [2*(BASEWIDTH/10), 7 * (BASEHEIGHT / 10)])
                drawList.append(creditsScreen)

                exitScreen = MenuOption('Exit (Esc)', [2*(BASEWIDTH/10), 8 * (BASEHEIGHT / 10)])
                drawList.append(exitScreen)


            def make_level_select():
                global displaySurface, drawList
                displaySurface = levelSelectSurface
                drawList = []
                level1 = MenuOption('stinky level select', [2*(BASEWIDTH/10), 3 * (BASEHEIGHT / 10)])
                drawList.append(level1)

                exitScreen = MenuOption('Exit (Esc)', [2*(BASEWIDTH/10), 8 * (BASEHEIGHT / 10)])
                drawList.append(exitScreen)


            def make_endless_menu():
                global displaySurface, drawList
                displaySurface = endlessSurface
                drawList = []
                endlessOption1 = MenuOption("Feature coming soon!", [2*(BASEWIDTH/10), 3 * (BASEHEIGHT / 10)])
                drawList.append(endlessOption1)

                exitScreen = MenuOption('Exit (Esc)', [2*(BASEWIDTH/10), 8 * (BASEHEIGHT / 10)])
                drawList.append(exitScreen)


            def make_options_menu():
                global displaySurface, drawList
                displaySurface = optionsSurface
                drawList = []
                option1 = MenuOption('Change Fullscreen', [2*(BASEWIDTH/10), 3 * (BASEHEIGHT / 10)])
                drawList.append(option1)
                option2 = MenuOption("Another option", [2*(BASEWIDTH/10), 4 * (BASEHEIGHT / 10)])
                drawList.append(option2)

                exitScreen = MenuOption('Exit (Esc)', [2*(BASEWIDTH/10), 8 * (BASEHEIGHT / 10)])
                drawList.append(exitScreen)


            def make_progress_menu():
                global displaySurface, drawList
                displaySurface = progressSurface
                drawList = []
                option1 = MenuOption("Wow! You're making great progress.", [2*(BASEWIDTH/10), 3 * (BASEHEIGHT / 10)])
                drawList.append(option1)

                exitScreen = MenuOption('Exit (Esc)', [2*(BASEWIDTH/10), 8 * (BASEHEIGHT / 10)])
                drawList.append(exitScreen)


            def make_credits_screen():
                global displaySurface, drawList
                displaySurface = creditsSurface
                drawList = []
                option1 = MenuOption("Made by Dom, well done him.", [2*(BASEWIDTH/10), 3 * (BASEHEIGHT / 10)])
                drawList.append(option1)

                exitScreen = MenuOption('Exit (Esc)', [2*(BASEWIDTH/10), 8 * (BASEHEIGHT / 10)])
                drawList.append(exitScreen)


            def make_exit_screen():
                global displaySurface, drawList
                displaySurface = exitSurface
                drawList = []
                option1 = MenuOption("110% sure.", [3*(BASEWIDTH/10), 3 * (BASEHEIGHT / 10)])
                drawList.append(option1)
                option2 = MenuOption("Only 90%, go back!", [5*(BASEWIDTH/10), 3 * (BASEHEIGHT / 10)])
                drawList.append(option2)

            make_main_menu()


            class Cursor:
                def __init__(self):
                    size = 8 * resoScale
                    self.image = pygame.Surface([size, size])
                    self.image.fill(BLACK)
                    # Draw triangle from three points
                    pygame.draw.polygon(self.image, BLUE, [[0, 0], [0, size/2], [size/2, size/4]], 0)
                    self.image.set_colorkey(BLACK)
                    self.position = [0, 0]


            cursor = Cursor()

            while 1:
                # Do main menu
                gameStart = False

                # Get user inputs
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quitGame = True
                        inMenu = False  # TODO look up signals and slots for quitting the game
                    if event.type == pygame.VIDEORESIZE:
                        change_resolution(event.w, event.h)
                        draw_menu()
                    if event.type == pygame.KEYDOWN:
                        # Cursor movement
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                            move_cursor(0)
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                            move_cursor(1)
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            move_cursor(2)
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            move_cursor(3)

                        # Cursor select
                        if event.key == pygame.K_SPACE:
                            do_menu(0)
                            # gameStart = True
                            # inMenu = False

                        # Quit game
                        if event.key == pygame.K_ESCAPE:
                            do_menu(1)

                        # print(menuState, cursorState)

                # Do computations
                # If the menuState is a certain number, the menu is exited and something else happens
                if menuState == 1:
                    gameStart = True
                    inMenu = False
                elif menuState == 7:
                    quitGame = True
                    inMenu = False

                cursor.position[0] = drawList[cursorState].position[0] - 5 * resoScale
                cursor.position[1] = drawList[cursorState].position[1] + 3 * resoScale

                # Draw everything
                main_surf.fill(BLACK)

                main_surf.blit(displaySurface, ((BASEWIDTH - displaySurface.get_width()) / 2, BASEHEIGHT / 10))
                for thing in drawList:
                    main_surf.blit(thing.image, thing.position)
                main_surf.blit(cursor.image, cursor.position)
                pygame.transform.scale(main_surf, (WIDTH, HEIGHT), screen)

                pygame.display.flip()

                if not inMenu:
                    break

        if gameStart:

            import math
            import random

            import guns
            import baddies

            def setup_nodes():
                """
                Returns the positions of the nodes the player will move between
                :return: nodes
                """
                nodes = []
                for j in range(yNodes):
                    for i in range(xNodes):
                        nodes.append([i * (BASEWIDTH / xNodes) + (BASEWIDTH / xNodes) / 2,
                                      j * (BASEHEIGHT / yNodes) + (BASEHEIGHT / yNodes) / 2])
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


            class Player(pygame.sprite.Sprite):
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
                radius = int(2 * objectSize * resoScale)
                # Other attributes
                moveSpeed = 0.03 * objectSize

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

                    self.colour = WHITE

                    # Modification for collision detection

                    h = self.radius
                    self.rect = pygame.Rect(self.x - h / 2, self.y - h / 2, h * 2, h * 2)

                    for i in range(4):
                        self.equippedGuns.append(guns.SprayGun(i))

                def move(self, dr):
                    """
                    Set the new position variables. The player is not moved here, but in update().
                    :param dr: The direction of travel.
                    :return: None
                    """
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

                    self.do_guns()

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
                        bulletSprites.add(bullet)

                def draw_ammo(self):
                    """
                    Draw the ammo bars.
                    :return:
                    """
                    ammoBarPositionModifier = 0
                    ammoBarStart = WIDTH - 30 * 1
                    for gun in self.equippedGuns:
                        ammoBarPositionModifier += 4 * 1  # For getting next y positions
                        ammo = (gun.ammo / gun.maxAmmo)  # Get ammo as a fraction
                        maxBarSize = ammoBarStart + 1 * 25  # TODO should be constant, don't set every frame pls
                        ammoBarEnd = ammoBarStart + ammo * 1 * 25  # For getting a constant bar width ~ Dylan
                        thickness = 1  # So I don't have to keep typing 4 ~ Dylan

                        # ADDITION #1 - 'Running out of ammo' change

                        colour = WHITE
                        if ammo < 0.2:
                            colour = RED  # If low % of ammo remaining, change bar to red ~ Dylan

                        barY = HEIGHT - 20 * 1 + ammoBarPositionModifier
                        pygame.draw.line(screen, colour, [ammoBarStart, barY], [ammoBarEnd, barY], thickness)

                        # ADDITION #2  - Simple ammo counter

                        # lineWidth = barWidth - (WIDTH - 100)  # how long is the ammo bar? ~ Dylan

                        ammoCount = gun.barSplits  # how many pieces to split the bar into.
                        # ammoCounts of 1 to ~50 show well, beyond that it becomes hard to read ~ Dylan

                        increment = (maxBarSize - ammoBarStart) / ammoCount  # positions to split the bar

                        j = 1
                        while j < ammoCount:
                            offset = j * increment
                            pygame.draw.line(screen, BLACK, [ammoBarStart + offset, barY - thickness / 2],
                                             [ammoBarStart + offset, barY + thickness / 2], 1)
                            j += 1

                            # Take max ammo, divide length of bar by amount of bullets
                            # Add lines at increments of the bar.

                            # If the ammo bars are going to have outlines, we could just blit the outline over the coloured bar.

                def do_guns(self):
                    """
                    Function to do all passive gun related actions, like recharging and bullet life checking.
                    :return: None
                    """
                    for gun in self.equippedGuns:
                        gun.recharge()

                    for thing in bulletSprites:
                        thing.timeToLive -= 10
                        if thing.timeToLive <= 0:
                            bulletSprites.remove(thing)

            # Start actually initialising stuff
            done = False

            playerSprites = pygame.sprite.Group()
            bulletSprites = pygame.sprite.Group()
            enemySprites = pygame.sprite.Group()

            # 15:9 is a good ratio
            nodeMultiplier = 3  # This determines the level 'size' - TODO make level select control this
            xNodes = 5 * nodeMultiplier
            yNodes = 3 * nodeMultiplier
            playerNodes = setup_nodes()

            player = Player()
            playerSprites.add(player)
            # For the screen fading
            surf = pygame.Surface([WIDTH, HEIGHT])
            surf.fill(BLACK)
            surf.set_alpha(10)

            main_surf.fill(BLACK)

            # -------- Main Program Loop -----------
            while not done:
                # --- Input logic here
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.VIDEORESIZE:
                        change_resolution(event.w, event.h)
                        draw_menu()
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
                    enemySprites.add(enemy)
                    print(len(enemySprites.sprites()))
                    # allSprites.add(enemy)
                    pass

                if keys[pygame.K_ESCAPE]:
                    done = True


                    # --- Game logic should go here

                # enemy behaviour
                # (apologies - this is a mess. We'll have to consider if another class is required for this)

                maxEnemies = 5  # maxEnemies on screen at once: increase this for crazy results

                if 1:  # Set to 0 to turn off random enemy spawning
                    while len(enemySprites) < maxEnemies:
                        """
                        1. Choose whether left/right or top/bottom (1/4)
                        2. Depending on choice, set x or y randomly
                        """
                        i = random.randint(0, 3)
                        if i == 0:
                            # spawn at top
                            y = -30
                            x = random.randint(-30, BASEWIDTH + 30)
                        elif i == 1:
                            # spawn at bottom
                            y = BASEHEIGHT + 30
                            x = random.randint(-30, BASEWIDTH + 30)
                        elif i == 2:
                            # spawn at right
                            x = BASEWIDTH + 30
                            y = random.randint(-30, BASEHEIGHT + 30)
                        elif i == 3:
                            # spawn at left
                            x = -30
                            y = random.randint(-30, BASEHEIGHT + 30)
                        else:
                            print("ERROR")

                        enemy = baddies.Fodder([x, y])  # - for testing
                        enemySprites.add(enemy)

                # ----------------------------- Group Updates ------------------------------------
                playerSprites.update()
                bulletSprites.update()
                enemySprites.update()
                for enemy in enemySprites:
                    enemy.act([player.x, player.y])  # take action based on the player's position
                    if enemy.dead:
                        enemySprites.remove(enemy)

                # ----------------------------- Collision checks ---------------------------------

                # Enemies - check for player collisions, and with other enemies
                for enemy in enemySprites:
                    col_list = pygame.sprite.spritecollide(enemy, playerSprites, False)
                    for thing in col_list:
                        playerSprites.remove(thing)  # TODO player take damage/death animation, respawning.
                        # done = True

                # Bullets - check for collisions with enemies
                for bullet in bulletSprites:
                    col_list = pygame.sprite.spritecollide(bullet, enemySprites, False)
                    for thing in col_list:
                        dead = thing.take_damage(bullet.damage)
                        if dead:  # I know I can minimise this, but it's better like this for readers innit
                            enemySprites.remove(thing)
                    if col_list:
                        bullet.destroy()

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

                # --- Drawing code should go here
                main_surf.blit(surf, [0, 0])

                for pos in playerNodes:
                    pygame.draw.line(main_surf, WHITE, pos, pos, 1)

                # allSprites.clear(screen, background) # Don't think this is required
                playerSprites.draw(main_surf)
                player.draw_ammo()

                bulletSprites.draw(main_surf)
                enemySprites.draw(main_surf)
                for enemy in enemySprites:
                    enemy.lifebar()

                # --- Go ahead and update the screen with what we've drawn.
                pygame.transform.scale(main_surf, (WIDTH, HEIGHT), screen)
                #screen.blit(main_surf, [0, 0])
                pygame.display.flip()

                # --- Limit to 60 frames per second
                clock.tick(fps)
                dt += 1
                if dt == fps:
                    dt = 0

                    # print(clock.get_fps())

            gameStart = False
            inMenu = True

    # Close the window and quit.
    fileReader.save_game_settings()
    pygame.quit()
