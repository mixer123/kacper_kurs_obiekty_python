from card import Card
from random import shuffle



class Talia:
    def __init__(self):
        self.card =[]
        for color in Card.possible_colors:
            for value in Card.possible_values:
                self.card.append(Card(name=value, color=color))
    def shuffle(self):
      shuffle(self.card)
    def hit(self):
        return self.card.pop()


    def __str__(self):
        return self.card
#
# talia = Talia()
# print(talia.card)
# for i in talia.card:
#     print(i.name, i.color)