import os
import sys

from lib.hexadecimal import get_word, merge_hexadecimal, split_hexadecimal
from lib.physical_constraints import value_location
from lib.util import save, load, load_json


def notice(key, update_value, location):
    if key not in location:
        print(f"{key} is not in physical_constraints.jsb")
        os.system("pause")
        sys.exit(-1)

    if key == "min_delay_for_shirt_tug_do":
        if update_value > 255 or update_value < 0:
            print(f"Range of {key} : 0~255")
            os.system("pause")
            sys.exit(-1)


def convert_value(data_all, head, tail, update_value):
    before = get_word(data_all, head, tail)
    before = merge_hexadecimal(before)

    replaced = split_hexadecimal(update_value)
    replaced = replaced[-(tail - head) :]
    for j, i in enumerate(range(tail, head, -1)):
        data_all[i] = replaced[j]

    after = get_word(data_all, head, tail)
    after = merge_hexadecimal(after)

    return before, after, data_all


def update_physical_constraints(jsb_file, json_file, update_file):
    jsb_data = load(jsb_file)
    update_values = load_json(json_file)

    for key in update_values:
        update_value = update_values[key]
        notice(key, update_value, value_location)
        head1 = value_location[key]["head"]
        tail1 = value_location[key]["tail"]
        head2 = value_location[key]["head2"]
        tail2 = value_location[key]["tail2"]

        before, after, jsb_data = convert_value(jsb_data, head1, tail1, update_value)
        if before != after:
            print(key, before, "->", after)
        before, after, jsb_data = convert_value(jsb_data, head2, tail2, update_value)

    save(jsb_data, update_file)


def main():
    original_jsb = "physical_constraints.jsb"
    update_json = "physical_constraints.json"
    update_jsb = "physical_constraints_update.jsb"
    update_physical_constraints(original_jsb, update_json, update_jsb)


if __name__ == "__main__":
    github_url = "https://github.com/wonss737/fm24-matchengine-maker.git"
    print(f"You can get more informatino at {github_url}\n")
    main()
    os.system("pause")
