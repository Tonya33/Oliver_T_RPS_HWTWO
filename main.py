from random import randint

# add player and computer lives
choices = ["rock", "paper", "scissors"]


# save the player as a varible called player
# the value of player will be one of three choices to type (input)
#
# player will be the weapon the player chooses via input
player = False

# and array is just a container. It holds multiple values in a 0-based index
# you can store anything in an arra(y and retrieve it later. Arrays have a square bracket notation
#Boolean values are True or False - you can use these to check state

playerLives = 5
computerLives = 5
# define a win / lose function and invoke it in our game loop when lives run out (player or computer)

# create an infinite loop (for now) so that we can keep playing


def winorlose(status):
	print("You " + status + "! Would you like to play again?")
	choice = input(" Y / N ")

	global playerLives
	global computerLives
	global player

	if choice == "n":
			print("Better luck next time!")
			exit()
	else:
			#reset and restart
		playerlives= 5
		computerLives= 5
		player = False


while player is False:

	player = input("Choose your weapon! rock, paper or scissors:")
	computer = choices[randint(0,2)]


	print("computer chose: " + computer)
	print("player chose: " + player)

	if (computer == player):
		print("tie! try again")

	elif (player == "rock"):
		if (computer == "paper"):
			print("you lose!")
			playerLives = playerLives - 1
		else:
			print("you win!")
			computerLives = computerLives -1

	elif (player == "scissors"):
		if (computer == "paper"):
			print("You win!")
			computerLives = computerLives -1
		else:
			print("You lose!")
			playerLives = playerLives - 1

	elif (player == "paper"):
		if (computer == "rock"):
			print("You win!")
			computerLives = computerLives -1
		else:
			print("You lose!")
			playerLives = playerLives - 1

	print("computer Life count: " + str(computerLives))
	print("player Life count: " + str(playerLives))


	if playerLives == 0:
		winorlose("lost")

	elif computerLives == 0:
	winorlose("won")

	player = False
