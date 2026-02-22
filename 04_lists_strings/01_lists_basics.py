# 01_list_basics.py

# Examples of list basics using variables, input, output, and conditions

# create a list and access elements

numbers = [10, 20, 30, 40]  # list of numbers
print("numbers =", numbers)  # display list with the values

print("first =", numbers[0])  # first element
print("last =", numbers[-1])  # last element
print("length =", len(numbers))  # number of elements

print()  # blank line

# read values into a list (with input)

count = int(
    input("How many numbers do you want to enter? ")
)  # read text, convert to int, the user enters value from the keyboard

values = []  # empty list

for i in range(1, count + 1):  # loop from 1 to count, the last value is included
    x = int(
        input(f"Number {i}: ")
    )  # read text, convert to int, the user enters value from the keyboard
    values.append(x)  # add value at the end of the list

print("values =", values)  # display list with the values
print()  # blank line

# loop through a list and classify values

positive_count = 0  # set to int
negative_count = 0  # set to int
zero_count = 0  # set to int

print("classify values from the list")

for x in values:  # loop through the list values
    if x > 0:  # if value is positive
        positive_count = positive_count + 1  # counting positive values
        print(f"{x} is positive")
    elif x < 0:  # if value is negative
        negative_count = negative_count + 1  # counting negative values
        print(f"{x} is negative")
    else:  # if value is zero
        zero_count = zero_count + 1  # counting zero values
        print(f"{x} is zero")

print()  # blank line
print("Summary:")
print(f"Positives = {positive_count}")  # print positive values
print(f"Negatives = {negative_count}")  # print negative values
print(f"Zeros = {zero_count}")  # print zero values

print()  # blank line

# compute sum and average from the list

total = 0  # set to int
for x in values:  # loop through list values
    total = total + x  # total is increasing

print(f"Sum = {total}")  # print sum

if len(values) > 0:  # if list is not empty
    average = total / len(values)  # calculate average
    print(f"Average = {average}")  # print average
else:  # if list is empty
    print("Average cannot be computed because the list is empty.")  # print this text

print()  # blank line
