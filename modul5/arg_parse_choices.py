''' Narzędzie np do robienia programów w konsoli
Dokładam parametry opcjonalne z listą wartości
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-m',
                    '--mode',
                    help='Parametr1',
                    choices=['encrypt','decrypt']
                    )


try:
    args = parser.parse_args()
    print(args)
except:
    print('błąd parametrów')
