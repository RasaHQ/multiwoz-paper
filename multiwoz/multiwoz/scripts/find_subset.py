
"""
This script helps to find the best possible choice of domains
such that we can split the set of all stories into two subsets
that do not share any domains.
"""

import argparse
from itertools import combinations

arg_parser = argparse.ArgumentParser(description="Find large disjoint subsets of stories.")
arg_parser.add_argument("filename", type=str, help="Name of the story file")


def read_stories(filename: str):
    active_story = ""
    all_domains = set()
    data = {}

    with open(filename, "r") as story_file:
        for line in story_file:
            if line.startswith("##"):
                active_story = line[2:].strip()
                data[active_story] = set()
            elif line.lstrip().startswith("- ") and not line.lstrip().startswith("- slot"):
                domain = line.strip().split("_")[-1]
                if domain != "general":
                    data[active_story].add(domain)
                    all_domains.add(domain)

    return data, all_domains


if __name__ == '__main__':

    args = arg_parser.parse_args()
    data, domains = read_stories(args.filename)

    num_domains = len(domains)
    num_stories = len(data)

    print(f"The file contains {num_stories} stories about {num_domains} domains.")

    print()
    lengths = [len(data[d]) for d in data]
    for n in range(1, num_domains + 1):
        count = lengths.count(n)
        print(f"{count:>4} stories contain {n} domain(s)")

    print()

    splits = []
    for subset_size in [1, 2, 3]:
        for separated_domains in combinations(domains, subset_size):
            complementary_set = domains - set(separated_domains)
            # How many stories contain only these domains?
            count_in = 0
            # How many stories do not contain these domains?
            count_out = 0
            for story in data:
                if data[story] <= set(separated_domains):
                    count_in += 1
                if data[story] <= complementary_set:
                    count_out += 1

            splits.append({
                "split": set(separated_domains),
                "in": count_in,
                "out": count_out,
                "min": min(count_in, count_out)
            })

    print("Best splits:")
    for split in sorted(splits, key=lambda s: s['min'], reverse=True)[:15]:
        print(f"{sorted(split['split'])} with {split['in']} in and {split['out']} out")
