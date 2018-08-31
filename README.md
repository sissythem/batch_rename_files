# Batch rename

## Rename files

Use rename_files.py to rename multiple files in a directory. Replace json file with the path of the directory, the strategy you want and the new name you want to use.
The supported strategies are:
* Prefix: add a String at the beginning of the filename
* Suffix: add a String at the end of the filename and before its type (e.g. test1.txt ---> test1hello.txt)
* Infix: add a String in a specific position in the filename. Remember to specify the position in the properties.json file
* Replace: replace some characters of the filename with a new String. Remember to specify the starting position (position field in properties.json) and also the number of characters to replace (characters_to_replace field in properties.json). If the latter is set as -1, the program will replace all the characters apart from the file type and position field will not be taken into account.

## Rename directories

To rename the immediate sub-directories of a directory, use the rename_directories.py. The renaming strategies are similar as above with the difference that the file type is not needed here. In order to select the renaming strategy use the json file as above.
