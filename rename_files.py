
import os
import utils

strategies = ["prefix", "suffix", "infix", "replace"]


def rename_files():
    json_properties = utils.read_configurations("properties.json")
    directory = json_properties["path"]
    rename_strategy = json_properties["rename_strategy"]["strategy"]
    name_to_add = json_properties["new_name"]
    if rename_strategy == strategies[0]:
        prefix_rename_strategy(directory, name_to_add)
    elif rename_strategy == strategies[1]:
        suffix_rename_strategy(directory, name_to_add)
    elif rename_strategy == strategies[2]:
        infix_rename_strategy(json_properties, name_to_add)
    elif rename_strategy == strategies[3]:
        replace_rename_strategy(directory, name_to_add)


def prefix_rename_strategy(directory, name_to_add):
    [os.rename(os.path.join(directory, f), os.path.join(directory, name_to_add) + str(f)) for f in
     os.listdir(directory)]


def suffix_rename_strategy(directory, name_to_add):
    for f in os.listdir(directory):
        suffix, name_parts = utils.split_filename_suffix(f)
        old_name = "".join(name_parts)
        os.rename(os.path.join(directory, f), os.path.join(directory, str(old_name) + name_to_add + str(suffix)))


def infix_rename_strategy(json_properties, name_to_add):
    directory = json_properties["path"]
    position = json_properties["rename_strategy"]["position"]
    for f in os.listdir(directory):
        suffix, name_parts = utils.split_filename_suffix(f)
        first_part, second_part = utils.split_filename_in_position(position, name_parts)
        final_name = "".join(first_part + list(name_to_add) + second_part) + suffix
        os.rename(os.path.join(directory, f), os.path.join(directory, final_name))


def replace_rename_strategy(directory, name_to_add):
    [os.rename(os.path.join(directory, f), os.path.join(directory, name_to_add + str(i) + utils.split_filename_suffix(f)[0]))
     for i, f in enumerate(os.listdir(directory))]


if __name__ == '__main__':
    rename_files()