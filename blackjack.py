#Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
wins = 0
loses = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        str_representation = str(self.get_value()) + ' Hand contains'
        
        for card in self.cards:
            str_representation += ' ' + str(card)
        
        return str_representation

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        total = 0
        aces = 0
        for card in self.cards:
            if card.get_rank() == 'A':
                aces += 1
            total += VALUES[card.get_rank()]
        
        for i in range(aces):
            if total < 21 and total + 10 < 21:
                total += 10
        
        return total
   
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, (pos[0] + CARD_SIZE[0] * i, pos[1]))
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop()
        return card
    
    def __str__(self):
        str_representation = 'Deck contains'
        
        for card in self.cards:
            str_representation += ' ' + str(card)
        
        return str_representation


def deal():
    global outcome, in_play
    global deck, player_hand, dealer_hand
    global loses
   
    if in_play:
        loses += 1
        in_play = False
        outcome = 'You have lost! New deal?'

    else:        
        outcome = 'Hit or stand?'
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        print 'Player hand: ' + str(player_hand)
        print 'Dealer hand: ' + str(dealer_hand)

        in_play = True

def hit():
    global outcome, in_play
    global deck, player_hand
    global wins, loses
    
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())

        if player_hand.get_value() > 21:
            in_play = False
            outcome = 'You have busted! Dealer wins! New deal?'
            loses += 1

        
def stand():
    global outcome, in_play
    global deck, dealer_hand, player_hand
    global wins, loses

    if in_play:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
            print str(dealer_hand)
    
        in_play = False

        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()

        if player_value > 21:
            outcome = 'You have busted! Dealer wins! New deal?'
            loses += 1
        elif dealer_value > 21:
            outcome = 'Dealer has busted! You win! New deal?'
            wins += 1
        elif player_value > dealer_value:
            outcome = 'You win! New deal?'
            wins += 1
        elif player_value < dealer_value:
            outcome = 'Dealer wins! New deal?'
            loses += 1
        else:
            outcome = 'Tie! New deal?'

        print outcome

def draw_back_card(canvas, pos):
    card_loc = (card_back.get_width()/4, card_back.get_height()/2)

    canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    
# draw handler    
def draw(canvas):
    global dealer_hand, player_hand, outcome, in_play
    global card_back
    global wins, loses

    canvas.draw_text('Blackjack', (250, 30), 30, 'black')
    
    dealer_hand.draw(canvas, (20, 40))
    player_hand.draw(canvas, (20, 40 + CARD_SIZE[1]))

    if in_play:
        draw_back_card(canvas, (20, 40))

    
    canvas.draw_text(outcome, (50, 300), 30, 'black')
    canvas.draw_text('Wins '+str(wins), (20, 30), 20, 'black')
    canvas.draw_text('Loses '+str(loses), (100, 30), 20, 'black')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


deal()
frame.start()

