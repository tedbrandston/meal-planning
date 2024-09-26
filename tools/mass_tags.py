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
        help="tag to add to each file")

    parser.add_argument(
        "--link-append",
        help="add something to the end of each link")

    return parser.parse_args()

def add_tag(tag, line):
    if tag in line:
        return line
    line = line.strip()
    line = line.strip(']')
    line += ', '
    line += args.add_tag
    line += ']\n'
    return line

def link_append(string, line):
    line = line.strip()
    line += string
    line += '\n'
    return line

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
            for num, line in enumerate(lines):
                if line.startswith('tags:') and args.add_tag:
                    lines[num] = add_tag(args.add_tag, line)
                if line.startswith('link:') and args.link_append:
                    lines[num] = link_append(args.link_append, line)
        with open(file, 'w') as wfp:
            wfp.writelines(lines)


if __name__ == '__main__':
    args = parse_args()
    main(args)
