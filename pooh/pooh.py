#!/usr/bin/env python
import argparse
from os import getcwd


def main():
    parser = argparse.ArgumentParser(
        description="{}".format("A tool to automatically generate .gitignore file for your project"), formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('-u', '--update', action="store_true",
                        help='give path of music files\' directory', default=getcwd())

    parser.add_argument('-s', '--song', action='store', dest='song_name',
                        help='Only fix metadata of the file specified', default=None)

    parser.add_argument('-c', '--config', action='store_true', dest='config',
                        help="Add API Keys to config\n\n")

    parser.add_argument('-n', '--norename', action='store_true',
                        help='Does not rename files to song title\n\n')

    parser.add_argument('-f', '--format', action='store', dest='rename_format', help='''Specify the Name format used in renaming,
                        Valid Keywords are:
                        {title}{artist}{album}\n\n)''')

    args = parser.parse_args()


if __name__ == "__main__":
    main()
