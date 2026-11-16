# Mission 4: How Programs Run

## Mission Objective

To run a simple Python program and understand the difference between how compilers and interpreters translate or execute programs.

---

## Task 4.1: Create and Run a Python Program

### Program: hello.py

```python
print("Hello from Python")
```

### Command Used

```bash
python3 hello.py
```

### Output

```text
Hello from Python
```

### Observation

The Python program executed successfully and displayed the message `Hello from Python` in the Terminal.

The `python3` command starts the Python interpreter, which executes the instructions in the Python file.

---

## Task 4.2: Compare Compiler and Interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates the source code before program execution | Executes instructions at runtime |
| Typical output | Produces machine code or an executable file | Usually executes without producing a standalone executable |
| One example | C, C++ | Python, JavaScript |
| One advantage | Compiled programs can execute quickly | Makes testing and executing programs convenient |

### Difference Between Compiler and Interpreter

A compiler translates source code into another form, often machine code, before the program is executed. An interpreter executes program instructions at runtime. A compiler can produce an executable program, while an interpreter generally executes the program using its runtime environment. Compilers can offer faster execution, whereas interpreters make it convenient to test and run programs.

---

## Commands Used

| Command | Purpose |
|---|---|
| `touch hello.py` | Creates a Python file |
| `code hello.py` | Opens the file in VS Code |
| `python3 hello.py` | Executes the Python program |

---

## Conclusion

In this mission, I successfully created and executed a Python program using the Terminal. I learned how a compiler translates source code before execution and how an interpreter executes instructions at runtime. I also understood their differences, examples, and advantages.

**Mission 4 completed.**