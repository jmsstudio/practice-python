import random
import simplegui

range_limit = 100

def new_game():
    # initialize global variables
    global secret_number, range_limit, num_guess
    
    print "=== GUESS THE NUMBER ==="
    num_guess = 0
    secret_number = random.randrange(0, range_limit)

def range100():
    # changes the range to [0,100) and starts a new game 
    global range_limit, max_guesses
    range_limit = 100
    max_guesses = 7
    new_game()

def range1000():
    # changes the range to [0,1000) and starts a new game     
    global range_limit, max_guesses
    range_limit = 1000
    max_guesses = 10
    new_game()
    
def input_guess(guess):
    # main game logic
    global secret_number, max_guesses, num_guess
    
    num_guess += 1
    _guess = int(guess)
    print "Guess was " + str(_guess)
    
    if num_guess > max_guesses:
        print "Game over - number of guesses exceeded " + str(max_guesses)
        new_game()
    else:
        if _guess > secret_number:
            print "Higher"
        elif _guess < secret_number:
            print "Lower"
        else:
            print "Correct"
            new_game()

    
frame = simplegui.create_frame("Guess the number", 200, 300)

frame.add_button("Reset - Range [0-100)", range100)
frame.add_button("Reset - Range [0-1000)", range1000)
frame.add_input("Guess the number", input_guess, 40)

frame.start()

range100()