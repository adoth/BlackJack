from Blackjack.scr.card import Card
import unittest


class TestCard(unittest.TestCase):
    def test_num_suit(self):
        data = [
            (101, 1),
            (201, 2),
            (301, 3),
            (401, 4)
        ]

        for number, actual in data:
            self.assertEqual(Card(number).num_suit, actual)

    def test_num_rank(self):
        data = [
            (101, (1, 11)),
            (105, 5),
            (110, 10),
            (211, 10),
            (312, 10),
            (313, 10)
        ]

        for number, actual in data:
            self.assertEqual(Card(number).num_rank, actual)

    def test_display_suit(self):
        data = [
            (101, "ハート"),
            (201, "スペード"),
            (301, "ダイヤ"),
            (401, "クラブ")
        ]

        for number, actual in data:
            self.assertEqual(Card(number).display_suit, actual)

    def test_display_rank(self):
        data = [
            (101, "A"),
            (105, "5"),
            (110, "10"),
            (111, "J"),
            (112, "Q"),
            (113, "K")
            ]

        for number, actual in data:
            self.assertEqual(Card(number).display_rank, actual)


if __name__ == '__main__':
    unittest.main()
