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

class Regular(Enemy):
		
	def __init__(self, sep):
		
		super().__init__()
		
		if type(sep) != int and type(sep) != float:
			raise TypeError("sep must be a number")
		else:
			self.__point = Point(pyxel.rndi(40, 80), -sep)
		
		self.__is_alive = True
		self.__lives = 1
		self.__type = 0
		self.__width = constants.REGULAR_UP_1[3]
		self.__height = constants.REGULAR_UP_1[4]
		self.__dir = 1 if random.random() <= 0.5 else -1
		self.__speed_x = constants.REGULAR_SPEED[0] * self.__dir
		self.__speed_y = constants.REGULAR_SPEED[1]
		self.__shot = random.randint(10, pyxel.height/2)
		self.__bullets = []
		self.__bullet_type = constants.BULLET_ENEMY
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
	def lives(self):
		return self.__lives
		
	@lives.setter 
	def lives(self, value):
		self.__lives = value
		
	@property 
	def bullets(self):
		return self.__bullets
		
	@property
	def type(self):
		return self.__type
		
	def __disparar(self):
		if self.__point.y == self.__shot:
			self.__bullets.append(Bullet(self.__point.x + self.__width/2,
									 self.__point.y + self.__height,
									 self.__bullet_type))
		
	def __bajar(self):
		self.__point.y += self.__speed_y
		
	def __increase_height(self):
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
		pyxel.blt(self.__point.x, self.__point.y, 
			constants.REGULAR_DOWN_1[0],
			constants.REGULAR_DOWN_1[1] if pyxel.frame_count % 5 == 0 else constants.REGULAR_DOWN_2[1],
			constants.REGULAR_DOWN_1[2],
			constants.REGULAR_DOWN_1[3], constants.REGULAR_DOWN_1[4],
			constants.TRANSPARENT)
		
	def __pintar_subida(self):
		pyxel.blt(self.__point.x, self.__point.y, constants.REGULAR_UP_1[0],
			constants.REGULAR_UP_1[1] if pyxel.frame_count % 5 == 0 else constants.REGULAR_UP_2[1],
			constants.REGULAR_UP_1[2],
			constants.REGULAR_UP_1[3], constants.REGULAR_UP_1[4],
			constants.TRANSPARENT)
		
	def __mover(self):
		if self.__point.y < 0 and self.__bajando:
			self.__bajar()
		if self.__point.y >= 0 and self.__point.y < pyxel.height/2 and self.__bajando:
			self.__bajar()
			self.__derecha()
		if self.__point.y >= pyxel.height/2:
			self.__bajando = False
		if not self.__bajando:
			self.__increase_height()
			self.__izquierda()
		
	def update(self):
		self.__mover()
		self.__disparar()
		self.__desaparecer(self.__bullets)

	def draw(self):
		if self.__is_alive:
			if self.__bajando:
				self.__pintar_bajada()
			if not self.__bajando:
				self.__pintar_subida()
		for b in self.__bullets:
			b.draw()