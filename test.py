import unittest
from blackjack import Participant
from blackjack import Player
from blackjack import Card


participant = Participant('player1')
player = Player('player1')


class TestCard(unittest.TestCase):
    def test_num_suit(self):
        self.assertEqual(Card(101).num_suit, 1)
        self.assertEqual(Card(201).num_suit, 2)
        self.assertEqual(Card(301).num_suit, 3)
        self.assertEqual(Card(401).num_suit, 4)

    def test_num_rank(self):
        self.assertEqual(Card(101).num_rank, (1, 11))
        self.assertEqual(Card(105).num_rank, 5)
        self.assertEqual(Card(110).num_rank, 10)
        self.assertEqual(Card(111).num_rank, 10)
        self.assertEqual(Card(112).num_rank, 10)
        self.assertEqual(Card(113).num_rank, 10)

    def test_display_suit(self):
        self.assertEqual(Card(101).display_suit, "ハート")
        self.assertEqual(Card(201).display_suit, "スペード")
        self.assertEqual(Card(301).display_suit, "ダイヤ")
        self.assertEqual(Card(401).display_suit, "クラブ")

    def test_display_rank(self):
        self.assertEqual(Card(101).display_rank, "A")
        self.assertEqual(Card(105).display_rank, "5")
        self.assertEqual(Card(110).display_rank, "10")
        self.assertEqual(Card(111).display_rank, "J")
        self.assertEqual(Card(112).display_rank, "Q")
        self.assertEqual(Card(113).display_rank, "K")


class TestParticipant(unittest.TestCase):
    def test_include_ace_and_just_twenty_one(self):
        participant.rank = [(1, 11), 10]
        actual = participant.get_score()
        self.assertEqual(21, actual)

    def test_just_twenty_one(self):
        participant.rank = [2, 10, 9]
        actual = participant.get_score()
        self.assertEqual(21, actual)

    def test_not_include_ace_sum(self):
        participant.rank = [10, 10]
        actual = participant.get_score()
        self.assertEqual(20, actual)

    def test_include_two_ace(self):
        participant.rank = [(1, 11), (1, 11)]
        actual = participant.get_score()
        self.assertEqual(12, actual)

    def test_include_two_ace_lower_twenty_one(self):
        participant.rank = [(1, 11), (1, 11), 3]
        actual = participant.get_score()
        self.assertEqual(15, actual)

    def test_include_two_ace_not_over_twenty_one(self):
        participant.rank = [(1, 11), (1, 11), 10]
        actual = participant.get_score()
        self.assertEqual(12, actual)

    def test_three_ace_over_twenty_one(self):
        participant.rank = [(1, 11), 10, (1, 11), 10, (1, 11)]
        self.assertEqual(participant.get_score(), 23)

    def test_natural_black_jack_true1(self):
        participant.rank = [(1, 11), 10]
        self.assertTrue(participant.is_natural_black_jack())

    def test_natural_black_jack_true2(self):
        participant.rank = [10, (1, 11)]
        self.assertTrue(participant.is_natural_black_jack())

    def test_natural_black_jack_false1(self):
        participant.rank = [10, 10]
        self.assertFalse(participant.is_natural_black_jack())

    def test_natural_black_jack_false2(self):
        participant.rank = [(1, 11), 10, 10]
        self.assertFalse(participant.is_natural_black_jack())

    def test_natural_black_jack_false3(self):
        participant.rank = [9, 2, 10]
        self.assertFalse(participant.is_natural_black_jack())


class TestPlayer(unittest.TestCase):
    def test_can_split_true1(self):
        player.rank = [1, 1]
        self.assertTrue(player.can_split())

    def test_can_split_true2(self):
        player.rank = [10, 10]
        self.assertTrue(player.can_split())

    def test_can_split_false(self):
        player.rank = [9, 9, 9]
        self.assertFalse(player.can_split())

    def test_can_double_down_true1(self):
        player.rank = [1, 2]
        player.balance = 1000
        player.bet = 100
        self.assertTrue(player.can_double_down())

    def test_can_double_down_false1(self):
        player.rank = [1, 2, 3]
        player.balance = 1000
        player.bet = 100
        self.assertFalse(player.can_double_down())

    def test_can_double_down_false2(self):
        player.rank = [1, 2]
        player.balance = 300
        player.bet = 700
        self.assertFalse(player.can_double_down())


if __name__ == '__main__':
    unittest.main()
