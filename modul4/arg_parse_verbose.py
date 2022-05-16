''' Narzędzie np do robienia programów w konsoli
Można wywołać z paramtrem -v, -vv, -vvvv itd
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v',
                    '--verbose',
                    action='count',
                    default=0
                    )


try:
    args = parser.parse_args()
    if  args.verbose == 1:
        print("1")
    if args.verbose == 2:
        print('2')
    if args.verbose == 0:
        print('default')
except:
    print('błąd parametrów')
