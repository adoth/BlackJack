from blackjack import Deck, Player, Dealer
from time import sleep


def split_func(player, deck):
    # TODO: split時の credit
    global player_left_hand, player_right_hand
    player_left_hand = Player('player left', player.credit, player.bet)
    player_right_hand = Player('player right', player.credit, player.bet)

    print('\n---left')
    player_left_hand.set_hand(player.hand[0])
    player_left_hand.set_hand(deck.draw_card())
    player_left_hand.done_split = True
    player_turn(player_left_hand, deck)

    print('\n--right')
    player_right_hand.set_hand(player.hand[1])
    player_right_hand.set_hand(deck.draw_card())
    player_right_hand.done_split = True
    player_turn(player_right_hand, deck)


def player_turn(player, deck):
    while True:
        player.display_score()
        player_intention = player.get_player_intention()

        if player_intention == 'hit':
            player.set_hand(deck.draw_card())
        elif player_intention in ['double down', 'doubledown', 'double']:
            player.credit -= player.bet
            player.bet *= 2
            player.set_hand(deck.draw_card())
            player.display_score()
            break
        elif player_intention == 'split':
            player.done_split = True
            split_func(player, deck)
            break
        if player_intention == 'stand' or player.is_busted():
            player.display_score()
            break


def dealer_turn(dealer, deck):
    dealer.display_hole_card()

    while dealer.is_continue():
        dealer.display_score()
        dealer.set_hand(deck.draw_card())
    dealer.display_score()


def get_division_and_print_result(player1, player2):
    player1.display_score()
    player2.display_score()
    print('-' * 100)

    if player1.is_natural_black_jack() and player2.is_natural_black_jack():
        print('引き分け')
        return 1
    elif player1.is_natural_black_jack():
        print('{} is natural black jack'.format(player1.name))
        print('あなたの勝ちです')
        return 2.5
    elif player2.is_natural_black_jack():
        print('{} is natural black jack'.format(player2.name))
        print('あなたの負けです')
        return 0
    elif player1.is_busted():
        print('あなたの負けです')
        return 0
    elif player2.is_busted():
        print('あなたの勝ちです')
        return 2
    elif player1.get_score() > player2.get_score():
        print('あなたの勝ちです')
        return 2
    elif player2.get_score() > player1.get_score():
        print('あなたの負けです')
        return 0
    elif player1.get_score() == player2.get_score():
        print('引き分け')
        return 1


def play():
    deck = Deck()
    player = Player('player', 1000, 500)
    dealer = Dealer('dealer')

    print('-' * 100)
    player.set_hand(deck.draw_card())
    player.set_hand(deck.draw_card())
    print('-' * 100)
    dealer.set_hand(deck.draw_card())  # UP CARD
    dealer.set_hand(deck.draw_card(), display=False)  # HOLE CARD
    print('-' * 100 + '\n')

    player_turn(player, deck)

    print()

    dealer_turn(dealer, deck)

    print('\n' + '-' * 100)
    sleep(2)

    if player.done_split:
        division = get_division_and_print_result(player_left_hand, dealer)

        player.credit += player.bet * division
        print('you get {}'.format(player.bet * division))
        print('-' * 100)
        print()
        division = get_division_and_print_result(player_right_hand, dealer)
        player.credit += player.bet * division
        print('you get {}'.format(player.bet * division))
    else:
        division = get_division_and_print_result(player, dealer)
        player.credit += player.bet * division
        print('you get {}'.format(player.bet * division))

    print(player.credit)


def _main():
    play()


if __name__ == '__main__':
    _main()
