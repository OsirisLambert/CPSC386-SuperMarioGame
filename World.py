import Settings
from pygame import time, transform
from pygame.sprite import Sprite

class World(Sprite):
    def __init__(self, world, level, size):
        Sprite.__init__(self)
        self.world = world
        self.level = level
        self.size = size
        self.image = Settings.BACKGROUND_IMAGES['{}'.format(str(self.world) + '-' + str(self.level))]
        self.image = transform.scale(self.image, (8000, 672))
        self.bgWidth, self.bgHeight = self.image.get_rect().size

        self.stageWidth = self.bgWidth
        self.stagePosX = 0
        self.startScrollingPosX = 600  # half screen width
        self.playerPosX = 20
        self.actualPosX = 20
        self.rel_x = 0

        self.left_bound = 50

        self.buffer = .5 * Settings.SCREEN_WIDTH
        self.relativeLeft = 0
        self.relativeRight = Settings.SCREEN_WIDTH
        self.rect = self.image.get_rect(topleft=(0, 0))
        #Settings.SCREEN.blit(self.image, self.rect)
        self.gameTimer = time.get_ticks()

'''
    def increment(self, mario, currentTime):
        #Settings.SCREEN.blit(self.image, self.rect)
        movement = self.player.velocity_right - self.player.velocity_left
        maxMovement = movement * (.85 * Settings.MARIO_RUN_SPEED)
        if mario.rect.x in range(int(self.relativeLeft + self.buffer - maxMovement) - 1,
                                  int(self.relativeLeft + self.buffer + maxMovement) + 1):
            if movement == mario.velocity_left:
                if mario.rect.x > self.relativeLeft + self.buffer:
                    mario.update(currentTime)
            elif movement == mario.velocity_right and self.relativeRight == self.size:
                mario.update(currentTime)
            elif maxMovement == 0:
                mario.update(currentTime)
            else:
                if self.relativeRight > self.size:
                    self.relativeRight = self.size
                else:
                    mario.update(currentTime, False)
                    self.relativeLeft += Settings.MARIO_RUN_SPEED * (.85 * mario.velocity_right)
                    self.relativeRight += Settings.MARIO_RUN_SPEED * (.85 * mario.velocity_right)
                return True
            return False

        return False
'''