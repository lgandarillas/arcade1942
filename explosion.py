"""
Luis Gandarillas Fernandez - Arcade 1942

Run game: python3 juego.py
"""

import pyxel
import constants
from point import Point

class Explosion:
    """Explosiones de las balas al impactar con objetos"""    
    def __init__(self, x, y):
        
        if type(x) != int and type(x) != float:
            raise TypeError("x debe der un numero")
        if type(y) != int and type(y) != float:
            raise TypeError("x debe der un numero")
        else:
            # Defino las coordenadas (x, y) en las que pintar la explosion
            self.__point = Point(x, y)
        
        # Radio inicial de la explosion
        self.__radius = 1
        
        # Inicialmente la explosion esta viva
        self.__is_alive = True
        
    @property
    def is_alive(self):
        return self.__is_alive
        
    def __crecer(self):
        """La explosion crece hasta cierto radio y despues desaparece."""
        self.__radius += 1
    
    def __desaparecer(self):
        """Cuando la explosion es demasiado grande desaparece."""
        if self.__radius > 6:
            self.__is_alive = False
    
    def update(self):
        self.__crecer()
        self.__desaparecer()
            
    def draw(self):
        # Color amarillo para el exterior de la explosion
        pyxel.circ(self.__point.x, self.__point.y, 
                   self.__radius, constants.AMARILLO)
        
        # Color rojo para el interior de la explosion (radio mas pequeño)
        pyxel.circ(self.__point.x, self.__point.y, 
                   self.__radius -2 , constants.ROJO)
