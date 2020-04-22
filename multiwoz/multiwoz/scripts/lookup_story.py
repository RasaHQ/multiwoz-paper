
import os
import multiwoz.parser
import readline
import random
import argparse

arg_parser = argparse.ArgumentParser(description="Print a story from MultiWOZ.")
arg_parser.add_argument("--raw-actions", "-a", action="store_true", default=False,
                        help="Show original action names for Wizard")


class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options
                                if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None


if __name__ == '__main__':

    args = arg_parser.parse_args()
    multiwoz.dialog_turn.default_name_merge_list = {}

    # Example application: Display particular dialog
    parser = multiwoz.parser.MultiWOZParser(
        directory=os.path.abspath("multiwoz/data"),
        version="2.1",
        simplification_level=1,
        include_action_specs=False
    )

    completer = MyCompleter(parser.story_names)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')

    while True:
        search_string = input("\nStory name ('r' for random): ")

        if search_string == "r":
            search_string = random.choice(parser.story_names)

        if search_string.strip() == "":
            break

        if search_string.startswith("story_"):
            search_string = search_string[6:]

        if not search_string.endswith(".json"):
            search_string += ".json"

        if search_string in parser.story_names:
            if args.raw_actions:
                parser.demo_raw_actions(search_string)
            else:
                parser.parse_story(search_string, verbose=2)
