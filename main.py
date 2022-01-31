import random
#List to randomly choose opponent
myList = ["rock", "paper", "scissors"]
ranNum = random.randint(0,2)

#Checks to see wheter or not you win, lose, or tie
def check(choose, rand):
    print("Your opponent chose " + myList[rand])
    if choose == "rock":
        if rand == 0:
            print("You tied!\n")
        elif rand == 1:
            print("You lost!\n")
        elif rand == 2:
            print("You win!\n")

    elif choose == "paper":
        if rand == 0:
            print("You win!\n")
        elif rand == 1:
            print("You tie!\n")
        elif rand == 2:
            print("You lose!\n")

    elif choose == "scissors":
        if rand == 0:
            print("You lose!\n")
        elif rand == 1:
            print("You win!\n")
        elif rand == 2:
            print("You tie!\n")

#Gets user input for rock, paper, or scissors
def chooseIcon():
    chosen = input("Type 'Rock', 'Paper', or 'Scissors' to choose!\n").lower()
    if chosen == "rock":
        check("rock", ranNum)
    elif chosen == "paper":
        check("paper", ranNum)
    elif chosen == "scissors":
        check("scissors", ranNum)
    else:
        print("That is an invalid answer please write 'Rock', 'Paper', or 'Scissors'\n")
        chooseIcon()

#Infinite loop to restart the game
while True:
        wantToPlay = input("Do you want to play rock, paper, scissors?\n").lower()
        if wantToPlay == "yes":
            chooseIcon()
