"""
Rock-paper-scissors-lizard-Spock game

Each of the items are represented in the program 
by a number, as follows:
0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors
"""

import random

def name_to_number(name):
    """ 
        Helper function that converts 
        a name to a number between 0 and 4
    """
    num = -1
    if name == "rock":
        num = 0
    elif name == "Spock":
        num = 1
    elif name == "paper":
        num = 2
    elif name == "lizard":
        num = 3
    elif name == "scissors":
        num = 4
    
    return num

def number_to_name(num):
    """ 
        Helper function that converts a number (0 to 4) into a name 
        representing one of the items of the program
    """
    name = ""
    if num == 0:
        name = "rock"
    elif num == 1:
        name = "Spock"
    elif num == 2:
        name = "paper"
    elif num == 3:
        name = "lizard"
    elif num == 4:
        name == "scissors"
    
    return name

def rpsls(player_choice):
    """
        Executes the game rules
    """
    print "\n"
    
    print "Player chooses " + player_choice
    
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0, 4)
    
    comp_choice = number_to_name(comp_number)

    print "Computer chooses " + comp_choice
    
    x = (comp_number - player_number) % 5
    
    if x == 0:
        print "Player and computer tie!"
    elif x <= 2:
        print "Computer wins!"
    else:
        print "Player wins!"
    
    
# testing the code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
