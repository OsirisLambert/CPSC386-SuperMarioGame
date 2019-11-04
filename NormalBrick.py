import Settings
from pygame import *
from pygame.sprite import Sprite
import unmoveable_item

class NormalBrick(Sprite):
    def __init__(self, xpos, ypos, *args):
        Sprite.__init__(self)
        self.image = transform.scale(Settings.IMAGES['0'], (40, 40))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.image_break1 = transform.scale(Settings.UNMOVE_ITEM_IMAGES['37'], (20, 20))
        self.break_rect1 = self.image_break1.get_rect(topleft=(self.rect.x + 20, ypos))
        self.image_break2 = transform.scale(Settings.UNMOVE_ITEM_IMAGES['36'], (20, 20))
        self.break_rect2 = self.image_break2.get_rect(topleft=(self.rect.x+20, ypos+20))
        self.image_break3 = transform.scale(Settings.UNMOVE_ITEM_IMAGES['37'], (20, 20))
        self.break_rect3 = self.image_break3.get_rect(topleft=(self.rect.x, ypos+20))
        self.break_index_left = 0
        self.break_index_right = 0
        self.break_index_down  = 680 - ypos


        self.startingY = self.rect.bottom
        self.gameTimer = time.get_ticks()
        self.falling = False
        self.trigger = True
        self.bump = False
        self.destroy = False
        self.playSound = False

    def explode(self):
        if self.break_index_left > -10:
            self.break_index_left -= 1
            self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['36'], (20, 20))
            self.rect.x += self.break_index_left
            self.break_rect2.x += self.break_index_left
        if self.break_index_right < 10:
            self.break_index_right += 1
            self.break_rect1.x += self.break_index_right
            self.break_rect3.x += self.break_index_right
        if self.break_index_down < 680:
            self.break_index_down += 1
            self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['37'], (20, 20))
            self.rect.y += 10
            self.break_rect1.y += 10
            self.break_rect2.y += 10
            self.break_rect3.y += 10

    def update(self, currentTime):
        if currentTime - self.gameTimer > Settings.BLOCK_JUMP_FREQUENCY:
            if self.bump and not self.destroy:
                """
                if self.playSound:
                    PLAYSOUND
                    self.playSound = False
                """
                if self.startingY - self.rect.bottom < Settings.BLOCK_JUMP_HEIGHT and not self.falling:
                    self.rect.y -= Settings.BLOCK_JUMP_SPEED
                elif self.startingY - self.rect.bottom >= Settings.BLOCK_JUMP_HEIGHT or self.falling:
                    self.falling = True
                    self.rect.y += Settings.BLOCK_JUMP_SPEED
                    if self.rect.bottom == self.startingY:
                        self.falling = False
                        self.bump = False
                        self.playSound = True
            if self.destroy:
                self.explode()
                Settings.SCREEN.blit(self.image_break1, self.break_rect1)
                Settings.SCREEN.blit(self.image_break2, self.break_rect2)
                Settings.SCREEN.blit(self.image_break3, self.break_rect3)
            self.gameTimer = time.get_ticks()
        Settings.SCREEN.blit(self.image, self.rect)

    def Activate(self, marioState):
        if not self.bump and not self.destroy:
            if marioState != "Mini":
                self.destroy = True
            else:
                self.bump = True