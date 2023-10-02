"""
Luis Gandarillas Fernandez - Arcade 1942

Run game: python3 juego.py
"""

import pyxel
import random
import constants
from point import Point
from bala import Bala
from enemigo import Enemigo

class Regular(Enemigo):
    """En grupos de varios aviones, sin una formacion especifica, podran 
    dispararte. Una vez que alcanzan la mitad de la pantalla vuelven por 
    la parte superior de la pantalla y desaparecen."""
    
    def __init__(self, sep):
        
        super().__init__()
        
        if type(sep) != int and type(sep) != float:
            raise TypeError("sep debe der un numero")
        else:
            # Definimos la posicion inicial del enemigo
            self.__point = Point(pyxel.rndi(40, 80), -sep)
        
        # Inicialmente esta vivo y tiene 1 vida
        self.__is_alive = True
        self.__vidas = 1
        
        # Defino el tipo de enemigo
        self.__type = 0
        
        # Definimos ancho y alto
        self.__width = constants.REGULAR_UP_1[3]
        self.__height = constants.REGULAR_UP_1[4]
        
        # Dir decide aleatoriamente si baja hacia la derecha o izquierda
        self.__dir = 1 if random.random() <= 0.5 else -1
        
        # Asignar velocidades
        self.__speed_x = constants.REGULAR_SPEED[0] * self.__dir
        self.__speed_y = constants.REGULAR_SPEED[1]
        
        # Selecciono aleatoriamente el momento del disparo
        self.__disparo = random.randint(10, pyxel.height/2)
        
        # Creo lista de balas
        self.__balas = []
        self.__bala_type = constants.BALA_ENEMY
        
        # Determinar si el avion baja o sube
        self.__bajando = True
        
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
        if self.__point.y == self.__disparo:
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
        pyxel.blt(self.__point.x, self.__point.y, 
            constants.REGULAR_DOWN_1[0],
            constants.REGULAR_DOWN_1[1] if pyxel.frame_count % 5 == 0 else constants.REGULAR_DOWN_2[1],
            constants.REGULAR_DOWN_1[2],
            constants.REGULAR_DOWN_1[3], constants.REGULAR_DOWN_1[4],
            constants.TRANSPARENTE)
    
    def __pintar_subida(self):
        """Pinta el sprite de subida."""
        pyxel.blt(self.__point.x, self.__point.y, constants.REGULAR_UP_1[0],
            constants.REGULAR_UP_1[1] if pyxel.frame_count % 5 == 0 else constants.REGULAR_UP_2[1],
            constants.REGULAR_UP_1[2],
            constants.REGULAR_UP_1[3], constants.REGULAR_UP_1[4],
            constants.TRANSPARENTE)
    
    def __mover(self):
        # En el primer tramo el enemigo baja hasta la altura de la pantalla
        if self.__point.y < 0 and self.__bajando:
            self.__bajar()
        
        # En el segundo tramo el enemigo baja torcido hacia un lado
        if self.__point.y >= 0 and self.__point.y < pyxel.height/2 and self.__bajando:
            self.__bajar()
            self.__derecha()
        
        # Cuando alcanza la profundidad 100 pixeles, deja de bajar
        if self.__point.y >= pyxel.height/2:
            self.__bajando = False
        
        # El sprite sube torcido hacia un lado
        if not self.__bajando:
            self.__subir()
            self.__izquierda()
    
    def update(self):
        # Comprobar movimientos del enemigo regular
        self.__mover()
        
        # Comprobar si el enemigo ha disparado
        self.__disparar()
        
        # Hacer que la bala desaparezca si esta muerta
        self.__desaparecer(self.__balas)


    def draw(self):
        if self.__is_alive:
            # Pintar sprite avion bajando
            if self.__bajando:
                self.__pintar_bajada()
            
            # Pintar sprite avion subiendo
            if not self.__bajando:
                self.__pintar_subida()

        for b in self.__balas:
            b.draw()
