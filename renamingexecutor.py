import rename_files
import rename_directories


class RenamingExecutor:
    file_type = ""
    root_directory_path = ""
    renaming_strategy = ""
    position = 0
    characters_to_replace = 0
    new_name = ""
    strategies = ["prefix", "suffix", "infix", "replace"]

    def __init__(self, file_type, root_directory_path, renaming_strategy, position, characters_to_replace, new_name):
        self.file_type = file_type
        self.root_directory_path = root_directory_path
        self.renaming_strategy = renaming_strategy
        self.position = position
        self.characters_to_replace = characters_to_replace
        self.new_name = new_name

    def rename_files(self):
        if self.renaming_strategy == self.strategies[0]:
            rename_files.prefix_rename_strategy(self.root_directory_path, self.new_name)
        elif self.renaming_strategy == self.strategies[1]:
            rename_files.suffix_rename_strategy(self.root_directory_path, self.new_name)
        elif self.renaming_strategy == self.strategies[2]:
            rename_files.infix_rename_strategy(self.root_directory_path, self.position, self.new_name)
        elif self.renaming_strategy == self.strategies[3]:
            rename_files.replace_rename_strategy(self.root_directory_path, self.position, self.new_name,
                                                 self.characters_to_replace)

    def rename_directories(self):
        if self.renaming_strategy == self.strategies[0]:
            rename_directories.prefix_rename_strategy(self.root_directory_path, self.new_name)
        elif self.renaming_strategy == self.strategies[1]:
            rename_directories.suffix_rename_strategy(self.root_directory_path, self.new_name)
        elif self.renaming_strategy == self.strategies[2]:
            rename_directories.infix_rename_strategy(self.root_directory_path, self.position, self.new_name)
        elif self.renaming_strategy == self.strategies[3]:
            rename_directories.replace_rename_strategy(self.root_directory_path, self.position, self.new_name,
                                                       self.characters_to_replace)
