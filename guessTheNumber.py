# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# importing necessary packages
import simplegui
import random
import math

# initialize global variables used in your code here
num_range = 100
counter = 0
secret_number = 0

# helper functions to start and restart the game

# Helper function counter_cal 
# it takes num_range as parameter 
# and calculate the number of guesses player shoud get.
# By default num_range = 100"""
def counter_cal(num):
    global counter
    for i in range(num_range):
        if (math.pow(2, i) >= (num_range + 1)):
            break
    counter = i
    return counter

# Helper function secret_num
# it takes num_range as parameter 
# and generated random number depending on the range selected 
# by default num_range = 100"""" 
def secret_num(num):
    global secret_number
    global num_range
    secret_number = random.randrange(0, num_range)
    return secret_number
            
def new_game():
    global num_range
    if num_range == 100:
        # Calling counter_cal to find value of guesses 
        # respective to num_range value
        counter = counter_cal(num_range)
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is", counter
    elif num_range == 1000:
        counter = counter_cal(num_range)
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is", counter
    # Calling secret_numb function to generate random number
    # respective to range selected
    secret_num(num_range)
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    low = 0
    high = 100
    num_range = high - low
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    low = 0
    high = 1000
    num_range = high - low
    new_game()

def input_guess(guess):
    # main game logic goes here	
    global num_range
    global counter
    global secret_number
  
    # Converting string value caputered from input button to integer 
    # and storing in a local variable num_guess
    num_guess = int(guess)
    
    # if/elif/else code to find out the number if counter value is > 0
    if counter > 0:
        # Reducting the counter by one after submission of each value
        counter = counter - 1
        if secret_number < num_guess:
            print "Guess was", num_guess
            print "Number of remaining guesses is", counter
            print "Lower!"
 
        elif secret_number > num_guess:
            print "Guess was", num_guess
            print "Number of remaining guesses is", counter
            print "Higher!"
                
        elif secret_number == num_guess:
            print "Guess was", num_guess
            print "Number of remaining guesses is", counter
            print "Correct!"
            new_game()
    if counter == 0:
        print "Guess was", num_guess
        print "Number of remaining guesses is", counter
        print "You ran out of guesses. The number was", secret_number
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)
frame.add_input('Enter a guess', input_guess, 200)

# call new_game 
new_game()
