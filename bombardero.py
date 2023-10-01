"""
Luis Gandarillas Fernandez - 100471965@alumnos.uc3m.es
Olivia Grima Perez - 100474858@alumnos.uc3m.es

Juego 1942
Ejecutar el juego desde juego.py
"""

import pyxel
import random
import constants
from point import Point
from bala import Bala
from enemigo import Enemigo

class Bombardero(Enemigo):
    """ Es más grande que el resto de aviones. Aparece solo, dispara varias
    veces y requiere varios impactos para ser destruido."""
    
    def __init__(self, sep):
        
        super().__init__()
        
        if type(sep) != int and type(sep) != float:
            raise TypeError("sep debe der un numero")
        else:
            # Definimos la posicion inicial del enemigo, x aleatoria entre (5, 30)
            # La posicion y depende de sep para que no se superpongan
            self.__point = Point(random.randint(5, 30), -sep)
        
        # Inicialmente esta vivo y tiene 3 vidas
        self.__is_alive = True
        self.__vidas = 3
        
        # Defino el tipo de enemigo
        self.__type = 2
        
        # Definimos ancho y alto
        self.__width = constants.BOMB_DOWN_1[3]
        self.__height = constants.BOMB_DOWN_1[4]
        
        # Asignar velocidades
        self.__speed_x = constants.BOMB_SPEED[0]
        self.__speed_y = constants.BOMB_SPEED[1]
        
        # Selecciono aleatoriamente el momento del disparo
        self.__disparo = random.randint(30, 50)
        
        # Creo lista de balas
        self.__balas = []
        self.__bala_type = constants.BALA_ENEMY
        
        # Seleccionamos el contador de frames
        self.__frames = -sep
        
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
    
    @property
    def vidas(self):
        return self.__vidas
    
    @vidas.setter 
    def vidas(self, value):
        self.__vidas = value
    
    @property 
    def balas(self):
        return self.__balas
    
    @property
    def type(self):
        return self.__type
    
    def __disparar(self):
        """Cuando los frames coinciden con el valor aleatorio del disparo
        el avion dispara."""
        if self.__point.x == self.__disparo or self.__point.y == self.__disparo:
            self.__balas.append(Bala(self.__point.x + self.__width/2,
                                     self.__point.y + self.__height,
                                     self.__bala_type))
    
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
    
    def __desaparecer(self, lst):
        """Elimina los objetos que no estan vivos de la lista."""
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
    def __morir(self):
        """El objeto muere asignando el valor booleano False a la variable."""
        self.__is_alive = False
    
    def __pintar_bajada(self):
        """Pinta el sprite de bajada."""
        pyxel.blt(self.__point.x, self.__point.y, constants.BOMB_DOWN_2[0],
            constants.BOMB_DOWN_1[1] if self.__frames % 5 == 0 else constants.BOMB_DOWN_2[1],
            constants.BOMB_DOWN_1[2] if self.__frames % 5 == 0 else constants.BOMB_DOWN_2[2], 
            constants.BOMB_DOWN_1[3], constants.BOMB_DOWN_1[4],
            constants.TRANSPARENTE)
        
    def __pintar_subida(self):
        """Pinta el sprite de subida."""
        pyxel.blt(self.__point.x, self.__point.y,constants.BOMB_UP_1[0],
            constants.BOMB_UP_1[1] if self.__frames % 5 == 0 else constants.BOMB_UP_2[1],
            constants.BOMB_UP_1[2],
            constants.BOMB_UP_1[3], constants.BOMB_UP_1[4],
            constants.TRANSPARENTE)
    
    def __pintar_derecha(self):
        """Pinta el sprite haci ala derecha."""
        pyxel.blt(self.__point.x, self.__point.y, constants.BOMB_DER[0],
            constants.BOMB_DER[1],
            constants.BOMB_DER[2],
            constants.BOMB_DER[3], constants.BOMB_DER[4],
            constants.TRANSPARENTE)
    
    def __mover(self):
        """Controla los movimientos del bombardero."""
        # En el primer intervalo de frames el avion baja
        if self.__frames > 400 and self.__frames < 500:
            self.__bajar()
        
        # En el segundo intervalo de frames el avion se desplaza hacia la derecha
        if self.__frames > 500 and self.__frames < 560:
            self.__derecha()
        
        # En el tercer intervalo de frames el avion sube
        elif self.__frames > 560:
            self.__subir()
        
        # Cuando supera el ultimo intervalo de frames muere
        elif self.__frames > 660:
            self.__morir()
    
    def update(self):
        # Aumenta el contador de frames
        self.__frames += 1
        
        # Comprobar que se mueve el bombardero
        self.__mover()
        
        # Cada frame comprueba si el bombardero ha disparado
        self.__disparar()
        
        # Cada frame compueba que balas deben desaparecer
        self.__desaparecer(self.__balas)
        
            
    def draw(self):
        if self.__is_alive:
            # Pinto sprite de bombardero bajando
            if self.__frames > 400 and self.__frames < 500:
                self.__pintar_bajada()
            
            # Pinto sprite de bombardero hacia la derecha
            if self.__frames > 500 and self.__frames < 560:
                self.__pintar_derecha()
            
            # Pinto sprite de bombardero subiendo
            elif self.__frames >560:
                self.__pintar_subida()
        
        # Itero la lista de balas y dibujo las existentes
        for b in self.__balas:
            b.draw()