# -*- coding: utf-8 -*-
import random


# class that represents an Agent that chooses a number to be guessed by the player
class Chooser:

	def __init__(self):
		# set the number choosen, randomly
		self.number = random.randint(1,101)


	def compare(self,numberProvided):
		# returns the difference so if the number provided is bigger it will return a positive value
		# if the number is smaller it will returna negative value
		# if the number is the same it will return 0
		return numberProvided - self.number


	def getNumber(self):
		return self.number