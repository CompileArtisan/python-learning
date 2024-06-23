def main():
    pass


class Student:
    
    # static methods in Python
    @staticmethod
    def isTeenager(age):
        return 13 <= age <= 19
    
    # class methods in Python
    @classmethod
    
    
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