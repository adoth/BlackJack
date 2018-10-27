from Blackjack.scr.hand import Hand


class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def set_hand(self, card, display=True):
        self.hand.set_hand(card, display=display)

    def display_hole_card(self):
        card = self.hand.hand[1]
        print("{} の HOLE CARD は {} の {} です。".format(self.name, card.display_suit, card.display_rank))

    def is_continue(self):
        return self.hand.calculate_total_score() < 17

    def display_score(self):
        print("{} のスコアは {}".format(self.name, self.hand.calculate_total_score()))
