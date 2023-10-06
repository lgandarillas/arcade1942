"""
Arcade 1942

File: main.py
Author: Luis Gandarillas
"""

import pyxel
import constants
from intro import Intro
from level import Level
from gameover import Gameover

class Game():
		
	def __init__(self):
		pyxel.init(constants.SCREEN_W, constants.SCREEN_H, title="1942") 
		pyxel.load("sprites1942.pyxres")
		pyxel.play(0, 0, loop = True)
		self.__intro = Intro()
		self.__level = Level()
		self.__gameover = Gameover()
		self.__scene = constants.SCENE_INTRO
		pyxel.run(self.update, self.draw)   
		
	def __check_scene(self):
		if self.__scene == constants.SCENE_INTRO:
			self.__intro.update()
			if self.__intro.get_scene == constants.SCENE_LEVEL:
				self.__scene = constants.SCENE_LEVEL		
		elif self.__scene == constants.SCENE_LEVEL:
			self.__level.update()
			if self.__level.get_scene == constants.SCENE_GAMEOVER:
				self.__scene = constants.SCENE_GAMEOVER
		
	def __draw_scene(self):
		if self.__scene == constants.SCENE_INTRO:
			self.__intro.draw()
		
		elif self.__scene == constants.SCENE_LEVEL:
			self.__level.draw()
		
		elif self.__scene == constants.SCENE_GAMEOVER:
			self.__gameover.draw()
		
	def update(self):
		if pyxel.btnp(pyxel.KEY_Q): 
			pyxel.quit()		
		self.__check_scene()
		
		
	def draw(self):
		pyxel.cls(constants.BLUE)
		self.__draw_scene()
		
Game()