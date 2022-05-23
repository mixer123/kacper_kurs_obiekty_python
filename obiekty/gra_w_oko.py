from card import Card
from talia import Talia
from player import Player

class Game:
    def __init__(self):
        self.deck = Talia()
        self.deck.shuffle()
    def play(self):
        key = None
        user = Player()
        card = self.deck.hit()
        user.take_cards(card)
        card = self.deck.hit()
        user.take_cards(card)

        print('User karty')
        for i in user.cards:
            print(i.name, i.color)
        print('user ma ', user.score())
        croupier = Player()
        card = self.deck.hit()
        croupier.take_cards(card)
        card = self.deck.hit()
        croupier.take_cards(card)
        print('Croupier karty')
        for i in croupier.cards:
            print(i.name, i.color)
        print('Croupier ma ', croupier.score())
        while key != 'q' or None:
            if user.score() > 21 :
                print('Koniec gry')
                if croupier.score() > user.score() and croupier.score() < 21:
                    print('Croupier wygrał')
                    break
                else:
                    print('User wygrał')
                break
            else:
                key = input(' q=exit Grasz dalej ??')
                if key !='q':
                    card = self.deck.hit()
                    user.take_cards(card)
                    user.score()
                    print('user ma ', user.score())
                if croupier.score() > user.score() and croupier.score() < 21:
                    print(f'Croupier wygrał. User ma {user.score()} Croupier ma {croupier.score()} ')
                    break
                else:
                    print(f'User wygrał. User ma {user.score()} Croupier ma {croupier.score()} ')
                    break


game = Game()
game.play()
