"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import pyxel
import constants

from point import Point


class Island:
    
    def __init__(self, tipo):
        if tipo != 0 and tipo != 1:
            raise ValueError("The island type must be 0 or 1.")
        else:
            self.__tipo = tipo

        if self.__tipo == 0:
            self.__point = Point(0, -constants.ISLAND_1[4])
        elif self.__tipo == 1:
            self.__point = Point(60, -150)
        
        self.__movimiento = constants.FONDO_SPEED

    @property
    def x(self):
        return self.__point.x
    
    @property 
    def y(self):
        return self.__point.y
    
    def __bajar(self):
        self.__point.y += self.__movimiento
    
    def __reaparecer(self):
        if self.__point.y > pyxel.height + constants.ISLAND_1[4]:
            self.__point.y = -constants.ISLAND_1[4]
    
    def update(self):
        self.__bajar()
        self.__reaparecer()
    
    def draw(self):
        if self.__tipo == 0:
            pyxel.blt(self.__point.x, self.__point.y, constants.ISLAND_1[0],
                      constants.ISLAND_1[1], constants.ISLAND_1[2],
                      constants.ISLAND_1[3], constants.ISLAND_1[4],
                      constants.TRANSPARENT)
            
        if self.__tipo == 1:
            pyxel.blt(self.__point.x, self.__point.y, constants.ISLAND_2[0],
                constants.ISLAND_2[1], constants.ISLAND_2[2],
                constants.ISLAND_2[3], constants.ISLAND_2[4],
                constants.TRANSPARENT)