from Deck import *
import random

class AI:
    def __init__(self):
        self.hand = []

    def turn(self, card):
        playable_cards = []
        for c in self.hand:
            if c.color == card.color or c.value == card.value or c.color == "Black":
                playable_cards.append(c)

        if len(playable_cards) > 0:
            chosen = random.choice(playable_cards)
            self.hand.remove(chosen)
            if chosen.color == "Black":
                chosen.color = random.choice(["Red", "Green", "Blue", "Yellow"])
            return chosen
        return "draw"
