# -*- coding: utf-8 -*-
from Players import Chooser


if __name__ == '__main__':

	playing = True

	print("Hi!")
	while playing :
		try :
			option = int(input("If you want to guess my number write 1 , if you want me to guess your number write 2, to finish write any other number: "))
		except:
			# in case the user inputs any other thing not castable to int we handle this asining 3 to the option to quit
			option = 3

		if option == 1 :
			guessed = False
			# create an object of type Chooser that chooses a random number between 1 and 100
			player = Chooser()
			while not guessed:
				# read the number of the user
				number = int(input("Please, make a guess... "))
				# get the direction towards the choosen number
				direction = player.compare(number)
				if direction > 0 :
					# the number provided by the user is higher than the choosen by the computer
					print("Sorry, but your number is bigger than mine ...")
				elif direction < 0 :
					# the number provided by the user is lower than the choosen by the computer
					print("Sorry, but your number is smallers than mine ...")
				else:
					# the number has been guessed
					guessed = True
					print("Congratulations, you have guessed my number!")
					print("My number is "+str(player.getNumber())+" ! ")
			
		elif option == 2 :
			

		else :
			playing = False
			print("Bye bye! Thanks for the fun!")


		

