from Blackjack.scr.deck import Deck
from Blackjack.scr.player import Player
from Blackjack.scr.dealer import Dealer


class Game:
    def __init__(self):
        self.player = Player('player')
        self.dealer = Dealer('dealer')
        self.deck = Deck()
        self.player_left = self.player_right = None

    def play(self):
        self.first_turn(self.player)
        self.first_turn(self.dealer)

        self.player_turn(self.player)
        self.dealer_turn()

        self.result()

    def first_turn(self, player):
        player.hand.set_hand(self.deck.draw_card())
        if type(player) == Dealer:
            player.hand.set_hand(self.deck.draw_card(), display=False)
        else:
            player.hand.set_hand(self.deck.draw_card())

    def split_func(self, player):
        self.player_left = Player('player left')
        self.player_right = Player('player right')

        print('\n---left')
        self.player_left.hand.set_hand(player.hand.hand[0])
        self.player_left.hand.set_hand(self.deck.draw_card())
        self.player_left.hand.done_split = True
        self.player_turn(self.player_left)

        print('\n--right')
        self.player_right.hand.set_hand(player.hand.hand[1])
        self.player_right.hand.set_hand(self.deck.draw_card())
        self.player_right.hand.done_split = True
        self.player_turn(self.player_right)

    def player_turn(self, player):
        while True:
            player.display_score()
            if player.hand.is_busted():
                break
            print()

            player_intention = player.input_player_intention()

            if player_intention == 'hit':
                player.hand.set_hand(self.deck.draw_card())
            elif player_intention in ['double down', 'doubledown', 'double']:
                player.hand.set_hand(self.deck.draw_card())
                player.display_score()
                break
            elif player_intention == 'split':
                player.done_split = True
                self.split_func(player)
                break
            elif player_intention == 'stand':
                player.display_score()
                break

    def dealer_turn(self):
        self.dealer.display_hole_card()

        while self.dealer.is_continue():
            self.dealer.display_score()
            self.dealer.hand.set_hand(self.deck.draw_card())
        self.dealer.display_score()

    def display_result(self, player1):
        player1.display_score()
        self.dealer.display_score()
        print('-' * 100)

        if player1.hand.is_natural_blackjack() and self.dealer.hand.is_natural_blackjack():
            print('引き分け')

        elif player1.hand.is_natural_blackjack():
            print('{} is natural black jack'.format(player1.name))
            print('あなたの勝ちです')

        elif self.dealer.hand.is_natural_blackjack():
            print('{} is natural black jack'.format(self.dealer.name))
            print('あなたの負けです')

        elif player1.hand.is_busted():
            print('あなたの負けです')

        elif self.dealer.hand.is_busted():
            print('あなたの勝ちです')

        elif player1.hand.calculate_total_score() > self.dealer.hand.calculate_total_score():
            print('あなたの勝ちです')

        elif self.dealer.hand.calculate_total_score() > player1.hand.calculate_total_score():
            print('あなたの負けです')

        elif player1.hand.calculate_total_score() == self.dealer.hand.calculate_total_score():
            print('引き分け')

    def result(self):
        if self.player.done_split:
            self.display_result(self.player_left)
            print('-' * 100)
            print()
            self.display_result(self.player_right)

        else:
            self.display_result(self.player)


if __name__ == '__main__':
    Game().play()
