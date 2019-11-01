import random
from pygame import *
from pygame.sprite import Sprite
import Settings

# a mushroom traitor that walks back and forth
class Goomba(Sprite):
    def __init__(self, xpos, ypos, direction):
        Sprite.__init__(self)
        self.speed = 2
        self.direction = direction
        self.is_alive = True
        self.images = ['72', '76']
        self.index = 0
        self.counter = 0
        self.dethklok = 0
        self.isStanding = True
        self.image = Settings.ENEMY_IMAGES[str(self.images[self.index])] # 72, 73, 76
        self.rect = self.image.get_rect(topleft=(xpos,ypos))
        self.hitWall = False
        self.fireBallDeath = False
        self.reachedApex = False
        self.jumpamount = 20
        self.jumped_amount = 0

    def Fall(self):
        if not self.isStanding:
            self.rect.y += Settings.MARIO_FALL_SPEED


    def Die_Horrifically(self):
        self.image = Settings.ENEMY_IMAGES['72']
        if not self.reachedApex:
            if self.jumped_amount < self.jumpamount:
                self.rect.y -= 10
                self.jumped_amount += 10
            else:
                self.reachedApex = True
        else:
           self.rect.y += 10

    def explode(self):
        self.image = transform.scale(Settings.ENEMY_DEATH_IMAGES['73'], (40, 10))
        pos = self.rect.bottomleft
        self.rect = self.image.get_rect(bottomleft=pos)
        if self.dethklok > 40:
            self.kill()
        else:
            self.dethklok += 1

    def update(self, lowerBound, upperBound):
        if abs(self.rect.x) >= lowerBound and self.rect.x <= upperBound:
            if self.is_alive:
                if self.counter > 4:
                    if self.index < 1:
                        self.index += 1
                    else:
                        self.index = 0
                    self.image = Settings.ENEMY_IMAGES[str(self.images[self.index])]
                    self.counter = 0
                else:
                    self.counter += 1

                self.Fall()
                if self.hitWall:
                    self.direction *= -1
                    self.hitWall = False
                self.rect.x += self.speed * self.direction
                self.isStanding = False
            else:
                if self.fireBallDeath:
                    self.Die_Horrifically()
                else:
                    self.explode()
        Settings.SCREEN.blit(self.image, self.rect)