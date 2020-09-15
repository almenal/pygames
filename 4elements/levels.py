"""This module includes the Level class definition, as well as the 
defition of every Levels object of the game. Since importing all levels at once is
not efficient, write in the main script
importlib.import_module('levels').__getattribute__('levelXX')
with levelXX as the Level object to import"""

class Level():
	def __init__(self):
		self.image = None
