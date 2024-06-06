def main():
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    print(f"The sum of {a} and {b} is {sum(a,b)}.")


def sum(a,b):
    if a.isdigit() and b.isdigit():
        return int(a) + int(b)
    else:
        return False
    
main()

# let the actual code be the first thing someone sees when digging into your program, and have your functions at the end
# but in python, you can't use something first and then define it, since this is an interpreter
# the only solution is:
#       put all your code in a main function
#       then declare and define all your other function
#       then the very last line, will be calling your main function
# this way, everything, is known to the interpreter.