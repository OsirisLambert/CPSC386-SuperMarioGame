import Settings
from pygame import *
from pygame.sprite import Sprite

class Castle(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.image = transform.scale(Settings.IMAGES['11'], (220, 200))
        self.rect = self.image.get_rect(topleft=(xpos,ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)