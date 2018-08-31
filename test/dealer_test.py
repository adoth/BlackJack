from Blackjack.scr.dealer import Dealer
from Blackjack.scr.card import Card
import unittest


class TestDealer(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer("dealer")

    def test_is_continue(self):
        data = [
            ([Card(103), Card(204), Card(205)], True),
            ([Card(101), Card(403), Card(405), Card(206)], True),
            ([Card(101), Card(202), Card(404)], False),
            ([Card(101), Card(408), Card(105), Card(303)], False),
            ([Card(101), Card(112)], False),
            ([Card(101), Card(108), Card(202)], False)
        ]

        for handlist, actual in data:
            with self.subTest(handlist=handlist, actual=actual):
                self.dealer.hand.hand = handlist
                self.assertIs(self.dealer.is_continue(), actual)


if __name__ == '__main__':
    unittest.main()
