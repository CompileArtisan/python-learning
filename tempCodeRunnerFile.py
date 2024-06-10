    file = open("Python015fileIO.txt", "w") 
    # "w" is for write mode
    # what this does is, it creates a file if it doesn't exist
    # and if it does, it overwrites the contents
    # this is how you write to a file:
    file.write(input("Enter something: "))
    file.close()