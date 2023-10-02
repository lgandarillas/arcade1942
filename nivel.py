"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import pyxel
import constants
from island import Island
from player import Player
from regular import Regular
from bombardier import Bombardier
from rojo import Rojo
from superbombardero import Superbombardero
from explosion import Explosion

class Nivel:
    
    def __init__(self):
        self.__islas = self.__createIslas()
        self.__enemigos = self.__createEnemigos()
        self.__explosiones = list()
        self.__player = Player()
        self.__nivel = constants.SCENE_NIVEL
    
    @property
    def get_scene(self):
        return self.__nivel
    
    def __createIslas(self):
        islas = []
        
        islas.append(Island(0))
        islas.append(Island(1))
        
        return islas
    
    def __createEnemigos(self):
        enemigos = []
        dif = 500
        self.__createRegulares(enemigos)
        self.__createRojos(enemigos, dif)
        self.__createBombarderos(enemigos)#, dif)
        
        enemigos.append(Superbombardero())
        return enemigos
    
    def __createRegulares(self, lst):
        for i in range(1, 21):
            sep = i * 4 * constants.REGULAR_UP_1[3]
            r = Regular(sep)
            lst.append(r)
    
    def __createRojos(self, lst, dif):
        for i in range(1, 6):
            sep = dif + i * 100
            r = Rojo(sep)
            lst.append(r)
    
    def __createBombarderos(self, lst):
        for i in range(1, 3):
            sep = i * constants.BOMB_DOWN_1[3]
            b = Bombardier(sep)
            lst.append(b)
    
    def __matar(self, lst):
        self.__matar_enemigos(lst)
        self.__matar_player(lst)
    
    def __matar_enemigos(self, lst):
        for e in lst:
            for b in self.__player.balas:
                if (e.x + e.w > b.x
                    and b.x + b.w > e.x
                    and e.y + e.h > b.y
                    and b.y + b.h > e.y):
                    
                    self.__explosiones.append(Explosion(e.x + e.w /2, e.y + e.h/2))
                    b.is_alive = False
                    
                    e.vidas -= 1
                    if e.vidas == 0:
                        e.is_alive = False                        
                        if e.type == 0:
                            self.__player.score += 100                        
                        elif e.type == 1:
                            self.__player.score += 150                        
                        elif e.type == 2:
                            self.__player.score += 500                        
                        elif e.type == 3:        
                            self.__player.score += 1000                        
                        else:
                            self.__player.score = 0
    
    def __matar_player(self, lst):
        if not self.__player.loop:
            for e in lst:
                for b in e.balas:
                    if (self.__player.x + self.__player.w > b.x
                        and b.x + b.w > self.__player.x
                        and self.__player.y + self.__player.h > b.y
                        and b.y + b.h > self.__player.y):                        
                        self.__explosiones.append(Explosion(self.__player.x + self.__player.w /2, 
                                                            self.__player.y + self.__player.h/2))
                        b.is_alive = False        
                        self.__player.vidas -= 1                        
                        if self.__player.score > self.__player.max_score:
                            self.__player.max_score = self.__player.score                        
                        self.__player.score = 0                        
                        if self.__player.vidas == 0:
                            self.__player.is_alive = False
    
    def __check_bonus(self):
        bonus = True
        for e in self.__enemigos:
            if e.type == 1:
                bonus = False
        if bonus:
            self.__player.vidas += 1
            self.__player.bonus = True

    def __chocar(self, lst):
        if not self.__player.loop:
            for e in lst:
                if (self.__player.x + self.__player.w > e.x
                    and e.x + e.w > self.__player.x
                    and self.__player.y + self.__player.h > e.y
                    and e.y + e.h > self.__player.y):                    
                    self.__explosiones.append(Explosion(self.__player.x + self.__player.w /2, 
                                                        self.__player.y + self.__player.h/2))
                    e.is_alive = False    
                    self.__player.vidas -= 1                    
                    if self.__player.score > self.__player.max_score:
                        self.__player.max_score = self.__player.score                    
                    self.__player.score = 0                    
                    if self.__player.vidas == 0:
                        self.__player.is_alive = False

    def __desaparecer(self, lst):
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
     
    def update(self):
        self.__desaparecer(self.__explosiones)
        self.__matar(self.__enemigos)
        self.__desaparecer(self.__enemigos)
        self.__chocar(self.__enemigos)
        self.__check_bonus()
        for i in self.__islas:
            i.update()
        self.__player.update() 
        if pyxel.frame_count > 1400 or self.__player.vidas == 0:
            self.__nivel = constants.SCENE_GAMEOVER
        
    def draw(self):
        for i in self.__islas:
            i.draw()
        for e in self.__enemigos:
            e.draw()
        self.__player.draw()
        for e in self.__explosiones:
            e.draw()
        s = f"SCORE: {self.__player.score:>4}"
        m = f"MAX:   {self.__player.max_score:>4}"
        v = f"VIDAS:{self.__player.vidas:>4}"
        pyxel.text(5, 4, s, 7)
        pyxel.text(5, 10, m, 7)
        pyxel.text(70, 4, v, 7)