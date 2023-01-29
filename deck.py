import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []  # generate empty list of cards

    # generate the deck by looping through the list 52 times
    def generate_deck(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j))

    # counts the amount of cards in the deck
    def count_deck(self):
        return len(self.cards)

    # function that removes card from the deck at random and returns a list of cards
    def draw_card(self, iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards
