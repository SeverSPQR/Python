from TodoJournal import TodoJournal
import sys
from args import parse_args
from todo import run
def main():
    try:

        cli_args = sys.argv[1:]

        args = parse_args(cli_args)

        return run(args)
    except Exception as e:
        print(e)
        return 1