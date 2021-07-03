from Deck import *
from AI import *
import random

deck = Deck()
deck.build()

class Hand:
    def __init__(self):
        self.cards = []
        for x in range(7):
            self.add(deck.draw())

    def add(self, card):
        self.cards.append(card)

    def remove(self, card):
        self.cards.remove(card)

    def print_hand(self):
        for x in range(len(self.cards)):
            if self.cards[x].color != "Black":
                print("{}.) {} {}".format(x+1, self.cards[x].color, self.cards[x].value))
            else:
                print("{}.) {}".format(x+1, self.cards[x].value))

def compare(card, top):
    if(card.color == top.color or card.value == top.value or card.color == "Black"):
        return True
    return False

#If the initial deck runs out of cards, this takes the discard deck, reshuffles it, and makes the deck the discard pile.
def reshuffle(d):
    for card in d:
        #Since the color of the Wilds and Draw 4s will change based on user input, reshuffling the deck will turn the colors back into black.
        if d.value == "Wild" or d.value == "Draw 4":
            d.color = "Black"
    deck.cards = deck.cards + d.cards[:-1] #Last card in the list is the top card of the discard.
    deck.shuffle()

#This method take into account special, reverse, draw 2, and draw 4 cards, as well as turn flow.
def compute_card(t, c):
    if c.value == "Draw 2":
        if t == "ai":
            hand.add(deck.draw())
            hand.add(deck.draw())
        else:
            ai.hand.append(deck.draw())
            ai.hand.append(deck.draw())

    elif c.value == "Draw 4":
        if t == "ai":
            for x in range(4):
                hand.add(deck.draw())
        else:
            for x in range(4):
                ai.hand.append(deck.draw)
    #Since it's 1 AI, reverse works as a skip.
    elif c.value not in ['Skip', 'Reverse']:
        return True
    return False

turn = "player"
discard = Deck()
hand = Hand()
ai = AI()

for x in range(7):
    ai.hand.append(deck.draw())
discard.cards.append(deck.draw())
#Draws cards until there is a number value on top
while not isinstance(discard.cards[-1].value, int):
    discard.cards.append(deck.draw())

while len(hand.cards) > 0 and len(ai.hand) > 0:
    #If the deck runs below 4 cards, it will take the rest of the discard and shuffle it into the deck. This avoids it blowing up if a draw 4 is used with 3 cards left in the deck.
    if len(deck.cards) <= 4:
        reshuffle()
        discard.cards = discard.cards[-1]
    played_card = Card("blank", "blank") #Since taking the card at the top of the discard messes up the method if it isn't numerical, I instead pass the card played or a special blank card if a card was drawn.
    if turn == "player":
        print("\n-----------------------------------------------------------------------\n")
        print("Deck has {} cards in it.".format(len(deck.cards)))
        if(len(ai.hand) > 1):
            print("AI has {} cards.".format(len(ai.hand)))
        else:
            print("AI has Uno!")
        print("Card is {} {}".format(discard.cards[-1].color, discard.cards[-1].value))
        hand.print_hand()
        hand_size = len(hand.cards)
        while(len(hand.cards) == hand_size): #As long as the player doesnt draw or play a card
            c = input("What card are you playing? (Or type 'draw' to draw a card): ")
            if c.lower() == "draw":
                hand.add(deck.draw())
            elif c.isnumeric() and int(c) <= len(hand.cards) and int(c) > 0:
                if compare(hand.cards[int(c)-1], discard.cards[-1]):
                    played_card = hand.cards[int(c)-1]
                    discard.add(played_card)
                    hand.remove(played_card)
                else:
                    print("That card doesn't work. (You know better)")
            else:
                print("Invalid input.")
    else:
        print("\n-----------------------------------------------------------------------\n")
        c = ai.turn(discard.cards[-1])
        if c == "draw":
            print("The AI drew a card.")
            ai.hand.append(deck.draw())
        else:
            print("The AI played a {} {}.".format(c.color, c.value))
            discard.add(c)
            played_card = c
    if compute_card(turn, played_card):
        if(turn == "player"):
            turn = 'ai'
        else:
            turn = 'player'
print("\n-----------------------------------------------------------------------\n")
if len(hand.cards) > 0:
    print("You lost!")
else:
    print("You won!")
