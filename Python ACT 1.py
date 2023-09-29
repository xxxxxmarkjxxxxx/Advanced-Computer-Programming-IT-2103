#!/usr/bin/python3

name = str(input("Input your name:"))
age = int(input("Input your age:"))
add = str(input("Input your address:"))

print("Your name is:",name)
print("Your age is:",age)
print("Your address is:",add)

byear = int(input("Input your birthyear:"))
cyear = int(input("Input the current year:"))

age = cyear - byear
print("Your age is:",age)
