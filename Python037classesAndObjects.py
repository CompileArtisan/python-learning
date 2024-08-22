def main():
    p1 = Person("Rahul", 29)
    print(p1)
    p1.set_weight(65)
    print(p1.get_weight())
    print(p1.__weight) # error
    
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__weight = 0  # Private attribute
        
    def set_weight(self, weight: float):
        self.__weight = weight
        
    def get_weight(self):
        return self.__weight
    
    def __str__(self):
        return f"\n\nName: {self.name}\nAge: {self.age}\n\n"
    
class Student(Person):
    def __init__(self, name: str, age: int, roll_no: int):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        
    def __str__(self):
        return f"\n\nName: {self.name}\nAge: {self.age}\nRoll No: {self.roll_no}\n\n"
    
if __name__ == "__main__":
    main()