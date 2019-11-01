from pygame import *
from pygame.sprite import Sprite
import Settings


class Move_step(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.image = image.load('Images/10.png')
        self.image = transform.scale(self.image, (100, 10))
        self.rect = self.image.get_rect(topleft=(xpos,ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)