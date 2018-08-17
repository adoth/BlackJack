from random import shuffle
from itertools import product


# ******************** Card Class ********************

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
        self.card = number
        self.num_suit = number // 100
        self.num_rank = [min(10, number % 100), (1, 11)][number % 100 == 1]
        self.display_suit = Card.SUITS[number // 100]
        self.display_rank = Card.RANKS.get(number % 100, str(number % 100))


# ******************** Deck Class ********************


class Deck:
    def __init__(self):
        self.__deck = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.__deck.append(Card(suit * 100 + rank))
        shuffle(self.__deck)

    def draw_card(self):
        return self.__deck.pop()


# ******************** Participant Class ********************


class Participant:
    def __init__(self, name):
        self.name = name
        self.rank = []
        self.hand = []

    def set_hand(self, card, *, display=True):
        if display:
            print('{} の引いたカードは {} の {} です'.format(self.name, card.display_suit, card.display_rank))
        else:
            print('{} の引いたカードはわかりません'.format(self.name))

        self.rank.append(card.num_rank)
        self.hand.append(card)

    def get_score(self):
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
        return self.get_score() > 21

    def is_natural_black_jack(self):
        if len(self.rank) == 2:
            first_card = self.rank[0]
            second_card = self.rank[1]
            if (first_card == 10 and second_card == (1, 11)) or (first_card == (1, 11) and second_card == 10):
                return True
        return False

    def display_score(self):
        print('{} のスコアは {}'.format(self.name, self.get_score()))


# ******************** Player Class ********************

class Player(Participant):
    def __init__(self, name, balance=0, bet=0):
        super().__init__(name)
        self.balance = balance - bet
        self.bet = bet
        self.done_split = False

    def can_split(self):
        if self.done_split or len(self.rank) > 2:
            return False
        return self.rank[0] == self.rank[1] and self.balance >= self.bet

    def can_double_down(self):
        return len(self.rank) == 2 and self.balance >= self.bet

    def get_player_intention(self):
        while True:
            if self.can_split() and self.can_double_down():
                player_intention = input('HIT or STAND or Double Down or Split?\n>').lower()
                if player_intention in ['hit', 'stand', 'double down', 'doubledown', 'double', 'split']:
                    return player_intention
            elif self.can_double_down():
                player_intention = input('HIT or STAND or Double Down?\n>').lower()
                if player_intention in ['hit', 'stand', 'double down', 'doubledown', 'double']:
                    return player_intention
            else:
                player_intention = input('HIT or STAND?\n>').lower()
                if player_intention in ['hit', 'stand']:
                    return player_intention


# ******************** Dealer Class ********************

class Dealer(Participant):
    def display_hole_card(self):
        card = self.hand[1]
        print('{} の HOLE CARD は {} の {} です'.format(self.name, card.display_suit, card.display_rank))

    def is_continue(self):
        return self.get_score() < 17
