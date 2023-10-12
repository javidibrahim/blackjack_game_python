import random
import os

def clear():
  os.system('cls')

clear()

#function
def calculateTotal(arr):
    total = 0
    for i in arr:
        total +=i
    return total

def showUserHand(arr):
    print("[", end = "")
    for i in range(0, len(arr)):
        print(arr[i], end="")
        if i != len(arr)-1:
            print(", ", end = "")
    print("]")

def findHighest(arr):
    lowest = 0
    for i in arr:
        lowest = i
        if(lowest > i):
            lowest = i
    return lowest


#create a deck
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
sizeOfDeck = len(deck)

player = []
computer = []
moves = 2

playerPtr = 0
computPtr = 0
#pick randomly 2 numbers for each player
for i in range(0, moves):
    player.append(deck[random.randint(0, sizeOfDeck-1)])
    computer.append(deck[random.randint(0, sizeOfDeck-1)])

#highest of cards for computer finds one time from first two cards
lowest = findHighest(computer)

#calculate totals
playerPtr = calculateTotal(player)
computPtr = calculateTotal(computer)

showUserHand(player)
print(f"Total player points: {playerPtr}")
print(f"Current computer points: {lowest}")

playerWin = False
computerWin = False
draw = False


while playerWin == False and computerWin == False and draw == False:

    if playerPtr == 21:
        playerWin = True
    elif computerWin == 21:
        computerWin = True


        #ask if user wants to deal
    deal = (input("Do you want to deal (y/n):  ")).lower()

    ### input validation ###
    while deal != "y" and deal != "n":
        deal = input("Enter: y or n:  ")

    if deal == "y":
        player.append(deck[random.randint(0, sizeOfDeck-1)])
        playerPtr = calculateTotal(player)
        showUserHand(player)
        if playerPtr > 21:
            if 11 in player:
                player.remove(11)
                player.append(1)
                playerPtr = calculateTotal(player)
            else:
                computerWin = True

    if deal == "n":
        playerPtr = calculateTotal(player)
        computPtr = calculateTotal(computer)
        while computPtr < 17:
            
            computer.append(deck[random.randint(0, sizeOfDeck-1)])
            computPtr = calculateTotal(computer)
            #if scores go higher than 21
            if computPtr > 21:
                playerWin = True

        if playerPtr > computPtr:
            playerWin = True
        elif computPtr > playerPtr:
            computerWin = True
        else:
            draw = True

print("")


if playerWin == True:
    print("You won")
elif computerWin == True:
    print("Dealer won")
else:
    print("It's a draw")


print(f"Total player points: {playerPtr}", end = " ")
showUserHand(player)
print(f"Total computer points: {computPtr}", end = " ")
showUserHand(computer)