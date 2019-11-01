import Settings
from pygame import *
from pygame.sprite import Sprite

class GroundUpBrick(Sprite):
    def __init__(self, xpos, ypos, level='1-1'):
        Sprite.__init__(self)
        if level == '1-2':
            self.image = transform.scale((Settings.IMAGES['17']), (40, 40))
        else:
            self.image = transform.scale((Settings.IMAGES['6']), (40, 40))
        self.rect = self.image.get_rect(topleft=(xpos,ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)


class GroundBrick(Sprite):
    def __init__(self, xpos, ypos, level='1-1'):
        Sprite.__init__(self)
        if level == '1-2':
            self.image = transform.scale((Settings.IMAGES['16']), (40, 80))
        else:
            self.image = transform.scale((Settings.IMAGES['5']), (40, 80))
        self.rect = self.image.get_rect(topleft=(xpos,ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)
