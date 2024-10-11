def main():
    table = [
        ["P1", 2,  6, 3],  # ProcessID, ArrivalTime, BurstTime, Priority
        ["P2", 5,  2, 1],
        ["P3", 1,  8, 4],
        ["P4", 0,  3, 2],
        ["P5", 4,  4, 5]
    ]
    priority_scheduling(table)
    
def priority_scheduling(table):
    table.sort(key=lambda x: x[1])
    table = [x + [0 for i in range(3)] for x in table]
    
    current_time = 0
    completed = 0
    ready_queue = []
    
    while completed < len(table):
        for process in table:
            if process[1] <= current_time and process not in ready_queue and process[4] == 0:
                ready_queue.append(process)
        
        if not ready_queue:
            current_time += 1
            continue
        
        ready_queue.sort(key=lambda x: x[3])  # Sort by priority
        
        current_process = ready_queue.pop(0)
        
        current_time += current_process[2]
        current_process[4] = current_time
        
        current_process[5] = current_process[4] - current_process[1] - current_process[2]
        current_process[6] = current_process[4] - current_process[1]
        
        completed += 1
    
    print("Gantt chart:")
    print("0", end="")
    for process in sorted(table, key=lambda x: x[4]):
        print(f" -> {process[0]} -> {process[4]}", end="")
    print()
    
    print("\nTable:")        
    for i in ["ProcessID","ArrivalTime", "BurstTime", "Priority", "CompletionTime", "WaitingTime", "TurnaroundTime"]:
        print(f"{i:<15}", end="")
    print()      
    for process in table:
        for item in process:
            print(f"{item:<15}", end="")
        print()
    
    avg_waiting_time = sum([x[5] for x in table]) / len(table)
    avg_turnaround_time = sum([x[6] for x in table]) / len(table)
    
    print(f"\nAverage waiting time: {avg_waiting_time:.2f}")
    print(f"Average turnaround time: {avg_turnaround_time:.2f}")
    
if __name__ == "__main__":
    main()
