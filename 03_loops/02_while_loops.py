# 02_while_loops.py

# Exemples of while loops using variables, input, output and conditions

# while with counter (with input)

# loop from start to end, the last value is included

start = int(
    input("Start: ")
)  # read text, convert to int, the user enters value from the keyboard
end = int(
    input("End: ")
)  # read text, convert to int, the user enters value from the keyboard

# if start is bigger than end. swap them
if start > end:
    start, end = end, start

i = start  # start from first value
print("while loop from start to end")
while i <= end:
    if i % 2 == 0:  # if value is even
        print(f"{i} is even")
    else:  # if value is odd
        print(f"{i} is odd")
    i = i + 1  # counting values

print()  # blank line

# while sum from 1 to n (with input)

n = int(
    input("n: ")
)  # read text, convert to int, the user enters value from the keyboard

total = 0  # set to int
i = 1  # set to int

print("sum from 1 to n")
while i <= n:
    total = total + i  # the total is increasing
    i = i + 1  # counting values
print(f"Sum = {total}")
print()  # blank line


# while read N numbers in a loop, classify them (conditions), then print a summary

n = int(
    input("How many numbers do you want to enter? ")
)  # read text, convert to int, the user enters value from the keyboard

total = 0  # set to int
positive_count = 0  # set to int
negative_count = 0  # set to int
zero_count = 0  # set to int

print("Read numbers and classify them")
index = 1  # index start from the first position
while index <= n:
    value = int(
        input(f"Number {index}: ")
    )  # read text, convert to int, the user enters value from the keyboard
    total = total + value  # the total is increasing

    if value > 0:  # if value is bigger than 0
        positive_count = positive_count + 1  # counting the positive values
        print(f"{value} is positive")
    elif value < 0:  # if value is less than 0
        negative_count = negative_count + 1  # counting the negative values
        print(f"{value} is negative")
    else:  # if value is 0
        zero_count = zero_count + 1  # counting zero values
        print(f"{value} is zero")

    index = index + 1  # index is increasing

print()  # blank line
print("Summary:")
print(f"Sum = {total}")
print(f"Positives = {positive_count}")
print(f"Negatives = {negative_count}")
print(f"Zeros = {zero_count}")

if n > 0:  # if values are bigger than 0
    average = total / n  # calculate the average
    print(f"Average = {average}")
else:  # if values are less than 0
    print("Average cannot be computed because n is 0.")

print()  # blank line

# while input validation (repeat until valid input)

x = int(
    input("Positive number: ")
)  # read text, convert to int, the user enters value from the keyboard

while x <= 0:  # if the entered value is non-negative
    print("Please enter a positive number")
    x = int(
        input("Positive number: ")
    )  # read text, convert to int, the user enters value from the keyboard

print(f"Valid number = {x}")  # print valid number
print()  # blank line
