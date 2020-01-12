import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-pos', '--position', action='store_true')

args = parser.parse_args()
print(args.position)