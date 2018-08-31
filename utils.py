import json


def read_configurations(filename):
    """
    Function for reading properties file in json format, so as
    to load the necessary properties for renaming the requested files
    :param filename: a string with the name of the json file
    :return: a dictionary containing the json object
    """
    with open(filename) as json_data_file:
        data = json.load(json_data_file)
    return data


def split_filename_suffix(filename):
    """
    Function to get the name of a file as well as its type
    :param filename: the name of the file to be split
    :return: the two parts of the file (name + type)
    """
    name_parts = filename.split(".")
    suffix = "." + str(name_parts[-1])
    name_parts.remove(name_parts[-1])
    return suffix, name_parts


def split_filename_in_position(position, list_old_name_without_suffix):
    """
    Function to split the name of the file in two parts (it is necessary to
    provide the file name without the type (.txt, .csv etc)
    :param position: the position to split the file
    :param list_old_name_without_suffix: the initial name of the file
    :return: the lists of the two parts of the file name
    """
    old_name = "".join(list_old_name_without_suffix)
    old_name_list = list(old_name)
    first_part = old_name_list[:position]
    second_part = old_name_list[position:]
    return first_part, second_part
