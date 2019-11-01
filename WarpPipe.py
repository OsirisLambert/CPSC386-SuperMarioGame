import Settings
from pygame import *
from pygame.sprite import Sprite

class NormalPipe(Sprite):
    def __init__(self, xpos, ypos, width, height):
        Sprite.__init__(self)
        self.image = transform.scale(Settings.IMAGES['7'], (width, height))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)


class Long_pipe(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.image = transform.scale(Settings.IMAGES['18'], (160, 320))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)