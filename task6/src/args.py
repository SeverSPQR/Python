import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    composing = parser.add_argument_group("Writing new todos",
                                          "чтобы добавить новую запись в туду лист необходимо выполнить Х")
    composing.add_argument("text", metavar="", nargs="*")
    return parser.parse_intermixed_args(args)