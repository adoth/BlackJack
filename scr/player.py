from Blackjack.scr.hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.done_split = False

    def set_hand(self, card):
        self.hand.set_hand(card)

    def can_split(self):
        if self.done_split or len(self.hand.hand) > 2:
            return False
        return self.hand.hand[0].num_rank == self.hand.hand[1].num_rank

    def can_double_down(self):
        return len(self.hand.hand) == 2

    def input_player_intention(self):
        display_words = {(True, True): 'HIT or STAND or Double Down or Split?\n>',
                         (False, True): 'HIT or STAND or Double Down?\n>',
                         (False, False): 'HIT or STAND?\n>'}

        correct_response = {(True, True): ['hit', 'stand', 'double down', 'doubledown', 'double', 'split'],
                            (False, True): ['hit', 'stand', 'double down', 'doubledown', 'double'],
                            (False, False): ['hit', 'stand']}

        while True:
            can_split = self.can_split()
            can_double_down = self.can_double_down()
            player_intention = input(display_words[(can_split, can_double_down)]).lower()

            if player_intention in correct_response[(can_split, can_double_down)]:
                return player_intention

    def display_score(self):
        print("{} のスコアは {}".format(self.name, self.hand.calculate_total_score()))
