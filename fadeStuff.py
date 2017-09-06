from definitions import *
fadeRate = 30


class FaderManager:
    def __init__(self):
        self.drawList = pygame.sprite.Group()  # Contains positions for fadey items. For each position, draw fadey item.

    def do_fading(self):
        print("EHREH")
        for item in self.drawList:
            kill = item.fade()
            if kill:
                self.drawList.remove(item)


class fadeSprite(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def fade(self):
        kill = False
        a = self.image.get_alpha()
        a -= fadeRate
        if a <= 0:
            kill = True
        else:
            self.image.set_alpha(a)
        return kill

FM = FaderManager()


class drawObject(pygame.sprite.Sprite):
    """
    An object that is drawn.
    Contains variables that every drawn object has, namely position, a list of 'fade objects' and the fadeObjects' colours.
    This is an abstract class.
    """
    colour = WHITE

    def do_fader(self):
        """
        This should be inherited by every child class. Each child needs to define its own actual drawing, though.
        :return:
        """
        # TODO only 1 fadeSprite per position, otherwise that position will appear really bright.
        newFadeSprite = fadeSprite(self.image.copy(), (self.x, self.y))
        FM.drawList.add(newFadeSprite)

