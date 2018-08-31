from Blackjack.scr.player import Player
from Blackjack.scr.card import Card
import unittest


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_name = "Player"
        self.player = Player(self.player_name)

    def test_can_split(self):
        data = (
            ([Card(101), Card(201)], True),
            ([Card(112), Card(413)], True),
            ([Card(109), Card(209), Card(309)], False)
        )

        for handlist, actual in data:
            with self.subTest(handlist=handlist, actual=actual):
                self.player.hand.hand = handlist
                self.assertEqual(self.player.can_split(), actual)

    def test_can_double_down(self):
        data = (
            ([Card(101), Card(201)], True),
            ([Card(112), Card(413)], True),
            ([Card(109), Card(209), Card(309)], False)
        )

        for handlist, actual in data:
            with self.subTest(handlist=handlist, actual=actual):
                self.player.hand.hand = handlist
                self.assertEqual(self.player.can_double_down(), actual)


if __name__ == '__main__':
    unittest.main()
