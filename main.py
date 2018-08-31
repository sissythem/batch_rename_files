import utils
import renamingexecutor

types = ["file", "directory"]

if __name__ == '__main__':
    json_properties = utils.read_configurations("properties.json")
    renaming_executor = renamingexecutor.RenamingExecutor(json_properties["type"], json_properties["path"],
                                                          json_properties["rename_strategy"],
                                                          json_properties["position"],
                                                          json_properties["characters_to_replace"],
                                                          json_properties["new_name"])
    if json_properties["type"] == "file":
        renaming_executor.rename_files()
    elif json_properties["type"] == "directory":
        renaming_executor.rename_directories()
