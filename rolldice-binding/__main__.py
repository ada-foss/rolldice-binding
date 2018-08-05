import argparse
import sys
from core import *

def main():
    parser = argparse.ArgumentParser(description='A command line utility to'
            ' interpret dice roll expressions')

    parser.add_argument('expressions', nargs='+',
            help='any expressions to parse and run')
    parser.add_argument('renderer', default='pretty',
            help='which renderer to use (default: pretty)')

    args = parser.parse_args()

    try:
        renderer = get_renderer(args.renderer)
    except ImportError:
        print('no such renderer:', args.renderer)
        sys.exit(1)
    else:
        enact_expressions(args.expressions, renderer, args)
