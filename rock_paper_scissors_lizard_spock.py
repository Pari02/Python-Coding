# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

# function name_to_number
# using if/elif/else to assign number for each name
def name_to_number(name):
    
    if name == "rock":
        number = 0    
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3      
    elif name == "scissors":
        number = 4    
    else:
        print "Please choose a valid name"
    return number
# End of function name_to_number

# function number_to_name
# using if/elif/else to assign name for each number between 0-4
def number_to_name(number):
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"  
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"    
    else:
        print "Invalid number"
    return name
# End of function number_to_name

# function rpsls 
# for the game of rock-paper-scissors-lizard-Spock
def rpsls(player_choice): 
    
    # converting player's choice to number 
    # using name_to_number function for calculation
    player_number = name_to_number(player_choice)
    
    # print player's choice    
    print "Player chooses", player_choice  

    # generating random number for computer's choice using random.randrange function 
    comp_number = random.randrange(0,5)
    
    # print computer's choice
    # using function number_to_name to print respective name for computer's choice
    print "Computer chooses", number_to_name(comp_number) 
    
# calculate the differene between player number and computer number to find the winner
    winner = (player_number - comp_number)

# using if/elif/else to print the winner 
# if winner is 1,2 player wins
# if winner is 3,4 computer wins
# if winner = 0 player and computer ties
# added "\n" after each print statement to print an empty line

    if winner == 0:
        print "Player and computer tie!\n"
    elif winner > 0:
        if winner == 1 or winner == 2:
            print "Player wins!\n"
        elif winner == 3 or winner == 4:
            print "Computer wins!\n"
    elif winner < 0:
        winner = winner + 5
        if winner == 1 or winner == 2:
            print "Player wins!\n"
        elif winner == 3 or winner == 4:
            print "Computer wins!\n"
            
# End of function rpsls
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")