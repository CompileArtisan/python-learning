def main():
    x = Student("Praanesh", 23123, 19)
    print(x.name)
    print(x.rollNumber)
    print(x.age)
    
    x.age = 18.5
    
    print()
    print(x.name)
    print(x.rollNumber)
    print(x.age)

class Student:
    def __init__(self, name, rollNumber, age):
        self.name = name
        self.rollNumber = rollNumber
        self.age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def rollNumber(self):
        return self._rollNumber
    
    @rollNumber.setter
    def rollNumber(self, rollNumber):
        if 0 < rollNumber <= 24000:
            self._rollNumber = rollNumber
        else:
            self._rollNumber = 0
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    

if __name__ == "__main__":
    main()
    
    
# by looking at the __init__() method, it looks like name, rollNumber and age are instance variables
# But the getters and setters below, make each of them a 'property'
# Everytime x.name is accessed, it forces control to a getter or a setter

# Even in the __init__(), method, self.name invokes the setters