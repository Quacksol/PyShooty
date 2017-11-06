from definitions import *
import os
"""
This module handles reading and writing to savefiles
Calls definitions to change game settings
"""
import re


def make_new_save_file():
    """
    Called if there is no save file present, for whatever reason.
    Just make the new file, set settings to default
    :return: None
    """
    with open('savefile.txt', 'w') as file:
        file_xRes = 320
        file.write("xRes = %d\n" % file_xRes)
        file_yRes = 240
        file.write('yRes = %d\n' % file_yRes)
        fullscreen = 0
        file.write(('fullscreen = %d\n' % fullscreen))


def read_game_settings():
    """
    Only really called on game startup - reads the game settings from last time.
    :return: None
    """
    global WIDTH, HEIGHT, fullscreen
    if os.path.isfile('savefile.txt'):
        with open('savefile.txt', 'r') as file:
            for line in file:
                match = re.match(r"(\w+) = (\d+)", line)
                if match:
                    if "xRes" in match.group(1):
                        WIDTH = int(match.group(2))
                    if "yRes" in match.group(1):
                        HEIGHT = int(match.group(2))
                    if "fullscreen" in match.group(1):
                        if '0' in match.group(2):
                            fullscreen = False
                        elif '1' in match.group(2):
                            fullscreen = True
                        else:
                            print("Invalid fullscreen read.")
    else:
        make_new_save_file()


def save_game_settings():
    """
    Save all the settings, no point only saving one bit that might have changed
    :return:
    """
    with open('savefile.txt', 'w') as file:
        file.write("xRes = %d\n" % WIDTH)
        file.write('yRes = %d\n' % HEIGHT)
        file.write(('fullscreen = %d\n' % fullscreen))
