# inputs: 
# 1. Number of processes
# 2. Process ID
# 3. Arrival time of each process
#   i. All arrive at time = 0
#   ii. All arrive at different times
# 4. Burst times of each process

def main():
    table = [
    #     ID ,AT, BT
        ["P1", 0, 10], 
        ["P2", 3,  4], 
        ["P3", 5,  8], 
        ["P4", 7, 13], 
        ["P5",100,  5]
    ]
    fcfs(table)
    
def fcfs(table):
    table.sort(key=lambda x: x[1])
    table = [x + [0 for i in range(3)] for x in table]
    table[0][3] = table[0][1] + table[0][2]
    for i in range(1, len(table)):
        table[i][3] = max(table[i-1][3], table[i][1]) + table[i][2]
        table[i][4] = max(table[i-1][3] - table[i][1], 0)
    for i in range(len(table)):
        table[i][5] = table[i][3] - table[i][1]
    for i in ["ProcessID","ArrivalTime", "BurstTime", "CompletionTime", "WaitingTime", "TurnaroundTime"]:
        print(f"{i:<15}", end="")
    print()      
    for i in table:
        for j in i:
            print(f"{j:<15}", end="")
        print()
    print("Average waiting time:", sum([x[4] for x in table])/len(table))
    print("Average turnaround time:", sum([x[5] for x in table])/len(table))
    
    
if __name__ == "__main__":
    main()