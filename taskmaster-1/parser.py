
import json
import re
from termcolor import colored
import os


DEBUG = False
INPUT_FILE = "./data/TASKMASTER-1-2019/self-dialogs.json"
# INPUT_FILE = "./data/TASKMASTER-1-2019/woz-dialogs.json"


def intervals_overlap(interval1, interval2):
    a1, b1 = interval1
    a2, b2 = interval2
    return not(b1 < a2 or a1 > b2)


def simplify_intervals(interval_list):
    interval_list = sorted(interval_list, key=lambda ab: ab[0])
    result = []
    for interval in interval_list:
        # Does `result` contain an overlapping range?
        if result and intervals_overlap(result[-1], interval):
            result[-1] = [min(result[-1][0], interval[0]), max(result[-1][1], interval[1])]
        else:
            result.append(interval)
    return result


def map_entity_name(name: str):
    parts = name.split(".")
    assert len(parts) >= 2, f"{parts} has more than tree elements!"
    assert "_" in parts[0]
    if len(parts) >= 3:
        # Things like "restaurant_reservation.name.restaurant.reject"
        return parts[1] + "." + parts[2]
    else:
        # Things like "coffee_ordering.preference"
        return parts[0] + "." + parts[1]


regex_price = re.compile(r"\$[\d\.,]+|[\d\.,]+\$")
regex_number = re.compile(r"\d+[\.,:]\d+|\d+[\.,:]|\d+")
regex_bad_symbols = re.compile(r"[/:\"'`#\*&%\-\$\^]+")


class TopicClassifier:

    def __init__(self):
        self._regex_uber = re.compile(r"\buber\b|\blyft\b|pick up|picked up|dropoff|ride|drop off", flags=re.IGNORECASE)
        self._regex_movie = re.compile(r"\bmovie|\bcinema|\bfilm|\bhorror\b|\bscifi\b|\bfiction\b|\bwatch|\bticket|\bscreen|\bshowing|\bthe\bshow|\btheater|\bplay", flags=re.IGNORECASE)
        self._regex_restaurant = re.compile(r"\brestaurant|\bfood|\ballergies", flags=re.IGNORECASE)
        self._regex_coffee = re.compile(r"\bcoffee|\bdrink|\bmilk|\bstarbucks\b", flags=re.IGNORECASE)
        self._regex_pizza = re.compile(r"pizza|\btopping", flags=re.IGNORECASE)
        self._regex_auto = re.compile(r"\bauto\b|\bcar\b|\brepair\b|\bfix\b", flags=re.IGNORECASE)

    def __call__(self, string, tokens=None):
        return self.classify(string, tokens)

    def classify(self, string, tokens=None):

        if tokens:
            token = tokens.pop()
            return token.split(".")[0].split("_")[0]

        if self._regex_uber.search(string):
            return "uber"
        elif self._regex_auto.search(string):
            return "auto"
        elif self._regex_coffee.search(string):
            return "coffee"
        elif self._regex_movie.search(string):
            return "movie"
        elif self._regex_pizza.search(string):
            return "food"
        elif self._regex_restaurant.search(string):
            return "food"
        else:
            return "general"


if __name__ == '__main__':

    with open(INPUT_FILE, "r") as file:
        all_data = json.load(file)

    train_file_name = "./data/" + os.path.basename(INPUT_FILE)[:-5] + "-train.md"
    test_file_name = "./data/" + os.path.basename(INPUT_FILE)[:-5] + "-test.md"
    domain_file_name = "./data/" + os.path.basename(INPUT_FILE)[:-5] + "-domain.md"
    action_map_file_name = "./data/" + os.path.basename(INPUT_FILE)[:-5] + "-action_map.json"

    num_train = int(input("Number of training stories (max 6166): "))  # 80%
    num_test = round(num_train / 4.0)                       # 20%
    print(f"Number of testing stories:  {num_test}\n")

    count_train = 0
    count_test = 0
    action_map = {}

    classify = TopicClassifier()

    print(f"Exporting training stories to `{train_file_name}`")
    print(f"Exporting test stories to `{test_file_name}`")

    with open(train_file_name, "w+") as train_file:
        with open(test_file_name, "w+") as test_file:
            for data in all_data:
                if count_train < num_train:
                    file = train_file
                    count_train += 1
                else:
                    file = test_file
                    count_test += 1
                if count_test > num_test:
                    break

                if data['conversation_id'] == "dlg-fdd242eb-56be-48c0-a56e-5478472500d0":
                    # Conversations after this tend to be badly annotated in woz-dialogs dataset
                    print("Reached dlg-fdd242eb-56be-48c0-a56e-5478472500d0")
                    break

                domain = data["instruction_id"].split("-")[0]
                if domain in ["restaurant", "pizza"]:
                    domain = "food"
                assert domain in ["uber", "auto", "coffee", "movie", "food"]

                file.write(f"## {data['conversation_id']}\n")
                for turn in data["utterances"]:
                    index = turn["index"]
                    speaker = turn["speaker"]
                    text = turn["text"]
                    segments = turn.get("segments", None)
                    if DEBUG:
                        print(text)
                    replacements = {}
                    all_tokens = set()
                    new_text = ""
                    if segments:
                        # Fill replacement dict with lists of intervals for each entity, like this:
                        # replacements = {"ENTITY": [["a1", "b1"], ["a2", "b2"], ["a3", "b3"]]}
                        for segment in segments:
                            a = segment["start_index"]
                            b = segment["end_index"]
                            for annotation in segment['annotations']:
                                all_tokens.add(annotation["name"])
                                entity = map_entity_name(annotation["name"])
                                if entity in replacements:
                                    if [a, b] not in replacements[entity]:
                                        replacements[entity].append([a, b])
                                else:
                                    replacements[entity] = [[a, b]]

                            ent = "_" * (b - a)
                            text = text[:a] + ent + text[b:]

                        # Merge overlapping intervals
                        for entity in replacements:
                            replacements[entity] = simplify_intervals(replacements[entity])

                        # Substitute the entities
                        snippets = [{"original": text, "replacement": text,
                                     "len": len(text), "was_replaced": False}]
                        for entity, interval_list in replacements.items():
                            for interval in interval_list:
                                a, b = interval
                                # Find the snippet that contains index a
                                idx = snippets[0]["len"]
                                i = 0
                                while idx < a and i < len(snippets) - 1:
                                    i += 1
                                    idx += snippets[i]["len"]
                                string = snippets[i]["original"]
                                prolog = string[:(a - idx)]
                                middle = string[(a - idx):(b - idx)]
                                if b < idx:
                                    epilog = string[(b - idx):]
                                else:
                                    epilog = ""
                                snippets[i] = {"original": prolog, "replacement": prolog,
                                               "len": len(prolog), "was_replaced": False}
                                snippets.insert(i + 1, {"original": middle, "replacement": f"_{entity}_",
                                                        "len": len(middle), "was_replaced": True})
                                snippets.insert(i + 2, {"original": epilog, "replacement": epilog,
                                                        "len": len(epilog), "was_replaced": False})

                        for snippet in snippets:
                            if snippet["was_replaced"]:
                                if DEBUG:
                                    new_text += colored(snippet["replacement"], "blue")
                                else:
                                    new_text += snippet["replacement"]
                            else:
                                new_text += snippet["replacement"]
                    else:
                        new_text = text

                    # Post-process string
                    # > Replace price tags
                    new_text = regex_price.sub("_price_", new_text)
                    # > Replace numbers
                    new_text = regex_number.sub("_number_", new_text)
                    # > Dirty bugfix | ToDo: Why is this necessary?
                    new_text = re.sub("_+", "_", new_text)
                    # > Bad symbols
                    new_text = regex_bad_symbols.sub(" ", new_text)
                    # > Strip spaces
                    new_text = new_text.strip()
                    # > Empty string
                    new_text = new_text if new_text else "NOTHING"

                    if speaker == "USER":
                        file.write(f"* {new_text}\n")
                    elif speaker == "ASSISTANT":
                        file.write(f"   - {new_text}\n")
                        # action_map[new_text] = sorted(list(all_tokens))
                        action_map[new_text] = [domain, classify(new_text)] + sorted(list(all_tokens))
                    else:
                        raise ValueError(f"Speaker {speaker} is unusual.")

                    if DEBUG:
                        print(text + colored(f" ({replacements})", "red"))
                        print(new_text)
                        print()
                file.write("\n")

    print(f"Exporting domain to `{domain_file_name}`")

    with open(domain_file_name, "w+") as domain_file:
        domain_file.write("actions:\n")
        for action in sorted(list(action_map)):
            domain_file.write(f"   - {action}\n")

    print(f"Exporting action_map to `{action_map_file_name}`")

    with open(action_map_file_name, "w+") as action_map_file:
        json.dump(action_map, action_map_file)
