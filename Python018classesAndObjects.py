# this program delves into functions being objects in python

def say_hello():
    print("Hello, world!")

# Assigning the function to a variable
function_object = say_hello

# Calling the function using the variable
function_object()


# Functions can be passed as arguments to other functions
def say_hello():
    return "Hello, world!"

def call_say_hello(say_hello):
    print(say_hello()) 
    
# function that makes a function
def create_adder(x):
    def adder(y):
        return x + y
    return adder    

add_10 = create_adder(10)
print(add_10(3)) # returns 13
    