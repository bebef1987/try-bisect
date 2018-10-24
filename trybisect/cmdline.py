import argparse
import os


def create_parser():
    parser = argparse.ArgumentParser()
    add_arg = parser.add_argument

    add_arg('-g', '--good', required=True, dest='good',
            help="last known good rev")
    add_arg('-b', '--bad', required=True, dest='bad',
            help="last known bad rev")
    add_arg('-c', '--command', required=True, dest='command',
            help="try build command line. See https://mozilla-releng.net/trychooser/")

    add_arg('-p', '--path_to_repo', required=False, dest='path_to_repo',
            help="path to hg repo")

    return parser


def parse_args(argv=None):
    parser = create_parser()
    args = parser.parse_args(argv)
    return args
