from gameComponents import gameVars


def compare(computer):
    if (computer == gameVars.player):
        print("=+=+=+=+=TIE! try again=+=+=+=+=")

    elif (gameVars.player == "rock"):
        if (computer == "paper"):
            print("===========You lose!=============")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("+++++++++++++++++You win!++++++++++++")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "scissors"):
        if (computer == "paper"):
            print("+++++++++++++++++You win!++++++++++++")
            gameVars.computerLives = gameVars.computerLives - 1
        else:
            print("===========You lose!=============")
            gameVars.playerLives = gameVars.playerLives - 1

    elif (gameVars.player == "paper"):
        if (computer == "rock"):
            print("+++++++++++++++++You win!++++++++++++")
            gameVars.computerLives = gameVars.computerLives - 1
        else:
            print("===========You lose!=============")
            gameVars.playerLives = gameVars.playerLives - 1
