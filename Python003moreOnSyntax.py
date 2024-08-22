

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