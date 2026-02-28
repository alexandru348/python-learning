# 04_folder_report.py

# Example of script who creates a complete report for a folder

from pathlib import Path # for working with folder / file paths

folder_path = input("Folder path (Enter = 07_scripts_and_automations/test_data): ").strip() # read text, the user enters value from the keyboard, trims spaces from the beginning and the end

if folder_path == "": # if the user did not enter the folder path
    folder_path = "07_scripts_and_automations/test_data" # set the folder path

folder_path = Path(folder_path) # folder path

print("folder =", folder_path) # display the folder path in the console
print("resolved =", folder_path.resolve()) # display the complete path in the console
print() # blank line

if folder_path.exists(): # if the folder path exists
    print("This folder exists.") # display this text in the console
    if folder_path.is_dir(): # if it is a folder
        print("This is a folder.") # display this text in the console
    else: # if it is not a folder
        print("This path exists, but it is not a folder.") # display this text in the console
        raise SystemExit # stop the program
else: # if the folder does not exist
    print("This folder does not exist.") # display this text in the console
    raise SystemExit # stop the program

print() # blank line

items = list(folder_path.iterdir()) # convert elements into a list
print(f"Total items in folder: {len(items)}") # display the total of items in the folder

filtered_files = [] # empty list

for item in items: # loop through the list
    if item.is_file(): # if the item is a file
        filtered_files.append(item) # it is added at the end of the list

print(f"Total files in folder: {len(filtered_files)}") # display the total of files in the folder
print()

if len(filtered_files) == 0: # if the list is empty
    print("No files found in the folder") # display this text in the console
    raise SystemExit # stop the program

filtered_files.sort(key=lambda item: item.name.lower()) # the sorting of the list by name
print("Files sorted by name:") # display this text in the console

for item in filtered_files: # loop through the list
    print(item.name) # display the files from the sorted list

print() # blank line

counts = {} # empty dict

for file in filtered_files: # loop through the list
    ext = file.suffix.lower() # convert the extension to lowercase (.PNG -> .png)

    if ext == "": # if the file has no extension
        ext = "no extension" # set the label for them

    counts[ext] = counts.get(ext, 0) + 1 # counting extension

print("Summary (files by extensions): ") # display the summary in the console

for ext in sorted(counts.keys()): # loop through the dictionary
    print(f"{ext}: {counts[ext]}") # display the counting and the extensions

print() # blank line
print(f"Final total files: {len(filtered_files)}") # display the total of final files in the console
print() # blank line