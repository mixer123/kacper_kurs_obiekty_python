from functools import lru_cache

@lru_cache(maxsize=128)
def len_of_word(word):
    print('ilosc slow')
    vowels = [letter for letter in word if letter in 'aeoiuy']
    return {'letters':len(word),
            'vowels':len(vowels)}


print(len_of_word('ssdsdsdbvvb'))
print(len_of_word('ssdsdsdbvvb'))