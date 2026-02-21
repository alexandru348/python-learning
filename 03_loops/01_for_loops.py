# 01_for_loops.py

# Examples of for loops using variables, input, output and conditions

# for with range() and simple conditions (with input)

start = int(input("Start: "))  # the user enters value from the keyboard
end = int(input("End: "))  # the user enters value from the keyboard

# if start is bigger than end, swap them
if start > end:
    start, end = end, start

print("range() and conditions")
for i in range(start, end + 1):  # loop from start to end, the last value is included
    if i % 2 == 0:  # if the value is even
        print(f"{i} is even")
    else:  # if the value is odd
        print(f"{i} is odd")

print()  # blank line

# for over a list using conditions (with input)

count = int(
    input("How many names do you want to enter? ")
)  # the user enters value from the keyboard

names = []  # list of names
for i in range(1, count + 1):  # loop from 1 to count, the last value is included
    name = input(f"Name {i}: ")  # the user enters the name from the keyboard
    names.append(name)  # the value of the variable is taken and added to the list

print("Loop through a list using conditions")
for name in names:  # loop through the names from the list
    if len(name) <= 3:  # if the length of the name is equal or less than 3
        print(f"{name} is a short name")
    else:  # if the length of the name is greater than 3
        print(f"{name} is a longer name")

print()

# read N numbers in a loop, classify them (conditions), then print a summary

n = int(
    input("How many numbers do you want to enter? ")
)  # the user enters value from the keyboard

total = 0  # set to int
positive_count = 0  # set to int
negative_count = 0  # set to int
zero_count = 0  # set to int

print("Read numbers and classify them")
for index in range(1, n + 1):  # loop from 1 to n, the last value is included
    value = int(
        input(f"Number {index}: ")
    )  # the user enters the number from the keyboard
    total = total + value  # the total is increasing

    if value > 0:  # if the value is greater than 0
        positive_count = (
            positive_count + 1
        )  # the number of positive values is increasing
        print(f"{value} is positive")
    elif value < 0:  # if the value is less than 0
        negative_count = (
            negative_count + 1
        )  # the number of negative values is increasing
        print(f"{value} is negative")
    else:  # if the value is equal to zero
        zero_count = zero_count + 1  # the number of zero values is increasing
        print(f"{value} is zero")

print()  # blank line
print("Summary:")
print(f"Sum = {total}")  # print sum
print(f"Positives = {positive_count}")  # print positive count
print(f"Negatives = {negative_count}")  # print negative count
print(f"Zeros = {zero_count}")  # print zeros count

if n > 0:  # if the value is greater than 0
    average = total / n  # the average is calculated
    print(f"Average = {average}")  # print average
else:  # if the value is equal to zero
    print("Average cannot be computed because n is 0.")  # print this text

print()  # blank line

# for with enumerate(index, value) and conditions (with input)

count = int(
    input("How many colors do you want to enter? ")
)  # the user enters value from keyboard

colors = []  # list of colors
for i in range(1, count + 1):  # loop from 1 to count, the last value is included
    color = input(f"Color {i}: ")  # the user enters the name of color from the keyboard
    colors.append(color)  # the value of variable is taken and added to the list

print("enumerate() gives index and value")
for idx, color in enumerate(colors):  # enumerate colors
    if idx == 0:  # if the name of the color is on the first position
        print(f"{idx}: {color} (first)")  # print (first) next to the name of color
    else:  # if the name of the color is on other position (second, third)
        print(f"{idx}: {color}")  # doesn't print first anymore

print()  # blank line
