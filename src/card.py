class Card:
    SUITS = {
        1: 'ハート',
        2: 'スペード',
        3: 'ダイヤ',
        4: 'クラブ'
    }

    RANKS = {
        1: 'A',
        11: 'J',
        12: 'Q',
        13: 'K'
    }

    def __init__(self, number):
        self.num_suit = number // 100
        self.num_rank = [min(10, number % 100), (1, 11)][number % 100 == 1]
        self.display_suit = Card.SUITS[number // 100]
        self.display_rank = Card.RANKS.get(number % 100, str(number % 100))
