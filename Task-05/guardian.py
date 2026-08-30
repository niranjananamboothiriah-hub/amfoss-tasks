import os
import time
import psutil
import curses


def get_processes():
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append(
                {
                    "pid": info["pid"],
                    "name": info["name"] or "Unknown",
                    "cpu": info["cpu_percent"],
                    "memory": info["memory_percent"],
                }
            )

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda p: p["cpu"], reverse=True)
    return processes


def terminate_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        return f"Process {pid} terminated."
    except psutil.NoSuchProcess:
        return f"Process {pid} no longer exists."
    except psutil.AccessDenied:
        return f"Permission denied for process {pid}."
    except Exception as error:
        return f"Error: {error}"


def guardian(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(500)

    selected = 0
    message = ""

    while True:
        processes = get_processes()

        if not processes:
            selected = 0
        else:
            selected = min(selected, len(processes) - 1)

        stdscr.erase()

        height, width = stdscr.getmaxyx()

        title = "GRAND LINE GUARDIAN - SYSTEM MONITOR"
        stdscr.addstr(0, 2, "=" * min(width - 4, 90))
        stdscr.addstr(1, 2, title[: width - 4])
        stdscr.addstr(2, 2, "=" * min(width - 4, 90))

        stdscr.addstr(
            4,
            2,
            f"Total Active Processes: {len(processes)}"
        )

        stdscr.addstr(
            5,
            2,
            "UP/DOWN: Select   ENTER: Terminate   Q: Quit"
        )

        header = f"{'PID':<10}{'PROCESS NAME':<30}{'CPU %':>10}{'MEMORY %':>12}"
        stdscr.addstr(7, 2, header[: width - 4])

        stdscr.addstr(
            8,
            2,
            "-" * min(width - 4, 70)
        )

        max_rows = height - 11

        for index, process in enumerate(processes[:max_rows]):
            line = (
                f"{process['pid']:<10}"
                f"{process['name'][:29]:<30}"
                f"{process['cpu']:>9.2f}"
                f"{process['memory']:>11.2f}"
            )

            if index == selected:
                stdscr.addstr(
                    9 + index,
                    2,
                    line[: width - 4],
                    curses.A_REVERSE
                )
            else:
                stdscr.addstr(
                    9 + index,
                    2,
                    line[: width - 4]
                )

        if message:
            message_y = height - 2
            stdscr.addstr(
                message_y,
                2,
                message[: width - 4]
            )

        stdscr.refresh()

        key = stdscr.getch()

        if key in (ord("q"), ord("Q")):
            break

        elif key == curses.KEY_UP:
            selected = max(0, selected - 1)

        elif key == curses.KEY_DOWN:
            selected = min(len(processes) - 1, selected + 1)

        elif key in (10, 13):
            if processes:
                pid = processes[selected]["pid"]
                message = terminate_process(pid)
                time.sleep(0.5)


def main():
    try:
        curses.wrapper(guardian)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()