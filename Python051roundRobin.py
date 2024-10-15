from collections import deque

def round_robin_scheduler(processes, time_quantum):
    time = 0
    ready_queue = deque()
    completed_processes = []
    n = len(processes)
    
    # Create a copy of processes to manipulate
    remaining_processes = [process.copy() for process in processes]
    
    # Dictionary to keep track of waiting time for each process
    waiting_time = {process[0]: 0 for process in processes}
    
    while len(completed_processes) < n:
        # Check for newly arrived processes
        for process in remaining_processes:
            if process[1] <= time and process not in ready_queue:
                ready_queue.append(process)
        
        if ready_queue:
            current_process = ready_queue.popleft()
            process_id, arrival_time, burst_time = current_process
            
            # Update waiting time for the current process
            waiting_time[process_id] += time - max(arrival_time, time - burst_time)
            
            if burst_time <= time_quantum:
                time += burst_time
                turnaround_time = time - arrival_time
                completed_processes.append([process_id, turnaround_time, waiting_time[process_id]])
                remaining_processes.remove(current_process)
            else:
                time += time_quantum
                current_process[2] -= time_quantum
                
                # Check for newly arrived processes again
                for process in remaining_processes:
                    if process[1] <= time and process not in ready_queue and process != current_process:
                        ready_queue.append(process)
                
                ready_queue.append(current_process)
            
            # Update waiting time for all processes in the ready queue
            for process in ready_queue:
                if process != current_process:
                    waiting_time[process[0]] += min(time_quantum, burst_time)
        else:
            time += 1
    
    return completed_processes

# Example usage
table = [
    ["P1", 0, 10],
    ["P2", 3, 4],
    ["P3", 5, 8],
    ["P4", 7, 13],
    ["P5", 100, 5]
]

time_quantum = 2
result = round_robin_scheduler(table, time_quantum)

print("Process | Turnaround Time | Waiting Time")
print("----------------------------------------")
for process in result:
    print(f"{process[0]:7} | {process[1]:15} | {process[2]:11}")

# Calculate and print average turnaround time and waiting time
avg_turnaround_time = sum(process[1] for process in result) / len(result)
avg_waiting_time = sum(process[2] for process in result) / len(result)
print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
print(f"Average Waiting Time: {avg_waiting_time:.2f}")