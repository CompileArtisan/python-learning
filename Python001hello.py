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

