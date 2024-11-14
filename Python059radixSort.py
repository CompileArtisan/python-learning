def main():
    print(radixSort([175, 171, 173, 9]))
    
def radixSort(arr):
    n = len(str(max(arr)))
    for i in range(n):
        sorted = [[] for _ in range(10)]   
        for num in arr:
            sorted[(num//10**i)%10].append(num)
        arr = []
        for i in sorted:
            for j in i:
                if isinstance(j, int):
                    arr.append(j)
    return arr
            
    

if __name__ == "__main__":
    main()