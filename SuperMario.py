import Mario
import Settings
import World
import Text
import WORLD_MAP
import fireball
from pygame import *

class SuperMario:
    def __init__(self):
        mixer.pre_init(44100, -16, 1, 4096)
        mixer.init()
        init()
        self.clock = time.Clock()
        self.screen = Settings.SCREEN
        self.should_exit = False
        self.gameTimer = time.get_ticks()
        self.gameTime = 400

    def initGame(self):

        mixer.init()
        self.SOUNDS = {}
        for sound_name in ['smb_breakblock', 'smb_bump', 'smb_coin', 'smb_fireball',
                           'smb_jump-small', 'smb_jump-super', 'smb_kick', 'smb_mariodie',
                           'smb_pipe', 'smb_powerup', 'smb_powerup_appears', 'smb_stomp',
                           'smb_warning', 'smb_gameover']:
            self.SOUNDS[sound_name] = mixer.Sound(Settings.SOUND_PATH + '{}.wav'.format(sound_name))
            self.SOUNDS[sound_name].set_volume(0.2)
        mixer.music.load('music.ogg')
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)
        self.player_xpos = 700
        self.player_ypos = 480
        self.gameTimer_tock = 400
        self.tock_index = 0

        self.warningPlayed = False

        self.coinAmount = 0

        self.player = Mario.Mario(self.player_xpos, self.player_ypos)
        self.world = World.World(1, 1, 1400)

        self.enemies = sprite.Group()
        self.goombas = sprite.Group()
        self.koopas = sprite.Group()

        self.playerGroup = sprite.Group()
        self.textGroup = sprite.Group()

        self.blocks = sprite.Group()
        self.groundBlocks = sprite.Group()
        self.QuestionBlocks = sprite.Group()
        self.normalBlocks = sprite.Group()
        self.normalPipes = sprite.Group()
        self.groundUpBlocks = sprite.Group()
        self.move_steps = sprite.Group()
        self.long_pipes = sprite.Group()
        self.flags = sprite.Group()
        self.castles = sprite.Group()

        self.instruction_board = sprite.Group()
        self.brushes = sprite.Group()
        self.clouds = sprite.Group()
        self.mountains = sprite.Group()
        self.unmove_items = sprite.Group()

        self.fireballs = sprite.Group()
        self.fireball_amount = 5
        self.fireball_timer = 0

        self.itemGroup = sprite.Group()
        self.mushrooms = sprite.Group()
        self.flowers = sprite.Group()
        self.coins = sprite.Group()

        self.score = 0
        self.lives = 3

        self.spaceDown = False
        self.newLifeHandle = False

        self.steadyText = sprite.Group()

        self.playerGroup.add(self.player)
        WORLD_MAP.world1_1(game)

    def handleDeath(self, currentTime):
        mixer.music.pause()
        self.SOUNDS['smb_mariodie'].play()
        self.player.isAlive = False
        while not self.player.update(currentTime):
            display.update()
            self.screen.blit(self.world.image, (self.world.rel_x - self.world.bgWidth, 0))
            if self.world.rel_x < 1200:  # screen width
                self.screen.blit(self.world.image, (self.world.rel_x, 0))
            for item in self.unmove_items:
                self.screen.blit(item.image, item.rect)
            for block in self.blocks:
                self.screen.blit(block.image, block.rect)
            for item in self.itemGroup:
                self.screen.blit(item.image, item.rect)
            for enemy in self.enemies:
                self.screen.blit(enemy.image, enemy.rect)
            for fireball in self.fireballs:
                self.screen.blit(fireball.image, fireball.rect)
        self.Kill_All(self.player_xpos, self.player_ypos, '1-1')
        mixer.music.set_pos(0)
        mixer.music.unpause()


    def Kill_All(self, player_xpos, player_ypos, level):
        self.lives -= 1
        for block in self.blocks:
            block.kill()
        for item in self.itemGroup:
            item.kill()
        for enemy in self.enemies:
            enemy.kill()
        for text in self.textGroup:
            text.kill()
        for player in self.playerGroup:
            player.kill()
        for fireball in self.fireballs:
            fireball.kill()
        for item in self.unmove_items:
            item.kill()
        self.player = Mario.Mario(player_xpos, player_ypos)
        self.playerGroup.add(self.player)
        self.world.kill()
        self.world = World.World(1, 1, 1400)
        if level == '1-1':
            WORLD_MAP.world1_1(game)
        self.newLifeHandle = False
        self.gameTimer_tock = 400

    def checkInput(self, currenttime):
        if currenttime - self.gameTimer > Settings.GAME_FPS:
            self.keys = key.get_pressed()
            for e in event.get():
                if e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        self.spaceDown = True
                if e.type == KEYUP:
                    if e.key == K_SPACE:
                        self.spaceDown = False

            if self.spaceDown:
                if not self.player.isJumping and self.player.isStanding:
                    if self.player.jump_height == 0 and not self.player.isJumping and self.player.jumpCounter == 0:
                        if self.player.state != 'Mini':
                            self.SOUNDS['smb_jump-super'].play()
                        else:
                            self.SOUNDS['smb_jump-small'].play()
                        self.player.isJumping = True
                        self.player.jump_height = 1
                    self.player.jumpCounter += 1
                else:
                    if self.player.jumpCounter > 2 and self.player.jump_height == 1:
                        self.player.jump_height = 2
                    if self.player.jumpCounter > 7 and self.player.jump_height == 2:
                        self.player.jump_height = 3
                    self.player.jumpCounter += 1
            else:
                self.player.jumpCounter = 0

            if self.keys[K_DOWN] and self.player.state != 'Mini':
                self.player.isCrouching = True
                self.player.idle = True
                self.player.runLeft = False
                self.player.runRight = False
            else:
                self.player.isCrouching = False
                if self.keys[K_LCTRL] or self.keys[K_RCTRL]:
                    if self.player.state == 'Fire' and self.fireball_timer == 0 and self.fireball_amount > 0:
                        self.SOUNDS['smb_fireball'].play()
                        self.fireball_amount -= 1
                        self.player.shootFire = True
                        self.fireballs.add(fireball.fireball(self.player.rect.x, self.player.rect.y,
                                                             self.player.direction))
                        self.fireball_timer = 8
                    else:
                        if self.fireball_timer > 0:
                            self.fireball_timer -= 1

                if self.keys[K_LEFT] and not self.keys[K_RIGHT]:
                    self.player.idle = False
                    self.player.runLeft = True
                    self.player.runRight = False
                elif self.keys[K_RIGHT] and not self.keys[K_LEFT]:
                    self.player.idle = False
                    self.player.runRight = True
                    self.player.runLeft = False
                else:
                    self.player.idle = True
                    self.player.runLeft = False
                    self.player.runLeft = False

    def check_camera(self):
        #-------move mario--------------------
        velocity = self.player.velocity
        self.world.playerPosX += (Settings.MARIO_RUN_SPEED * (-1 if velocity < 0 else 1 if velocity > 0 else 0))
        self.world.actualPosX += (Settings.MARIO_RUN_SPEED * (-1 if velocity < 0 else 1 if velocity > 0 else 0))
        self.left_bound = self.world.actualPosX % 600
        if self.world.playerPosX > self.world.stageWidth:
            self.world.playerPosX = self.world.stageWidth
        if self.player.rect.x < self.world.left_bound - 40: # half width of mario
            self.world.playerPosX = self.world.left_bound
        if self.world.playerPosX < self.world.startScrollingPosX:
            self.player.rect.right = self.world.playerPosX
        elif self.world.playerPosX > self.world.stageWidth - self.world.startScrollingPosX:
            self.player.rect.right = self.world.playerPosX - self.world.stageWidth + 1200 # screen width
        else:
            self.player.rect.right = self.world.startScrollingPosX
            if self.world.actualPosX > 600:
                if self.world.playerPosX >= 600:
                    self.world.playerPosX = 599
                    for block in self.blocks:
                        if block not in self.normalBlocks:
                            block.rect.x -= Settings.MARIO_RUN_SPEED
                    for block in self.normalBlocks:
                        block.rect.x -= Settings.MARIO_RUN_SPEED
                        block.break_rect1.x -= Settings.MARIO_RUN_SPEED
                        block.break_rect2.x -= Settings.MARIO_RUN_SPEED
                        block.break_rect3.x -= Settings.MARIO_RUN_SPEED
                    for item in self.itemGroup:
                        item.rect.x -= Settings.MARIO_RUN_SPEED
                    for enemy in self.enemies:
                        enemy.rect.x -= Settings.MARIO_RUN_SPEED
                    for item in self.unmove_items:
                        item.rect.x -= Settings.MARIO_RUN_SPEED
                    for fireball in self.fireballs:
                        fireball.rect.x -= 6
            if self.player.direction == 1:
                self.world.stagePosX -= velocity
            elif self.player.direction == -1:
                self.world.playerPosX = self.world.startScrollingPosX
        self.world.rel_x = self.world.stagePosX % self.world.bgWidth

    def update(self, currentTime):
        if currentTime - self.gameTimer > Settings.GAME_FPS:
            self.screen.blit(self.world.image, (self.world.rel_x - self.world.bgWidth, 0))
            if self.world.rel_x < 1200:  # screen width
                self.screen.blit(self.world.image, (self.world.rel_x, 0))

            self.unmove_items.update(currentTime)
            self.player.update(currentTime)
            self.itemGroup.update(currentTime)
            self.fireballs.update()
            self.blocks.update(currentTime)
            self.textGroup.update(currentTime)
            self.enemies.update(self.left_bound - 500, self.left_bound + Settings.SCREEN_WIDTH)
            self.gameTimer = time.get_ticks()

    def check_Terrain(self, mario, collision):
        boot = False
        if mario.rect.bottom in (collision.rect.top + index for index in range(0, Settings.MARIO_FALL_SPEED + 3)):
            if mario.rect.right not in range(collision.rect.left - 15, collision.rect.left + 7) \
                    and mario.rect.left not in range(collision.rect.right - 7, collision.rect.right + 15):
                if not mario.isReachedApex:
                    if mario.rect.bottom < mario.lastGroundYPos and mario.isJumping:
                        mario.isJumping = False
                        self.player.jump_height = 0
                    mario.lastGroundYPos = collision.rect.top + 1
                    mario.rect.bottom = collision.rect.top + 1
                    mario.isStanding = True
                if mario.isReachedApex:
                    mario.lastGroundYPos = collision.rect.top + 1
                    mario.rect.bottom = collision.rect.top + 1
                    mario.isStanding = True
                    mario.isReachedApex = False
                    mario.isJumping = False
                    self.player.jump_height = 0
        if mario.rect.colliderect(collision.rect):
            if mario.rect.top in range(collision.rect.bottom - 20, collision.rect.bottom):
                if mario.rect.right not in range(collision.rect.left - 1, collision.rect.left + 3) \
                        and mario.rect.left not in range(collision.rect.right - 3, collision.rect.right + 1) \
                        and not mario.isReachedApex:
                    boot = True
                    mario.isJumping = False
                    mario.jump_height = 0
                    if collision in self.QuestionBlocks:
                        if not collision.gotHit:
                            if collision.contents == 'Coin':
                                self.SOUNDS['smb_coin'].play()
                                self.score += 200
                                self.coinAmount += 1
                            collision.Activate(mario.state, collision.rect.x, collision.rect.y,
                                               self.itemGroup, self.mushrooms, self.flowers, self.coins,
                                               self.SOUNDS['smb_powerup_appears'])
                    if collision in self.normalBlocks:
                        if mario.state != 'Mini':
                            self.SOUNDS['smb_breakblock'].play()
                        else:
                            self.SOUNDS['smb_bump'].play()
                        collision.Activate(mario.state)
        if mario.rect.left in (collision.rect.right + 3 - index for index in range(0, 41)) and not boot:
            if mario.rect.top not \
                    in (collision.rect.bottom - index for index in range(0, Settings.MARIO_JUMP_SPEED - 1)):
                if mario.rect.bottom > collision.rect.top + 1:
                    mario.rect.left = collision.rect.right + 2
                    mario.velocity = 0
                    mario.runLeft = False
        if mario.rect.right in (collision.rect.left - 3 + index for index in range(0, 41)):
            if mario.rect.top not \
                    in (collision.rect.bottom - index for index in range(0, Settings.MARIO_JUMP_SPEED - 1)) and not boot:
                if mario.rect.bottom > collision.rect.top + 1:
                    mario.rect.right = collision.rect.left - 2
                    mario.velocity = 0
                    mario.runRight = False


    def checkCollisions(self, currentTime):
        if not self.player.movementLock:
            collision = sprite.groupcollide(self.playerGroup, self.blocks, False, False)
            grow_collision = sprite.groupcollide(self.playerGroup, self.itemGroup, False, False)
            enemy_collision = sprite.groupcollide(self.playerGroup, self.enemies, False, False)
        item_collison = sprite.groupcollide(self.itemGroup, self.blocks, False, False)
        fireball_world_collision = sprite.groupcollide(self.fireballs, self.blocks, False, False)
        fireball_enemy_collision = sprite.groupcollide(self.fireballs, self.enemies, False, False)
        enemy_world_collison = sprite.groupcollide(self.enemies, self.blocks, False, False)
        enemy_enemy_collison = sprite.groupcollide(self.goombas, self.koopas, False, False)
        if not self.player.movementLock:
            if collision:
                for mario, block in collision.items():
                    for collision in block:
                        self.check_Terrain(mario, collision)
            else:
                self.player.isStanding = False
            if grow_collision:
                for mario, items in grow_collision.items():
                    for item in items:
                        if mario.rect.bottom in range(item.rect.top - 2, item.rect.bottom + 2):
                            if mario.state == 'Mini' and item in self.mushrooms and not item.isEmerging:
                                self.SOUNDS['smb_powerup'].play()
                                mario.changeMarioState('Mushroom')
                                item.kill()
                            if mario.state == 'Big' and item in self.flowers and not item.isEmerging:
                                self.SOUNDS['smb_powerup'].play()
                                mario.changeMarioState('Flower')
                                item.kill()
                            if mario.state == 'Fire' and item in self.flowers and not item.isEmerging:
                                self.SOUNDS['smb_coin'].play()
                                text = Text.Text(Settings.FONT, 20, '1000', (255, 255, 255), item.rect.x,
                                                 item.rect.y - (45 if self.player.state == 'Mini' else 85))
                                self.textGroup.add(text)
                                self.score += 1000
                                item.kill()
                            if mario.state == 'Big' and item in self.mushrooms and not item.isEmerging:
                                self.SOUNDS['smb_coin'].play()
                                text = Text.Text(Settings.FONT, 20, '1000', (255, 255, 255), item.rect.x,
                                                 item.rect.y - (45 if self.player.state == 'Mini' else 85))
                                self.textGroup.add(text)
                                self.score += 1000
                                item.kill()
            if enemy_collision:
                for mario, baddies in enemy_collision.items():
                    for enemy in baddies:
                        if enemy.is_alive:
                            if mario.rect.bottom < enemy.rect.top + 10:
                                if enemy in self.koopas:
                                    if enemy.hasShell:
                                        self.SOUNDS['smb_stomp'].play()
                                        mario.isJumping = True
                                        mario.jump_height = 1
                                        mario.isReachedApex = False
                                        enemy.hasShell = False
                                    else:
                                        self.SOUNDS['smb_kick'].play()
                                        enemy.Spin(mario.direction)
                                        mario.isJumping = True
                                        mario.jump_height = 1
                                        mario.isReachedApex = False
                                if enemy in self.goombas:
                                    self.SOUNDS['smb_stomp'].play()
                                    mario.isJumping = True
                                    mario.jump_height = 1
                                    mario.isReachedApex = False
                                    enemy.is_alive = False
                                    text = Text.Text(Settings.FONT, 20, '200', (255, 255, 255), enemy.rect.x,
                                                     enemy.rect.y - (45 if self.player.state == 'Mini' else 85))
                                    self.textGroup.add(text)
                                    self.score += 200
                            else:
                                if enemy in self.koopas:
                                    if not enemy.hasShell and not enemy.isMoving:
                                        self.SOUNDS['smb_kick'].play()
                                        enemy.Spin(mario.direction)
                                    else:
                                        if mario.state != 'Mini':
                                            mario.changeMarioState('Damage')
                                        else:
                                            self.handleDeath(currentTime)
                                else:
                                    if mario.state != 'Mini':
                                        self.SOUNDS['smb_pipe'].play()
                                        mario.changeMarioState('Damage')
                                    else:
                                        self.SOUNDS['smb_mariodie'].play()
                                        self.handleDeath(currentTime)
        if enemy_enemy_collison:
            for goomba, koopas in enemy_enemy_collison.items():
                for koopa in koopas:
                    if goomba.is_alive and koopa.is_alive:
                        if koopa.isMoving:
                            self.SOUNDS['smb_kick'].play()
                            goomba.fireBallDeath = True
                            goomba.is_alive = False
                            score = 200 + (0 if koopa.enemies_hit == 0 else 100 if koopa.enemies_hit == 1
                                           else 300 if koopa.enemies_hit == 2 else 600 if koopa.enemies_hit == 3
                                           else 800)
                            text = Text.Text(Settings.FONT, 20, str(score), (255, 255, 255), goomba.rect.x,
                                             goomba.rect.y - 5)
                            self.textGroup.add(text)
                            self.score += score
                        else:
                            koopa.hitWall = True
                            goomba.hitWall = True
        if item_collison:
            for item, block in item_collison.items():
                for collision in block:
                    if item in self.mushrooms:
                        if item.rect.bottom in range(collision.rect.top-6, collision.rect.top + 13):
                            item.rect.bottom = collision.rect.top + 1
                            item.isStanding = True
                        if item.rect.left in (collision.rect.right + 3 - index for index in range(0, 41)) or \
                                item.rect.right in (collision.rect.left - 3 + index for index in range(0, 41)):
                            if item.rect.bottom not in range(collision.rect.top - 2, collision.rect.top + 2):
                                item.hitWall = True
        if fireball_world_collision:
            for fireball, terrain in fireball_world_collision.items():
                for block in terrain:
                    if fireball.rect.top <= block.rect.bottom + 3 and fireball.rect.top >= block.rect.top:
                        fireball.is_alive = False
                        self.fireball_amount += 1
                    if fireball.rect.bottom in range(block.rect.top - 6, block.rect.top + 13):
                        fireball.rect.bottom = block.rect.top + 1
                        fireball.rising = 1
                        fireball.last_y = block.rect.top - 1
                    if fireball.rect.left in (block.rect.right + 3 - index for index in range(0, 41)) or \
                            fireball.rect.right in (block.rect.left - 3 + index for index in range(0, 41)):
                        if fireball.rect.bottom not in range(block.rect.top - 2, block.rect.top + 2):
                            fireball.is_alive = False
                            self.fireball_amount += 1
        if fireball_enemy_collision:
            for fireball, baddies in fireball_enemy_collision.items():
                for enemy in baddies:
                    if fireball.is_alive:
                        if enemy in self.koopas:
                            if enemy.is_alive:
                                self.SOUNDS['smb_kick'].play()
                                enemy.is_alive = False
                                text = Text.Text(Settings.FONT, 20, '200', (255, 255, 255), enemy.rect.x, enemy.rect.y - 5)
                                self.textGroup.add(text)
                                self.score += 200
                                fireball.is_alive = False
                        if enemy in self.goombas:
                            if enemy.is_alive:
                                self.SOUNDS['smb_kick'].play()
                                enemy.is_alive = False
                                enemy.fireBallDeath = True
                                text = Text.Text(Settings.FONT, 20, '200', (255, 255, 255), enemy.rect.x, enemy.rect.y - 5)
                                self.textGroup.add(text)
                                self.score += 200
                                fireball.is_alive = False

        if enemy_world_collison:
            for enemy, terrain in enemy_world_collison.items():
                for block in terrain:
                    if enemy.rect.bottom in range(block.rect.top - 6, block.rect.top + 13):
                        if enemy in self.koopas:
                            if enemy.is_alive:
                                enemy.rect.bottom = block.rect.top + 1
                                enemy.isStanding = True
                        if enemy in self.goombas:
                            if enemy.is_alive:
                                enemy.rect.bottom = block.rect.top + 1
                                enemy.isStanding = True
                    if enemy.rect.left in (block.rect.right + 3 - index for index in range(0, 41)) or \
                            enemy.rect.right in (block.rect.left - 3 + index for index in range(0, 41)):
                        if enemy.rect.bottom not in range(block.rect.top - 2, block.rect.top + 2):
                            enemy.hitWall = True


    def draw_UI(self):
        for text in self.steadyText:
            text.kill()
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, 'SCORE', (255, 255, 255),
                               200, 5))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, str(self.score), (255, 255, 255),
                               200, 25))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, 'TIME', (255, 255, 255),
                                            400, 5))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, str(self.gameTimer_tock), (255, 255, 255),
                                            400, 25))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, 'WORLD', (255, 255, 255),
                                            600, 5))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, '1-1', (255, 255, 255),
                                            620, 25))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, 'COINS', (255, 255, 255),
                                            800, 5))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, str(self.coinAmount), (255, 255, 255),
                                            827, 25))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, 'LIVES', (255, 255, 255),
                                            1000, 5))
        self.steadyText.add(Text.steadyText(Settings.FONT, 20, str(self.lives), (255, 255, 255),
                                            1027, 25))
        self.steadyText.update()

    def mainLoop(self):
        self.initGame()
        while True:
            if self.tock_index > 4:
                self.gameTimer_tock -= 1
                self.tock_index = 0
                if self.gameTimer_tock < 100:
                    if not self.warningPlayed:
                        self.SOUNDS['smb_warning'].play()
                        self.warningPlayed = True
            else:
                self.tock_index += 1
            currentTicks = time.get_ticks()
            if self.lives < 0:
                self.SOUNDS['smb_gameover'].play()
                self.lives = 3
                self.score = 0
            if self.gameTimer_tock <= 0:
                self.SOUNDS['smb_mariodie'].play()
                self.handleDeath(currentTicks)
            if not self.player.movementLock:
                self.checkInput(currentTicks)
                self.check_camera()
            self.checkCollisions(currentTicks)
            self.update(currentTicks)
            self.draw_UI()
            display.update()
            self.clock.tick(30)

if __name__ == '__main__':
    game = SuperMario()
    game.mainLoop()