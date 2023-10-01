"""
Luis Gandarillas Fernandez - 100471965@alumnos.uc3m.es
Olivia Grima Perez - 100474858@alumnos.uc3m.es

Juego 1942
Ejecutar el juego desde juego.py

Constantes a utilizar en el juego.
"""

# Dimensiones
SCREEN_W = 120
SCREEN_H = 160


# Colores
TRANSPARENTE = 2
AZUL = 5
ROJO = 8
AMARILLO = 10


# Bancos imagenes
BANCO = [0, 1, 2]


# Valores
SEP = 15


# Velocidad = [speed_x, speed_y]
LOCKHEED_SPEED = [5, 4]

REGULAR_SPEED = [0.5, 1.5]

ROJO_SPEED = [1, 1]

BOMB_SPEED = [1.2, 1.2]

SUPERB_SPEED = [0.2, 1.5]

BALA_P_SPEED = 6
BALA_E_SPEED = 2.5

FONDO_SPEED = 1.5


# Escenas
SCENE_INTRO = 0
SCENE_NIVEL = 1
SCENE_GAMEOVER = 2


# Sprites [banco, coord_x, coord_y, width, height]
LOCKHEED_1 = [0, 4, 5, 24, 15]
LOCKHEED_2 = [0, 37, 5, 24, 25]
LOCKHEED_LOOP = [0, 67, 26, 26, 12]

REGULAR_UP_1 = [0, 6, 135, 14, 13]
REGULAR_UP_2 = [0, 25, 135, 14, 13]
REGULAR_DOWN_1 = [0, 24, 174, 15, 14]
REGULAR_DOWN_2 =  [0, 6, 174, 15, 14]

BALA = [0, 88, 81, 1, 5]
BALA_PLAYER = 0
BALA_ENEMY = 1

ISLA_1 = [2, 120, 0, 15, 39]
ISLA_2 = [2, 145, 2, 30, 28]

INTRO = [2, 11, 31, 97, 75]
GAMEOVER = [2, 1, 133, 554, 7]

BOMB_UP_1 = [1, 68, 196, 30, 22]
BOMB_UP_2 = [1, 2, 196, 30, 22]
BOMB_DOWN_1 = [1, 35, 197, 30, 22]
BOMB_DOWN_2 = [1, 2, 228, 30, 22]
BOMB_DER = [1, 137, 226, 24, 26]

SUPERB_UP_1 = [1, 0, 83, 62, 46]
SUPERB_UP_2 = [1, 65, 83, 62, 44]

ROJO_DER_1 =[1, 78, 2, 15, 14]
ROJO_DER_2 = [1, 95, 2, 15, 14]
ROJO_IZQ_1 = [1, 20, 42, 14, 14]
ROJO_IZQ_2 = [1, 36, 42, 14, 14]
ROJO_45 = [1, 60, 43, 12, 11]
ROJO_90 = [1, 2, 3, 14, 14]
ROJO_270 = [1, 59, 62, 14, 13]
ROJO_225 = [1, 116, 4, 11, 11]
ROJO_315 = [1, 99, 64, 11, 11]
ROJO_135 = [1, 78, 61, 15, 13]