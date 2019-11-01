import Settings
from pygame import *
from pygame.sprite import Sprite

class Flower(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.image = transform.scale(Settings.ITEMS_IMAGES['16'], (40, 40))
        self.rect = self.image.get_rect(topleft=(xpos,ypos))
        self.GrowHeight = 0
        self.gameTimer = time.get_ticks()
        self.isEmerging = True
        self.index = 0
        self.images = ['16', '17', '18']
        self.refreshRate = 3
        self.clock = 0

    def Emerge(self, currentTime):
        if currentTime - self.gameTimer > Settings.MUSHROOM_EMERGE_FREQUENCY:
            if self.GrowHeight < 20:
                self.rect.y -= 2
                self.GrowHeight += 1
            else:
                self.isEmerging = False
            self.gameTimer = time.get_ticks()

    def update(self, currentTime):
        if self.isEmerging:
            self.Emerge(currentTime)
        if self.clock > self.refreshRate:
            self.image = transform.scale(Settings.ITEMS_IMAGES[self.images[self.index]], (40, 40))
            pos = self.rect.bottomleft
            self.rect = self.image.get_rect(bottomleft=pos)
            if self.index >= len(self.images) - 1:
                self.index = 0
            else:
                self.index += 1
            self.clock = 0
        else:
            self.clock += 1

        Settings.SCREEN.blit(self.image, self.rect)