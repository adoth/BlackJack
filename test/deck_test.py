from Blackjack.src.deck import Deck
import unittest


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_loop_draw(self):
        for _ in range(100):
            self.deck.draw_card()
