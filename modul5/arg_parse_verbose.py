''' Narzędzie np do robienia programów w konsoli
Można wywołać z paramtrem -v, -vv, -vvvv itd
'''
import argparse
import os, os.path
parser = argparse.ArgumentParser()
parser.add_argument('-v',
                    '--verbose',
                    action='count',
                    default=0
                    )


try:
    args = parser.parse_args()
    if  args.verbose == 1: # -v
        print(len([name for name in os.listdir() if os.path.isfile(os.path.join('./', name))]))

    if args.verbose == 2: # -vv druk pierwszego pliku
        print([name for name in os.listdir() if os.path.isfile(os.path.join('./', name))][0])
    if args.verbose == 0:
        print('default')
except:
    print('błąd parametrów')
