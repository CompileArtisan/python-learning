def main():
    table = [
        ["P1", 2,  6, 3],  # ProcessID, ArrivalTime, BurstTime, Priority
        ["P2", 5,  2, 1],
        ["P3", 1,  8, 4],
        ["P4", 0,  3, 2],
        ["P5", 4,  4, 5]
    ]
    preemptive_priority_scheduling(table)
    
def preemptive_priority_scheduling(table):      
    processes = [Process(p[0], p[1], p[2], p[3]) for p in table]
    current_time = 0
    completed = 0
    timeline = []
    
    while completed < len(processes):
        ready_queue = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
        
        if not ready_queue:
            current_time += 1
            timeline.append(("Idle", current_time))
            continue
        
        ready_queue.sort(key=lambda x: (x.priority, x.arrival_time))
        current_process = ready_queue[0]
        
        current_process.remaining_time -= 1
        current_time += 1
        timeline.append((current_process.id, current_time))
        
        if current_process.remaining_time == 0:
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed += 1
    
    print("Gantt chart:")
    print("0", end="")
    for process_id, time in timeline:
        print(f" -> {process_id} -> {time}", end="")
    print()
    
    print("\nTable:")        
    headers = ["ProcessID", "ArrivalTime", "BurstTime", "Priority", "CompletionTime", "WaitingTime", "TurnaroundTime"]
    for header in headers:
        print(f"{header:<15}", end="")
    print()      
    for process in processes:
        print(f"{process.id:<15}{process.arrival_time:<15}{process.burst_time:<15}{process.priority:<15}"
              f"{process.completion_time:<15}{process.waiting_time:<15}{process.turnaround_time:<15}")
    
    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    
    print(f"\nAverage waiting time: {avg_waiting_time:.2f}")
    print(f"Average turnaround time: {avg_turnaround_time:.2f}")

class Process:
    def __init__(self, id, arrival_time, burst_time, priority):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

if __name__ == "__main__":
    main()