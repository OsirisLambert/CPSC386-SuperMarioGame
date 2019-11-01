from pygame import *
from pygame.sprite import Sprite
import Settings

class Mario(Sprite):
    def __init__(self, xpos, ypos, state='Mini'):
        Sprite.__init__(self)
        self.state = state
        self.image = Settings.MARIO_FIRE_IMAGES['14'] if self.state == "Fire" else Settings.MARIO_BIG_IMAGES['14'] \
            if self.state == 'Big' else Settings.MARIO_MINI_IMAGES['14']
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.index = 0
        self.lastGroundYPos = ypos
        self.direction = 1
        self.isCrouching = False
        self.isJumping = True
        self.fireball_timer = 0
        self.jump_height = 0
        self.jumpCounter = 0
        self.isReachedApex = True
        self.isStanding = False
        self.canGoLeft = True
        self.canGoRight = True
        self.velocity_y = 0
        self.velocity = 0
        self.runRight = False
        self.runLeft = False
        self.idle = True
        self.isAlive = True
        self.timer = time.get_ticks()
        self.moveTimer = time.get_ticks()
        self.moveTime = 0
        self.oldDirection = -self.direction
        self.imageTimer = 0
        self.tickImage = 4
        self.movementLock = False
        self.changeState = 'Unset'
        self.changeFrame = 0
        self.leftSprites = ['10', '11', '12', '11']
        self.rightSprites = ['15', '16', '17', '16']
        self.isDead = False
        self.startDie_y = None
        self.die_comic_jump_height = 200
        self.dethklok = 0
        self.deth_apex = False
        self.start_deth = True

    #this function is REDICULOUSLY HUGE. it's my shame i didnt do it in loops
    def changeMarioState(self, direction = 'loop'):
        self.movementLock = True
        if self.changeState == 'Unset':
            self.imageTimer = 0
            self.changeFrame = 0
            if self.state == 'Mini' and direction == 'Mushroom':
                self.changeState = 'Big'
            elif self.state == 'Big' and direction == 'Flower':
                self.changeState = 'Fire'
            elif self.state == 'Fire' and direction == 'Damage':
                self.changeState = 'Big'
            elif self.state == 'Big' and direction == 'Damage':
                self.changeState = 'Mini'
        else:
            if self.imageTimer >= self.tickImage:
                if self.state == 'Mini' and self.changeState == 'Big':
                    if self.changeFrame == 0:
                        self.image = transform.scale(Settings.MARIO_MINI_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 60))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 1:
                        self.image = transform.scale(Settings.MARIO_MINI_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 40))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 2:
                        self.image = transform.scale(Settings.MARIO_MINI_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 60))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 3:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 60))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 4:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 5:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 60))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 6:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    else:
                        self.state = 'Big'
                        self.changeState = 'Unset'
                        self.movementLock = False
                        self.changeFrame = 0
                    self.imageTimer = 0
                elif self.state == 'Big' and self.changeState == 'Fire':
                    if self.changeFrame == 0:
                        self.image = transform.scale(Settings.MARIO_FIRE_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 1:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 2:
                        self.image = transform.scale(Settings.MARIO_FIRE_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 3:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 4:
                        self.image = transform.scale(Settings.MARIO_FIRE_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    else:
                        self.state = 'Fire'
                        self.changeState = 'Unset'
                        self.movementLock = False
                        self.changeFrame = 0
                    self.imageTimer = 0
                elif self.state == 'Fire' and self.changeState == 'Big':
                    if self.changeFrame == 0:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 1:
                        self.image = transform.scale(Settings.MARIO_FIRE_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 2:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 3:
                        self.image = transform.scale(Settings.MARIO_FIRE_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 4:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    else:
                        self.state = 'Big'
                        self.changeState = 'Unset'
                        self.movementLock = False
                        self.changeFrame = 0
                    self.imageTimer = 0
                elif self.state == 'Big' and self.changeState == 'Mini':
                    if self.changeFrame == 0:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 60))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 1:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 80))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 2:
                        self.image = transform.scale(Settings.MARIO_BIG_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 60))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 3:
                        self.image = transform.scale(Settings.MARIO_MINI_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 60))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 4:
                        self.image = transform.scale(Settings.MARIO_MINI_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 40))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 5:
                        self.image = transform.scale(Settings.MARIO_MINI_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 60))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    elif self.changeFrame == 6:
                        self.image = transform.scale(Settings.MARIO_MINI_IMAGES[str(14 if self.direction == 1
                                                                                    else 13)], (40, 40))
                        self.changeFrame += 1
                        pos = self.rect.bottomleft
                        self.rect = self.image.get_rect(bottomleft=pos)
                    else:
                        self.state = 'Mini'
                        self.changeState = 'Unset'
                        self.movementLock = False
                        self.changeFrame = 0
                    self.imageTimer = 0
            else:
                self.imageTimer += 1

    def move(self):
        if self.velocity < 0:
            self.direction = -1
            if self.isJumping:
                self.image = Settings.MARIO_FIRE_IMAGES['7'] if self.state == 'Fire' else \
                    Settings.MARIO_BIG_IMAGES['7'] if self.state == 'Big' else \
                        Settings.MARIO_MINI_IMAGES['8']
            elif self.direction != self.oldDirection:
                self.imageTimer = self.tickImage - 1
                self.index = 0
                self.oldDirection = self.direction
            elif self.direction == self.oldDirection:
                if self.imageTimer >= self.tickImage:
                    if self.index < 3:
                        self.index += 1
                    else:
                        self.index = 0
                    self.image = Settings.MARIO_FIRE_IMAGES[self.leftSprites[self.index]] if \
                        self.state == 'Fire' else Settings.MARIO_BIG_IMAGES[self.leftSprites[self.index]] \
                        if self.state == 'Big' else Settings.MARIO_MINI_IMAGES[self.leftSprites[self.index]]
                    pos = self.rect.bottomleft
                    self.rect = self.image.get_rect(bottomleft=pos)
                    self.imageTimer = 0
                else:
                    self.imageTimer += 1
            self.rect.x -= Settings.MARIO_RUN_SPEED
        elif self.velocity > 0:
            self.direction = 1
            if self.isJumping:
                self.image = Settings.MARIO_FIRE_IMAGES['20'] if self.state == 'Fire' else \
                    Settings.MARIO_BIG_IMAGES['20'] if self.state == 'Big' else \
                        Settings.MARIO_MINI_IMAGES['19']
            elif self.direction != self.oldDirection:
                self.imageTimer = self.tickImage - 1
                self.index = 0
                self.oldDirection = self.direction
            elif self.direction == self.oldDirection:
                if self.imageTimer >= self.tickImage:
                    if self.index < 3:
                        self.index += 1
                    else:
                        self.index = 0
                    self.image = Settings.MARIO_FIRE_IMAGES[self.rightSprites[self.index]] if self.state == 'Fire' else\
                        Settings.MARIO_BIG_IMAGES[self.rightSprites[self.index]] if self.state == 'Big' else \
                            Settings.MARIO_MINI_IMAGES[self.rightSprites[self.index]]
                    pos = self.rect.bottomleft
                    self.rect = self.image.get_rect(bottomleft=pos)
                    self.imageTimer = 0
                else:
                    self.imageTimer += 1
            self.rect.x += Settings.MARIO_RUN_SPEED
        else:
            if self.direction == 1:
                if self.isJumping:
                    self.image = Settings.MARIO_FIRE_IMAGES['20'] if self.state == 'Fire' else \
                        Settings.MARIO_BIG_IMAGES['20'] if self.state == 'Big' else \
                            Settings.MARIO_MINI_IMAGES['19']
                else:
                    self.image = Settings.MARIO_FIRE_IMAGES['14'] if self.state == 'Fire' else \
                        Settings.MARIO_BIG_IMAGES['14'] if self.state == 'Big' else \
                        Settings.MARIO_MINI_IMAGES['14']
                    pos = self.rect.bottomleft
                    self.rect = self.image.get_rect(bottomleft=pos)
                    self.rect.x -= Settings.MARIO_RUN_SPEED
            else:
                if self.isJumping:
                    self.image = Settings.MARIO_FIRE_IMAGES['7'] if self.state == 'Fire' else \
                        Settings.MARIO_BIG_IMAGES['7'] if self.state == 'Big' else \
                            Settings.MARIO_MINI_IMAGES['8']
                else:
                    self.image = Settings.MARIO_FIRE_IMAGES['13'] if self.state == 'Fire' else \
                        Settings.MARIO_BIG_IMAGES['13'] if self.state == 'Big' else \
                            Settings.MARIO_MINI_IMAGES['13']
                    pos = self.rect.bottomleft
                    self.rect = self.image.get_rect(bottomleft=pos)
                    self.rect.x -= Settings.MARIO_RUN_SPEED

    def Run(self):
        if self.runRight:
            if self.velocity >= 0:
                if self.velocity < 7:
                    self.velocity += 1
                if self.velocity > 7:
                    self.velocity = 7
            elif self.velocity < 0:
                if self.velocity <= -2:
                    self.velocity = 0
                else:
                    self.velocity += 2
            self.runRight = False
        if self.runLeft:
            if self.velocity <= 0:
                if self.velocity > -7:
                    self.velocity -= 1
                if self.velocity < -7:
                    self.velocity = -7
            if self.velocity > 0:
                if self.velocity <= 2:
                    self.velocity = 0
                else:
                    self.velocity -= 2
            self.runLeft = False
        if self.idle:
            if self.velocity > 0:
                self.velocity -= 1
            if self.velocity < 0:
                self.velocity += 1
            self.idle = False
        if not self.isCrouching:
            self.move()

    def Jump(self):
        if self.isJumping:
            if self.lastGroundYPos - self.rect.bottom < Settings.MARIO_JUMP_HEIGHT_BIG \
                    and not self.isReachedApex and self.state != 'Mini':
                self.rect.y -= Settings.MARIO_JUMP_SPEED
                if self.lastGroundYPos - self.rect.bottom >= Settings.MARIO_JUMP_HEIGHT_BIG_MAX \
                        and self.jump_height == 3:
                    self.isReachedApex = True
                if self.lastGroundYPos - self.rect.bottom >= Settings.MARIO_JUMP_HEIGHT_BIG_NORMAL \
                        and self.jump_height == 2:
                    self.isReachedApex = True
                if self.lastGroundYPos - self.rect.bottom >= Settings.MARIO_JUMP_HEIGHT_BIG_MINI \
                        and self.jump_height == 1:
                    self.isReachedApex = True
            elif self.lastGroundYPos - self.rect.bottom < Settings.MARIO_JUMP_HEIGHT_MINI \
                    and not self.isReachedApex and self.state == 'Mini':
                self.rect.y -= Settings.MARIO_JUMP_SPEED
                if self.lastGroundYPos - self.rect.bottom >= Settings.MARIO_JUMP_HEIGHT_MINI_MAX \
                        and self.jump_height == 3:
                    self.isReachedApex = True
                if self.lastGroundYPos - self.rect.bottom >= Settings.MARIO_JUMP_HEIGHT_MINI_NORMAL \
                        and self.jump_height == 2:
                    self.isReachedApex = True
                if self.lastGroundYPos - self.rect.bottom >= Settings.MARIO_JUMP_HEIGHT_MINI_MINI \
                        and self.jump_height == 1:
                    self.isReachedApex = True
            else:
                self.rect.y += Settings.MARIO_FALL_SPEED

    def Fall(self):
        if not self.isJumping and not self.isStanding:
            self.rect.y += Settings.MARIO_FALL_SPEED

    def die_slowly(self):
        self.movementLock = True
        self.image = Settings.MARIO_MINI_IMAGES['0']
        if self.start_deth:
            self.startDie_y = self.rect.bottom
            self.dethklok = -6
            self.start_deth = False
        if self.dethklok >= 7:
            if not self.deth_apex and self.rect.bottom > self.startDie_y - self.die_comic_jump_height:
                self.rect.y -= 10
                self.dethklok = 0
            elif self.deth_apex or self.rect.bottom <= self.startDie_y - self.die_comic_jump_height:
                self.deth_apex = True
                self.rect.y += 10
                self.dethklok = 0
            if self.rect.top >= Settings.SCREEN_HEIGHT + 10:
                waiter = time.get_ticks()
                end = waiter + 1800
                while waiter < end:
                    waiter = time.get_ticks()
                return True
        else:
            self.dethklok += 1

    def Crouch(self):
        if self.isCrouching:
            if self.direction == 1:
                self.image = Settings.MARIO_FIRE_IMAGES['18'] if self.state == 'Fire' else \
                    Settings.MARIO_BIG_IMAGES['18']
                pos = self.rect.bottomleft
                self.rect = self.image.get_rect(bottomleft=pos)
            else:
                self.image = Settings.MARIO_FIRE_IMAGES['9'] if self.state == 'Fire' else \
                    Settings.MARIO_BIG_IMAGES['9']
                pos = self.rect.bottomleft
                self.rect = self.image.get_rect(bottomleft=pos)


    def update(self, currentTime, doesMove = True):
        if self.isAlive:
            if not self.movementLock:
                if self.fireball_timer > 0:
                    self.fireball_timer -= 1
                self.Jump()
                self.Run()
                self.Fall()
                self.Crouch()
            else:
                self.changeMarioState()
        else:
            if currentTime - self.moveTimer > self.moveTime:
                self.moveTimer += self.moveTime
                if self.die_slowly():
                    return True
        Settings.SCREEN.blit(self.image, self.rect)






