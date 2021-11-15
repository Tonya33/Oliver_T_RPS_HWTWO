from random import randint
from gameComponents import gameFunction, winLose, gameVars

while gameVars.player is False:

    gameVars.player = input("Choose your weapon! rock, paper or scissors:")
    computer = gameVars.choices[randint(0, 2)]

    gameFunction.compare(computer)

    print("player's weapon of choice: " + gameVars.player)
    print("computer's weapon of choice: " + computer)

    print("player LIFE COUNT: " + str(gameVars.playerLives))
    print("computer LIFE COUNT: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("were so close! sorry about your luck")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False
