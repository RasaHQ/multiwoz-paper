
"""This script displays individual stories from a file."""

import argparse
from termcolor import colored

arg_parser = argparse.ArgumentParser(description="Display individual stories from a file.")

arg_parser.add_argument("input", type=str, help="Input story file name")
arg_parser.add_argument("-i", type=int, default=1, help="Number of first story")
arg_parser.add_argument("--name", "-n", default=None, help="Name of first story")

if __name__ == '__main__':

    args = arg_parser.parse_args()

    # Input file name
    story_file_name = args.input

    # Index of first story
    i_first = args.i

    with open(story_file_name, "r") as story_file:
        i = 0
        print()
        for line in story_file:
            if line.startswith("##"):
                i += 1
            if i == i_first and line.strip():
                if line.startswith("##"):
                    if args.name is not None:
                        if line[2:].strip() != args.name:
                            i_first += 1
                            continue
                    print(colored(line.rstrip(), "blue"))
                elif line.startswith("*"):
                    print(colored(line.rstrip(), "cyan"))
                elif "<!--" in line:
                    print(colored(line.rstrip(), "red"))
                else:
                    print(line.rstrip())

            if i > i_first:
                print()
                if input("Print another story (y/n)? ") in ["y", "Y"]:
                    print()
                    if line.startswith("##"):
                        print(colored(line.rstrip(), "blue"))
                    i_first += 1
                else:
                    break
