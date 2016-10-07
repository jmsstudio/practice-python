# implementation of card game - Memory

import simplegui
import random

CARD_WIDTH = 50
CARD_HEIGHT = 100
#stores the card values (16 cards, 8 combinations)
numbers = []
exposed = []
cards_revealed = 0
cards_idx_of_turn = []
turns = 0

# helper function to initialize globals
def new_game():
    global numbers, exposed, cards_revealed
    
    numbers = range(8)
    numbers.extend(numbers)
    random.shuffle(numbers)
    
    turns = 0
    label.set_text("Turns = " + str(turns))
    cards_revealed = 0
    exposed = []
    for i in range(len(numbers)):
        exposed.append(False)

# define event handlers
def mouseclick(pos):
    global cards_revealed, cards_idx_of_turn, turns
    
    card_idx = pos[0] / CARD_WIDTH
    
    if not exposed[card_idx]:
        if cards_revealed == 1:
            turns += 1
            label.set_text("Turns = " + str(turns))
        
        if cards_revealed < 2:
            cards_revealed += 1
            
            cards_idx_of_turn.append(card_idx)
            
        else:
            #check match
            idx_card_1 = cards_idx_of_turn.pop()
            idx_card_2 = cards_idx_of_turn.pop()
            
            if not numbers[idx_card_1] == numbers[idx_card_2]:
                exposed[idx_card_1] = False
                exposed[idx_card_2] = False
                
            cards_revealed = 1
            cards_idx_of_turn.append(card_idx)
            
        exposed[card_idx] = True
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(numbers)):
        x = CARD_WIDTH * card_index + 10
        y = CARD_HEIGHT / 2 + 10
        colors = ['white', 'green', 'blue', 'yellow', 'red', 'gray', 'aliceblue', 'purple', '#ddd']

        if card_index > 8:
            color = colors[card_index - 8]
        else:
            color = colors[card_index]
            
        line_width = 50
        
        canvas.draw_text(str(numbers[card_index]), (x, y), 50, 'white')
        
        if (exposed[card_index] == False):
            canvas.draw_line((card_index * CARD_WIDTH + CARD_WIDTH/2, 0), (card_index * CARD_WIDTH + CARD_WIDTH/2, CARD_HEIGHT), CARD_WIDTH, color)
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
