from random import randint
from gameComponents import gameFunction, winLose, gameVars

while gameVars.player is False:

    gameVars.player = input("Choose your weapon! rock, paper or scissors:")
    computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + computer)

    print("player Life count: " + str(gameVars.playerLives))
    print("computer Life count: " + str(gameVars.computerLives))

    gameFunction.compare(computer)

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False
