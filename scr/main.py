from Blackjack.scr.deck import Deck
from Blackjack.scr.player import Player
from Blackjack.scr.dealer import Dealer
from time import sleep


def split_func(player, deck):
    global player_left, player_right
    player_left = player.Player('player left')
    player_right = player.Player('player right')

    print('\n---left')
    player_left.hand.set_hand(player.hand.hand[0])
    player_left.hand.set_hand(deck.draw_card())
    player_left.hand.done_split = True
    player_turn(player_left, deck)

    print('\n--right')
    player_right.hand.set_hand(player.hand.hand[1])
    player_right.hand.set_hand(deck.draw_card())
    player_right.hand.done_split = True
    player_turn(player_right, deck)


def player_turn(player, deck):
    while True:
        player.display_score()
        if player.hand.is_busted():
            break
        print()
        player_intention = player.input_player_intention()
        if player_intention == 'hit':
            player.hand.set_hand(deck.draw_card())
        elif player_intention in ['double down', 'doubledown', 'double']:
            player.hand.set_hand(deck.draw_card())
            player.display_score()
            break
        elif player_intention == 'split':
            player.done_split = True
            split_func(player, deck)
            break
        elif player_intention == 'stand':
            player.display_score()
            break


def dealer_turn(dealer, deck):
    dealer.display_hole_card()

    while dealer.is_continue():
        dealer.display_score()
        dealer.hand.set_hand(deck.draw_card())
    dealer.display_score()


def display_result(player1, player2):
    player1.display_score()
    player2.display_score()
    print('-' * 100)

    if player1.hand.is_natural_blackjack() and player2.hand.is_natural_blackjack():
        print('引き分け')

    elif player1.hand.is_natural_blackjack():
        print('{} is natural black jack'.format(player1.name))
        print('あなたの勝ちです')

    elif player2.hand.is_natural_blackjack():
        print('{} is natural black jack'.format(player2.name))
        print('あなたの負けです')

    elif player1.hand.is_busted():
        print('あなたの負けです')

    elif player2.hand.is_busted():
        print('あなたの勝ちです')

    elif player1.hand.calculate_total_score() > player2.hand.calculate_total_score():
        print('あなたの勝ちです')

    elif player2.hand.calculate_total_score() > player1.hand.calculate_total_score():
        print('あなたの負けです')

    elif player1.hand.calculate_total_score() == player2.hand.calculate_total_score():
        print('引き分け')


def play():
    deck = Deck()
    player = Player('player')
    dealer = Dealer('dealer')
    print('-' * 100)
    player.hand.set_hand(deck.draw_card())
    player.hand.set_hand(deck.draw_card())
    print('-' * 100)
    dealer.hand.set_hand(deck.draw_card())  # UP CARD
    dealer.hand.set_hand(deck.draw_card(), display=False)  # HOLE CARD
    print('-' * 100 + '\n')

    player_turn(player, deck)
    print()

    dealer_turn(dealer, deck)

    print('\n' + '-' * 100)
    sleep(2)

    if player.done_split:
        display_result(player_left, dealer)
        print('-' * 100)
        print()
        display_result(player_right, dealer)

    else:
        display_result(player, dealer)


def _main():
    play()


if __name__ == '__main__':
    _main()
