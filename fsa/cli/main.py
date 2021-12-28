import argparse

from . import commands


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='fsa',
        description='Finite state automata determiner',
    )

    subparsers = parser.add_subparsers(dest='command')

    determine = subparsers.add_parser('determine',
                                      help='Determines FSA')
    determine.add_argument('-f', '--filename', type=str, dest='filename',
                           help='YAML filename with translations table')

    args = parser.parse_args()

    if args.command == 'determine':
        commands.determine(args.filename)
    else:
        parser.print_help()
