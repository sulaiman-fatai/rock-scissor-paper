from ast import If
import random

#creates a list of all possible options
L = ["R", "P", "S"]
R="ROCKS"
P="PAPER"
S="SCISSOR"

print(f"\nWelcome to the Rock Paper Scissor game\n")
print("If the two players choose the same “character” it’s a tie, and the game repeats")
print(f"\nRock beats Scissors; Paper beats Rock; Scissors beats Paper\n")
#assign a random play to the computer
#and change our computer choice to there corresponding output string
computer =(random.choice(L))
if computer == "R":
    computer = "Rock" 
elif computer == "P":
    computer = "Paper"   
elif computer == "S":
    computer = "Scissors"
#set player to False
player = False
while player == False:
#set player to True
    player = input("Enter a choice(R, P, S?):")
    if player == computer:
        print("Player " +"("+player+ ")" + " : " + " CPU "+"("+computer+ ")")
        print("Its a Tie!")
        player = False
    elif player == "R": 
        player = R
        if computer == "S":
         computer = S
         print("Player " +"("+player+ ")" + " : " + " CPU "+"("+computer+ ")")
         print("You win!", player, "beats", computer)
        else:
            print("You lose!", computer, "covers", player)
    elif player == "P":
        player = P
        if computer == "R":
            computer = R
            print("Player " +"("+player+ ")" + " : " + " CPU "+"("+computer+ ")")
            print("You win!", player, "beats", computer)
        else:
            print("You lose!", computer, "cut", player)
    elif player == "S":
        player = S
        print("Player " +"("+player+ ")" + " : " + " CPU "+"("+computer+ ")")
        if computer == "P":
            computer = P
            print("You win!", player, "cut", computer)
        else:
            print("You lose...", computer, "smashes", player)
    else:
        print("That's not a valid play. Check your spelling!")
        print("Player " +"("+player+ ")" + " : " + " CPU "+"("+computer+ ")")
        computer =(random.choice(R))
        player = False    
    #player was set to True, but we want it to be False so the loop continues
 