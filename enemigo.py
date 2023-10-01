"""
Luis Gandarillas Fernandez - Arcade 1942

Run game: python3 juego.py
"""

import constants
from bala import Bala

class Enemigo:
    
    def __init__(self):
        self.__is_alive = True
        self.__balas = []
        self.__bala_type = constants.BALA_ENEMY
    
    def __bajar(self):
        """Hace que el objeto baje sumando posiciones a y."""
        self.__point.y += self.__speed_y
    
    def __subir(self):
        """Hace que el objeto suba restando posiciones a y."""
        self.__point.y -= self.__speed_y
    
    def __derecha(self):
        """Desplaza el objeto a la derecha sumando posiciones a x."""
        self.__point.x += self.__speed_x
    
    def __izquierda(self):
        """Desplaza el objeto a la izquierda restando posiciones a x."""
        self.__point.x -= self.__speed_x
    
    def __morir(self):
        """El objeto muere asignando el valor booleano False a la variable."""
        self.__is_alive = False
    
    def __desaparecer(self, lst):
        """Elimina los objetos que no estan vivos de la lista."""
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l

    def __disparar(self):
        """Cuando los frames coinciden con el valor aleatorio del disparo
        el avion dispara."""
        if self.__point.y % 20 == 0:
            self.__balas.append(Bala(self.__point.x + self.__width/2 -5,
                                     self.__point.y + self.__height,
                                     self.__bala_type))
            self.__balas.append(Bala(self.__point.x + self.__width/2 + 5,
                                     self.__point.y + self.__height,
                                     self.__bala_type))
