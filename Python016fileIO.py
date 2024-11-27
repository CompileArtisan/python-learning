def fileIO():
    # another way to open a file
    with open("Python015fileIO.txt", "a") as file:
        file.write("\n" + input("Enter something else: "))
        
    # this replaces this:
    file = open("Python015fileIO.txt", "a")
    file.write("\n" + input("Enter something else: "))
    file.close()



def fileIO2():
    import io
    with io.StringIO() as file:
        file.write("Hello")
        file.seek(0)
        print(file.read()) 
        
        
    with io.StringIO("Hello world world") as file:
        print(file.read())
        
if __name__ == "__main__":
    # fileIO()
    fileIO2()