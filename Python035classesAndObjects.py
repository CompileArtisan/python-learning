def main():
    p1 = Person("Rahul", 29)
    print(p1)
    p2 = Person.from_dob("Mohit", (12, 3, 1977))
    print(p2)
    print(Person.get_person_count())
    
class Person:
    count = 0  

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.count += 1  # Increment the count when a new person object is created

    @classmethod
    def from_dob(cls, name: str, dob: tuple):
        return cls(name, 2024 - dob[2])

    def __str__(self):
        return f"\n\nName: {self.name}\nAge: {self.age}\n\n"

    @classmethod
    def get_person_count(cls):
        return cls.count
    
    
if __name__ == "__main__":
    main()