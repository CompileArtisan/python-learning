def main():
    student = Student(input("Enter name: "), input("Enter city: "))
    print(f"You are {student.name} from {student.city}")

class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city      
    
# The java code for creating a student constructor, is:
    
#     Student(String name, String city){
#         this.name = name;
#         this.city = city;
#     } 
    
# in Python though, it's like this:

#     def __init__(self, name, city):
#         self.name = name
#         self.city = city 

#    calling the constructor is the same, but defining the 
# constructor is slightly different.

#    You'll have to manually pass in the current object
# 'self' (just like 'this') into the constructor 
# '__init__()'





if __name__=="__main__":
    main()