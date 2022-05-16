from card import Card
class Player:
    def __init__(self):
        self.cards =[]
    def take_cards(self, card:Card):
        self.cards.append(card)
    def show_cards(self):
        return self.cards

    def score(self):
        sum = 0
        sum_A =0
        sum_F = 0
        for card in self.cards:
            if card.name in ['J','K','Q']:
                sum += 10
                sum_F +=1

            if card.name in ['2','3','4','5','6','7','8','9','10']:
                sum += int(card.name)
            if card.name == "A":
                sum_A += 1
        if sum_A == 2 or (sum_A == 1 and sum_F == 1):
            sum = 21
        return sum



