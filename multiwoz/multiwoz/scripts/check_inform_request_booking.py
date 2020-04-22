
"""This script checks if inform_booking and request_booking occur together - they shouldn't."""

import sys

if __name__ == '__main__':

    # Concatenate stories
    bad_stories = set()
    with open(sys.argv[1], "r") as file:
        active_story = ""
        action_stack = set()
        for line in file:
            line = line.strip()
            if line.startswith("##"):
                active_story = line[2:].strip()
            if line.startswith("*"):
                # if "inform_booking" in action_stack and len(action_stack) == 1:
                if "inform_booking" in action_stack and "request_booking" in action_stack:
                    bad_stories.add(active_story)
                action_stack.clear()
            if line.startswith("-"):
                action_stack.add(line[2:])

    print(f"Found {len(bad_stories)} bad stories:")
    for story in bad_stories:
        print(f"  {story}")
