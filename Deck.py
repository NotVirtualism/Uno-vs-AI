from Card import *
import random

class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        #2 of each number but 0, two of each special card, and 4 of each wilds.
        for c in ["Red", "Blue", "Green", "Yellow"]:
            self.cards.append(Card(c, 0))

            for v in range(1,10):
                self.cards.append(Card(c, v))
                self.cards.append(Card(c, v))

            for v in ["Reverse", "Skip", "Draw 2"]:
                self.cards.append(Card(c, v))
                self.cards.append(Card(c, v))

        for x in range(4):
            self.cards.append(Card("Black", "Wild"))
            self.cards.append(Card("Black", "Draw 4"))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop(0)

    #discard pile only method
    def add(self, card):
        while card.color == "Black":
            new_col = input("What color would you like to change it to?: ").capitalize()
            if new_col not in "Red Green Blue Yellow":
                print("Invalid color.")
            else:
                card.color = new_col
        self.cards.append(card)
        
