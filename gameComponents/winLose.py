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