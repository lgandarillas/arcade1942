"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import pyxel
import constants

class Intro():
    
    def __init__(self):
        self.__intro = constants.SCENE_INTRO
        
    @property
    def get_scene(self):
        return self.__intro
    
    def update(self):
        if self.__intro == constants.SCENE_INTRO:
            if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.frame_count > 150:
                self.__intro = constants.SCENE_NIVEL

    def draw(self):
        pyxel.blt(12, 42, constants.INTRO[0], constants.INTRO[1],
                  constants.INTRO[2], constants.INTRO[3],
                  constants.INTRO[4], constants.TRANSPARENTE)
        pyxel.text(31, 126, "- PRESS ENTER -", 11)