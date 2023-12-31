"""
Arcade 1942

File: level.py
Author: Luis Gandarillas
"""

import pyxel
import constants
from island import Island
from player import Player
from regular import Regular
from bombardier import Bombardier
from red import Red
from superbombardier import Superbombardier
from explosion import Explosion

class Level:
		
	def __init__(self):
		self.__islands = self.__createIslands()
		self.__enemigos = self.__createEnemigos()
		self.__explosiones = list()
		self.__player = Player()
		self.__level = constants.SCENE_LEVEL
		
	@property
	def get_scene(self):
		return self.__level
		
	def __createIslands(self):
		islands = []
		
		islands.append(Island(0))
		islands.append(Island(1))
		
		return islands
		
	def __createEnemigos(self):
		enemigos = []
		dif = 500
		self.__createRegulares(enemigos)
		self.__createRojos(enemigos, dif)
		self.__createBombarderos(enemigos)#, dif)
		
		enemigos.append(Superbombardier())
		return enemigos
		
	def __createRegulares(self, lst):
		for i in range(1, 21):
			sep = i * 4 * constants.REGULAR_UP_1[3]
			r = Regular(sep)
			lst.append(r)
		
	def __createRojos(self, lst, dif):
		for i in range(1, 6):
			sep = dif + i * 100
			r = Red(sep)
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
			for b in self.__player.bullets:
				if (e.x + e.w > b.x
					and b.x + b.w > e.x
					and e.y + e.h > b.y
					and b.y + b.h > e.y):
					
					self.__explosiones.append(Explosion(e.x + e.w /2, e.y + e.h/2))
					b.is_alive = False
					
					e.lives -= 1
					if e.lives == 0:
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
				for b in e.bullets:
					if (self.__player.x + self.__player.w > b.x
						and b.x + b.w > self.__player.x
						and self.__player.y + self.__player.h > b.y
						and b.y + b.h > self.__player.y):						
						self.__explosiones.append(Explosion(self.__player.x + self.__player.w /2, 
															self.__player.y + self.__player.h/2))
						b.is_alive = False		
						self.__player.lives -= 1											
						self.__player.score = 0						
						if self.__player.lives == 0:
							self.__player.is_alive = False
		
	def __check_bonus(self):
		bonus = True
		for e in self.__enemigos:
			if e.type == 1:
				bonus = False
		if bonus:
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
					self.__player.lives -= 1									
					self.__player.score = 0					
					if self.__player.lives == 0:
						self.__player.is_alive = False

	def __disappear(self, lst):
		l = lst
		for e in l:
			e.update()
			if e.is_alive == False:
				l.remove(e)  
		return l
	 
	def update(self):
		self.__disappear(self.__explosiones)
		self.__matar(self.__enemigos)
		self.__disappear(self.__enemigos)
		self.__chocar(self.__enemigos)
		self.__check_bonus()
		for i in self.__islands:
			i.update()
		self.__player.update() 
		if pyxel.frame_count > 1400 or self.__player.lives == 0:
			self.__level = constants.SCENE_GAMEOVER
		
	def draw(self):
		for i in self.__islands:
			i.draw()
		for e in self.__enemigos:
			e.draw()
		self.__player.draw()
		for e in self.__explosiones:
			e.draw()
		s = f"SCORE: {self.__player.score:>4}"
		v = f"LIVES:{self.__player.lives:>4}"
		pyxel.text(5, 4, s, 7)
		pyxel.text(70, 4, v, 7)