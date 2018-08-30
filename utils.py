import json


def read_configurations(filename):
    with open(filename) as json_data_file:
        data = json.load(json_data_file)
    return data


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
