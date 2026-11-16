# Mission 3: Understand the Operating System

## Task 3.1: Explore the Operating System

**Operating System:** macOS  
**Version:** 27.2.1  
**Build Version:** 26B131

### System Information

| Item | Observation |
|---|---|
| Operating system | macOS |
| Version | 27.2.1 |
| Main filesystem size | 460 GiB |
| Storage used | 13 GiB |
| Storage available | 347 GiB |
| Storage capacity used | 4% |
| Total processes | 822 |
| Running processes | 3 |
| Sleeping processes | 819 |
| CPU idle | 85.41% |
| Physical memory used | 15 GiB |
| Physical memory unused | 540 MiB |

**Commands used:**
- `sw_vers`
- `whoami` (username redacted)
- `df -h /`
- `top -l 1 -n 10`

**Observation:** The system was mostly idle during the snapshot, with 85.41% CPU idle.

## Task 3.2: Understand Processes and PIDs

A process is a program currently being executed by the operating system.

A PID (Process ID) is a unique number assigned to a running process.

**Commands used:**
- `ps -axo pid,comm | head -n 11`
- `pgrep -fl Finder`

**Observations:**
- PID 1 belongs to the macOS `launchd` process.
- Finder was running with PID 686 during the observation.
- Other processes included `logd`, `UserEventAgent`, and `fseventsd`.

**Conclusion:** Each running process has an identifier that helps the operating system distinguish and manage it.

## Task 3.3: Understand Paths and Permissions

### Absolute Path

An absolute path specifies the complete location of a file or directory, starting from the root directory.

Example (redacted):

`/Users/[redacted]/Documents/digital-detective-8475`

### Relative Path

A relative path specifies a location in relation to the current working directory.

Example:

`mission-03-operating-system/README.md`

### File Permissions

Permissions control who can read, write, or execute a file.

| Symbol | Meaning |
|---|---|
| r | Read |
| w | Write |
| x | Execute |
| - | Permission not granted |

**Commands used:**
- `pwd`
- `ls -l`
- `ls -l README.md`
- `chmod 600 permission-practice.txt`
- `chmod 644 permission-practice.txt`

### Permission Experiment

| Stage | Permission | Meaning |
|---|---|---|
| Initial | `-rw-r--r--` | Owner can read/write; others can read |
| After chmod 600 | `-rw-------` | Only owner can read/write |
| After chmod 644 | `-rw-r--r--` | Owner can read/write; others can read |

A temporary file was created for this experiment and deleted afterward.

## Task 3.4: Operating System Responsibilities

| Responsibility | Explanation |
|---|---|
| Process Management | Manages running processes and CPU scheduling. |
| Memory Management | Allocates and manages RAM for applications. |
| Device Management | Controls hardware devices such as keyboards, displays, and printers. |
| File Management | Organizes files and directories and manages storage. |
| User Interface | Provides graphical interfaces and command-line shells for interaction. |
| Security Management | Protects system resources through permissions and access controls. |

## Final Conclusion

Through this mission, I explored macOS system information, running processes, process IDs, file paths, and file permissions. I also learned the major responsibilities of an operating system and practised changing file permissions safely using `chmod`.

**Mission 3 completed.**