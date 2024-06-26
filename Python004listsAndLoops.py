answer = input("Do you want to continue? yes or no: ").lower()
if answer in ["yes","y"]:
    print("Continuing...")
elif answer in ["no","n"]:
    print("Exiting...")
else:
    print("Invalid input")

#loops
for i in [1,2,4,8]:
    print(i)

for i in range(4): # range(n) returns an iterable collection of whole numbers until n, i.e. 0,1,2,3,...n
    print(i)

for i in range(1,6): # range(start, end excluded)
    print(i)
    
for i in range(3,13,3): # range(start, end excluded , skip value)
    print(i)
    

x = [0,1,2,3]
print(x) # prints: [0, 1, 2, 3]

y = range(4)
print(y) # prints: range(0,4)
# range can't be used as a list.


# random example of string object
word = input("Enter something: ")
print(f"All capitalised: {word.upper()}")
print(f"First letter cap: {word.capitalize()}")
print(word.isdigit())

# strings can be multiplied:
string = "Abc" * 4 # = AbcAbcAbcAbc
print(string)

# lists can have multiple data types 
randomList = [True, 303, "Person"]
for item in randomList:
    print(item)