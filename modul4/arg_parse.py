''' Narzędzie np do robienia programów w konsoli'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name1', help='Parametr1')
parser.add_argument('name2', help='Parametr 2')
try:
    args = parser.parse_args()
    print(args)
except:
    print('błąd parametrów')
