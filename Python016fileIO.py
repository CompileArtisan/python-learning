# another way to open a file
with open("Python015fileIO.txt", "a") as file:
    file.write("\n" + input("Enter something else: "))
    
# this replaces this:
file = open("Python015fileIO.txt", "a")
file.write("\n" + input("Enter something else: "))
file.close()