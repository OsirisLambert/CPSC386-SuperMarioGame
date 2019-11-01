from pygame import *
from pygame.sprite import Sprite
from math import ceil
import Settings

class fireball(Sprite):
    def __init__(self, xpos, ypos, direction):
        Sprite.__init__(self)
        self.images = ['190', '191', '192', '193']
        self.index = 0
        self.image = transform.scale(Settings.IMAGES['190'], (10, 10))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.counter = 0
        self.last_y = self.rect.bottom
        self.rising = -1
        self.jump_height = 60
        self.direction = direction
        self.speed = 9
        self.is_alive = True
        self.breakNext = False
        self.topArc = 5

    def Bounce(self):
        if self.rising > 0:
            if self.rect.bottom <= self.last_y - self.jump_height:
                self.rising *= -1
            else:
                self.rect.y -= 1 + ceil((self.jump_height - (self.last_y - self.rect.bottom)) / 10)
        else:
            self.rect.y += 7

    def explode(self):
        if self.counter > 4:
            self.image = Settings.IMAGES['194']
            if self.breakNext:
                self.kill()
            else:
                self.breakNext = True
        else:
            self.counter += 1

    def update(self):
        if self.is_alive:
            if self.counter > 4:
                if self.index < 3:
                    self.index += 1
                else:
                    self.index = 0
                self.image = transform.scale(Settings.IMAGES[str(self.images[self.index])], (10, 10))
                self.counter = 0
            else:
                self.counter += 1

            self.Bounce()
            self.rect.x += self.speed * self.direction
            self.isStanding = False
        else:
            self.explode()
        Settings.SCREEN.blit(self.image, self.rect)