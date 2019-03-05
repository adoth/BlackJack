from random import shuffle

from Blackjack.src.card import Card


class Deck:
    def __init__(self):
        self.__deck = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.__deck.append(Card(suit * 100 + rank))
        shuffle(self.__deck)

    def draw_card(self):
        try:
            return self.__deck.pop()
        except IndexError:
            self.__init__()
