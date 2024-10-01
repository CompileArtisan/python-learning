# input and output statements
print("hey on line 1")
print('hey on line 2') # single quotes are also valid. No backticks though

# same as:
# print("hey on line 1"); print("hey on line 2")

name = input("What's your name? ") # no datatype for variables.
print("Obama says hello",name) # comma separated values are concatenated with a space
print("hello","word","sorry","world")
print("Trump says hey there " + name) # + operator concatenates strings

print("\n\n") # \n is newline character. \n\n is two newlines

city = input("Where are you from? ")
print(f"Hello {name}. You are from {city}.") # f-string, which stands for formatted string

# here's another way of formatted strings:
print("Hello {}. You are from {}.".format(name,city)) # {} are placeholders for variables

# print() is most comparable to System.out.println() in java


randomString = '''This is a multiline string.
It is  enclosed in triple quotes.
So ig you can write anything here.'''
print(randomString)

''' 
Multi-line strings can be used as multiline comments in python.
'''

"Generally, strings as plain statements in python don't do anything. They are just ignored."


x = 3
print(x**2)

# format specifiers for spacing out
print("The value of pi is approximately %0.5f" %3.14159) # this is the C way of doing it
# another example

# width means the total number of characters to be printed
# precision means the number of digits after the decimal point

# width works only if the number of characters is less than the width

# example where width actually works:
print("The value of a random number is %10.3f" %12.34567) # this will print "     12.346" as the total number of characters is 10 and the number of characters in the number is 7


# the same thing can be done using the format() method
print("The value of pi is approximately {0:0.5f}".format(3.14159))

# string formatting using f-strings
myString = "World"
print(f"Hello {myString:>10} Hello")

# padding strings to the left
print(f"Hello {myString:<10} Hello")

# centering strings
print(f"Hello {myString:^10} Hello")



# sep in print
print("Hello","World",sep=" ") # default separator is a space
print("Hello","World",sep="") # no separator
