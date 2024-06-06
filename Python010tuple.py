def main():
    details = student()
    print(f"You are {details[0]}, from {details[1]}")

def student():
    return input("Enter the student's name: "), input("Enter the student's city: ")
# this returns a tuple of two strings

if __name__ == "__main__":
    main()