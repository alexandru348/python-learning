# 02_variabiles.py
# Examples of variables, assignment and reassignment, types, conversions

x = 10 # set to int value
print(x) # display output
y = 3.14 # set to float value
print(y) # display output
z = "Alex" # set to string value
print(z) # display output
print("x type:", type(x)) # show type of value in console
print("y type:", type(y)) # show type of value in console
print("z type:", type(z)) # show type of value in console

a = 10 # set to int value
b = 3 # set to int value
print("a + b =", a + b) # display output and calculate a + b
print("a - b =", a - b) # display output and calculate a - b
print("a * b =", a * b) # display output and calculate a * b
print("a / b =", a / b) # display output and calculate a / b

d = 5 # set to int value
print("d =", d) # display output
d = d + 1 # calculate d + 1 (update d)
print("d = d + 1 ->", d) # display output
d = d - 2 # calculate d - 2 (update d)
print("d = d - 2 ->", d) # display output
d = d * 3 # calculate d * 3 (update d)
print("d = d * 3 ->", d) # display output
d = d / 2 # calculate d / 2 (update d, in Python "/" always returns float)
print("d = d / 2 ->", d) # display output
print() # blank line
name = input("Name: ") # read text  (string)
age = int(input("Age: ")) # read text, convert to int

print("Hello,", name) # display output
print("Next year you will be", age + 1) # display output (increase the age by 1)
