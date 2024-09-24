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
    
# lists can be multiplied
x = [0]*4 # 1x4 matrix
print(x)

# another example
x = [[1]*4]*3 # 3x4 matrix
print(x)

# or
x = [[1]*4 for _ in range(3)]
print(x)



l1 = ["cat", "dog", "monkey", "donkey"]

for element in enumerate(l1):
    print(element) # element is a tuple
    print(element[0]) # index of the element in the original list
    print(element[1]) # the actual element in the original list
    
for element in l1:
    print(element) # the same as print(element[1]) in the previous block
    
# enumerate also contains an optional secondary parameter: custom index
l2 = ["cat", "dog", "monkey", "donkey"]
for index, element in enumerate(l2, 10):
    print(index, element)
    
list1 = [22,33,44,56]
print(list(enumerate(list1))) 
# o/p: [(0, 22), (1, 33), (2, 44), (3, 56)]

    
list = [1, 2, 3, 4]
list2 = ["lol", "99"]
list.extend(list2)
for i in list:
    print(i)
    
    
# concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)
list4 = sum([list1, list2], start = [])
print(list4)
# list4 = sum([list1, list2], start = 0) # TypeError: can only concatenate list (not "int") to list
list5 = sum([list1, list2], start = [0])
print(list5)
list6 = sum([list1, list2], start = [0, 0])
print(list6)


# single line for loop and if statement
x = [i for i in range(10) if i % 2 == 0]
print(x)

# this short syntax of for loop and if condition in one line can only be used when you want to store the result in a list or a dictionary

# dictionary functions
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get("a"))
print(dict1.get("d")) # returns None
print(dict1.get("d", "Not found")) # returns "Not found"
print(dict1.pop("a")) # removes the key-value pair and returns the value
print(dict1)