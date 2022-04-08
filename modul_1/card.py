from random import shuffle
class Card:
    possible_values = ['2','3','4','5','6','7','8','9','10', 'J','K','A','Q']
    possible_colors = {
        'sapdes':'\u2664',
        'diamonds':'\u2662',
        'hearts':'\u2661',
        'clubs':'\u2667'
    }
    def __init__(self, name, color):
        self.color = self.possible_colors[color]
        self.name = name


    def __str__(self):
        self.name
