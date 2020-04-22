
import sys
import os

from multiwoz import dialog_turn
from multiwoz.parser import MultiWOZParser
from termcolor import colored

if __name__ == '__main__':

    # Example application: Display text samples that correspond to given actions
    max_examples = 5 if len(sys.argv) < 2 else int(sys.argv[1])
    dialog_turn.default_name_merge_list = {}
    parser = MultiWOZParser(directory=os.path.abspath("./multiwoz/data"), keep_book_booking=True, keep_nooffer=True, keep_reqmore=True, include_action_specs=False)
    while True:
        search_string = input("\nLookup: ")
        if search_string == "":
            break
        samples = parser.find_example_action_text(search_string, single=True,
                                                  max_examples=max_examples, include_user=True)
        print(colored(f"Examples of \"{search_string}\":", "magenta"))
        for s in samples:
            print(" " + s)
