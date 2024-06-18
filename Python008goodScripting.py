import Python007goodScripting as calculator
def main():
    print(calculator.mult(3,4))
    
def incompleteFunction():
    ...
    
# in python, no code is denoted by "ellipsis" aka triple-dot
# both pass and ellipsis are placeholders
# ellipsis is an indication that some code is missing
# pass is an indication that you're intentionally doing nothing

def function_we_could_add_later_on():
    pass

# do note that both pass and ellipsis, doesn't impact any code under it. 
# You can have a pass or ellipsis anywhere and it will do nothing.

if __name__ == "__main__":
    main()