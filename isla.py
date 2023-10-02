"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import pyxel
import constants

from point import Point


class Isla:
    
    def __init__(self, tipo):
        
        # Asigno el tipo de isla
        if tipo != 0 and tipo != 1:
            raise ValueError("El tipo de isla debe ser 0 o 1.")
        else:
            self.__tipo = tipo
        
        # Creo una isla en la posicion (x, y)
        if self.__tipo == 0:
            self.__point = Point(0, -constants.ISLA_1[4])
        elif self.__tipo == 1:
            self.__point = Point(60, -150)
        
        # La isla se desplaza desde el punto de referencia visual del avion
        self.__movimiento = constants.FONDO_SPEED

    @property
    def x(self):
        return self.__point.x
    
    @property 
    def y(self):
        return self.__point.y
    
    def __bajar(self):
        """ Hace que la isla se despace (movimiento de la tierra) para que
        desde el sistema de referencia del jugador de sensacion de movimiento."""
        self.__point.y += self.__movimiento
    
    def __reaparecer(self):
        """ Cuando la isla sale por abajo de la pantalla reaparece arriba."""
        if self.__point.y > pyxel.height + constants.ISLA_1[4]:
            self.__point.y = -constants.ISLA_1[4]
    
    def update(self):
        self.__bajar()
        self.__reaparecer()
    
    def draw(self):
        if self.__tipo == 0:
            pyxel.blt(self.__point.x, self.__point.y, constants.ISLA_1[0],
                      constants.ISLA_1[1], constants.ISLA_1[2],
                      constants.ISLA_1[3], constants.ISLA_1[4],
                      constants.TRANSPARENTE)
            
        if self.__tipo == 1:
            pyxel.blt(self.__point.x, self.__point.y, constants.ISLA_2[0],
                constants.ISLA_2[1], constants.ISLA_2[2],
                constants.ISLA_2[3], constants.ISLA_2[4],
                constants.TRANSPARENTE)
