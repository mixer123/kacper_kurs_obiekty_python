from card import Card

def test_creation():
    card = Card('2','\u2664')
    assert card.color== '\u2664'
    assert card.value == 'A'