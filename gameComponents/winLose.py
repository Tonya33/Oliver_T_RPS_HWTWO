from gameComponents import gameVars


def winorlose(status):
    print("you " + status)

    choice = input("do you want to play again? y/n: ")
    global playerLives
    global computerLives
    global player

    if choice == "n":
        print("========= see ya! (better luck next time!) ==========")
        exit()
    elif choice == "y":
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        print("Welcome Back :)")
        gameVars.player = False
