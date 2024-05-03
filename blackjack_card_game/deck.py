from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for suit_num in range(0, 4):
            for val_num in range(1, 14):
                self.cards.append(Card(val_num, suit_num))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, num_cards):
        cards = self.cards[-num_cards:]
        self.cards = self.cards[:-num_cards]

        return cards

deck = Deck()