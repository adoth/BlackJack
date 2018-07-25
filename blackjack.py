from random import shuffle
from itertools import product

SUITS = {
    1: '　ハート　',
    2: 'スペード　',
    3: '　ダイヤ　',
    4: 'クローバー'
}

RANKS = {
    1: 'A',
    11: 'J',
    12: 'Q',
    13: 'K'
}


class Deck:
    def __init__(self):
        self.__deck = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.__deck.append(suit * 100 + rank)
        shuffle(self.__deck)

    def draw_card(self):
        return self.__deck.pop()


class Participant:
    def __init__(self, name):
        self.count_cards = 0
        self.name = name
        self.rank = []
        self.draw_card_history = []

    def get_sum(self):
        ace = [rank for rank in self.rank if type(rank) is tuple]
        if not ace:
            return sum(self.rank)
        else:
            except_ace_score = sum([rank for rank in self.rank if type(rank) is not tuple])
            ace_score = [sum(x) for x in product(*ace)]
            score = [ace_score[i] + except_ace_score for i in range(len(ace_score))]
            under_21_score = [i for i in score if i <= 21]
            if under_21_score:
                return max(under_21_score)
            else:
                return min(score)

    def is_busted(self):
        return self.get_sum() > 21

    def is_natural_black_jack(self):
        if len(self.rank) == 2:
            first_card = self.rank[0]
            second_card = self.rank[1]
            if (first_card == 10 and second_card == (1, 11)) or (first_card == (1, 11) and second_card == 10):
                return True
        return False

    @staticmethod
    def get_num_suit_rank(card):
        suit = card // 100
        rank = min(10, card % 100)
        return suit, rank

    @staticmethod
    def get_display_suit_rank(card):
        suit = card // 100
        rank = card % 100
        display_suit = SUITS[suit]
        display_rank = RANKS.get(rank, str(rank))
        return display_suit, display_rank

    def set_hand(self, card):
        num_suit, num_rank = self.get_num_suit_rank(card)
        if num_rank == 1:
            self.rank.append((1, 11))
        else:
            self.rank.append(num_rank)
        self.draw_card_history.append(card)
        self.count_cards += 1

    def display_draw_card(self, n, *, display=True):
        display_suit, display_rank = self.get_display_suit_rank(self.draw_card_history[n - 1])
        if display:
            print('{} の引いたカードは {} の {} です'.format(self.name, display_suit, display_rank))
        else:
            print('{} の引いたカードはわかりません'.format(self.name))

    def display_score(self):
        print('{} のスコアは {}'.format(self.name, self.get_sum()))


class Player(Participant):
    def __init__(self, name):
        super().__init__(name)
        self.split = False
        self.double_down = False

    def can_split(self):
        _, first_card_rank = self.get_num_suit_rank(self.draw_card_history[0])
        _, second_card_rank = self.get_num_suit_rank(self.draw_card_history[1])
        return first_card_rank == second_card_rank and len(self.draw_card_history) == 2

    def get_player_intention(self):
        while True:
            if self.can_split():
                player_intention = input('HIT or STAND or Double Down or Split?\n>').lower()
                if player_intention in ['hit', 'stand', 'double down', 'doubledown', 'double', 'split']:
                    return player_intention
            elif self.count_cards == 2:
                player_intention = input('HIT or STAND or Double Down?\n>').lower()
                if player_intention in ['hit', 'stand', 'double down', 'doubledown', 'double']:
                    return player_intention
            else:
                player_intention = input('HIT or STAND?\n>').lower()
                if player_intention in ['hit', 'stand']:
                    return player_intention


class Dealer(Participant):
    def display_hole_card(self):
        card = self.draw_card_history[1]
        display_suit, display_rank = self.get_display_suit_rank(card)
        print('{} の HOLE CARD は {} の {} です'.format(self.name, display_suit, display_rank))

    def is_continue(self):
        return self.get_sum() < 17
