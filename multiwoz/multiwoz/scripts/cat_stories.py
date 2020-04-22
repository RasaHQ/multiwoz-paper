
"""This script displays individual stories from a file."""

import argparse

arg_parser = argparse.ArgumentParser(description="Concatenate two story files.")

arg_parser.add_argument("target", type=str, help="Name of the story file that is to be edited")
arg_parser.add_argument("extra", type=str, help="Name of the story file that is to be added")
arg_parser.add_argument("--filter", "-f", nargs=1, help="Name of list of stories that is allowed")

if __name__ == '__main__':

    args = arg_parser.parse_args()

    # Read whitelist from filter file
    whitelist = []
    if args.filter:
        with open(args.filter[0], "r") as file:
            for line in file:
                if line:
                    whitelist.append(line.strip())

    # Concatenate stories
    num_merged = 0
    with open(args.extra, "r") as extra_file:
        with open(args.target, "a") as target_file:
            active_story = ""
            for line in extra_file:
                if line.startswith("##"):
                    active_story = line[2:].strip()
                    if whitelist and (active_story not in whitelist):
                        active_story = ""
                    else:
                        num_merged += 1

                if active_story:
                    target_file.write(line)

    print(f"Concatenated {num_merged} stories")
