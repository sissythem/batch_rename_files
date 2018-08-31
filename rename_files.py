import os
import utils


def prefix_rename_strategy(directory, name_to_add):
    """
    Add a prefix to the filename
    :param directory: the path to the root directory
    :param name_to_add: the prefix to be added in the filename
    """
    [os.rename(os.path.join(directory, f), os.path.join(directory, name_to_add) + str(f)) for f in
     os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def suffix_rename_strategy(directory, name_to_add):
    """
    Add a suffix to the filename. This will be added before the suffix with the
    file type (e.g. test.txt is the initial filename and we want to add _1 => test_1.txt)
    :param directory: the path to the root directory
    :param name_to_add: the prefix to be added in the filename
    """
    for f in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, f)):
            suffix, name_parts = utils.split_filename_suffix(f)
            old_name = "".join(name_parts)
            os.rename(os.path.join(directory, f), os.path.join(directory, str(old_name) + name_to_add + str(suffix)))


def infix_rename_strategy(directory, position, name_to_add):
    """
    Add some characters inside the filename
    :return:
    """
    for f in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, f)):
            suffix, name_parts = utils.split_filename_suffix(f)
            first_part, second_part = utils.split_filename_in_position(position, name_parts)
            final_name = "".join(first_part + list(name_to_add) + second_part) + suffix
            os.rename(os.path.join(directory, f), os.path.join(directory, final_name))


def replace_all_rename_strategy(directory, new_name):
    """
    Replace the filename with a new name (in case of multiple files an incremented number will be
    added at the end of the name). The type of the file will remain as is.
    :param directory: the path to the root directory
    :param new_name: the prefix to be added in the filename
    """
    count = 0
    for f in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, f)):
            count = count + 1
            os.rename(os.path.join(directory, f),
                      os.path.join(directory, new_name + str(count) + utils.split_filename_suffix(f)[0]))


def replace_rename_strategy(directory, position, name_to_add, characters_to_replace):
    """
    Replace some (or all the) characters of a filename with the specified ones.
    Check if the whole name should be replaces - in this case the replace_all_rename_strategy will be used -
    otherwise the filename is split in the position where the characters will be replaced, the new characters
    are added and at the end of the name the file type is also added
    :return:
    """
    if characters_to_replace == -1:
        replace_all_rename_strategy(directory, name_to_add)
        return
    for f in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, f)):
            suffix, name_parts = utils.split_filename_suffix(f)
            old_name = "".join(name_parts)
            filename = old_name[:position] + name_to_add + old_name[position + characters_to_replace:] + suffix
            os.rename(os.path.join(directory, f), os.path.join(directory, filename))
