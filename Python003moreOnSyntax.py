

# in C, we use braces to define a block of code. In python, we use a colon and indentation.

# eg. in C:
# if (x > 5){
#     printf("x is greater than 5");
# }


# x = input("Enter a number: ") 
# in python:
# if x > 5:
#     print("x is greater than 5")

# but yes, this will throw an error because x is a string, not an integer

# to fix this, typecast x to an integer
# if int(x) > 5:
#     print("x is greater than 5")

# a quick example of a simple if condition
if int(input("Enter a number ")) > int(input("Enter another number ")):
    print("First number is greater")
else:
    print("Second number is greater")


# you can also use elif, which is short for else if
x = input("Do you agree? 'Y' or 'N' ")
if x == 'Y' or x == 'y': # in python, it's "or" not "||"
    print("You agreed")
elif x == 'N' or x == 'n':
    print("You disagreed")
else: 
    print("Invalid input")

# strings are compared lexicographically in python.
# eg:
print("apple" > "banana") # False

# "in" is a keyword in python that checks if something is present in something else  
print("apple" in "pineapple") # True
print(3 in [1,2,3,4,5]) # True

# you can also use "not in"
print("apple" not in "banana") # True

# you can also use "is" and "is not" to check if two objects are the same
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2) # True, as they are equal in value
print(list1 is list2) # False, as they might be equal in value, but they aren't the same object

# you can also use "and" and "or" to combine conditions
print(5 > 3 and 5 < 10) # True


# you can also use "pass" to do nothing
if 5 > 3:
    pass    # this will do nothing
else:
    print("This will not be printed")

# you can also use "not" to negate a condition
if not 5 > 3:
    print("This will not be printed")
else:
    print("This will be printed")
    
    
# when dealing with numbers, you don't need to worry about type conversions aka. int to float or whatever. 
# eg.
num1 = 40
num2 = 3
lol = num1/num2
print(lol)

# the python equivalent of C's format-specifier, is a formatted string aka f"{lol}"
# "%0.5f" in python is f"{lol:.5f}"

print(f"{lol:.5f}")

print("The value of pi is approximately %0.5f" %3.14159) # this is the C way of doing it
# another example

# width means the total number of characters to be printed
# precision means the number of digits after the decimal point

# width works only if the number of characters is less than the width

# example where width actually works:
print("The value of a random number is %10.3f" %12.34567) # this will print "     12.346" as the total number of characters is 10 and the number of characters in the number is 7
# if the number of characters is greater than the width, the width will be ignored
# if the number of characters is less than the width, the remaining characters will be filled with spaces

# switch case in python:
x = 5
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _: # default case
        print("Invalid input")
        
# no break statement. Only one among the cases will be executed


# multiline statements:
# you can use backslashes to continue a statement on the next line
print("Hello \
World")
x= 5\
+3 -\
2
print(x)

type('39') # str

x = 4.5
print(x.is_integer()) # o/p: False
num = x.as_integer_ratio() # this basically tells you the fraction of the number
print(num) # o/p: (9, 2) which means 4.5 is 9/2

imaginary = 3 + 4j
print(imaginary.real) # o/p: 3.0
print(imaginary.imag) # o/p: 4.0


# id function
# id(object) returns the memory address of the object
x = 5
print(id(x)) # o/p: 1407073664


# string splicing
string = "0123456789"
print(string[0]) 
print(string[1]) 
print(string[-1]) 
print(string[0:4])

# tuples
# An empty tuple can be initiated with empty parentheses.
# But a tuple with one or more elements, must contain at least one comma to be a tuple
# eg.
tuple1 = () 
print(type(tuple1)) # o/p: <class 'tuple'>
tuple2 = (1)
print(type(tuple2)) # o/p: <class 'int'>
tuple3 = (1,)
print(type(tuple3)) # o/p: <class 'tuple'>

# lists aren't like that tho
list1 = []
print(type(list1)) # o/p: <class 'list'>


# sets
set1 = {1,2,3,4,5}
set2 = {0,1,2,3,4,5,6,7,8,9}
print(set1.issubset(set2)) # o/p: True
print(set2.issuperset(set1)) # o/p: True
print(set1.union(set2)) # o/p: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1.intersection(set2)) # o/p: {1, 2, 3, 4, 5}
print(set1.difference(set2)) # o/p: set()
print(set2.difference(set1)) # o/p: {0, 6, 7, 8, 9}
print(set1.symmetric_difference(set2)) # o/p: {0, 6, 7, 8, 9}


print(repr("Hello, World!")) # o/p: 'Hello, World!'
print(repr(1000)) # o/p: 1000
print(repr(3.14)) # o/p: 3.14
print(repr(True)) # o/p: True
print(repr(False)) # o/p: False
print(repr([1,2,3,4,5])) # o/p: [1, 2, 3, 4, 5]
print(repr((1,2,3,4,5))) # o/p: (1, 2, 3, 4, 5)
print(repr({1,2,3,4,5})) # o/p: {1, 2, 3, 4, 5}
print(repr({1: "one", 2: "two", 3: "three"})) # o/p: {1: 'one', 2: 'two', 3: 'three'}


# bytes
# bytes are immutable
# bytearray are mutable
# bytes are used to store binary data
# eg.
x = b"Hello"

# or

x = bytes([72, 101, 108, 108, 111])

print(x) # o/p: b'Hello'
print(x[0]) # o/p: 72
print(x[1]) # o/p: 101

# x[0] = 65 # TypeError: 'bytes' object does not support item assignment

# for that:

x = bytearray([72, 101, 108, 108, 111])
x[0] = 65
print(x)
