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
        self.gameTimer = time.get_ticks()
