import argparse
''' Parametry -q oraz -v wzajemnie się wykluczają - dzięki add_mutually_exclusive_group'''
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true')
group.add_argument('-q', '--quiet', action='store_true')
args = parser.parse_args()
print(args)