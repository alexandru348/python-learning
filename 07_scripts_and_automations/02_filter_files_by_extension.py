# 02_filter_files_by_extension.py

# Example of script who sort files and filter them by extension, without renaming and modifying them

from pathlib import Path # import for working with folder / file paths

folder_path = input(
    "folder path (Enter = 07_scripts_and_automations/test_data):" # read text, the user enters value from the keyboard
).strip() # trims spaces from the beginning and the end

if folder_path == "": # if the user did not enter the folder path
    folder_path = "07_scripts_and_automations/test_data" # set the folder path

ext = input("Extension (ex: .png or png):").strip() # read text, the user enters value from the keyboard, trims spaces from the beginning and the end

ext = ext.lower() # set the extension to be recognized in lowercase, regardless of how the user types it in the console

if ext == "": # if the user did not write the extension
    ext = ".png" # set the required extension
elif ext.startswith("."): # if the user enters the extension with a dot
    ext = ext # keep the requested extension
else: # if the user wrote the extension
    ext = "." + ext # the extension is added

folder_path = Path(folder_path) # folder path

print("folder = ", folder_path) # displays the path in the console
print("extension =", ext) # displays the extension in the console
print() # blank line

if folder_path.exists(): # if the folder path exists
    if folder_path.is_dir(): # check if it is a folder
        print("The folder exists") # displays this text in the console
    else: # if it is not a folder
        print("This path exists, but it is not a folder") # displays this text in the console
        raise SystemExit # stop the program
else: # if the folder path does not exist
    print("The folder doesn't exist") # display this text in the console
    raise SystemExit # stop the program

print() # blank line

items = list(folder_path.iterdir()) # convert elements into a list
print(f"Total items in folder: {len(items)}") # displays the total items in the folder

filtered_files = [] # empty list

for item in items: # get items from folder
    if item.is_file(): # if the item is a file
        if item.suffix.lower() == ext: # if the file has the required extension
            filtered_files.append(item) # is added to the end of the list

print(f"Matched files: {len(filtered_files)}") # displays the files that match to the request
print() # blank line

if len(filtered_files) == 0: # if the list is empty
    print(f"No files with extension {ext}") # displays this text in the console
    raise SystemExit # stop the program

filtered_files.sort(key=lambda item: item.name.lower()) # the criterion for sorting files by name converted to lowercase

print("Filtered files sorted by name") # displays files filtered by extension name

for item in filtered_files: # loop through the items from the list
    print(item.name) # displays the items in the list

print(f"Total matched files: {len(filtered_files)}") # displays the total number of files in the console
print() # blank line