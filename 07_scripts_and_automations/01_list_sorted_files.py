# 01_list_sorted_files.py

# Example of script who is sorting files after names and numbers, without renaming and modifying them

from pathlib import Path  # import for working with folder / folder paths

folder_path = Path("07_scripts_and_automations/test_data")  # folder path
files = []  # empty list
if folder_path.exists():  # if folder path exists
    files = list(
        folder_path.iterdir()
    )  # take the files from the folder and put into a list
    print(folder_path)  # display folder path in console
    if len(files) == 0:  # if the list is empty
        print(
            "The list is empty"
        )  # display this message in console, in case the list is empty
    else:  # if the list is not empty
        files = sorted(
            files, key=lambda item: item.name
        )  # sort the list alphabetically after the name of files (item.name)
        print(
            "The list is not empty"
        )  # display this message in console, in case the list is not empty
    for item in files:  # loop through the list
        print(item.name)  # display files from the folder, ordering after name
    print(f"Total files: {len(files)}")  # display total files
else:  # if folder path doesn't exist
    print(
        "the folder doesn't exist"
    )  # display this messsage in console, in case the folder doesn't exist
