"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import constants
from bala import Bullet

class Enemigo:
    
    def __init__(self):
        self.__is_alive = True
        self.__balas = []
        self.__bala_type = constants.BALA_ENEMY
    
    def __bajar(self):
        self.__point.y += self.__speed_y
    
    def __subir(self):
        self.__point.y -= self.__speed_y
    
    def __derecha(self):
        self.__point.x += self.__speed_x
    
    def __izquierda(self):
        self.__point.x -= self.__speed_x
    
    def __morir(self):
        self.__is_alive = False
    
    def __desaparecer(self, lst):
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l

    def __disparar(self):
        if self.__point.y % 20 == 0:
            self.__balas.append(Bala(self.__point.x + self.__width/2 -5,
                                     self.__point.y + self.__height,
                                     self.__bala_type))
            self.__balas.append(Bala(self.__point.x + self.__width/2 + 5,
                                     self.__point.y + self.__height,
                                     self.__bala_type))