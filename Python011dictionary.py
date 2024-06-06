def main():
    student1 = student()
    print(f'You are {student1["name"]}, who is {student1["age"]} years old and resides in {student1["city"]}')

def student():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    return {"name": name , "age": age , "city" : city,}




if __name__ == "__main__":
    main()
