# ran into issues naming this new python file.
# was wondering why it couldn't open the file .
# realized it was because I didn't put ".py" after the name.
# felt very stupid but felt good trouble shooting it

# Variables and Types
from locale import format_string
from traceback import format_stack


print("Variables and Types")

mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# ran into issues with the "hello" part.
# it kept saying I had a syntax error with the ":"
# didn't really see what was wrong with it. It looked fine.
# ended up rewriting it and it worked.

print(" ")
print("Lists")
# Lists
numbers = [1,2,3]
strings = ["Hello", "World"]
names = ["John", "Eric", "Jessica"]

#write my code here
second_name = "Eric"

print(numbers)
print(strings)
print("The sacond name on the names is %s" % second_name)

# I tried this using the correct second name and then with a different one to see what would happen.

print(" ")
print("Basic Operators")
# Basic Operators
x = object()
y = object()

x_list = ["x" * 10]
y_list = ["y" * 10]
big_list = [x_list + y_list]

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# what is %d? short cuts to get to end of line (not end of code)? -- NVM figured out these are argument specifiers.
# this was my 2nd attempt. Still got it wrong. First attempt i did exponents on accident.

print(" ")

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = [x_list + y_list]

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# third try. I messed up the brackets in big list. Was not getting 20 objects. I understand why it was showing 1 object.

print(" ")

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Finally got it right. Understand my mistakes. 
# I need to remember to save before running the file

print(" ")

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

print(" ")

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# Forgot to add in the testing part.

print(" ")

# String Formatting
print("String Formatting")
print(" ")

# how do we comment out a section of code? I will try creating different files on another commit/push. Then maybe merge/call all files into the main one. Probably good practice.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# This one was confusing. I got tripped up because I thought I had to write it in the "print" function. After doing it I understand what I was doing wrong.
print(" ")
print("Basic String Operations")

# len = length --> to remember

