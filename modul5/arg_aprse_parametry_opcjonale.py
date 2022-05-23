''' Narzędzie np do robienia programów w konsoli
Dokładam parametry opcjonalne
'''
import argparse
parser = argparse.ArgumentParser()
''' -n jest parametrem opcjonalnym. Zamiast -n można napisać --name1'''
parser.add_argument('-n', '--name1', help='Parametr1')
''' Trzeba wywołac : -n wartość_parametru name1
np. python3 nazwaPliku.py -n adam
'''

try:
    args = parser.parse_args()
    print(args)
except:
    print('błąd parametrów')
