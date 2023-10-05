"""
Arcade 1942
by: Luis Gandarillas

Run game: python3 main.py
"""

import constants
from bullet import Bullet

class Enemy:

	def __init__(self):
		self.__is_alive = True
		self.__bullets = []
		self.__bullet_type = constants.BULLET_ENEMY
		
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
		
	def __disappear(self, lst):
		l = lst
		for e in l:
			e.update()
			if e.is_alive == False:
				l.remove(e)  
		return l

	def __shoot(self):
		if self.__point.y % 20 == 0:
			self.__bullets.append(Bullet(self.__point.x + self.__width/2 -5,
									 self.__point.y + self.__height,
									 self.__bullet_type))
			self.__bullets.append(Bullet(self.__point.x + self.__width/2 + 5,
									 self.__point.y + self.__height,
									 self.__bullet_type))