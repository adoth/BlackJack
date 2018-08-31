from Blackjack.scr.hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.done_split = False

    def can_split(self):
        if self.done_split or len(self.hand.hand) > 2:
            return False
        return self.hand.hand[0].num_rank == self.hand.hand[1].num_rank

    def can_double_down(self):
        return len(self.hand.hand) == 2

    def input_player_intention(self):
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

    def display_score(self):
        print("{} のスコアは {}".format(self.name, self.hand.calculate_total_score()))
