# 01_dictionary_basics.py

# Examples of dictionary basics using variables, input, output, and conditions

# create a dictionary and access values

person = {"name": "George", "age": 30}  # dictionary with keys and values
print("person =", person)  # display dictionary in console

print("name =", person["name"])  # access value by key
print("age =", person["age"])  # access value by key

person["age"] = 31  # update value by key
person["city"] = "Bucuresti"  # add new key and value

print(
    "updated person =", person
)  # display updated value and new value added in dictionary

if "country" in person:  # checks if key exists
    print("country =", person["country"])  # display country in console
else:  # if key does not exist
    print("country key not found")  # display this text in console

print()  # blank line

# read keys and values into a dictionary (with input)

count = int(
    input("How many items do you want to enter? ")
)  # read text, convert to int, the user enters value from the keyboard

items = {}  # empty dictionary
for i in range(1, count + 1):  # loop from 1 to count, the last value is included
    key = input(f"Key {i}: ")  # read text, the user enters value from the keyboard
    value = input(f"Value {i}: ")  # read text, the user enters value from the keyboard
    items[key] = value  # add key and value to dictionary

print("items =", items)  # display items in console
print()  # blank line

# loop through a dictionary (keys and values)

print("loop through items")  # display this text in console
for k, v in items.items():  # loop through keys and values
    print(f"{k} -> {v}")  # display keys and values in console

print()  # blank line

# counting using a dictionary (with input)

n = int(
    input("How many words do you want to enter? ")
)  # read text, convert to int, the user enters value from the keyboard

counts = {}  # empty dictionary
for i in range(1, n + 1):  # loop from 1 to n, the last value is included
    word = input(f"Word {i}: ")  # read text, the user enters value from the keyboard
    counts[word] = counts.get(word, 0) + 1  # counting occurrences

print()  # blank line
print("counts =", counts)  # display counts in console

print("Summary:")  # display summary in console
for word, c in counts.items():  # loop through keys and values
    print(f"{word} = {c}")  # display counting in console

print()  # blank line
