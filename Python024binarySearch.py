import random

def main():
    arr = []
    for i in range(11):
        arr.append(random.randint(0, 10))
    for i in range(len(arr)-1):
        print(arr[i], end = " ")
    print()
    if binarySearch(arr, int(input("Enter a number to search for in this random array: "))):
        print("Found")
    else:
        print("not found")

def binarySearch(array, value):
    array = sorted(array)
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = int((lo + hi)/2)
        if value == array[mid]:
            return True
        elif value < array[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False
        
 
    


if __name__ == "__main__":
    main()