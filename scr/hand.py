from itertools import product


class Hand:
    def __init__(self):
        self.hand = []

    def set_hand(self, card, *, display=True):
        if display:
            print("{} - {}".format(card.display_suit, card.display_rank))
        else:
            print("you can't see HOLE CARD")

        self.hand.append(card)

    def calculate_total_score(self):
        list_for_calculating_score = [card.num_rank for card in self.hand]
        ace = [rank for rank in list_for_calculating_score if type(rank) is tuple]
        if not ace:
            return sum(list_for_calculating_score)
        else:
            except_ace_score = sum([rank for rank in list_for_calculating_score if type(rank) is not tuple])
            ace_score = [sum(x) for x in product(*ace)]
            score = [ace_score[i] + except_ace_score for i in range(len(ace_score))]
            under_21_score = [i for i in score if i <= 21]
            if under_21_score:
                return max(under_21_score)
            else:
                return min(score)

    def is_busted(self):
        return self.calculate_total_score() > 21

    def is_natural_blackjack(self):
        if len(self.hand) == 2:
            first_card = self.hand[0].num_rank
            second_card = self.hand[1].num_rank
            if (first_card == 10 and second_card == (1, 11)) or (first_card == (1, 11) and second_card == 10):
                return True
        return False
