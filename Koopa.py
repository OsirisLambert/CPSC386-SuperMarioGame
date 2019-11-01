from pygame import *
from pygame.sprite import Sprite
import Settings

# a mushroom traitor that walks back and forth
class Koopa(Sprite):
    def __init__(self, xpos, ypos, direction):
        Sprite.__init__(self)
        self.speed = 2
        self.direction = direction
        self.is_alive = True
        self.hasShell = True
        self.images_left = ['87', '96']
        self.images_right = ['106', '97']
        self.images_get_up = '113'
        self.shell = '118'
        self.isMoving = False
        self.index = 0
        self.counter = 0
        self.dethklok = 0
        self.isStanding = True
        if self.direction == 1:
            self.image = Settings.ENEMY_IMAGES[str(self.images_right[self.index])] # 72, 73, 76
        else:
            self.image = Settings.ENEMY_IMAGES[str(self.images_left[self.index])]  # 72, 73, 76
        self.rect = self.image.get_rect(topleft=(xpos,ypos))
        self.hitWall = False
        self.enemies_hit = 0
        self.get_up_timer = 0
        self.get_up = False
        self.in_process = False
        self.reachedApex = False
        self.jumpamount = 20
        self.jumped_amount = 0

    def Fall(self):
        if not self.isStanding:
            self.rect.y += Settings.MARIO_FALL_SPEED

    def Explode(self):
        self.image = Settings.ENEMY_IMAGES[self.shell]
        if not self.reachedApex:
            if self.jumped_amount < self.jumpamount:
                self.rect.y -= 10
                self.jumped_amount += 10
            else:
                self.reachedApex = True
        else:
           self.rect.y += 10

    def Deshell(self):
        self.hasShell = False

    def Spin(self, direction):
        if not self.isMoving:
            self.enemies_hit = 0
            self.isMoving = True
            self.direction = direction
        else:
            self.enemies_hit = 0
            self.isMoving = False

    def getUp(self):
        if self.get_up_timer < 75:
            self.get_up_timer += 1
        else:
            self.hasShell = True
            self.get_up = True

    def update(self, lowerBound, upperBound):
        if abs(self.rect.x) >= lowerBound and self.rect.x <= upperBound:
            if self.is_alive:
                if not self.isMoving:
                    self.enemies_hit = 0
                if self.counter > 4:
                    if self.index < 1:
                        self.index += 1
                    else:
                        self.index = 0
                    if self.hasShell and not self.get_up:
                        if self.direction == 1:
                            self.image = Settings.ENEMY_IMAGES[str(self.images_right[self.index])]
                        else:
                            self.image = Settings.ENEMY_IMAGES[str(self.images_left[self.index])]
                    else:
                        if self.get_up:
                            if not self.in_process:
                                self.image = Settings.ENEMY_IMAGES[self.images_get_up]
                                self.in_process = True
                            else:
                                if self.direction == 1:
                                    self.image = Settings.ENEMY_IMAGES[str(self.images_right[self.index])]
                                    self.get_up = False
                                    self.in_process = False
                                    self.get_up_timer = 0
                                elif self.direction == -1:
                                    self.image = Settings.ENEMY_IMAGES[str(self.images_left[self.index])]
                                    self.get_up = False
                                    self.in_process = False
                                    self.get_up_timer = 0
                        else:
                            self.image = Settings.ENEMY_IMAGES[self.shell]
                    self.counter = 0
                else:
                    self.counter += 1

                self.Fall()
                if self.hitWall:
                    self.direction *= -1
                    self.hitWall = False
                if self.hasShell:
                    self.rect.x += self.speed * self.direction
                elif not self.hasShell and self.isMoving:
                    self.rect.x += self.direction * 15
                if not self.hasShell and not self.isMoving:
                    self.getUp()
                self.isStanding = False
            else:
                self.Explode()
            if self.rect.top > Settings.SCREEN_HEIGHT:
                self.kill()
        Settings.SCREEN.blit(self.image, self.rect)