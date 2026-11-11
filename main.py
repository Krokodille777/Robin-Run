from collections import deque

def round_robin(processes, quantum): #Round Robin Scheduling Algorithm
    queue = deque(processes)
    time = 0
    timeline = []
    completion = {}

    while queue: # While there are processes in the queue
        name, rem = queue.popleft()
        run = min(quantum, rem)

        timeline.append((name, time, time + run))
        time += run
        rem -= run

        if rem > 0:
            queue.append((name, rem)) # Add the process back to the queue if it still has remaining time
        else:
            completion[name] = time # Record the completion time for the process if it has finished executing

    return timeline, completion


def read_input (): # Read input from the user

    print("Press Enter to use the example data, \n OR enter number of processes: ")
    line = input("Number of processes: ")

    if line == "":
        return [("P1", 10), ("P2", 5), ("P3", 8)], 2

    n = int(line)
    processes = []
    for i in range(n):
        default_name = chr(ord("A") + i) # Default process name. chr(ord("A") + i) generates names like A, B, C, etc.
        name = input(f"Process {i + 1} [{default_name}] name: ").strip() or default_name
        burst = int(input(f"Execution for {name}: ")) # Burst time is the time required for the process to complete its execution
        if burst <= 0:
            raise ValueError("Execution time must be a positive integer!") #If the burst time is not a positive integer, raise a ValueError
        processes.append((name, burst))
    quantum = int (input("Enter quantum time: "))
    if quantum <= 0: #Quantum must also be a positive integer, otherwise raise a ValueError
        raise ValueError("Quantum time must be a positive integer!")
    return processes, quantum


def print_results(processes, quantum, timeline, completion): # Print the results of the Round Robin scheduling
    print("\nProcesses:")
    for name, burst in processes:
        print(f"  Process {name} - Execution time: {burst}, Quantum: {quantum}")
 
    # Execution order
    order = ", ".join(f"Process {name} ({end - start})" for name, start, end in timeline)
    print("\nExecution order:", order)


    # Gantt chart
    print("\nДіаграма Ганта:")
    bar = "|"
    scale = ""
    for name, start, end in timeline:
        cell = f" {name} ".center(max(4, (end - start) * 2))
        bar += cell + "|"
        scale += str(start).ljust(len(cell) + 1)
    scale += str(timeline[-1][2])
    print(bar)
    print(scale)
 
 
def main():
    try: # Read input from the user and handle any ValueErrors that may arise
        processes, quantum = read_input()
    except ValueError as e:
        print("Input error:", e)
        return
 
    timeline, completion = round_robin(processes, quantum) 
    print_results(processes, quantum, timeline, completion)
 
 
if __name__ == "__main__": # If this script is run directly (not imported), call the main function
    main()
        