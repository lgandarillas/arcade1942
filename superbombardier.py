"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import pyxel
import constants
import random
from point import Point
from bullet import Bullet
from enemy import Enemy

class Superbombardier(Enemy):
    
    def __init__(self):
        
        super().__init__()

        self.__point = Point(random.randint(10, 40), pyxel.height)
        self.__is_alive = True
        self.__lives = 8
        self.__type = 3
        self.__width = constants.SUPERB_UP_1[3]
        self.__height = constants.SUPERB_UP_1[4]
        self.__dir = 1 if random.random() <= 0.5 else -1
        self.__speed_x = constants.SUPERB_SPEED[0] * self.__dir
        self.__speed_y = constants.SUPERB_SPEED[1]
        self.__bala_type = constants.BULLET_ENEMY
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
    def lives(self):
        return self.__lives
    
    @lives.setter 
    def lives(self, value):
        self.__lives = value
    
    @property 
    def balas(self):
        return self.__balas
    
    @property
    def type(self):
        return self.__type
    
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
    
    def __pintar_subida(self):
        pyxel.blt(self.__point.x, self.__point.y, constants.SUPERB_UP_1[0],
            constants.SUPERB_UP_1[1] if pyxel.frame_count % 5 == 0 else constants.SUPERB_UP_2[1],
            constants.SUPERB_UP_1[2], 
            constants.SUPERB_UP_1[3], constants.SUPERB_UP_1[4],
            constants.TRANSPARENT)
    
    def __disparar(self):
        if self.__point.y % 20 == 0:
            self.__balas.append(Bullet(self.__point.x + self.__width/2 -5,
                                     self.__point.y + self.__height,
                                     self.__bala_type))
            self.__balas.append(Bullet(self.__point.x + self.__width/2 + 5,
                                     self.__point.y + self.__height,
                                     self.__bala_type))
    
    def __desaparecer(self, lst):
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
    def __mover(self):
        if pyxel.frame_count > 1200 and pyxel.frame_count < 1240:
            self.__subir()
        if pyxel.frame_count >= 1240:
            self.__subir()
            self.__derecha()
        if self.__point.y < - 2 * constants.SUPERB_UP_1[4]:
            self.__morir()
    
    def update(self):
        self.__mover()
        self.__disparar()
        self.__desaparecer(self.__balas)
     
    def draw(self):
        if self.__is_alive:
            if pyxel.frame_count > 1200:
                self.__pintar_subida()        
        for b in self.__balas:
            b.draw()