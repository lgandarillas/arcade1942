"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import pyxel
import constants
from point import Point


class Bala:
    """ Clase para las balas que dispara el jugador y los enemigos."""
    def __init__(self, x, y, tipo):
        
        
        if type(x) != int and type(x) != float:
            raise TypeError("x debe der un numero")
        if type(y) != int and type(y) != float:
            raise TypeError("x debe der un numero")
        else:
            # Asignamos la posicion inicial de la bala
            self.__point = Point(x, y)
        
        # Inicialmente esta viva
        self.__is_alive = True
        
        # Asignamos el tipo de bala
        if tipo != 0 and tipo != 1:
            raise ValueError("El tipo de bala debe ser 0 o 1.")
        else:
            self.__type = tipo
        
        # Asignamos ancho, alto y velocidad si es bala tipo Player
        if self.__type == constants.BALA_PLAYER:  
            self.__width = constants.BALA[3]
            self.__height = constants.BALA[4]
            self.__speed = constants.BALA_P_SPEED
           
        # Asignamos ancho, alto y velocidad si es bala tipo Enemigo
        elif self.__type == constants.BALA_ENEMY:
            self.__width = 2
            self.__height = 2
            self.__speed = constants.BALA_E_SPEED
            
    @property
    def is_alive(self):
        return self.__is_alive
    
    @is_alive.setter  
    def is_alive(self, value):
        self.__is_alive = value
    
    @property
    def x(self):
        return self.__point.x 
    
    @property
    def y(self):
        return self.__point.y 
    
    @property 
    def w(self):
        return self.__width
    
    @property
    def h(self):
        return self.__height
    
    def __subir(self):
        """Hace que la bala suba en la pantalla restando posiciones a la 
        coordenada y."""
        self.__point.y -= self.__speed
    
    def __bajar(self):
        """Hace que la bala baje en la pantalla sumando posiciones a la
        coordenada y."""
        self.__point.y += self.__speed
    
    def __morir(self):
        # Si la bala es del jugador muere al salir por arriba
        if self.__type == constants.BALA_PLAYER and self.__point.y < 5:
            self.__is_alive = False
        
        # Si la bala es de los enemigos muere al salir por abajo
        elif self.__type == constants.BALA_ENEMY and self.__point.y > pyxel.height -5:
            self.__is_alive = False
    
    def __pintar_bala_p(self):
        """Pintar sprite de la bala disparada por Player."""
        pyxel.blt(self.__point.x, self.__point.y, constants.BANCO[0],
                  constants.BALA[1], constants.BALA[2],
                  constants.BALA[3], constants.BALA[4],
                  constants.TRANSPARENTE)
    
    def __pintar_bala_e(self):
        """Pintar sprite de la bala disparada por el enemigo."""
        pyxel.circ(self.__point.x, self.__point.y, 1 , constants.ROJO)
        
        
    def update(self):
        # Hacemos que la bala avance por cada frame
        if self.__type == constants.BALA_PLAYER:
            self.__subir()
        if self.__type == constants.BALA_ENEMY:
            self.__bajar()
        
        # Si se sale de la pantalla (margen de su altura) no esta viva
        self.__morir()
        
    def draw(self):
        # Si la bala esta viva y es del jugador, la pinto
        if self.__is_alive and self.__type == constants.BALA_PLAYER:
            self.__pintar_bala_p()
        
        # Si la bala esta viva y es del enemigo, la pinto
        elif self.__is_alive and  self.__type == constants.BALA_ENEMY:
            self.__pintar_bala_e()
