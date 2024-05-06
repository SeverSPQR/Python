from TodoJournal import TodoJournal
import sys
import argparse

def main():
    try:
        # 1. Спарсить аргументы командной
        cli_args = sys.argv[1:]
        # 2. обработать аргументы командной строки
        args = parse_args(cli_args)
        # 2. вызвать соответствующие функции
        return run(args)
    except Exception as e:
        # TODO Создать свое исключение для обработки такой ситуцации (будем обсуждать на следующих пз)
        print(e)
        return 1