def main():
    file = open("Python015fileIO.txt", "w")
    # "w" is for write mode
    # what this does is, it creates a file if it doesn't exist
    # and if it does, it overwrites the contents
    # this is how you write to a file:
    file.write(input("Enter something: ")) # it also prints the number of characters written, on the console
    file.close() # only if you do this, will your changes be saved
    




    file = open("Python015fileIO.txt", "r")
    # "r" is for read mode
    # what this does is, it reads the contents of the file    
    # if the file doesn't exist, it throws an error
    # this is how you extract the contents of the file:
    print(file.read())
    file.close()
    




    file = open("Python015fileIO.txt", "a")
    # "a" is for append mode
    # what this does is, it appends the contents to the file
    # if the file doesn't exists, it creates a file
    # this is how you append to a file:
    file.write("\n" + input("Enter something else: "))
    file.close()
    

  
    # to delete a file:
    import os
    os.remove("Python015fileIO.txt")
    
    


if __name__=="__main__":
    main()