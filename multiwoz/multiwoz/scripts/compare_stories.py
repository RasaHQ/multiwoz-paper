
"""This script compares mistakes of same stories from different files."""

import argparse
from termcolor import colored

arg_parser = argparse.ArgumentParser(description="Display individual stories from a file.")

arg_parser.add_argument("base", type=str, help="Input story file name 1")
arg_parser.add_argument("compare", type=str, help="Input story file name 2")
arg_parser.add_argument("--name", "-n", default=None, help="Name of first story")


def read_stories(file):
    stories = {}
    story = []
    story_name = None
    for line in file:
        if line.startswith("##"):
            if story:
                stories[story_name] = story
                story = []
            story_name = line[3:].strip()
        elif line.startswith("*"):
            story.append({
                "target": line.strip(),
                "prediction": None,
                "type": "intent",
                "correct": True
            })
        elif "<!--" in line:
            p = line.find("<!--")
            target = line[:p].strip()
            prediction = line[p + 4:-4].strip()
            story.append({
                "target": target,
                "prediction": prediction,
                "type": "action",
                "correct": False
            })
        elif line.lstrip().startswith("-"):
            story.append({
                "target": line,
                "prediction": None,
                "type": "action",
                "correct": True
            })

    stories[story_name] = story

    return stories


if __name__ == '__main__':

    args = arg_parser.parse_args()

    # Input file names
    story_file_name_1 = args.base
    story_file_name_2 = args.compare

    # "story_PMUL0713"

    # Load all stories from both files

    with open(story_file_name_1, "r") as file:
        stories_1 = read_stories(file)

    with open(story_file_name_2, "r") as file:
        stories_2 = read_stories(file)

    # Find all stories that are common to both files
    story_name_list = set(stories_1).intersection(set(stories_2))

    print(f"{len(story_name_list)} stories are shared between the two files\n")

    # Find pair of stories which have mistakes at the same turns
    similar_stories = []
    for story_name in story_name_list:
        story_1 = stories_1[story_name]
        story_2 = stories_2[story_name]

        similar = True
        act_1 = story_1.pop()
        act_2 = story_2.pop()
        act_1_correct = True
        act_2_correct = True
        while act_1 and act_2:

            if act_1["type"] == "intent" and act_2["type"] == "intent":
                act_1_correct = act_1["correct"]
                act_2_correct = act_2["correct"]
                act_1 = story_1.pop() if story_1 else None
                act_2 = story_2.pop() if story_2 else None
            elif act_1["type"] == "action":
                act_1_correct = act_1_correct and act_1["correct"]
                act_1 = story_1.pop() if story_1 else None
            elif act_2["type"] == "action":
                act_2_correct = act_2_correct and act_2["correct"]
                act_2 = story_2.pop() if story_2 else None

            if (act_1 is None and act_2 is None) or (act_1["type"] == "intent" and act_2["type"] == "intent"):
                if act_1_correct != act_2_correct:
                    similar = False
                    break

        if similar:
            print(story_name)
            similar_stories.append(story_name)
