# Mission 2 — Become Comfortable with Terminal

## Objective
Learn basic Terminal commands, practise file operations, understand command flags and pipes, and explore package managers.

## Task 2.1 — Basic Terminal Operations

| Command | Purpose |
|---|---|
| pwd | Displays the current working directory |
| ls | Lists files and folders |
| ls -l | Displays detailed directory information |
| cd | Changes the current directory |
| mkdir | Creates a directory |
| touch | Creates an empty file |
| cp | Copies files |
| mv | Moves or renames files |
| cat | Displays file contents |

## Task 2.2 — File Operations

Created a folder named `terminal-practice` and a file named `notes.txt`.

### Commands Used

| Command | Purpose |
|---|---|
| mkdir terminal-practice | Creates a practice folder |
| cd terminal-practice | Enters the folder |
| echo "My name is Prithvi." > notes.txt | Creates a file and writes the first line |
| echo "I am learning Terminal commands." >> notes.txt | Appends a second line |
| cat notes.txt | Displays the file contents |
| cp notes.txt backup.txt | Creates a backup copy |
| mv backup.txt notes-backup.txt | Renames the backup file |

### Difference Between Redirection Operators

- `>` replaces existing file contents.
- `>>` appends content without removing existing text.

### Difference Between Copy and Move

- `cp` creates a separate copy of a file.
- `mv` moves or renames a file.

## Task 2.3 — Flags and Pipes

### Command Flags

| Command | Purpose |
|---|---|
| ls | Normal directory listing |
| ls -l | Detailed directory listing |
| ls -la | Detailed listing including hidden files |
| ls -lh | Detailed listing with human-readable file sizes |
| ls -lah | Combines detailed listing, hidden files and readable sizes |

### Understanding Pipes

A pipe (`|`) sends the output of one command as input to another command.

Example:

`ls -l | head -n 5`

Explanation:
- `ls -l` displays detailed directory information.
- `head -n 5` displays the first five lines.
- The pipe connects the two commands.

## Task 2.4 — Package Managers

### What is a Package Manager?

A package manager is a tool used to install, update and remove software packages. It also helps manage software dependencies.

### Homebrew

Homebrew is a commonly used package manager for macOS.

Commands used:
- `brew --version` — Checks the installed Homebrew version.
- `brew list` — Lists installed packages.
- `brew list --versions` — Displays installed package versions.

### Why Are Package Managers Useful?

Package managers simplify software installation, updates and removal. They help manage dependencies and make software maintenance easier. Without them, users would need to manually download, install and update software and its dependencies.

### My Homebrew Observation

[Record whether Homebrew is installed and its actual version. If installed, record a few package names from your local output.]

## Learning Reflection

1. Learned how to navigate directories using Terminal.
2. Practised creating, copying and renaming files.
3. Understood the difference between overwriting and appending.
4. Learned how flags modify command behaviour.
5. Understood how pipes connect commands.
6. Learned the purpose of package managers.

## Conclusion

This mission helped me become familiar with command-line operations on macOS and understand how Terminal can be used to manage files, directories and software.