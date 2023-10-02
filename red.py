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

class Red(Enemy):
    
    def __init__(self, sep):
        
        super().__init__()
        
        if type(sep) != int and type(sep) != float:
            raise TypeError("sep must be a number")
        else:
            self.__point = Point(-sep, 50)
        
        self.__is_alive = True
        self.__lives = 1
        self.__type = 1
        self.__width = constants.RED_DER_1[3]
        self.__height = constants.RED_DER_1[4]
        self.__speed = constants.RED_SPEED[0]
        self.__disparo = random.randint(-20, 50)
        self.__balas = []
        self.__vueltas = 2 if random.random() <= 0.5 else 3
        self.__vueltas_dadas = 0
        self.__recto = True
        self.__cuarto1 = False
        self.__cuarto23 = False
        self.__cuarto4 = False
        

    def __disparar(self):
        if self.__disparo == self.__point.x:
            self.__balas.append(Bullet(self.__point.x + constants.BOMB_DOWN_1[3]/2,
                                     self.__point.y + constants.BOMB_DOWN_1[4],
                                     constants.BULLET_ENEMY))
    
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
    
    def __derecha(self):
        self.__point.x += self.__speed
    
    def __izquierda(self):
        self.__point.x -= self.__speed
        
    def __mover_recta_i(self):
        if self.__point.x < 60 and self.__recto:
            self.__derecha()
            if self.__point.x == 60:
                self.__recto = False
                self.__cuarto1 = True
    
    def __mover_recta_f(self):
        if self.__recto and self.__point.x >= 60:
            self.__derecha()
        if self.__point.x > 120:
            self.__morir()
     
    def __mover_cuarto1(self):
        if self.__point.x >= 60 and self.__cuarto1:
            x = self.__point.x + self.__speed
            self.__derecha()
            self.__point.y = 70 - (-x**2 + 120*x - 3200)**(1/2)
            if self.__point.x == 80:
                self.__cuarto1 = False
                self.__cuarto23 = True
    
    def __mover_cuarto23(self):
        if self.__point.x <= 80 and self.__cuarto23:
            x = self.__point.x - self.__speed
            self.__izquierda()
            self.__point.y = 70 + (-x**2 + 120*x - 3200)**(1/2)
            if self.__point.x == 40:
                self.__cuarto23 = False
                self.__cuarto4 = True
            
    def __mover_cuarto4(self):
        if self.__point.x >= 40 and self.__point.x < 60 and self.__cuarto4:
            x = self.__point.x + self.__speed
            self.__derecha()
            self.__point.y = 70 - (-x**2 + 120*x - 3200)**(1/2)            
            if self.__point.x == 60:
                self.__cuarto4 = False
                self.__vueltas_dadas += 1
                if self.__vueltas_dadas == self.__vueltas:
                    self.__recto = True
                else:
                    self.__cuarto1 = True
    
        
    def __desaparecer(self, lst):
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
    
    def __morir(self):
        self.__is_alive = False


    def __pintar_recto(self):
        pyxel.blt(self.__point.x, self.__point.y, constants.RED_DER_1[0],
            constants.RED_DER_1[1] if pyxel.frame_count % 5 == 0 else\
                constants.RED_DER_2[1],
            constants.RED_DER_1[2],
            constants.RED_DER_1[3], constants.RED_DER_1[4],
            constants.TRANSPARENT)
    
    
    def __pintar_cuarto1(self):
        pyxel.blt(self.__point.x, self.__point.y, constants.RED_315[0],
            constants.RED_315[1],
            constants.RED_315[2],
            constants.RED_315[3], constants.RED_315[4],
            constants.TRANSPARENT)  
        
        
    def __pintar_cuarto23(self):
        if self.__point.x >= 60:
            pyxel.blt(self.__point.x, self.__point.y, constants.RED_225[0],
                constants.RED_225[1],
                constants.RED_225[2],
                constants.RED_225[3], constants.RED_225[4],
                constants.TRANSPARENT)
        if self.__point.x < 60:
            pyxel.blt(self.__point.x, self.__point.y, constants.RED_135[0],
                constants.RED_135[1],
                constants.RED_135[2],
                constants.RED_135[3], constants.RED_135[4],
                constants.TRANSPARENT) 
    
    
    def __pintar_cuarto4(self):
        pyxel.blt(self.__point.x, self.__point.y, constants.RED_45[0],
            constants.RED_45[1],
            constants.RED_45[2],
            constants.RED_45[3], constants.RED_45[4],
            constants.TRANSPARENT) 
    
    def __mover(self):
        self.__mover_recta_i()
        self.__mover_cuarto1()
        self.__mover_cuarto23()
        self.__mover_cuarto4()
        self.__mover_recta_f()
        
    def update(self):
        self.__mover()
        self.__disparar()
        self.__desaparecer(self.__balas)
        

    def draw(self):
        if self.__is_alive:
            for b in self.__balas:
                b.draw()
        
        if self.__recto:
            self.__pintar_recto()
        
        if self.__cuarto1:
            self.__pintar_cuarto1()
        
        if self.__cuarto23:
            self.__pintar_cuarto23()
        
        if self.__cuarto4:
            self.__pintar_cuarto4()