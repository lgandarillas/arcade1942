"""
Arcade 1942

File: constants.py
Author: Luis Gandarillas
"""

# Dimensions
SCREEN_W = 120
SCREEN_H = 160

# Colors
TRANSPARENT = 2
BLUE = 5
RED = 8
YELLOW = 10

# Image banks
BANK = [0, 1, 2]

# Values
SEP = 15

# Speed = [speed_x, speed_y]
LOCKHEED_SPEED = [5, 4]
REGULAR_SPEED = [0.5, 1.5]
RED_SPEED = [1, 1]
BOMB_SPEED = [1.2, 1.2]
SUPERB_SPEED = [0.2, 1.5]
BULLET_P_SPEED = 6
BULLET_E_SPEED = 2.5
BACKGROUND_SPEED = 1.5

# Scenes
SCENE_INTRO = 0
SCENE_LEVEL = 1
SCENE_GAMEOVER = 2

# Sprites [bank, coord_x, coord_y, width, height]
LOCKHEED_1 = [0, 4, 5, 24, 15]
LOCKHEED_2 = [0, 37, 5, 24, 25]
LOCKHEED_LOOP = [0, 67, 26, 26, 12]
REGULAR_UP_1 = [0, 6, 135, 14, 13]
REGULAR_UP_2 = [0, 25, 135, 14, 13]
REGULAR_DOWN_1 = [0, 24, 174, 15, 14]
REGULAR_DOWN_2 =  [0, 6, 174, 15, 14]
BULLET = [0, 88, 81, 1, 5]
BULLET_PLAYER = 0
BULLET_ENEMY = 1
ISLAND_1 = [2, 120, 0, 15, 39]
ISLAND_2 = [2, 145, 2, 30, 28]
INTRO = [2, 11, 31, 97, 75]
GAMEOVER = [2, 1, 133, 554, 7]
BOMB_UP_1 = [1, 68, 196, 30, 22]
BOMB_UP_2 = [1, 2, 196, 30, 22]
BOMB_DOWN_1 = [1, 35, 197, 30, 22]
BOMB_DOWN_2 = [1, 2, 228, 30, 22]
BOMB_RIGHT = [1, 137, 226, 24, 26]
SUPERB_UP_1 = [1, 0, 83, 62, 46]
SUPERB_UP_2 = [1, 65, 83, 62, 44]
RED_DER_1 =[1, 78, 2, 15, 14]
RED_DER_2 = [1, 95, 2, 15, 14]
RED_IZQ_1 = [1, 20, 42, 14, 14]
RED_IZQ_2 = [1, 36, 42, 14, 14]
RED_45 = [1, 60, 43, 12, 11]
RED_90 = [1, 2, 3, 14, 14]
RED_270 = [1, 59, 62, 14, 13]
RED_225 = [1, 116, 4, 11, 11]
RED_315 = [1, 99, 64, 11, 11]
RED_135 = [1, 78, 61, 15, 13]