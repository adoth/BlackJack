from random import shuffle
from time import sleep


SUIT = {
    1: '　ハート　',
    2: 'スペード　',
    3: '　ダイヤ　',
    4: 'クローバー'
}

RANK = {
    1: 'A',
    11: 'J',
    12: 'Q',
    13: 'K'
}


class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.deck.append(suit*100 + rank)
        shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()


class Participant:
    def __init__(self, name):
        self.name = name
        self.rank = []
        self.draw_card_history = []

    def get_sum(self):
        return sum(self.rank)

    def get_suit_rank(self, card):
        num_suit = card // 100
        num_rank = card % 100
        display_suit = SUIT[num_suit]
        display_rank = RANK.get(num_rank, str(num_rank))
        return num_suit, num_rank, display_suit, display_rank

    def set_hand(self, card, *, display=True):
        _, num_rank, display_suit, display_rank = self.get_suit_rank(card)
        if display:
            print('{} の引いたカードは {} の {} です'.format(self.name, display_suit, display_rank))
        else:
            print('{} の引いたカードはわかりません'.format(self.name))
        self.rank.append(min(num_rank, 10))
        self.draw_card_history.append(card)

    def is_busted(self):
        return sum(self.rank) > 21

    def display_suit_rank(self, n):
        card = self.draw_card_history[n-1]
        _, _, display_suit, display_rank = self.get_suit_rank(card)
        print('{} が引いた {} 枚目のカードは {} の {} です'.format(self.name, n, display_suit, display_rank))


class Player(Participant):
    def is_double_down(self):
        print('{} のスコアは {}'.format(self.name, sum(self.rank)))
        return input('Double Down?\nyes or no\n>').lower() in ['yes', 'y', 'doubledown', 'double down']

    def is_continue(self):
        print('{} のスコアは {}'.format(self.name, sum(self.rank)))
        while True:
            input_word = input('HIT or STAND\n>').lower()
            if input_word == 'hit' or input_word == 'stand':
                return input_word


class Dealer(Participant):
    def is_continue(self):
        print('{} のスコアは {}'.format(self.name, sum(self.rank)))
        return self.get_sum() < 17


def game_result(player1, playe2):
    print('{} のスコアは {}'.format(player1.name, player1.get_sum()))
    print('{} のスコアは {}'.format(player2.name, player2.get_sum()))

    if player1.is_busted():
        print('あなたの負けです')
    elif player2.is_busted():
        print('あなたの勝ちです')
    elif player1.get_sum() > player2.get_sum():
        print('あなたの勝ちです')
    elif player2.get_sum() > player1.get_sum():
        print('あなたの負けです')
    elif player1.get_sum() == player2.get_sum():
        print('引き分け')


def play():

    deck = Deck()
    player = Player('player')
    dealer = Dealer('dealer')
    division = 1
    player.set_hand(deck.draw_card())
    player.set_hand(deck.draw_card())
    print('-' * 100)
    dealer.set_hand(deck.draw_card())  # UP CARD
    dealer.set_hand(deck.draw_card(), display=False)  # HOLE CARD
    print('-' * 100 + '\n')

    if player.is_double_down():
        player.set_hand(deck.draw_card())
        division = 1.5
    else:
        while player.is_continue():
            player.set_hand(deck.draw_card())
            if player.is_busted():
                break

    print()

    dealer.display_suit_rank(2)
    while dealer.is_continue():
        sleep(3)
        dealer.set_hand(deck.draw_card())
    print('\n' + '-' * 100)
    game_result(player, dealer)


def main():
    play()


if __name__ == '__main__':
    main()