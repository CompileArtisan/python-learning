# more on the input/output statements

# typecasting in python: dataType(whatever you want to typecast)
# eg:
# a = "5"
# b = int(a) # b is now an integer

# int() is a function that converts something to an integer. 


x = input("Enter a number: ")
y = input("Enter another number: ")
print(x+y) # this will concatenate the strings, not add the numbers

# to add the numbers, typecast them to integers
x = int(x)
y = int(y)
print(x+y)

# or another way is to typecast the input directly
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(a+b)

# by default, every print statement in python ends with a newline character. You can change it too:
print("Hello",end=" ") # end is an optional parameter. Default is \n
print("World") # this will be printed on the same line as the previous print statement