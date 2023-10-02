"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import pyxel
import constants
from point import Point

class Explosion:
    
    def __init__(self, x, y):
        
        if type(x) != int and type(x) != float:
            raise TypeError("x must be a number")
        if type(y) != int and type(y) != float:
            raise TypeError("x must be a number")
        else:
            self.__point = Point(x, y)        
        self.__radius = 1
        self.__is_alive = True
        
    @property
    def is_alive(self):
        return self.__is_alive
        
    def __crecer(self):
        self.__radius += 1
    
    def __desaparecer(self):
        if self.__radius > 6:
            self.__is_alive = False
    
    def update(self):
        self.__crecer()
        self.__desaparecer()
            
    def draw(self):
        pyxel.circ(self.__point.x, self.__point.y, 
                   self.__radius, constants.AMARILLO)        
        pyxel.circ(self.__point.x, self.__point.y, 
                   self.__radius -2 , constants.ROJO)
