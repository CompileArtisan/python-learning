import random

def main():
    arr = []
    for i in range(11):
        arr.append(random.randint(0, 10))
    for i in range(len(arr)-1):
        print(arr[i], end = " ")
    print()
    x = linearSearch(arr, int(input("Enter a number to search for in this random array: ")))
    if x:
        print(f"found at {x}")
    else:
        print("not found")

def linearSearch(array, value):
    for i in range(len(array)):
        if value == array[i]:
            return i       
 
    


if __name__ == "__main__":
    main()