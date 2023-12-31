"""
Arcade 1942

File: gameover.py
Author: Luis Gandarillas
"""

import pyxel
import constants

class Gameover():

	def __init__(self):
		self.__gameover = constants.SCENE_GAMEOVER
		
	@property
	def get_scene(self):
		return self.__gameover
		
	def draw(self):
		pyxel.blt(33, 76, constants.GAMEOVER[0], constants.GAMEOVER[1],
				  constants.GAMEOVER[2], constants.GAMEOVER[3],
				  constants.GAMEOVER[4], constants.TRANSPARENT)
		pyxel.text(25, 126, "- PRESS Q TO QUIT -", 11)