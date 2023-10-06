"""
Arcade 1942

File: player.py
Author: Luis Gandarillas
"""

import pyxel
import constants
from point import Point
from bullet import Bullet

class Player():
	def __init__(self):
		self.__point = Point(pyxel.width / 2 - constants.LOCKHEED_1[3]/2,
							 pyxel.height - constants.LOCKHEED_1[4])
		self.__is_alive = True
		self.__lives = 3
		self.__width = constants.LOCKHEED_1[3]
		self.__height = constants.LOCKHEED_1[4]
		self.__speed_x = constants.LOCKHEED_SPEED[0]
		self.__speed_y = constants.LOCKHEED_SPEED[1]
		self.__bullets = []
		self.__bullet_type = constants.BULLET_PLAYER
		self.__score = 0
		self.__loop = False
		self.__tloop = False
		self.__bonus = False
		
	def __reset(self):
		self.__point = Point(pyxel.width / 2 - constants.LOCKHEED_1[3]/2,
							 pyxel.height - constants.LOCKHEED_1[4])		
		self.__is_alive = True
		self.__score = 0
		
	def __shoot(self):
		if self.__bonus:
			if pyxel.btnp(pyxel.KEY_SPACE):
				self.__bullets.append(Bullet(self.x + self.__width/2 - 5, 
										 self.y, self.__bullet_type))
				pyxel.play(1, 2)
				self.__bullets.append(Bullet(self.x + self.__width/2 + 5, 
										 self.y, self.__bullet_type))
				pyxel.play(1, 2)
		else:
			if pyxel.btnp(pyxel.KEY_SPACE):
				self.__bullets.append(Bullet(self.x + self.__width/2, 
										 self.y, self.__bullet_type))
				pyxel.play(1, 2)
		
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
	def bonus(self):
		return self.__bonus
		
	@bonus.setter
	def bonus(self, value):
		self.__bonus = value
		
	@property 
	def loop(self):
		return self.__loop
		
	@property
	def score(self):
		return self.__score
		
	@score.setter 
	def score(self, value):
		self.__score = value
		
	@property
	def bullets(self):
		return self.__bullets
		
		
	def __lower_height(self):
		self.__point.y += self.__speed_y
		
	def __increase_height(self):
		self.__point.y -= self.__speed_y
		
	def __turn_right(self):
		self.__point.x += self.__speed_x
		
	def __turn_left(self):
		self.__point.x -= self.__speed_x
		
	def __hacer_loop(self):
		if pyxel.btn(pyxel.KEY_Z):
			self.__loop = True
			self.__tloop = pyxel.frame_count
		
	def __limitar(self):
		self.__point.x = max(self.__point.x, 0)
		self.__point.x = min(self.__point.x, pyxel.width - self.__width)
		self.__point.y = max(self.__point.y, 0)
		self.__point.y = min(self.__point.y, pyxel.height - self.__height)
		
	def __disappear(self, lst):
		l = lst
		for e in l:
			e.update()
			if e.is_alive == False:
				l.remove(e)  
		return l
		
	def __pintar_player(self):
		pyxel.blt(self.__point.x, self.__point.y,
			constants.LOCKHEED_1[0],
			constants.LOCKHEED_1[1] if pyxel.frame_count % 5 == 0 else constants.LOCKHEED_2[1],
			constants.LOCKHEED_1[2],
			constants.LOCKHEED_1[3], constants.LOCKHEED_1[4],
			constants.TRANSPARENT)
		
	def __pintar_loop(self):
		pyxel.blt(self.__point.x, self.__point.y,
			constants.LOCKHEED_LOOP[0], constants.LOCKHEED_LOOP[1], 
			constants.LOCKHEED_LOOP[2], constants.LOCKHEED_LOOP[3], 
			constants.LOCKHEED_LOOP[4], constants.TRANSPARENT)
		
	def __mover(self):
		if pyxel.btn(pyxel.KEY_LEFT):
			self.__turn_left()
		if pyxel.btn(pyxel.KEY_RIGHT):
			self.__turn_right()
		if pyxel.btn(pyxel.KEY_UP):
			self.__increase_height()
		if pyxel.btn(pyxel.KEY_DOWN):
			self.__lower_height()
		
	def update(self):
		self.__mover()
		self.__hacer_loop()
		self.__limitar()
		self.__shoot()
		self.__disappear(self.__bullets)	
		
	def draw(self):
		if self.__loop == False:
			self.__pintar_player()
		elif self.__loop == True and pyxel.frame_count - self.__tloop < 10:
			self.__pintar_loop()
		elif self.__loop == True and pyxel.frame_count - self.__tloop >= 10:
			self.__loop = False
			self.__tloop = False
		for b in self.__bullets:
			b.draw()