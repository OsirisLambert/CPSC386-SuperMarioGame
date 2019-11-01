import Settings
from pygame import *
from pygame.sprite import Sprite

class Instruction_board(Sprite):
    def __init__(self, xpos, ypos):
        Sprite.__init__(self)
        self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['35'], (600, 400))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)

class Cloud(Sprite):
    def __init__(self, xpos, ypos, type='small'):
        Sprite.__init__(self)
        self.type = type
        if self.type == 'small':
            self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['25'], (60, 60))
        else:
            self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['26'], (120, 60))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)


class Brush(Sprite):
    def __init__(self, xpos, ypos, type='small'):
        Sprite.__init__(self)
        self.type = type
        if self.type == 'small':
            self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['34'], (55, 45))
        else:
            self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['33'], (110, 45))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)


class Mountain(Sprite):
    def __init__(self, xpos, ypos, type='small'):
        Sprite.__init__(self)
        self.type = type
        if self.type == 'small':
            self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['32'], (65, 50))
        else:
            self.image = transform.scale(Settings.UNMOVE_ITEM_IMAGES['31'], (120, 100))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, currentTime):
        Settings.SCREEN.blit(self.image, self.rect)

