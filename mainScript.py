"""
This script is the main thing that is called. It initialises pygame and all that, then goes to the menu.
It basically is the menu. This while loop does the menu stuff,
and when the game starts exits that loops and goes into the game loop enters another loop.
"""
# imports
import shooty
from definitions import *

# setup stuff
pygame.display.set_caption("Real Life Video Game")
pygame.init()

pygame.font.init()
titleFont = pygame.font.SysFont("calibri", 10 * resoChange)
submenuFont = pygame.font.SysFont("calibri", 5 * resoChange)

quitGame = False
while not quitGame:
    inMenu = True
    if inMenu:
        menuTable = [[[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6]],  # Main menu
                     [[1, 0], [0, 0]],                                  # Level Select
                     [[2, 0], [0, 0]],                                  # Endless
                     [[3, 0], [0, 0]],                                  # Options
                     [[4, 0], [0, 0]],                                  # Progress
                     [[5, 0], [0, 0]],                                  # Credits
                     [[7, 0], [0, 0]],                                  # Exit confirmation
                     []]                                                # Actually exit

        cursorTable = [[[5, 1, 0, 0], [0, 2, 1, 1], [1, 3, 2, 2], [2, 4, 3, 3], [3, 5, 4, 4], [4, 0, 5, 5]],
                       [[0, 1, 0, 0], [0, 1, 0, 0]],
                       [[0, 1, 0, 0], [0, 1, 0, 0]],
                       [[0, 1, 0, 0], [0, 1, 0, 0]],
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
        displaySurface = None  # Start on title screen

        drawList = []


        def move_cursor(direction):
            """
            Judges if the cursor can move to the requested position,
            which depends on the current position and which menu we're in.
            :return: None
            """
            global cursorState
            cursorState = cursorTable[menuState][cursorState][direction]


        def move_menu(direction):
            """
            Changes the menu state, depending on current menu state and cursor selection.
            Also do any computing for any state change.
            :return: state = The new state for the state machine to move to.
            """
            # TODO Screen transitions won't be immediate as they are now.
            global menuState, cursorState, displaySurface
            menuState = menuTable[menuState][cursorState][direction]
            cursorState = 0
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


        class MenuOption:
            def __init__(self, text, position):
                self.text = text  # TODO You might not need this
                self.image = submenuFont.render(text, False, WHITE)
                self.position = [position[0], position[1]]


        def make_main_menu():
            global displaySurface, drawList
            displaySurface = titleSurface
            drawList = []
            mainMode = MenuOption('Main mode', [2*(WIDTH/10), 3 * (HEIGHT / 10)])
            drawList.append(mainMode)
            endlessMode = MenuOption('Endless mode', [2*(WIDTH/10), 4 * (HEIGHT / 10)])
            drawList.append(endlessMode)
            optionsScreen = MenuOption('Options', [2*(WIDTH/10), 5 * (HEIGHT / 10)])
            drawList.append(optionsScreen)
            progressScreen = MenuOption('Unlockables', [2*(WIDTH/10), 6 * (HEIGHT / 10)])
            drawList.append(progressScreen)
            creditsScreen = MenuOption('Credits', [2*(WIDTH/10), 7 * (HEIGHT / 10)])
            drawList.append(creditsScreen)

            exitScreen = MenuOption('Exit (Esc)', [2*(WIDTH/10), 8 * (HEIGHT / 10)])
            drawList.append(exitScreen)


        def make_level_select():
            global displaySurface, drawList
            displaySurface = levelSelectSurface
            drawList = []
            level1 = MenuOption('eh reh', [2*(WIDTH/10), 100])
            drawList.append(level1)

            exitScreen = MenuOption('Exit (Esc)', [2*(WIDTH/10), 8 * (HEIGHT / 10)])
            drawList.append(exitScreen)


        def make_endless_menu():
            global displaySurface, drawList
            displaySurface = endlessSurface
            drawList = []
            endlessOption1 = MenuOption("Feature coming soon!", [2*(WIDTH/10), 3 * (HEIGHT / 10)])
            drawList.append(endlessOption1)

            exitScreen = MenuOption('Exit (Esc)', [2*(WIDTH/10), 8 * (HEIGHT / 10)])
            drawList.append(exitScreen)


        def make_options_menu():
            global displaySurface, drawList
            displaySurface = optionsSurface
            drawList = []
            option1 = MenuOption('This is an option', [2*(WIDTH/10), 3 * (HEIGHT / 10)])
            drawList.append(option1)

            exitScreen = MenuOption('Exit (Esc)', [2*(WIDTH/10), 8 * (HEIGHT / 10)])
            drawList.append(exitScreen)


        def make_progress_menu():
            global displaySurface, drawList
            displaySurface = progressSurface
            drawList = []
            option1 = MenuOption("Wow! You're making great progress.", [2*(WIDTH/10), 3 * (HEIGHT / 10)])
            drawList.append(option1)

            exitScreen = MenuOption('Exit (Esc)', [2*(WIDTH/10), 8 * (HEIGHT / 10)])
            drawList.append(exitScreen)


        def make_credits_screen():
            global displaySurface, drawList
            displaySurface = creditsSurface
            drawList = []
            option1 = MenuOption("Made by Dom, well done him.", [2*(WIDTH/10), 3 * (HEIGHT / 10)])
            drawList.append(option1)

            exitScreen = MenuOption('Exit (Esc)', [2*(WIDTH/10), 8 * (HEIGHT / 10)])
            drawList.append(exitScreen)


        def make_exit_screen():
            global displaySurface, drawList
            displaySurface = exitSurface
            drawList = []
            option1 = MenuOption("110% sure.", [3*(WIDTH/10), 3 * (HEIGHT / 10)])
            drawList.append(option1)
            option2 = MenuOption("Only 90%, go back!", [5*(WIDTH/10), 3 * (HEIGHT / 10)])
            drawList.append(option2)

        make_main_menu()


        class Cursor:
            def __init__(self):
                size = 8 * resoChange
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
                        move_menu(0)
                        # gameStart = True
                        # inMenu = False

                    # Quit game
                    if event.key == pygame.K_ESCAPE:
                        move_menu(1)

                    print(menuState, cursorState)

            # Do computations
            # If the menuState is a certain number, the menu is exited and something else happens
            if menuState == 1:
                gameStart = True
                inMenu = False
            elif menuState == 7:
                quitGame = True
                inMenu = False

            cursor.position[0] = drawList[cursorState].position[0] - 5*resoChange
            cursor.position[1] = drawList[cursorState].position[1] + 0.25*resoChange

            # Draw everything
            screen.fill(BLACK)
            screen.blit(displaySurface, ((WIDTH - displaySurface.get_width()) / 2, HEIGHT / 10))
            for thing in drawList:
                screen.blit(thing.image, thing.position)
            screen.blit(cursor.image, cursor.position)
            pygame.display.flip()

            if not inMenu:
                break

    if gameStart:
        shooty.do_main()
        gameStart = False
        inMenu = True

# Close the window and quit.
pygame.quit()
