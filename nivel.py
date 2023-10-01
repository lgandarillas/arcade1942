"""
Luis Gandarillas Fernandez - Arcade 1942

Run game: python3 juego.py
"""

import pyxel
import constants
from isla import Isla
from player import Player
from regular import Regular
from bombardero import Bombardero
from rojo import Rojo
from superbombardero import Superbombardero
from explosion import Explosion

class Nivel:
    
    def __init__(self):
        # Creo islas
        self.__islas = self.__createIslas()

        # Creo una lista para almacenar los enemigos
        self.__enemigos = self.__createEnemigos()
        
        # Lista de explosiones
        self.__explosiones = list()
        
        # Creo jugador (lockhead)
        self.__player = Player()
        
        # Variable Nivel
        self.__nivel = constants.SCENE_NIVEL
    
    @property
    def get_scene(self):
        return self.__nivel
    
    def __createIslas(self):
        islas = []
        
        islas.append(Isla(0))
        islas.append(Isla(1))
        
        return islas
    
    def __createEnemigos(self):
        # Crear Regulares
        enemigos = []
        dif = 500
        self.__createRegulares(enemigos)

        # Crear Rojos
        self.__createRojos(enemigos, dif)
  
        # Crear Bombarderos
        self.__createBombarderos(enemigos)#, dif)

        # Crear Superbombardero
        enemigos.append(Superbombardero())
        
        return enemigos
    
    def __createRegulares(self, lst):
        """Crea y añade a la lista de enemigos 20 aviones regulares."""
        for i in range(1, 21):
            sep = i * 4 * constants.REGULAR_UP_1[3]
            r = Regular(sep)
            lst.append(r)
    
    def __createRojos(self, lst, dif):
        """Crea y añade a la lista de enemigos 5 aviones rojos."""
        for i in range(1, 6):
            sep = dif + i * 100
            r = Rojo(sep)
            lst.append(r)
    
    def __createBombarderos(self, lst):
        """Crea y añade a la lista de enemigos 2 bombarderos."""
        for i in range(1, 3):
            sep = i * constants.BOMB_DOWN_1[3]
            b = Bombardero(sep)
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
                    
                    # Mato la bala y creo una explosion
                    self.__explosiones.append(Explosion(e.x + e.w /2, e.y + e.h/2))
                    b.is_alive = False
                    
                    # Le resto una vida al objeto
                    e.vidas -= 1
                    if e.vidas == 0:
                        e.is_alive = False
                        
                        # Impacta con enemigo regular (tipo 0)
                        if e.type == 0:
                            self.__player.score += 100
                        
                        # Impacta con enemigo rojo (tipo 1)
                        elif e.type == 1:
                            self.__player.score += 150
                        
                        # Impacta con bombardero (tipo 2)
                        elif e.type == 2:
                            self.__player.score += 500
                        
                        # Impacta con superbombardero (tipo 3)
                        elif e.type == 3:        
                            self.__player.score += 1000
                        
                        # Impacta con el jugador
                        else:
                            self.__player.score = 0
    
    def __matar_player(self, lst):
        # Impacto con bala enemiga
        if not self.__player.loop:
            for e in lst:
                for b in e.balas:
                    if (self.__player.x + self.__player.w > b.x
                        and b.x + b.w > self.__player.x
                        and self.__player.y + self.__player.h > b.y
                        and b.y + b.h > self.__player.y):
                        # La bala enemiga ha impactado a player
                        
                        # Mato la bala y creo una explosion
                        self.__explosiones.append(Explosion(self.__player.x + self.__player.w /2, 
                                                            self.__player.y + self.__player.h/2))
                        b.is_alive = False
        
                        # Le resto una vida al objeto
                        self.__player.vidas -= 1
                        
                        # Actualizo max score
                        if self.__player.score > self.__player.max_score:
                            self.__player.max_score = self.__player.score
                        
                        # Defino el score a 0
                        self.__player.score = 0
                        
                        # Si se queda sin vidas, muere
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
                    # El enemigo y player se han chocdo
                    
                    # Mato la bala y creo una explosion
                    self.__explosiones.append(Explosion(self.__player.x + self.__player.w /2, 
                                                        self.__player.y + self.__player.h/2))
                    e.is_alive = False
    
                    # Le resto una vida al objeto
                    self.__player.vidas -= 1
                    
                    # Actualizo max score
                    if self.__player.score > self.__player.max_score:
                        self.__player.max_score = self.__player.score
                    
                    # Defino el score a 0
                    self.__player.score = 0
                    
                    # Si se queda sin vidas, muere
                    if self.__player.vidas == 0:
                        self.__player.is_alive = False

    def __desaparecer(self, lst):
        """Elimina los objetos que no estan vivos de la lista."""
        l = lst
        for e in l:
            e.update()
            if e.is_alive == False:
                l.remove(e)  
        return l
    
     
    def update(self):
        # Comprobar si las explosiones han muerto
        self.__desaparecer(self.__explosiones)
        
        # Comprobar en las listas de enemigos si he matado enemigos
        # Comprobar en las listas de enemigos si han matado a player
        self.__matar(self.__enemigos)
        
        # Hacer que los objetos desaparezcan
        self.__desaparecer(self.__enemigos)
        
        # Ver si ha habido choques
        self.__chocar(self.__enemigos)
        
        # Verificar si hemos activado el bonus
        self.__check_bonus()
        
        # Actualizar isla
        for i in self.__islas:
            i.update()
        
        # Actualizar player
        self.__player.update() 

        # Si pulsas ENTER cambia a la escena de Game Over o termina el juego
        if pyxel.frame_count > 1400 or self.__player.vidas == 0:
            self.__nivel = constants.SCENE_GAMEOVER
        
    def draw(self):
        # Dibujar isla
        for i in self.__islas:
            i.draw()
        
        # Dibujar enemigos
        for e in self.__enemigos:
            e.draw()

        # Dibujar jugador
        self.__player.draw()
        
        # Dibujar explosiones
        for e in self.__explosiones:
            e.draw()
        
        # Dibujar score, max_score, vidas
        s = f"SCORE: {self.__player.score:>4}"
        m = f"MAX:   {self.__player.max_score:>4}"
        v = f"VIDAS:{self.__player.vidas:>4}"
        pyxel.text(5, 4, s, 7)
        pyxel.text(5, 10, m, 7)
        pyxel.text(70, 4, v, 7)
