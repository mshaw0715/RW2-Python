import sys, random

print("")

mesg = """
Enter . . .
1 for Rock
2 for Paper
3 for Scissors:\n\n
"""

rps = ("nothing", "Rock", "Paper", "Scissors")

playerchoice = input(mesg)
player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You chose " + playerchoice + " " + rps[player] + ".")
print("Python chose " + computerchoice + " " + rps[computer] + ".")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("Tie Game!")
else:
    print("Python Wins!")