def main():
    print(radixSort([170, 45, 75, 90, 802, 24, 2, 66]))
    
def radixSort(arr):
    n = len(str(max(arr)))
    m = 10
    for i in range(n):
        sorted = [[] for _ in range(10)]   
        for num in arr:
            sorted[(num//m)%10].append(num)
        arr = []
        for i in sorted:
            for j in i:
                if isinstance(j, int):
                    arr.append(j)
        m*=10
    return arr
            
    

if __name__ == "__main__":
    main()