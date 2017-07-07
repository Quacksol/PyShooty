from definitions import *
fadeRate = 10


class fadeSprite(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.alpha = 255
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

    def fade(self):
        kill = False
        self.image.set_alpha(self.alpha)
        self.alpha -= fadeRate
        if self.alpha <= 0:
            kill = True
        return kill


class drawObject(pygame.sprite.Sprite):
    """
    An object that is drawn.
    Contains variables that every drawn object has, namely position, a list of 'fade objects' and the fadeObjects' colours.
    This is an abstract class.
    """
    drawList = pygame.sprite.Group()  # Contains positions for fadey items. For each position, draw fadey item.
    colour = WHITE

    def do_fader(self, image, position):
        """
        This should be inherited by every child class. Each child needs to define its own actual drawing, though.
        :return:
        """

        newFadeSprite = fadeSprite(image, position)
        self.drawList.add(newFadeSprite)
        for item in self.drawList:
            kill = item.fade()
            if kill:
                self.drawList.remove(item)
        self.drawList.draw(screen)
