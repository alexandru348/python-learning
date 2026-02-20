a = 20 # set to int
b = 25 # set to int
if a > b: # if a is greater than b
    print(a) 
else: # if b is greater than or equal to a
    print(b) 
if a == 0 and b == 0: # if a and b are equal to zero
    print("Values are equal to zero") 
elif a != 0 and b != 0: # if a and b are different from zero
    print("Values are different from zero") 
else: # if one value is zero and the other is non-zero
    print("One value is zero and the other is non-zero") 
age = int(input("Age: ")) # read text, convert to int
if age == a: # if age is equal to a
    print(f"Age {age} is equal to {a}") 
elif age > a: # else if age is greater than a
    print(f"Age {age} is greater than {a}") 
else: # if age is less than a
    print(f"Age {age} is less than {a}") 
if age == b: # if age is equal to b
    print(f"Age {age} is equal to {b}") 
elif age > b: # else if age is greater than b
    print(f"Age {age} is greater than {b}") 
else: # if age is less than b
    print(f"Age {age} is less than {b}") 

