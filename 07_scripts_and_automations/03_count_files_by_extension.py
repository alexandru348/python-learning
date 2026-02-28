# 03_count_files_by_extension

# Example of script who count files by extension in a folder (summary)

from pathlib import Path # for working with folder / file paths

folder_path = input("Folder path (Enter = 07_scripts_and_automations/test_data): ").strip() # read text, the user enters value from the keyboard, trims spaces from the beginning and the end

if folder_path == "": # if the user did not enter the folder path from the keyboard
    folder_path = "07_scripts_and_automations/test_data" # set the folder path

folder_path = Path(folder_path) # folder path

print("folder =", folder_path) # displays the folder path in the console
print("resolved =", folder_path.resolve()) # display the complete path in the console
print()

if folder_path.exists(): # if the folder path exists
    print("This folder exists.") # display this text in the console
    if folder_path.is_dir(): # if it is a folder
        print("This is a folder.") # display this text in the console
    else: # if it is not a folder
        print("This path exists, but it is not a folder") # display this text in the console
        raise SystemExit # stop the program 
else: # if the folder path does not exist
    print("This folder does not exist.") # display this text in the console
    raise SystemExit # stop the program

items = list(folder_path.iterdir()) # convert elements into a list
print(f"Total items in folder: {len(items)}") # display the total items in the console

filtered_files = [] # empty list

for item in items: # loop through the items
    if item.is_file(): # if the item is a file
        filtered_files.append(item) # add the item to the end of the list

print(f"Total matched files in folder: {len(filtered_files)}") # display the total of matched files in the console
print() # blank line

if len(filtered_files) == 0: # if the list is empty
    print("No files found in the folder") # display this text in the console
    raise SystemExit # stop the program

counts = {} # empty dict

for file in filtered_files: # loop through the files
    ext = file.suffix.lower() # convert the extension to lowercase (.PNG -> .png)

    if ext == "": # if the file has no extension
        ext = "no extension" # label for files without extension

    counts[ext] = counts.get(ext, 0) + 1 # counting extension

print("Summary (files by extensions): ") # display the summary in the console

for ext in sorted(counts.keys()): # loop through extensions in sorted order
    print(f"{ext}: {counts[ext]}") # display the extension and count in the console

print() # blank line