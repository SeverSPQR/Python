from TodoJournal import TodoJournal
import sys
import argparse

def main():
    try:
        # 1. �������� ��������� ���������
        cli_args = sys.argv[1:]
        # 2. ���������� ��������� ��������� ������
        args = parse_args(cli_args)
        # 2. ������� ��������������� �������
        return run(args)
    except Exception as e:
        # TODO ������� ���� ���������� ��� ��������� ����� ��������� (����� ��������� �� ��������� ��)
        print(e)
        return 1