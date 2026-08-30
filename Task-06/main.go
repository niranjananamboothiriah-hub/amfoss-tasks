package main

import (
	"fmt"
	"sort"
)

// Process represents one process.
type Process struct {
	ID         string
	Arrival    int
	Burst      int
	Completion int
	Turnaround int
	Waiting    int
}

// calculateTimes calculates Turnaround Time and Waiting Time.
func calculateTimes(p *Process) {
	p.Turnaround = p.Completion - p.Arrival
	p.Waiting = p.Turnaround - p.Burst
}

// copyProcesses creates a separate copy of the process list.
func copyProcesses(processes []Process) []Process {
	result := make([]Process, len(processes))
	copy(result, processes)
	return result
}

// FCFS - First Come First Serve
func fcfs(processes []Process) ([]Process, []string, []int) {

	// Sort processes according to Arrival Time.
	sort.SliceStable(processes, func(i, j int) bool {
		return processes[i].Arrival < processes[j].Arrival
	})

	currentTime := 0

	order := []string{}
	times := []int{0}

	for i := range processes {

		// If CPU is idle, move time to the arrival time.
		if currentTime < processes[i].Arrival {
			currentTime = processes[i].Arrival

			order = append(order, "Idle")
			times = append(times, currentTime)
		}

		// Process starts and finishes.
		order = append(order, processes[i].ID)

		currentTime += processes[i].Burst

		processes[i].Completion = currentTime

		calculateTimes(&processes[i])

		times = append(times, currentTime)
	}

	return processes, order, times
}

// SJF - Shortest Job First (Non-Preemptive)
func sjf(processes []Process) ([]Process, []string, []int) {

	n := len(processes)

	completed := make([]bool, n)

	completedCount := 0
	currentTime := 0

	order := []string{}
	times := []int{0}

	for completedCount < n {

		shortest := -1

		// Find the shortest process that has arrived.
		for i := 0; i < n; i++ {

			if !completed[i] &&
				processes[i].Arrival <= currentTime {

				if shortest == -1 ||
					processes[i].Burst < processes[shortest].Burst {

					shortest = i
				}
			}
		}

		// If no process has arrived, move the clock forward.
		if shortest == -1 {

			nextArrival := -1

			for i := 0; i < n; i++ {

				if !completed[i] {

					if nextArrival == -1 ||
						processes[i].Arrival < nextArrival {

						nextArrival = processes[i].Arrival
					}
				}
			}

			order = append(order, "Idle")
			currentTime = nextArrival
			times = append(times, currentTime)

			continue
		}

		// Run the shortest process completely.
		order = append(order, processes[shortest].ID)

		currentTime += processes[shortest].Burst

		processes[shortest].Completion = currentTime

		calculateTimes(&processes[shortest])

		completed[shortest] = true
		completedCount++

		times = append(times, currentTime)
	}

	return processes, order, times
}

// Round Robin
func roundRobin(processes []Process, quantum int) ([]Process, []string, []int) {

	n := len(processes)

	// Sort by Arrival Time.
	sort.SliceStable(processes, func(i, j int) bool {
		return processes[i].Arrival < processes[j].Arrival
	})

	// Remaining Burst Time for every process.
	remaining := make([]int, n)

	for i := 0; i < n; i++ {
		remaining[i] = processes[i].Burst
	}

	// Queue contains process indexes.
	queue := []int{}

	// Keeps track of whether a process is already in queue.
	inQueue := make([]bool, n)

	currentTime := 0
	completed := 0

	order := []string{}
	times := []int{0}

	for completed < n {

		// Add all processes that have arrived.
		for i := 0; i < n; i++ {

			if processes[i].Arrival <= currentTime &&
				remaining[i] > 0 &&
				!inQueue[i] {

				queue = append(queue, i)
				inQueue[i] = true
			}
		}

		// If queue is empty, jump to the next arrival.
		if len(queue) == 0 {

			nextArrival := -1

			for i := 0; i < n; i++ {

				if remaining[i] > 0 {

					if nextArrival == -1 ||
						processes[i].Arrival < nextArrival {

						nextArrival = processes[i].Arrival
					}
				}
			}

			currentTime = nextArrival
			times = append(times, currentTime)

			continue
		}

		// Take the first process from the queue.
		index := queue[0]

		// Remove it from the front.
		queue = queue[1:]

		inQueue[index] = false

		// Normally run for the full time quantum.
		runTime := quantum

		// If less time remains, run only the remaining time.
		if remaining[index] < quantum {
			runTime = remaining[index]
		}

		// Run the process.
		order = append(order, processes[index].ID)

		currentTime += runTime

		remaining[index] -= runTime

		times = append(times, currentTime)

		// Add newly arrived processes to the queue.
		for i := 0; i < n; i++ {

			if processes[i].Arrival <= currentTime &&
				remaining[i] > 0 &&
				!inQueue[i] &&
				i != index {

				queue = append(queue, i)
				inQueue[i] = true
			}
		}

		// Check whether the process has finished.
		if remaining[index] == 0 {

			processes[index].Completion = currentTime

			calculateTimes(&processes[index])

			completed++

		} else {

			// Process is not finished.
			// Put it at the back of the queue.
			queue = append(queue, index)
			inQueue[index] = true
		}
	}

	return processes, order, times
}

// printGanttChart prints the execution order.
func printGanttChart(order []string, times []int) {

	fmt.Println("\nGantt Chart / Timeline:")
	fmt.Println()

	for _, id := range order {
		fmt.Printf("| %-7s", id)
	}

	fmt.Println("|")

	for _, time := range times {
		fmt.Printf("%-9d", time)
	}

	fmt.Println()
}

// printResults prints the process table and averages.
func printResults(processes []Process) {

	fmt.Println()
	fmt.Println("-------------------------------------------------------------")
	fmt.Printf("%-10s %-10s %-10s %-10s %-10s %-10s\n",
		"Process", "AT", "BT", "CT", "TAT", "WT")
	fmt.Println("-------------------------------------------------------------")

	totalWaiting := 0
	totalTurnaround := 0

	// Sort results by Process ID for easy reading.
	sort.SliceStable(processes, func(i, j int) bool {
		return processes[i].ID < processes[j].ID
	})

	for _, p := range processes {

		fmt.Printf("%-10s %-10d %-10d %-10d %-10d %-10d\n",
			p.ID,
			p.Arrival,
			p.Burst,
			p.Completion,
			p.Turnaround,
			p.Waiting)

		totalWaiting += p.Waiting
		totalTurnaround += p.Turnaround
	}

	fmt.Println("-------------------------------------------------------------")

	averageWaiting :=
		float64(totalWaiting) / float64(len(processes))

	averageTurnaround :=
		float64(totalTurnaround) / float64(len(processes))

	fmt.Printf("Average Waiting Time    : %.2f\n", averageWaiting)
	fmt.Printf("Average Turnaround Time : %.2f\n", averageTurnaround)

	fmt.Println("-------------------------------------------------------------")
}

// main function
func main() {

	fmt.Println()
	fmt.Println("==============================================")
	fmt.Println("       PIRATE KING'S SCHEDULER")
	fmt.Println("==============================================")

	// Ask for number of processes.
	var n int

	fmt.Print("\nEnter number of processes: ")
	fmt.Scan(&n)

	// Create process list.
	processes := make([]Process, n)

	// Take process information from the user.
	for i := 0; i < n; i++ {

		fmt.Printf("\nEnter details for Process %d\n", i+1)

		fmt.Print("Process ID: ")
		fmt.Scan(&processes[i].ID)

		fmt.Print("Arrival Time: ")
		fmt.Scan(&processes[i].Arrival)

		fmt.Print("Burst Time: ")
		fmt.Scan(&processes[i].Burst)
	}

	// Display algorithm menu.
	fmt.Println("\n==============================================")
	fmt.Println("Select Scheduling Algorithm")
	fmt.Println("==============================================")
	fmt.Println("1. FCFS - First Come First Serve")
	fmt.Println("2. SJF  - Shortest Job First (Non-Preemptive)")
	fmt.Println("3. RR   - Round Robin")

	var choice int

	fmt.Print("\nEnter your choice: ")
	fmt.Scan(&choice)

	var result []Process
	var order []string
	var times []int

	switch choice {

	case 1:

		fmt.Println("\nSelected Algorithm: FCFS")

		result, order, times =
			fcfs(copyProcesses(processes))

	case 2:

		fmt.Println("\nSelected Algorithm: SJF (Non-Preemptive)")

		result, order, times =
			sjf(copyProcesses(processes))

	case 3:

		var quantum int

		fmt.Println("\nSelected Algorithm: Round Robin")

		fmt.Print("Enter Time Quantum: ")
		fmt.Scan(&quantum)

		if quantum <= 0 {
			fmt.Println("Time Quantum must be greater than 0.")
			return
		}

		result, order, times =
			roundRobin(copyProcesses(processes), quantum)

	default:

		fmt.Println("Invalid choice.")
		return
	}

	// Display results.
	printGanttChart(order, times)

	printResults(result)

	fmt.Println("\nSimulation completed successfully! 🏴‍☠️")
}