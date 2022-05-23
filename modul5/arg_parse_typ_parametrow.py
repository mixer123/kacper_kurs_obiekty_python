''' Narzędzie np do robienia programów w konsoli'''
import argparse
parser = argparse.ArgumentParser()
def param_validator(value):
    if value.startswith('a'):
        raise argparse.ArgumentError()
    return value
parser.add_argument('-n', '--name1', type=param_validator , help='Parametr1')

try:
    args = parser.parse_args()
    print(args)
except argparse.ArgumentError:
    print('błąd typu argumentow')
except:
    print('błąd')
