"""
Luis Gandarillas Fernandez - 100471965@alumnos.uc3m.es
Olivia Grima Perez - 100474858@alumnos.uc3m.es

Juego 1942
Ejecutar el juego desde juego.py
"""

import pyxel
import constants
from intro import Intro
from nivel import Nivel
from gameover import Gameover


class Game():
    """ En esta clase implementamos el juego 1942"""
    
    def __init__(self):
        # Elementos API pyxel
        pyxel.init(constants.SCREEN_W, constants.SCREEN_H, title="1942") 
        
        # Cargo imagenes
        pyxel.load("sprites1942.pyxres")
        
        # Musica en bucle durante todo el juego
        pyxel.play(0, 0, loop = True)
        
        # Creo la intro
        self.__intro = Intro()
        
        # Creo el nivel
        self.__nivel = Nivel()
        
        # Creo gameover
        self.__gameover = Gameover()

        # Inicialmente asignamos la escena de la intro
        self.__scene = constants.SCENE_INTRO

        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)   
    
    def __check_scene(self):
        # Escena con la introduccion (portada)
        if self.__scene == constants.SCENE_INTRO:
            self.__intro.update()
            if self.__intro.get_scene == constants.SCENE_NIVEL:
                self.__scene = constants.SCENE_NIVEL
        
        # Escena con el juego
        elif self.__scene == constants.SCENE_NIVEL:
            self.__nivel.update()
            if self.__nivel.get_scene == constants.SCENE_GAMEOVER:
                self.__scene = constants.SCENE_GAMEOVER
        
    def __draw_scene(self):
        if self.__scene == constants.SCENE_INTRO:
            self.__intro.draw()
        
        elif self.__scene == constants.SCENE_NIVEL:
            self.__nivel.draw()
        
        elif self.__scene == constants.SCENE_GAMEOVER:
            self.__gameover.draw()
        
    def update(self):
        # si pulsas 'q' se cierra el juego
        if pyxel.btnp(pyxel.KEY_Q): 
            pyxel.quit()
        
        # Comprobar la escena en la que se encuentra el juego
        self.__check_scene()
        
    
    def draw(self):
        # Borrar pantalla en cada frame con el fondo azul
        pyxel.cls(constants.AZUL)
        
        # Dibujar los elementos de la escena en la que nos encontremos
        self.__draw_scene()
        
Game()