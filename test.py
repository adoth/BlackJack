import unittest
from blackjack import Participant
from blackjack import Player


participant = Participant('player1')
player = Player('player1')


class TestParticipant(unittest.TestCase):
    def test_num_suit_rank(self):
        self.assertEqual(participant.get_num_suit_rank(101),
                         (1, 1))
        self.assertEqual(participant.get_num_suit_rank(310),
                         (3, 10))
        self.assertEqual(participant.get_num_suit_rank(411),
                         (4, 10))
        self.assertEqual(participant.get_num_suit_rank(312),
                         (3, 10))

    def test_get_display_suit_rank(self):
        self.assertEqual(participant.get_display_suit_rank(101),
                         ('ハート', 'A'))
        self.assertEqual(participant.get_display_suit_rank(205),
                         ('スペード', '5'))
        self.assertEqual(participant.get_display_suit_rank(312),
                         ('ダイヤ', 'Q'))
        self.assertEqual(participant.get_display_suit_rank(411),
                         ('クラブ', 'J'))
        self.assertEqual(participant.get_display_suit_rank(113),
                         ('ハート', 'K'))

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
        player.hand = [101, 201]
        self.assertTrue(player.can_split())

    def test_can_split_true2(self):
        player.hand = [412, 410]
        self.assertTrue(player.can_split())

    def test_can_split_false(self):
        player.hand = [409, 109, 209]
        self.assertFalse(player.can_split())

    def test_can_double_down_true1(self):
        player.hand = [101, 102]
        player.credit = 1000
        player.bet = 100
        self.assertTrue(player.can_double_down())

    def test_can_double_down_false1(self):
        player.hand = [101, 102, 103]
        player.credit = 1000
        player.bet = 100
        self.assertFalse(player.can_double_down())

    def test_can_double_down_false2(self):
        player.hand = [101, 102]
        player.credit = 300
        player.bet = 700
        self.assertFalse(player.can_double_down())


if __name__ == '__main__':
    unittest.main()
