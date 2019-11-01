import Settings
from pygame import *
from pygame.sprite import Sprite

class CoinGet(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.timer = 0
        self.images = ['49', '32', '33']
        self.index = 0
        self.image = Settings.COIN_IMAGES['49']
        self.rect = self.image.get_rect(topleft = (xpos, ypos))
        self.jumpAmount = 60
        self.delay = 4
        self.jumpAmount = 0
        self.reached_apex = False

    def update(self, *args):
        if self.timer >= self.delay:
            if not self.reached_apex:
                self.rect.y -= 10
                self.jumpAmount += 10
                if self.jumpAmount == 20:
                    self.image = Settings.COIN_IMAGES['32']
                if self.jumpAmount == 40:
                    self.image = Settings.COIN_IMAGES['33']
                if self.jumpAmount == 60:
                    self.image = Settings.COIN_IMAGES['49']
                    self.reached_apex = True
            else:
                self.rect.y += 10
                self.jumpAmount -= 10
                if self.jumpAmount == 40:
                    self.image = Settings.COIN_IMAGES['32']
                if self.jumpAmount == 20:
                    self.image = Settings.COIN_IMAGES['33']
                if self.jumpAmount == 0:
                    self.kill()
        else:
            self.timer += 1
        Settings.SCREEN.blit(self.image, self.rect)