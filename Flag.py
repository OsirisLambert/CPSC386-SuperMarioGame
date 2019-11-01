import Settings
from pygame import *
from pygame.sprite import Sprite


class Flag(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.image = transform.scale(Settings.IMAGES['8'], (40, 40))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)


class Flagpole(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.image = transform.scale(Settings.IMAGES['9'], (10, 360))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.next_level = False

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)