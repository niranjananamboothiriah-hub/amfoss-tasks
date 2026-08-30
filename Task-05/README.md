# Grand Line Guardian

## 1. Overview

Grand Line Guardian is a terminal-based system monitoring tool developed as part of amFOSS Praveshan Task-05.

The application continuously monitors running processes in a Linux system and displays important process information in real time. It is inspired by terminal monitoring tools such as `top` and `htop`.

The main objective of this project is to understand Linux process management, system monitoring, Python process handling, and terminal-based user interfaces.

## 2. Features

The application provides:

* Process ID (PID)
* Process name
* CPU usage percentage
* Memory usage percentage
* Total number of active processes
* Continuous process monitoring
* Automatic refresh every 0.5 seconds
* CPU-based process sorting
* Keyboard navigation
* Selected-process highlighting
* Process termination
* Error handling for inaccessible or terminated processes
* Terminal-based user interface

## 3. Technologies Used

* Python 3
* psutil
* curses
* Linux
* Python virtual environment

## 4. How It Works

The program continuously performs the following steps:

1. Retrieves the currently running processes.
2. Collects the PID, process name, CPU usage and memory usage.
3. Handles processes that disappear or cannot be accessed.
4. Sorts processes according to CPU usage.
5. Displays the process information in the terminal.
6. Reads keyboard input.
7. Allows the user to move through the process list.
8. Allows the selected process to be terminated.
9. Repeats the monitoring cycle every 0.5 seconds.

## 5. Process Information

The `psutil` library is used to obtain information about running processes.

For every process, the program retrieves:

* `pid` - unique process identifier
* `name` - process name
* `cpu_percent` - CPU usage
* `memory_percent` - memory usage

Processes are stored as Python dictionaries so that their information can be accessed easily.

## 6. Linux `/proc` Virtual Filesystem

Linux provides process and system information through the `/proc` virtual filesystem.

Each running process generally has a directory inside `/proc` named after its PID.

For example:

```text
/proc/1234/
```

may contain information about process 1234.

Important files include:

```text
/proc/1234/status
/proc/1234/stat
/proc/1234/cmdline
```

The `/proc` filesystem is generated and maintained by the Linux kernel and provides information about the current state of the system.

Although this project uses `psutil` to access process information, understanding `/proc` helped me understand how Linux exposes process information internally.

## 7. Keyboard Controls

| Key        | Action                     |
| ---------- | -------------------------- |
| Up Arrow   | Move selection upward      |
| Down Arrow | Move selection downward    |
| Enter      | Terminate selected process |
| Q          | Quit the application       |

## 8. Error Handling

Processes can terminate while the program is reading their information. Some processes may also be inaccessible to the current user.

The program handles:

* `psutil.NoSuchProcess`
* `psutil.AccessDenied`

Instead of terminating the entire application, the affected process is skipped or an appropriate message is displayed.

## 9. Installation

Clone or download the project and enter the Task-05 directory.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## 10. Running the Application

Run:

```bash
python3 guardian.py
```

The terminal will display the currently running processes and continuously update the information.

Press `Q` to exit.

## 11. Why psutil?

Linux exposes process information through interfaces such as `/proc`. Manually parsing these files can be complicated and closely tied to Linux implementation details.

`psutil` provides a convenient Python API for retrieving process information while allowing the application to remain simple and readable.

## 12. Why curses?

The `curses` module is used to create the interactive terminal interface.

It allows the application to:

* Read keyboard input
* Detect arrow keys
* Position text on the terminal
* Highlight the selected process
* Refresh the terminal display

## 13. Concepts Learned

Through this project, I learned about:

* Linux processes
* Process IDs
* CPU and memory monitoring
* Linux `/proc` virtual filesystem
* Python process management
* Exception handling
* Terminal user interfaces
* Keyboard input handling
* Python virtual environments
* Dependency management
* Git and GitHub project organization

## 14. Resources Used

* Python documentation
* Linux manual pages
* psutil documentation
* curses documentation
* `/proc` filesystem documentation

## 15. Future Improvements

Possible future improvements include:

* CPU and memory graphs
* Process search and filtering
* Process sorting by different columns
* Confirmation before terminating a process

