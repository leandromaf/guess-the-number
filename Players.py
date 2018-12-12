# -*- coding: utf-8 -*-
import random
import pdb


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


# class that represents an Agent that try to guess the number though by the player
class Guesser:

	def __init__(self):
		# initilize a binary search setting the limits and the middle
		self.left = 1
		self.right = 100
		self.middle = self.__getMiddleIncrement()
		

	# just returns the value of the middle of the search process
	def guess(self):
		return self.middle

	def __getMiddleIncrement(self):
		return int((self.right - self.left)/2)

	# it performs a binary search
	def update(self,direction):
		
		if direction == "+":
			# the number that the player though is bigger
			# focus the search on the right side
			# update the left
			self.left = self.middle + 1
			# update the middle
			self.middle = self.middle + self.__getMiddleIncrement()

		elif direction == "-" :
			# the number that the player though is smaller
			# focus the search on the left side
			self.right = self.middle - 1
			self.middle = self.middle - self.__getMiddleIncrement()



