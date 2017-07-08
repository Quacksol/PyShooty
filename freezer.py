"""
I don't know how this works, but it sort of does - if you have cx_freeze installed, this should make an exe of the game.
"""
from cx_Freeze import setup, Executable
import sys

name = "VIDEO GAME"
file = r"C:\Users\Bane\PycharmProjects\fadeTest\shooty.py" # folder will be found in Bane

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re"]

setup(
        name = name,
        version = "0.1",
        description = "Sample cx_Freeze PyQt4 script",
        options = {"build_exe" : {"includes" : includes }},
executables = [Executable(file, base = base)])