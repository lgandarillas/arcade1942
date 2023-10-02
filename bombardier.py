"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import pyxel
import random
import constants
from point import Point
from bullet import Bullet
from enemy import Enemy

class Bombardier(Enemy):
    
    def __init__(self, sep):
        
        super().__init__()
        
        if type(sep) != int and type(sep) != float:
            raise TypeError("sep must be a number")
        else:
            self.__point = Point(random.randint(5, 30), -sep)
        
        self.__is_alive = True
        self.__lives = 3
        self.__type = 2
        self.__width = constants.BOMB_DOWN_1[3]
        self.__height = constants.BOMB_DOWN_1[4]
        self.__speed_x = constants.BOMB_SPEED[0]
        self.__speed_y = constants.BOMB_SPEED[1]        
        self.__shot = random.randint(30, 50)
        self.__balas = []
        self.__bala_type = constants.BULLET_ENEMY        
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
    
    def __disparar(self):
        if self.__point.x == self.__shot or self.__point.y == self.__shot:
            self.__balas.append(Bullet(self.__point.x + self.__width/2,
                                     self.__point.y + self.__height,
                                     self.__bala_type))
    
    def __bajar(self):
        self.__point.y += self.__speed_y
    
    def __subir(self):
        self.__point.y -= self.__speed_y
    
    def __derecha(self):
        self.__point.x += self.__speed_x
    
    def __izquierda(self):
        self.__point.x -= self.__speed_x
    
    def __desaparecer(self, lst):
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
    def __morir(self):
        self.__is_alive = False
    
    def __pintar_bajada(self):
        pyxel.blt(self.__point.x, self.__point.y, constants.BOMB_DOWN_2[0],
            constants.BOMB_DOWN_1[1] if self.__frames % 5 == 0 else constants.BOMB_DOWN_2[1],
            constants.BOMB_DOWN_1[2] if self.__frames % 5 == 0 else constants.BOMB_DOWN_2[2], 
            constants.BOMB_DOWN_1[3], constants.BOMB_DOWN_1[4],
            constants.TRANSPARENT)
        
    def __pintar_subida(self):
        pyxel.blt(self.__point.x, self.__point.y,constants.BOMB_UP_1[0],
            constants.BOMB_UP_1[1] if self.__frames % 5 == 0 else constants.BOMB_UP_2[1],
            constants.BOMB_UP_1[2],
            constants.BOMB_UP_1[3], constants.BOMB_UP_1[4],
            constants.TRANSPARENT)
    
    def __pintar_derecha(self):
        pyxel.blt(self.__point.x, self.__point.y, constants.BOMB_DER[0],
            constants.BOMB_DER[1],
            constants.BOMB_DER[2],
            constants.BOMB_DER[3], constants.BOMB_DER[4],
            constants.TRANSPARENT)
    
    def __mover(self):
        if self.__frames > 400 and self.__frames < 500:
            self.__bajar()
        if self.__frames > 500 and self.__frames < 560:
            self.__derecha()
        elif self.__frames > 560:
            self.__subir()
        elif self.__frames > 660:
            self.__morir()
    
    def update(self):
        self.__frames += 1
        self.__mover()
        self.__disparar()
        self.__desaparecer(self.__balas)
        
            
    def draw(self):
        if self.__is_alive:
            if self.__frames > 400 and self.__frames < 500:
                self.__pintar_bajada()
            if self.__frames > 500 and self.__frames < 560:
                self.__pintar_derecha()
            elif self.__frames >560:
                self.__pintar_subida()
        for b in self.__balas:
            b.draw()
