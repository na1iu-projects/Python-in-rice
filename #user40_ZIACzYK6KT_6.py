# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 0
max_range = 100
guess_times = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, guess_times, max_range
    if int(max_range) == 100:
        guess_times = 7
    elif int(max_range) == 1000:
        guess_times =10
    secret_number = random.randrange(0, max_range)
    print 'Please guess the number or press button to choose the guess range!'
    print 'You only have', guess_times, 'times to guess!'
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    global max_range
    # button that changes the range to [0,100) and starts a new game 
    max_range = 100
    # remove this when you add your code    
    new_game()

def range1000(): 
    global max_range
    # button that changes the range to [0,1000) and starts a new game    
    max_range = 1000
    new_game()
        
def input_guess(guess):
    # main game logic goes here	
    global secret_number, guess_times
    # remove this when you add your code
    guesses = int(guess)
    guess_times = guess_times - 1
    print "Guess was ", guesses
    if guesses < secret_number:
        print "Guess Higher"
        print 'You only have', guess_times, 'times to guess!'
    elif guesses > secret_number:
        print "Guess Lower"
        print 'You only have', guess_times, 'times to guess!'
    elif guesses == secret_number:
        print "Correct, congratulations! Let's do it again!"
        print
        new_game()
    
    if guess_times <= 0:
        print "Unfornately, you lost the game. Let's do it again"
        new_game()
    print
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
inp = frame.add_input("Guess number", input_guess, 100)
btn_rs = frame.add_button('Re-Start', new_game)
btn_range1 = frame.add_button('Range:0 ~ 100', range100)
btn_range2 = frame.add_button('Range:0 ~ 1000', range1000)

# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
