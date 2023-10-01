"""
Luis Gandarillas Fernandez - Arcade 1942

Run game: python3 juego.py
"""

import pyxel
import constants

class Intro():
    
    def __init__(self):
        # Asigna un valor para detectar que estamos en la introduccion
        self.__intro = constants.SCENE_INTRO
        
    @property
    def get_scene(self):
        """Devuelve la escena en la que nos encontramos."""
        return self.__intro
    
    def update(self):
        """Comprueba si hemos pulsado ENTER o si han pasado los 150 frames
        asignados para la introduccion."""
        if self.__intro == constants.SCENE_INTRO:
            if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.frame_count > 150:
                self.__intro = constants.SCENE_NIVEL

    def draw(self):
        """Pinto el logo del juego y el texto de inicio."""
        pyxel.blt(12, 42, constants.INTRO[0], constants.INTRO[1],
                  constants.INTRO[2], constants.INTRO[3],
                  constants.INTRO[4], constants.TRANSPARENTE)
        pyxel.text(31, 126, "- PRESS ENTER -", 11)
