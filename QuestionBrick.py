import Mushroom
import flower
import CoinGather
from pygame import *
from pygame.sprite import Sprite
import Settings

class QuestionBrick(Sprite):
    def __init__(self, xpos, ypos, contains='Coin', hidden=False):
        Sprite.__init__(self)
        self.hidden = hidden
        self.index = 78
        if not self.hidden:
            self.image = transform.scale(Settings.QUESTION_IMAGES['78'], (40, 40))
        self.rect = transform.scale(Settings.QUESTION_IMAGES['78'], (40, 40)).get_rect(topleft=(xpos,ypos))
        self.contents = 'star' if contains == 0 else 'Coin' if contains == 'Coin' else 'other'
        self.gotHit = False
        self.startingY = self.rect.bottom
        self.gameTimer = time.get_ticks()
        self.falling = False
        self.trigger = True
        self.emerged = False
        '''  UNCOMMENT WHEN WE HAVE SOUNDS
        self.soundPlayed = False
        self.coinSound = mixer.Sound(Settings.SOUND_PATH + 'coin.wav')
        self.mushroomSound = mixer.Sound(Settings.SOUND_PATH + 'mushroom.wav')
        self.flowerSound = mixer.Sound(Settings.SOUND_PATH + 'flower.wav')
        self.starSound = mixer.Sound(Settings.SOUND_PATH + 'star.wav')
        '''

    def update(self, currentTime):
        if currentTime - self.gameTimer > Settings.BLOCK_REFRESH_RATE:
            if not self.gotHit and self.trigger:
                if self.index > 81:
                    self.index = 78
                self.image = Settings.QUESTION_IMAGES[str(self.index)]
                self.image = transform.scale(self.image, (40, 40))
                self.index += 1
                self.gameTimer = time.get_ticks()
        if currentTime - self.gameTimer > Settings.BLOCK_JUMP_FREQUENCY:
            if self.gotHit and self.trigger:
                """
                if not self.soundPlayed:
                    if self.contains == 'coin':
                        self.coinSound.play()
                    if self.contains == 'mushroom':
                        self.coinMushroom.play()
                    if self.contains == 'flower':
                        self.flowerSound.play()
                    if self.contains == 'star':
                        self.starSound.play()   
                    self.soundPlayed = True             
                """
                if self.startingY - self.rect.bottom < Settings.BLOCK_JUMP_HEIGHT and not self.falling:
                    self.rect.y -= Settings.BLOCK_JUMP_SPEED
                else:
                    self.falling = True
                    self.rect.y += Settings.BLOCK_JUMP_SPEED
                    if self.rect.bottom == self.startingY:
                        self.trigger = False
                self.gameTimer = time.get_ticks()
        Settings.SCREEN.blit(self.image, self.rect)

    def Activate(self, marioState, xpos, ypos, itemGroup, mushrooms, flowers, coins, sound):
        if not self.gotHit:
            if self.contents != 'Star' and self.contents != 'Coin':
                sound.play()
                if marioState == 'Mini':
                    mushrooms.add(Mushroom.Mushroom(xpos, ypos))
                    itemGroup.add(mushrooms)
                elif marioState == 'Big' or marioState == 'Fire':
                    flowers.add(flower.Flower(xpos, ypos))
                    itemGroup.add(flowers)
            else:
                if self.contents == 'Coin':
                    coins.add(CoinGather.CoinGet(xpos + 10, ypos - 30))
                    itemGroup.add(coins)
            self.gotHit = True
            self.image = transform.scale(image.load(Settings.IMAGE_PATH + '4.png').convert_alpha(), (40, 40))


