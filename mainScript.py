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
mainFont = pygame.font.SysFont("calibri", 30)
# main
# 0 Menu state
# 1 In-game state
quitGame = False
while not quitGame:
    inMenu = True
    if inMenu:
        menuCursor = 0  # Position of the menu cursor
        menuState = 0  # Which state we are in the menu. See menu doc for info

        titleSurface = mainFont.render('The best game ever made in the world ever', False, WHITE)

        def move_cursor(direction):
            """
            Judges if the cursor can move to the requested position, which depends on the current position and which menu
            we're in.
            :return: None
            """
            pass

        def do_menu_SM():
            """
            Changes the menu state, depending on current menu state and cursor selection.
            :return: state = The new state for the state machine to move to.
            """
            # For now, just enter the game
            pass


        while 1:
            # Do main menu
            gameStart = False

            # Get user inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitGame = True
                    inMenu = False
                if event.type == pygame.KEYDOWN:
                    # Cursor movement
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        move_cursor(0)
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        move_cursor(2)
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        move_cursor(3)
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        move_cursor(1)

                    # Cursor select
                    if event.key == pygame.K_SPACE:
                        do_menu_SM()
                        gameStart = True
                        inMenu = False


                    # Quit game
                    if event.key == pygame.K_ESCAPE:
                        quitGame = True
                        inMenu = False

            # Do computations

            # Draw everything
            screen.fill(BLACK)
            pygame.draw.circle(screen, [200, 40, 100], (10, 10), 400, 1)
            screen.blit(titleSurface, ((WIDTH - titleSurface.get_width())/2, 100))

            pygame.display.flip()

            if not inMenu:
                break

    if gameStart:
        shooty.do_main()
        gameStart = False
        inMenu = True

# Close the window and quit.
pygame.quit()
