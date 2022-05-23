import argparse
''' Parametry append pozwala wielokrotnie użyć parametr -f'''
parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file', action='append')

args = parser.parse_args()
print(args)