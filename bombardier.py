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
		self.__bullets = []
		self.__bullet_type = constants.BULLET_ENEMY		
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
	def bullets(self):
		return self.__bullets
		
	@property
	def type(self):
		return self.__type
		
	def __shoot(self):
		if self.__point.x == self.__shot or self.__point.y == self.__shot:
			self.__bullets.append(Bullet(self.__point.x + self.__width/2,
									 self.__point.y + self.__height,
									 self.__bullet_type))
		
	def __lower_height(self):
		self.__point.y += self.__speed_y
		
	def __increase_height(self):
		self.__point.y -= self.__speed_y
		
	def __turn_right(self):
		self.__point.x += self.__speed_x
		
	def __turn_left(self):
		self.__point.x -= self.__speed_x
		
	def __disappear(self, lst):
		l = lst
		for e in l:
			e.update()
			if e.is_alive == False:
				l.remove(e)  
		return l
		
	def __die(self):
		self.__is_alive = False
		
	def __paint_descent(self):
		pyxel.blt(self.__point.x, self.__point.y, constants.BOMB_DOWN_2[0],
			constants.BOMB_DOWN_1[1] if self.__frames % 5 == 0 else constants.BOMB_DOWN_2[1],
			constants.BOMB_DOWN_1[2] if self.__frames % 5 == 0 else constants.BOMB_DOWN_2[2], 
			constants.BOMB_DOWN_1[3], constants.BOMB_DOWN_1[4],
			constants.TRANSPARENT)
		
	def __paint_rise(self):
		pyxel.blt(self.__point.x, self.__point.y,constants.BOMB_UP_1[0],
			constants.BOMB_UP_1[1] if self.__frames % 5 == 0 else constants.BOMB_UP_2[1],
			constants.BOMB_UP_1[2],
			constants.BOMB_UP_1[3], constants.BOMB_UP_1[4],
			constants.TRANSPARENT)
		
	def __pintar_turn_right(self):
		pyxel.blt(self.__point.x, self.__point.y, constants.BOMB_DER[0],
			constants.BOMB_DER[1],
			constants.BOMB_DER[2],
			constants.BOMB_DER[3], constants.BOMB_DER[4],
			constants.TRANSPARENT)
		
	def __mover(self):
		if self.__frames > 400 and self.__frames < 500:
			self.__lower_height()
		if self.__frames > 500 and self.__frames < 560:
			self.__turn_right()
		elif self.__frames > 560:
			self.__increase_height()
		elif self.__frames > 660:
			self.__die()
		
	def update(self):
		self.__frames += 1
		self.__mover()
		self.__shoot()
		self.__disappear(self.__bullets)
		
			
	def draw(self):
		if self.__is_alive:
			if self.__frames > 400 and self.__frames < 500:
				self.__paint_descent()
			if self.__frames > 500 and self.__frames < 560:
				self.__pintar_turn_right()
			elif self.__frames >560:
				self.__paint_rise()
		for b in self.__bullets:
			b.draw()