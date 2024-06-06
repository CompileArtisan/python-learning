# calculator
def main():
    print(mult(int(input("Enter the first number: ")), int(input("Enter the second number: "))))


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b



if __name__ == "__main__":
    main()
    
# __name__ is a special variable in python
# a ".py" file can be used in two ways: 
#   1. run as an individual file : __name__ is "__main__"
#   2. imported by another file. : __name__ is something else
# Let's say you don't use "if __name__ blah blah thing". 
# If you import this file in some other file, instead of only being able to use its function, 
# the imported file's main function will be executed.