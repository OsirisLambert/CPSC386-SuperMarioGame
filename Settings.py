from pygame import *
from os.path import abspath, dirname

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + '/fonts/'
IMAGE_PATH = BASE_PATH + '/Images/'
SOUND_PATH = BASE_PATH + '/Sounds/'
MARIO_MINI_PATH = BASE_PATH + '/Mario/mini/'
MARIO_BIG_PATH = BASE_PATH + '/Mario/big/'
MARIO_FIRE_PATH = BASE_PATH + '/Mario/fire/'
MISC_PATH = BASE_PATH + '/Misc/'
BACKGROUND_PATH = BASE_PATH + '/Level_Images/'
ITEM_PATH = BASE_PATH + '/Items/'
FONT = BASE_PATH + '/fonts/mario.ttf'
ENEMY_PATH = BASE_PATH + '/enemies/'
UNMOVE_ITEM_PATH = BASE_PATH +'/Misc-2/'
MISC3_PATH = BASE_PATH + '/Misc-3/'

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 672

SCREEN = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



MARIO_JUMP_HEIGHT_MINI_MINI = 85
MARIO_JUMP_HEIGHT_MINI_NORMAL = 120
MARIO_JUMP_HEIGHT_MINI_MAX = 200
MARIO_JUMP_HEIGHT_MINI = 200

MARIO_JUMP_HEIGHT_BIG_MINI = 85
MARIO_JUMP_HEIGHT_BIG_NORMAL = 200
MARIO_JUMP_HEIGHT_BIG_MAX = 240
MARIO_JUMP_HEIGHT_BIG = 240

MARIO_JUMP_SPEED = 12
MARIO_RUN_SPEED = 8
MARIO_MOVE_TIMER = 1
MARIO_FALL_SPEED = 12

WORLD_FALL_SPEED = 7
WORLD_LEEWAY_GAP = 10
BLOCK_JUMP_HEIGHT = 5
BLOCK_JUMP_SPEED = 1
BLOCK_JUMP_FREQUENCY = 5
BLOCK_REFRESH_RATE = 250


MUSHROOM_EMERGE_FREQUENCY = 5
MUSHROOM_OFFSET = 20
MUSHROOM_MOVE_SPEED = 5

GAME_FPS = 18

ENEMY_DEATH_NAMES = ['73']
ENEMY_DEATH_IMAGES = {name: image.load(ENEMY_PATH + '{}.png'.format(name)).convert_alpha()
                      for name in ENEMY_DEATH_NAMES}

ENEMY_IMG_NAMES = ['72', '76']
ENEMY_IMAGES = {name: transform.scale(image.load(ENEMY_PATH + '{}.png'.format(name)).convert_alpha(), (40, 40))
                for name in ENEMY_IMG_NAMES}

COIN_IMAGE_NAMES = ['49', '32', '33']
COIN_IMAGES = {name: transform.scale(image.load(MISC3_PATH + '{}.png'.format(name)).convert_alpha(), (20, 40))
                for name in COIN_IMAGE_NAMES}

ENEMY_IMG_NAMES = ['72', '76', '87', '96', '106', '97', '113', '118']
ENEMY_IMAGES = {name: transform.scale(image.load(ENEMY_PATH + '{}.png'.format(name)).convert_alpha(), (40, 40))
                for name in ENEMY_IMG_NAMES}

IMAGE_NAMES = ['0', '4', '5', '6', '7', '8', '9', '11', '12', '15', '16', '17', '18', '190', '191', '192', '193', '194']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMAGE_NAMES}

BACKGROUND_IMG_NAMES = ['1-1' , '1-2']
BACKGROUND_IMAGES = {name: image.load(BACKGROUND_PATH + '{}.png'.format(name)).convert_alpha()
                     for name in BACKGROUND_IMG_NAMES}

MARIO_MINI_IMG_NAMES = ['{}'.format(index)
                   for index in range(0, 28)]
MARIO_MINI_IMAGES = {name: transform.scale(image.load(MARIO_MINI_PATH + '{}.png'.format(name)).convert_alpha(), (40, 40))
                for name in MARIO_MINI_IMG_NAMES}

MARIO_BIG_IMG_NAMES = ['{}'.format(index)
                   for index in range(0, 28)]
MARIO_BIG_IMAGES = {name: transform.scale(image.load(MARIO_BIG_PATH + '{}.png'.format(name)).convert_alpha(), (40, 80))
                for name in MARIO_BIG_IMG_NAMES}

MARIO_FIRE_IMG_NAMES = ['{}'.format(index)
                   for index in range(0, 28)]
MARIO_FIRE_IMAGES = {name: transform.scale(image.load(MARIO_FIRE_PATH + '{}.png'.format(name)).convert_alpha(), (40, 80))
                for name in MARIO_FIRE_IMG_NAMES}

ITEMS_IMAGES = {'10', '15', '16','17', '18', '19', '20', '21', '22'}
ITEMS_IMAGES = {name: image.load(ITEM_PATH + '{}.png'.format(name)).convert_alpha()
          for name in ITEMS_IMAGES}


QUESTION_IMG_NAMES = ['{}'.format(index)
                      for index in range(78, 82)]
QUESTION_IMAGES = {name: image.load(MISC_PATH + '{}.png'.format(name)).convert_alpha()
                   for name in QUESTION_IMG_NAMES}


UNMOVE_ITEM_IMAGES = {'{}'.format(index)
                   for index in range(0, 40)}
UNMOVE_ITEM_IMAGES  = {name: image.load(UNMOVE_ITEM_PATH + '{}.png'.format(name)).convert_alpha()
          for name in UNMOVE_ITEM_IMAGES}