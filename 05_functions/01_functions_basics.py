# 01_functions_basics.py

# Examples of function basics using variables, input, output, and return

# function with no parameters


def greet():  # define function
    print("Hello")  # display output in console


greet()  # call function
print()  # blank line

# function with parameters (with input)

name = input("Name: ")  # read text, the user enters value from the keyboard
age = int(
    input("Age: ")
)  # read text, convert to int, the user enters value from the keyboard


def show_person(name, age):  # define function
    print(f"Name = {name}")  # display output in console
    print(f"Age = {age}")  # display output in console


print("Output:")  # show a label before printing results
show_person(name, age)  # call function
print()  # blank line

# function with return value (with input)

a = int(
    input("a: ")
)  # read text, convert to int, the user enters value from the keyboard
b = int(
    input("b: ")
)  # read text, convert to int, the user enters value from the keyboard


def add(a, b):  # define function
    result = a + b  # calculate sum
    return result  # return value


sum_result = add(a, b)  # call function and store result in a variable
print("Output:")  # show a label before printing results
print(f"Sum = {sum_result}")  # display output
print()  # blank line

# use function in a loop (list)

count = int(
    input("How many numbers do you want to enter? ")
)  # read text, convert to int, the user enters value from the keyboard

values = []  # empty list
for i in range(1, count + 1):  # loop from 1 to count, the last value is included
    x = int(
        input(f"Number {i}: ")
    )  # read text, convert to int, the user enters value from the keyboard
    values.append(x)  # add value at the end of the list


def is_even(n):  # define function
    return n % 2 == 0  # return True if the value is even, False if the value is odd


even_count = 0  # set to int
odd_count = 0  # set to int

print("Output:")  # show a label before printing results
print("classify numbers using a function")

for x in values:  # loop through the list values
    if is_even(x):  # call function in condition
        even_count = even_count + 1  # counting even values
        print(f"{x} is even")
    else:  # if value is odd
        odd_count = odd_count + 1  # counting odd values
        print(f"{x} is odd")

print()  # blank line
print("Summary:")
print(f"Evens = {even_count}")  # print even count
print(f"Odds = {odd_count}")  # print odd count
print()  # blank line
