"""
Arcade 1942

File: bullet.py
Author: Luis Gandarillas
"""

import pyxel
import constants
from point import Point


class Bullet:
		
	def __init__(self, x, y, kind):
		if type(x) != int and type(x) != float:
			raise TypeError("x must be a number")
		if type(y) != int and type(y) != float:
			raise TypeError("x must be a number")
		else:
			self.__point = Point(x, y)
		
		self.__is_alive = True
		
		if kind != 0 and kind != 1:
			raise ValueError("The bullet type must be 0 or 1.")
		else:
			self.__type = kind
		
		if self.__type == constants.BULLET_PLAYER:  
			self.__width = constants.BULLET[3]
			self.__height = constants.BULLET[4]
			self.__speed = constants.BULLET_P_SPEED
		elif self.__type == constants.BULLET_ENEMY:
			self.__width = 2
			self.__height = 2
			self.__speed = constants.BULLET_E_SPEED

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
		
	def __increase_height(self):
		self.__point.y -= self.__speed
		
	def __lower_height(self):
		self.__point.y += self.__speed
		
	def __die(self):
		if self.__type == constants.BULLET_PLAYER and self.__point.y < 5:
			self.__is_alive = False  
		elif self.__type == constants.BULLET_ENEMY and self.__point.y > pyxel.height -5:
			self.__is_alive = False
		
	def __pintar_bullet_p(self):
		pyxel.blt(self.__point.x, self.__point.y, constants.BANK[0],
				  constants.BULLET[1], constants.BULLET[2],
				  constants.BULLET[3], constants.BULLET[4],
				  constants.TRANSPARENT)
		
	def __pintar_bullet_e(self):
		pyxel.circ(self.__point.x, self.__point.y, 1 , constants.RED)
		
	def update(self):
		if self.__type == constants.BULLET_PLAYER:
			self.__increase_height()
		if self.__type == constants.BULLET_ENEMY:
			self.__lower_height()
		self.__die()
		
	def draw(self):
		if self.__is_alive and self.__type == constants.BULLET_PLAYER:
			self.__pintar_bullet_p()		
		elif self.__is_alive and  self.__type == constants.BULLET_ENEMY:
			self.__pintar_bullet_e()