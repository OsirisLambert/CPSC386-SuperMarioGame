import Settings
from pygame import *
from pygame.sprite import Sprite

class Mushroom(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.direction = 1 # go left->-1, go right->1
        self.image = transform.scale(Settings.ITEMS_IMAGES['10'], (40, 40))
        self.rect = self.image.get_rect(topleft=(xpos,ypos))
        self.GrowHeight = 0
        self.gameTimer = time.get_ticks()
        self.isEmerging = True
        self.hitWall = False
        self.isStanding = True

    def Fall(self):
        if not self.isStanding:
            self.rect.y += Settings.MARIO_FALL_SPEED

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
        else:
            self.Fall()
            if self.hitWall:
                self.direction *= -1
                self.hitWall = False
            self.rect.x += self.direction * Settings.MUSHROOM_MOVE_SPEED
        self.isStanding = False

        Settings.SCREEN.blit(self.image, self.rect)