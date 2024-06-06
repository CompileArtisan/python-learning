def main():
    student = Student(input("Enter name: "), input("Enter city: "))
    # instead of manually fetching values of instance variables and printing:
    print(student) # would be better, but you're just going to print the memory location
    
    # here's what's actually happening:
    #   when you're printing an object reference, a method "__str__()" gets called.
    #   so line 4 is actually, print(student.__str__())
    # so what we CAN do, is simply "overload" this method (although that's not the thing here)
    # it's not really overloading. It's just python's way of customizing objects


class Student:
    def __init__(self, name, city):
        self.name = name 
        self.city = city
        
    def __str__(self):
        return f"Name: {self.name}\nCity: {self.city}"
        
if __name__ == "__main__":
    main()
    