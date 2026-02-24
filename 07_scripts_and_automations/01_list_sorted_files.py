# 01_list_sorted_files.py

# Example of script who is sorting files after names and numbers, without renaming and modifying them

from pathlib import Path

folder_path = Path("07_scripts_and_automations/test_data")
files = []
if folder_path.exists():
    files = list(folder_path.iterdir())
    print(folder_path)
    if len(files) == 0:
        print("The list is empty")
    else:
        files = sorted(files, key=lambda item: item.name)
        print("The list is not empty")
    for item in files:
        print(item.name)
    print(f"Total files: {len(files)}")
else:
    print("the folder doesn't exist")
