"""
Arcade 1942

File: superbombardier.py
Author: Luis Gandarillas
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
		self.__bullet_type = constants.BULLET_ENEMY
		self.__bullets = []
	   
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
		
	def __lower_height(self):
		self.__point.y += self.__speed_y
		
	def __increase_height(self):
		self.__point.y -= self.__speed_y
		
	def __turn_right(self):
		self.__point.x += self.__speed_x
		
	def __turn_left(self):
		self.__point.x -= self.__speed_x
		
	def __die(self):
		self.__is_alive = False
		
	def __paint_rise(self):
		pyxel.blt(self.__point.x, self.__point.y, constants.SUPERB_UP_1[0],
			constants.SUPERB_UP_1[1] if pyxel.frame_count % 5 == 0 else constants.SUPERB_UP_2[1],
			constants.SUPERB_UP_1[2], 
			constants.SUPERB_UP_1[3], constants.SUPERB_UP_1[4],
			constants.TRANSPARENT)
		
	def __shoot(self):
		if self.__point.y % 20 == 0:
			self.__bullets.append(Bullet(self.__point.x + self.__width/2 -5,
									 self.__point.y + self.__height,
									 self.__bullet_type))
			self.__bullets.append(Bullet(self.__point.x + self.__width/2 + 5,
									 self.__point.y + self.__height,
									 self.__bullet_type))
		
	def __disappear(self, lst):
		l = lst
		for e in l:
			e.update()
			if e.is_alive == False:
				l.remove(e)  
		return l
		
	def __move(self):
		if pyxel.frame_count > 1200 and pyxel.frame_count < 1240:
			self.__increase_height()
		if pyxel.frame_count >= 1240:
			self.__increase_height()
			self.__turn_right()
		if self.__point.y < - 2 * constants.SUPERB_UP_1[4]:
			self.__die()
		
	def update(self):
		self.__move()
		self.__shoot()
		self.__disappear(self.__bullets)
	 
	def draw(self):
		if self.__is_alive:
			if pyxel.frame_count > 1200:
				self.__paint_rise()		
		for b in self.__bullets:
			b.draw()