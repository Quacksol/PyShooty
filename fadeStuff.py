from definitions import *
fadeRate = 1


def fade(theList, item):
    """
    Gets a colour, decreases it a bit. Checks it's close to BLACK, and removes from a list.
    :param item: the item passed in, which has a colour property.
    :param theList: list to remove from, if necessary.
    :return: darkened colour, to be be drawn be specific function
    """
    # Set pixel colour to less than what it is now
    col = item.colour
    col.hsla = [col.hsla[0], col.hsla[1], max((col.hsla[2] - fadeRate), 0), col.hsla[3]]
    if col.r < 10 and col.g < 10 and col.b < 10:
        # Remove from pixList, set pixel to BLACK
        theList.remove(item)
        col = BLACK

    return col


class fadeSprite:
    def __init__(self, position, col):
        self.position = position
        self.colour = col


class drawObject(pygame.sprite.Sprite):
    """
    An object that is drawn.
    Contains variables that every drawn object has, namely position, a list of 'fade objects' and the fadeObjects' colours.
    This is an abstract class.
    """
    x = 0   # X coord
    y = 0   # Y coord
    drawList = []  # Contains positions for fadey items. For each position, draw fadey item.
    colour = WHITE

    def draw(self, position):
        """
        This should be inherited by every child class. Each child needs to define its own actual drawing, though.
        :return:
        """
        newFadeSprite = fadeSprite(position, self.colour)
        self.drawList.append(newFadeSprite)
        for item in self.drawList:
            item.colour = fade(self.drawList, item)
        pass
