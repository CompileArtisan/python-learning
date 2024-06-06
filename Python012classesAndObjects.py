def main():
    david = getStudent()
    print(f"You are {david.name} from {david.city}")

def getStudent():
    student = Student()
    student.name = input("Enter your name: ")
    student.city = input("Enter your city: ")
    return student

#   before actual OOPS, this is a program to show how else you can manipulate objects in 
# python apart from the regular creation and usage of instance variables and methods

#   in python, you can add object specific variables, like name and city above. 


class Student:
    pass


if __name__ == "__main__":
    main()