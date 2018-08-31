from Blackjack.scr.hand import Hand
from Blackjack.scr.card import Card
import unittest


class TestHand(unittest.TestCase):
    def setUp(self):
        self.testHand = Hand()

    def test_calculate_total_score(self):
        data = (
            ([Card(101), Card(112)], 21),
            ([Card(113), Card(212), Card(402)], 22),
            ([Card(101), Card(201), Card(301), Card(401)], 14),
            ([Card(101), Card(301), Card(103)], 15),
            ([Card(101), Card(301), Card(210)], 12),
            ([Card(101), Card(301), Card(304), Card(313), Card(408)], 24)
        )

        for handlist, actual in data:
            with self.subTest(handlist=handlist, actual=actual):
                self.testHand.hand = handlist
                self.assertEqual(self.testHand.calculate_total_score(), actual)

    def test_is_busted(self):
        data = (
            ([Card(301), Card(110)], False),
            ([Card(213), Card(401), Card(202)], False),
            ([Card(101), Card(201), Card(301), Card(401)], False),
            ([Card(201), Card(101), Card(103)], False),
            ([Card(401), Card(201), Card(113)], False),
            ([Card(101), Card(401), Card(204), Card(310), Card(308)], True),
            ([Card(205), Card(105), Card(102), Card(405), Card(206)], True)
        )

        for handlist, actual in data:
            with self.subTest(handlist=handlist, actual=actual):
                self.testHand.hand = handlist
                self.assertIs(self.testHand.is_busted(), actual)

    def test_is_natural_blackjack(self):
        data = [
            ([Card(301), Card(112)], True),
            ([Card(313), Card(301)], True),
            ([Card(301), Card(213), Card(102)], False),
            ([Card(301), Card(303), Card(207)], False),
            ([Card(408), Card(203), Card(102), Card(406), Card(302)], False)
        ]

        for handlist, actual in data:
            with self.subTest(hanlist=handlist, actual=actual):
                self.testHand.hand = handlist
                self.assertIs(self.testHand.is_natural_blackjack(), actual)


if __name__ == '__main__':
    unittest.main()
