def main():
    p1 = Person("Rahul", 29)
    print(p1)
    e1 = Employee("Mohit", 45, 1001)
    print(e1)
    
    
# here are all ways to use inheritance in Python
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance

# Single Inheritance
# When a class inherits from a single class, it is called single inheritance.
# In the example below, the class Person is inherited by the class Employee.
# The class Employee has all the attributes and methods of the class Person.
# The class Employee can also have its own attributes and methods.
# The class Employee can also override the methods of the class Person.
# The class Employee can also have its own methods.
# The class Employee can also have its own constructor.

# Single Inheritance Example
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"\n\nName: {self.name}\nAge: {self.age}\n\n"
    
class Employee(Person):
    def __init__(self, name: str, age: int, emp_id: int):
        super().__init__(name, age)
        self.emp_id = emp_id

    def __str__(self):
        return f"\n\nName: {self.name}\nAge: {self.age}\nEmployee ID: {self.emp_id}\n\n"
    
# Multiple Inheritance
# When a class inherits from multiple classes, it is called multiple inheritance.
# In the example below, the class Person is inherited by the class Employee.
# The class Employee has all the attributes and methods of the class Person.
# The class Employee can also have its own attributes and methods.
# The class Employee can also override the methods of the class Person.
# The class Employee can also have its own methods.
# The class Employee can also have its own constructor.
# The class Employee can also inherit from another class, e.g., class Department.
# The class Department has its own attributes and methods.
# The class Employee can also override the methods of the class Department.
# The class Employee can also have its own methods.

# Multiple Inheritance Example
class Department:
    def __init__(self, dept_name: str, dept_id: int):
        self.dept_name = dept_name
        self.dept_id = dept_id

    def __str__(self):
        return f"\n\nDepartment Name: {self.dept_name}\nDepartment ID: {self.dept_id}\n\n"
    
class Employee(Person, Department):
    def __init__(self, name: str, age: int, emp_id: int, dept_name: str, dept_id: int):
        Person.__init__(self, name, age)
        Department.__init__(self, dept_name, dept_id)
        self.emp_id = emp_id

    def __str__(self):
        return f"\n\nName: {self.name}\nAge: {self.age}\nEmployee ID: {self.emp_id}\nDepartment Name: {self.dept_name}\nDepartment ID: {self.dept_id}\n\n"
    
# Multilevel Inheritance
# When a class inherits from another class, which in turn inherits from another class, it is called multilevel inheritance.
# In the example below, the class Person is inherited by the class Employee.
# The class Employee has all the attributes and methods of the class Person.
# The class Employee can also have its own attributes and methods.
# The class Employee can also override the methods of the class Person.
# The class Employee can also have its own methods.
# The class Employee can also have its own constructor.
# The class Employee can also inherit from another class, e.g., class Department.
# The class Department has its own attributes and methods.
# The class Employee can also override the methods of the class Department.
# The class Employee can also have its own methods.
# The class Department can also inherit from another class, e.g., class Company.
# The class Company has its own attributes and methods.
# The class Department can also override the methods of the class Company.
# The class Department can also have its own methods.

# Multilevel Inheritance Example
class Company:
    def __init__(self, company_name: str, company_id: int):
        self.company_name = company_name
        self.company_id = company_id

    def __str__(self):
        return f"\n\nCompany Name: {self.company_name}\nCompany ID: {self.company_id}\n\n"
    
class Department(Company):
    def __init__(self, company_name: str, company_id: int, dept_name: str, dept_id: int):
        Company.__init__(self, company_name, company_id)
        self.dept_name = dept_name
        self.dept_id = dept_id

    def __str__(self):
        return f"\n\nCompany Name: {self.company_name}\nCompany ID: {self.company_id}\nDepartment Name: {self.dept_name}\nDepartment ID: {self.dept_id}\n\n"
    
class Employee(Department):
    def __init__(self, company_name: str, company_id: int, dept_name: str, dept_id: int, name: str, age: int, emp_id: int):
        Department.__init__(self, company_name, company_id, dept_name, dept_id)
        self.name = name
        self.age = age
        self.emp_id = emp_id

    def __str__(self):
        return f"\n\nCompany Name: {self.company_name}\nCompany ID: {self.company_id}\nDepartment Name: {self.dept_name}\nDepartment ID: {self.dept_id}\nName: {self.name}\nAge: {self.age}\nEmployee ID: {self.emp_id}\n\n"
    
# Hierarchical Inheritance
# When a class is inherited by multiple classes, it is called hierarchical inheritance.
# In the example below, the class Person is inherited by the classes Employee and Student.
# The class Employee has all the attributes and methods of the class Person.
# The class Employee can also have its own attributes and methods.
# The class Employee can also override the methods of the class Person.
# The class Employee can also have its own methods.
# The class Employee can also have its own constructor.
# The class Student has all the attributes and methods of the class Person.
# The class Student can also have its own attributes and methods.
# The class Student can also override the methods of the class Person.
# The class Student can also have its own methods.
# The class Student can also have its own constructor.
                       


if __name__ == "__main__":
    main()