from random import randint
#add player and computer lives
playerLives = 5
computerLives = 5

# save the player as a varible called player
# the value of player will be one of three choices to type (input)
player = input("Choose rock, paper or scissors")

print("player chose: " + player)

# and array is just a container. It holds multiple values in a 0-based index
# you can store anything in an arra(y and retrieve it later. Arrays have a square bracket notation

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0,2)]

print("computer chose: " + computer)

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

print("computer Lives: " + str(computerLives))
print("player Lives: " + str(playerLives))

