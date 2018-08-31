import os
import utils

strategies = ["prefix", "suffix", "infix", "replace"]


def prefix_rename_strategy(directory, name_to_add):
    """
    Add a prefix to the directory name
    :param directory: the path to the root directory
    :param name_to_add: the prefix to be added in the directory name
    """
    [os.rename(os.path.join(directory, f), os.path.join(directory, name_to_add) + str(f)) for f in
     os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]


def suffix_rename_strategy(directory, name_to_add):
    """
    Add a suffix to the directory name
    :param directory: the path to the root directory
    :param name_to_add: the prefix to be added in the directory name
    """
    [os.rename(os.path.join(directory, f), os.path.join(directory, str(f) + name_to_add)) for f in
     os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]


def infix_rename_strategy():
    """
    Add some characters inside the directory name
    :return:
    """
    directory = json_properties["path"]
    position = json_properties["rename_strategy"]["position"]
    name_to_add = json_properties["new_name"]
    for f in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, f)):
            first_part, second_part = utils.split_filename_in_position(position, list(f))
            final_name = "".join(first_part + list(name_to_add) + second_part)
            os.rename(os.path.join(directory, f), os.path.join(directory, final_name))


def replace_all_rename_strategy(directory, new_name):
    """
    Replace the directory name with a new name (in case of multiple directories an incremented number will be
    added at the end of the name)
    :param directory: the path to the root directory
    :param new_name: the prefix to be added in the directory name
    """
    count = 0
    for f in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, f)):
            count = count+1
            os.rename(os.path.join(directory, f), os.path.join(directory, new_name + str(count)))


def replace_rename_strategy():
    """
    Replace some (or all the) characters of a directory name with the specified ones.
    Check if the whole name should be replaced - in this case the replace_all_rename_strategy will be used -
    otherwise the directory name will be split in the specified position and the characters will be replaced
    with the new name
    :return:
    """
    directory = json_properties["path"]
    position = json_properties["rename_strategy"]["position"]
    name_to_add = json_properties["new_name"]
    characters_to_replace = json_properties["rename_strategy"]["characters_to_replace"]
    if characters_to_replace == -1:
        replace_all_rename_strategy(directory, name_to_add)
        return
    for f in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, f)):
            filename = f[:position] + name_to_add + f[position + characters_to_replace:]
            os.rename(os.path.join(directory, f), os.path.join(directory, filename))


if __name__ == '__main__':
    json_properties = utils.read_configurations("properties.json")
    rename_strategy = json_properties["rename_strategy"]["strategy"]
    if rename_strategy == strategies[0]:
        prefix_rename_strategy(json_properties["path"], json_properties["new_name"])
    elif rename_strategy == strategies[1]:
        suffix_rename_strategy(json_properties["path"], json_properties["new_name"])
    elif rename_strategy == strategies[2]:
        infix_rename_strategy()
    elif rename_strategy == strategies[3]:
        replace_rename_strategy()
