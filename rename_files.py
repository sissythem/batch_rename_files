import json
import os

strategies = ["prefix", "suffix", "infix", "replace"]


def read_configurations(filename):
    with open(filename) as json_data_file:
        data = json.load(json_data_file)
    return data


def rename_files():
    json_properties = read_configurations("properties.json")
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
        suffix, name_parts = split_filename_suffix(f)
        old_name = "".join(name_parts)
        os.rename(os.path.join(directory, f), os.path.join(directory, str(old_name) + name_to_add + str(suffix)))


def infix_rename_strategy(json_properties, name_to_add):
    directory = json_properties["path"]
    position = json_properties["rename_strategy"]["position"]
    for f in os.listdir(directory):
        suffix, name_parts = split_filename_suffix(f)
        first_part, second_part = split_filename_in_position(position, name_parts)
        final_name = "".join(first_part + list(name_to_add) + second_part) + suffix
        os.rename(os.path.join(directory, f), os.path.join(directory, final_name))


def split_filename_suffix(filename):
    name_parts = filename.split(".")
    suffix = "." + str(name_parts[-1])
    name_parts.remove(name_parts[-1])
    return suffix, name_parts


def split_filename_in_position(position, list_old_name_without_suffix):
    old_name = "".join(list_old_name_without_suffix)
    old_name_list = list(old_name)
    first_part = old_name_list[:position]
    second_part = old_name_list[position:]
    return first_part, second_part


def replace_rename_strategy(directory, name_to_add):
    [os.rename(os.path.join(directory, f), os.path.join(directory, name_to_add + str(i) + split_filename_suffix(f)[0]))
     for i, f in enumerate(os.listdir(directory))]


if __name__ == '__main__':
    rename_files()
