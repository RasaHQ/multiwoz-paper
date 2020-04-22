
"""This script parses all stories and creates stories_....md files"""

import os
import random
from multiwoz.parser import MultiWOZParser
import argparse
import multiwoz.dialog_turn
from pathlib import Path
from tqdm import tqdm

#################################################
# Command line argument specification
#################################################

arg_parser = argparse.ArgumentParser(description="Parse MultiWOZ 2.0 or 2.1 to story file.")
arg_parser.add_argument("directory", type=str, help="Data directory")
arg_parser.add_argument("--dataset-version", "-d", default="2.0", const="2.1", choices=["2.0", "2.1"],
                        nargs="?", help="MultiWOZ version", type=str)
arg_parser.add_argument("--subset", "-s", default="all", const="test", choices=["all", "test", "val"],
                        nargs="?", help="MultiWOZ version", type=str)
arg_parser.add_argument("--debug", action="store_true", default=False,
                        help="Use small subset of data")

arg_parser.add_argument("--keep-book-booking", action="store_true", default=False,
                        help="Keep the book_booking actions. Otherwise, replace them with inform.")
arg_parser.add_argument("--keep-reqmore", action="store_true", default=False,
                        help="Keep the reqmore_general action. Otherwise, remove it unless unique.")
arg_parser.add_argument("--keep-nooffer", action="store_true", default=False,
                        help="Keep the nooffer action. Otherwise, replace it with nobook_booking.")
arg_parser.add_argument("--add-status-slots", action="store_true", default=False,
                        help="Add status slots to stories.")
arg_parser.add_argument("--action-encoding", default="aggregated",
                        choices=["individual", "aggregated", "minimal"],
                        nargs=1, help="Way in which actions are specified", type=str)
arg_parser.add_argument("--slot-encoding", default="categorical",
                        choices=["text", "categorical"], nargs=None,
                        help="Type of slots specified in domain file", type=str)
arg_parser.add_argument("--slot-simplification", type=int, default=1, const=2,
                        choices=[0, 1, 2, 3, 4],
                        nargs="?", help="Degree of slot simplification (0 = no simplification)")
arg_parser.add_argument("--chitchat", type=float, default=[0.0],
                        nargs="+", help="Chitchat infusion multiplicity weights (0 for no chitchat)")
arg_parser.add_argument("--chitchat-story-fraction", type=float, default=0.20,
                        nargs=None, help="Probability for a story to contain chitchat")
arg_parser.add_argument("--chitchat-variability", type=int, default=1,
                        nargs=None, help="Number of different chitchat intents")
arg_parser.add_argument("--name-merge-list", type=int, default=0, choices=[0, 1, 2, 3],
                        help="Which action name merge list to use. "
                             "(0): Do not merge action names"
                             "(1): Merge bye, greet, welcome to welcome"
                             "(2): Also merge inform, recommend, select to advise"
                             "(3): Also merge request, advise to reply")


class ChitChatInfuser:

    def __init__(self, multiplicity_weights, chance_that_story_has_chitchat=0.2, min_story_length=0):
        self._multiplicity_weights = multiplicity_weights
        self._chance_that_story_has_chitchat = chance_that_story_has_chitchat
        self._min_story_length = min_story_length
        self._active_story = None
        self._chitchat_on = None

    def __call__(self, story_name: str, n: int, n_max: int) -> int:
        """
        Decide how many chitchats should be inserted at the present position
        :param story_name: Name of the current story
        :param n: Position (turn) within the current story
        :param n_max: Length of the current story
        :return: Number of chitchats to be added
        """
        if self._active_story is None or self._active_story != story_name:
            self._active_story = story_name
            self._chitchat_on = (random.uniform(0., 1.) < self._chance_that_story_has_chitchat)

        if self._chitchat_on:
            if n_max >= self._min_story_length:
                return self._random_multiplicity()
            else:
                return 0
        else:
            return 0

    def _random_multiplicity(self):
        """
        Generates a random integer i with 0 <= i < len(w), where the probability P(i = n) = w[n] / sum(w)
        and w is self._multiplicity_weights.
        """
        w = self._multiplicity_weights
        w_total = sum(w)
        # Pick a real number `r` with 0 <= `r` < total of `b`
        r = random.uniform(0.0, w_total)
        # Initialize the variable `a` with the first entry of `b`
        a = w[0]

        # Accumulate entries in `w` until the result is at least as large as `r`
        i = 0
        while a < r:
            i += 1
            a += w[i]

        # Return how far we got
        return i


if __name__ == '__main__':

    random.seed(2019)
    args = arg_parser.parse_args()
    data_dir = os.path.abspath(args.directory)

    # Choose if we want to combine "request" with "inform"/"select"/"recommend"
    if args.name_merge_list == 0:
        multiwoz.dialog_turn.default_name_merge_list = {}
    elif args.name_merge_list == 1:
        multiwoz.dialog_turn.default_name_merge_list = {
            "action": {
                "bye": "welcome",
                "greet": "welcome"
            }
        }
    elif args.name_merge_list == 2:
        multiwoz.dialog_turn.default_name_merge_list = {
            "action": {
                "inform": "advise",
                "recommend": "advise",
                "select": "advise",
                "bye": "welcome",
                "greet": "welcome"
            }
        }
    elif args.name_merge_list == 3:
        multiwoz.dialog_turn.default_name_merge_list = {
            "action": {
                "inform": "reply",
                "recommend": "reply",
                "select": "reply",
                "request": "reply",
                "advise": "reply",  # Necessary because book_booking_DOMAIN becomes advise_DOMAIN
                "bye": "welcome",
                "greet": "welcome"
            }
        }
    else:
        raise ValueError(f"Invalid name-merge-list '{args.name_merge_list}'. Must be 0, 1, 2, or 3.")

    # Use `debug=True` for smaller data set
    parser = MultiWOZParser(
        directory=data_dir,
        version=args.dataset_version,
        debug=args.debug,
        simplification_level=args.slot_simplification,
        aggregate_actions=(args.action_encoding[0] in ["aggregated", "minimal"]),
        include_action_specs=(args.action_encoding[0] != "minimal"),
        keep_book_booking=args.keep_book_booking,
        keep_reqmore=args.keep_reqmore,
        keep_nooffer=args.keep_nooffer,
        add_status_slots=args.add_status_slots
    )

    assert len(parser.data) == len(parser.acts)
    print(f"Parsing {len(parser.data)} stories...")

    all_problems = []
    count = 0
    count_good = 0

    if os.path.exists("data/stories_all.md"):
        if input("Overwrite old stories (y/N)? ").lower() != "y":
            print("User abort.")
            exit(1)

    # Setup infusion of chitchat, if required
    if sum(args.chitchat) > 0.0:
        chitchat_infuser = ChitChatInfuser(args.chitchat,
                                           min_story_length=4,
                                           chance_that_story_has_chitchat=args.chitchat_story_fraction)
        chitchat_variability = args.chitchat_variability
    else:
        chitchat_infuser = None
        chitchat_variability = 1

    if args.subset == "all":
        # Write all stories
        pbar = tqdm(parser.story_names, desc="Stories")
        with open(Path(data_dir) / "stories_all.md", "w+") as story_file:
            with open(Path(data_dir) / "stories_vallist.md", "w+") as val_file:
                with open(Path(data_dir) / "stories_testlist.md", "w+") as test_file:
                    for name in parser.story_names:
                        story = parser.parse_story(name,
                                                   infuse_chitchat_callback=chitchat_infuser,
                                                   chitchat_variability=chitchat_variability)
                        count += 1
                        if story:
                            count_good += 1
                            story_file.write(story)

                            if name in parser.validation_list:
                                val_file.write(story)

                            if name in parser.test_list:
                                test_file.write(story)

        # Inform about number of bad stories
        assert count == len(parser.story_names)
        print(f"{count_good}/{count} = {100.0 * count_good / count:.2f}% of all stories were sufficiently labeled.")
    elif args.subset == "test":
        # Write stories in test list
        pbar = tqdm(parser.story_names, desc="Stories")
        with open(Path(data_dir) / "stories_all.md", "w+") as test_file:
            for name in pbar:
                if name in parser.test_list:
                    story = parser.parse_story(name,
                                               infuse_chitchat_callback=chitchat_infuser,
                                               chitchat_variability=chitchat_variability)
                    count += 1
                    if story:
                        count_good += 1
                        test_file.write(story)
        # Inform about number of bad stories
        assert count == 1000
        print(f"{count_good}/{count} = {100.0 * count_good / count:.2f}% of all "
              f"test stories were sufficiently labeled.")
    elif args.subset == "val":
        # Write stories in validation list
        pbar = tqdm(parser.story_names, desc="Stories")
        with open(Path(data_dir) / "stories_all.md", "w+") as val_file:
            for name in pbar:
                if name in parser.validation_list:
                    story = parser.parse_story(name,
                                               infuse_chitchat_callback=chitchat_infuser,
                                               chitchat_variability=chitchat_variability)
                    count += 1
                    if story:
                        count_good += 1
                        val_file.write(story)
        # Inform about number of bad stories
        assert count == 1000
        print(f"{count_good}/{count} = {100.0 * count_good / count:.2f}% of all "
              f"validation stories were sufficiently labeled.")

    print("Exporting domain file...")
    import multiwoz.domain_info

    with open("multiwoz/data/domain.yml", "w") as domain_file:

        # Intents
        domain_file.write("intents:\n")
        domain_file.write("  - inform\n")
        domain_file.write("  - bye\n")
        if sum(args.chitchat) > 0.0:
            if args.chitchat_variability > 1:
                for v in range(1, args.chitchat_variability + 1):
                    domain_file.write(f"  - chitchat_{v}\n")
            else:
                domain_file.write("  - chitchat\n")
        domain_file.write("\n")

        # Entities
        domain_file.write("entities:\n")
        for slot in sorted(list(multiwoz.domain_info.slots)):
            domain_file.write(f"  - {slot}\n")
        domain_file.write("\n")

        # Actions
        domain_file.write("actions:\n")
        for a in sorted(list(multiwoz.domain_info.actions)):
            domain_file.write(f"  - {a}\n")
        domain_file.write("\n")

        # Templates
        domain_file.write("templates:\n")
        for a in sorted(list(multiwoz.domain_info.actions)):
            domain_file.write(f"  {a}:\n")
            domain_file.write(f'  - text: "{a}"\n')
        domain_file.write("\n")

        # Slots
        domain_file.write("slots:\n")
        if args.slot_encoding == "text":
            for slot in sorted(list(multiwoz.domain_info.slots)):
                domain_file.write(f"  {slot}:\n")
                domain_file.write(f"    type: text\n")
        elif args.slot_encoding == "categorical":
            for slot in sorted(list(multiwoz.domain_info.slots)):
                domain_file.write(f"  {slot}:\n")
                if len(multiwoz.domain_info.slots[slot]) > 1:
                    domain_file.write(f"    type: categorical\n")
                    domain_file.write(f"    values:\n")
                    for value in sorted(multiwoz.domain_info.slots[slot]):
                        domain_file.write(f"    - {value}\n")
                else:
                    domain_file.write(f"    type: text\n")

    print()
    print("Tally of problems:")
    problem_tally = {}
    for problem in multiwoz.domain_info.problems:
        if problem["type"] in problem_tally:
            problem_tally[problem["type"]] += 1
        else:
            problem_tally[problem["type"]] = 1
    for t, c in problem_tally.items():
        print(f"  {t}: {c}")

    print("Done.")
