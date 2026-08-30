#  Task 06: Pirate King's Scheduler

##  Overview

Pirate King's Scheduler is a CPU Scheduling Simulator developed in "Golang"

The program simulates how processes (pirate crews) wait for and receive CPU execution time. It supports three CPU scheduling algorithms:

1. First Come First Serve (FCFS)
2. Shortest Job First (SJF - Non-Preemptive)
3. Round Robin (RR)

The program runs completely in the terminal and does not require a GUI.



##  Objectives

The main objectives of this task are:

- Understand CPU scheduling concepts.
- Implement different CPU scheduling algorithms in Go.
- Accept process information from the user.
- Calculate scheduling performance metrics.
- Display the execution sequence using a Gantt Chart.
- Compare the behaviour of different scheduling algorithms.



##  Features

The simulator accepts:

- Process ID
- Arrival Time
- Burst Time
- Time Quantum for Round Robin

The user can select one of the following algorithms:

- FCFS
- SJF (Non-Preemptive)
- Round Robin

The program calculates:

- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)
- Average Waiting Time
- Average Turnaround Time

It also displays the process execution order using a simple Gantt Chart / Timeline.



##  Scheduling Algorithms

### 1. First Come First Serve (FCFS)

FCFS executes processes in the order in which they arrive.

The process that arrives first gets the CPU first and continues until it finishes.

#### Advantages

- Simple to understand and implement.
- Fair according to arrival order.

#### Disadvantages

- A long process can make shorter processes wait for a long time.
- It is a non-preemptive scheduling algorithm.



### 2. Shortest Job First (SJF)

SJF selects the process with the shortest Burst Time among the processes that have already arrived.

This implementation uses "Non-Preemptive SJF", which means that once a process starts executing, it continues until completion.

#### Advantages

- Can reduce average waiting time.
- Short processes are completed quickly.

#### Disadvantages

- Longer processes may have to wait.
- The scheduler must know the Burst Time of processes.



### 3. Round Robin (RR)

Round Robin assigns each process a fixed amount of CPU time called the "Time Quantum"

If a process does not finish within its time quantum, it is placed at the back of the ready queue and another process gets the CPU.

This process continues until all processes are completed.

#### Advantages

- Provides fair CPU access to processes.
- Suitable for time-sharing systems.
- Prevents one process from using the CPU continuously.

#### Disadvantages

- Performance depends on the chosen Time Quantum.
- A very small Time Quantum can cause many context switches.



##  Scheduling Calculations:

### Completion Time (CT)

Completion Time is the time at which a process finishes execution.

### Turnaround Time (TAT)

Turnaround Time is calculated as:


TAT = Completion Time - Arrival Time

## Waiting Time(WT)

Waiting Time is calculated as:

WT = Turnaround Time - Burst Time

## Aerage Waiting Time
Average Waiting Time =
Total Waiting Time / Number of Processes

## Average Turnaround Time
Average Turnaround Time =
Total Turnaround Time / Number of Processes

## Program Approach:

* Ask the user for the number of processes.
* Read the Process ID, Arrival Time and Burst Time for each process.
* Display the scheduling algorithm menu.
* Ask the user to select FCFS, SJF or Round Robin.
* If Round Robin is selected, ask for the Time Quantum.
* Run the selected scheduling algorithm.
* Generate the process execution order.
* Generate a Gantt Chart / Timeline.
* Calculate Completion Time, Turnaround Time and Waiting Time.
* Calculate the average Waiting Time and Turnaround Time.
* Display all results in the terminal.

main.go

Contains the complete CPU scheduling simulator and implementations of:

FCFS
SJF
Round Robin
Gantt Chart generation
Scheduling calculations
User input handling
Result display

go.mod:

Contains the Go module information required for the project.

To run the go program:
go run main.go

* The following resources were used to understand the concepts required for this task:

Go Programming Language documentation
CPU Scheduling concepts and Operating Systems study materials
Tutorials and references for FCFS, SJF and Round Robin scheduling
VS Code for writing and testing the Go program.

what i learned:

During this task, I learned,

Basics of the Go programming language.
Go structures (struct).
Functions and function parameters.
Slices in Go.
Sorting data using Go's sort package.
Taking user input using fmt.Scan.
Implementing CPU scheduling algorithms.
Understanding Arrival Time and Burst Time.
Calculating Completion Time, Turnaround Time and Waiting Time.
Implementing a queue for Round Robin scheduling.
Generating a Gantt Chart using terminal output.
Working with Go modules.
Running Go programs from the terminal.

Challenges faced:

Some of the challenges during the task were understanding how Go programs are structured and learning how CPU scheduling algorithms work.

Implementing Round Robin was particularly challenging because processes have to be managed using a ready queue and can execute multiple times before completing.

Understanding the relationship between Arrival Time, Burst Time, Completion Time, Turnaround Time and Waiting Time was also an important part of the task.

Conclusion:


Pirate King's Scheduler demonstrates how different CPU scheduling algorithms manage processes competing for CPU execution.

The project helped me understand both the practical implementation of scheduling algorithms and the fundamentals of programming in Go.

The simulator can be used to observe how changing the scheduling algorithm or Time Quantum affects process execution, waiting time and turnaround time.

