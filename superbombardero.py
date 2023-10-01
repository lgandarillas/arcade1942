"""
Luis Gandarillas Fernandez - 100471965@alumnos.uc3m.es
Olivia Grima Perez - 100474858@alumnos.uc3m.es

Juego 1942
Ejecutar el juego desde juego.py
"""

import pyxel
import constants
import random
from point import Point
from bala import Bala
from enemigo import Enemigo

class Superbombardero(Enemigo):
    """ Es el avión más grande, requiere muchos impactos para ser destruido y 
    tiene la capacidad de disparar varios proyectiles simultáneamente."""
    
    def __init__(self):
        
        super().__init__()
        
        # Definimos la posicion inicial del enemigo, x aleatoria entre (10, 40)
        self.__point = Point(random.randint(10, 40), pyxel.height)
        
        # Inicialmente esta vivo y tiene 8 vidas
        self.__is_alive = True
        self.__vidas = 8
        
        # Defino el tipo de enemigo
        self.__type = 3

        # Definimos ancho y alto
        self.__width = constants.SUPERB_UP_1[3]
        self.__height = constants.SUPERB_UP_1[4]
        
        # Dir decide aleatoriamente si sube hacia la derecha o izquierda
        self.__dir = 1 if random.random() <= 0.5 else -1
        
        # Asignar velocidades
        self.__speed_x = constants.SUPERB_SPEED[0] * self.__dir
        self.__speed_y = constants.SUPERB_SPEED[1]
        
        
        # Selecciono aleatoriamente el momento del disparo
        self.__bala_type = constants.BALA_ENEMY
        
        # Lista donde almacenaremos las balas
        self.__balas = []
       
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
    
    def __pintar_subida(self):
        """Pinta el sprite de subida."""
        pyxel.blt(self.__point.x, self.__point.y, constants.SUPERB_UP_1[0],
            constants.SUPERB_UP_1[1] if pyxel.frame_count % 5 == 0 else constants.SUPERB_UP_2[1],
            constants.SUPERB_UP_1[2], 
            constants.SUPERB_UP_1[3], constants.SUPERB_UP_1[4],
            constants.TRANSPARENTE)
    
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
    
    def __desaparecer(self, lst):
        """Elimina los objetos que no estan vivos de la lista."""
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
    def __mover(self):
        """Comprueba los movimientos del superbombardero."""
        # Sube recto
        if pyxel.frame_count > 1200 and pyxel.frame_count < 1240:
            self.__subir()
            
        # Sube torcido
        if pyxel.frame_count >= 1240:
            self.__subir()
            self.__derecha()
        
        # Si se sale de la pantalla no esta vivo
        if self.__point.y < - 2 * constants.SUPERB_UP_1[4]:
            self.__morir()
    
    def update(self):
        
        # Comprueba los movimientos del superbombardero
        self.__mover()
            
        # Cada frame comprueba si el bombardero ha disparado
        self.__disparar()
        
        # Cada frame compueba que balas deben desaparecer
        self.__desaparecer(self.__balas)
     
    def draw(self):
        if self.__is_alive:
            # Desde los 1200 frames comienza a pintar el objeto.
            if pyxel.frame_count > 1200:
                self.__pintar_subida()
        
        # Itero la lista de balas y dibujo las existentes
        for b in self.__balas:
            b.draw()