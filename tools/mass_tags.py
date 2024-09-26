#! /usr/bin/env python3

import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files-list",
        help="text file with one filename per line of files to edit")

    parser.add_argument(
        "--add-tag",
        help="tag to add to the files")

    return parser.parse_args()


def main(args):
    if args.files_list:
        with open(args.files_list) as rfp:
            files_list = rfp.readlines()
        files_list = [f.strip() for f in files_list]
    else:
        files_list = os.listdir('content/recipes')
        files_list = [f'content/recipes/{f}' for f in files_list]

    for file in files_list:
        with open(file) as rfp:
            lines = rfp.readlines()
        if args.add_tag:
            for num, line in enumerate(lines):
                if line.startswith('tags:'):
                    if args.add_tag in line:
                        continue
                    line = line.strip()
                    line = line.strip(']')
                    line += ', '
                    line += args.add_tag
                    line += ']\n'
                    lines[num] = line
        with open(file, 'w') as wfp:
            wfp.writelines(lines)


if __name__ == '__main__':
    args = parse_args()
    main(args)
