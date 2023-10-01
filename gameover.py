"""
Luis Gandarillas Fernandez - 100471965@alumnos.uc3m.es
Olivia Grima Perez - 100474858@alumnos.uc3m.es

Juego 1942
Ejecutar el juego desde juego.py
"""

import pyxel
import constants

class Gameover():

    def __init__(self):
        self.__gameover = constants.SCENE_GAMEOVER
    
    @property
    def get_scene(self):
        """Devuelve la escena en la que nos encontramos."""
        return self.__gameover
    
    def draw(self):
        """Pinto el logo del final y el texto para salir del juego."""
        pyxel.blt(33, 76, constants.GAMEOVER[0], constants.GAMEOVER[1],
                  constants.GAMEOVER[2], constants.GAMEOVER[3],
                  constants.GAMEOVER[4], constants.TRANSPARENTE)
        pyxel.text(25, 126, "- PRESS Q TO QUIT -", 11)