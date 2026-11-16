# Mission 5: Numbers and Data

## Mission Objective

To understand how computers represent numbers and text using binary and hexadecimal number systems, verify conversions using Python, and build a simple number converter.

---

## Task 5.1: Convert Numbers by Hand

Computers represent information using bits. A bit can have a value of 0 or 1. A group of eight bits is called a byte.

### Number Systems

| Number System | Base | Digits |
|---|---:|---|
| Decimal | 10 | 0–9 |
| Binary | 2 | 0, 1 |
| Hexadecimal | 16 | 0–9, A–F |

In hexadecimal, A=10, B=11, C=12, D=13, E=14 and F=15.

### Manual Conversions

**1. Convert decimal 13 to binary**

Repeated division by 2:

| Division | Quotient | Remainder |
|---|---:|---:|
| 13 ÷ 2 | 6 | 1 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Reading remainders from bottom to top:

`(13)₁₀ = (1101)₂`

**2. Convert decimal 25 to binary**

| Division | Quotient | Remainder |
|---|---:|---:|
| 25 ÷ 2 | 12 | 1 |
| 12 ÷ 2 | 6 | 0 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Reading remainders from bottom to top:

`(25)₁₀ = (11001)₂`

**3. Convert binary 1010 to decimal**

`1 × 2³ + 0 × 2² + 1 × 2¹ + 0 × 2⁰`

`= 8 + 0 + 2 + 0 = 10`

**4. Convert binary 1101 to decimal**

`1 × 2³ + 1 × 2² + 0 × 2¹ + 1 × 2⁰`

`= 8 + 4 + 0 + 1 = 13`

**5. Convert hexadecimal A to decimal**

`A = 10`

Therefore, `(A)₁₆ = (10)₁₀`

**6. Convert hexadecimal 1F to decimal**

`1 × 16¹ + 15 × 16⁰`

`= 16 + 15 = 31`

**7. Convert binary 1111 to hexadecimal**

`1111₂ = 8 + 4 + 2 + 1 = 15`

Decimal 15 corresponds to hexadecimal F.

Therefore, `(1111)₂ = (F)₁₆`

### Final Conversion Answers

| Question | Answer |
|---|---|
| Decimal 13 to binary | 1101 |
| Decimal 25 to binary | 11001 |
| Binary 1010 to decimal | 10 |
| Binary 1101 to decimal | 13 |
| Hexadecimal A to decimal | 10 |
| Hexadecimal 1F to decimal | 31 |
| Binary 1111 to hexadecimal | F |

---

## Task 5.2: Verify Using Python

Python provides built-in functions to convert numbers between different number systems.

### Python Functions Used

| Function | Purpose |
|---|---|
| `bin()` | Converts an integer to binary |
| `int(value, 2)` | Converts binary to decimal |
| `hex()` | Converts an integer to hexadecimal |
| `int(value, 16)` | Converts hexadecimal to decimal |

### Python Verification Results

| Conversion | Python Expression | Result |
|---|---|---|
| Decimal 13 to binary | `bin(13)` | `0b1101` |
| Decimal 25 to binary | `bin(25)` | `0b11001` |
| Binary 1010 to decimal | `int('1010', 2)` | `10` |
| Binary 1101 to decimal | `int('1101', 2)` | `13` |
| Decimal 31 to hexadecimal | `hex(31)` | `0x1f` |
| Hexadecimal A to decimal | `int('A', 16)` | `10` |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` |
| Binary 1111 to hexadecimal | `hex(int('1111', 2))` | `0xf` |

**Observation:** All Python conversion results matched the manual calculations.

---

## Task 5.3: Build a Small Number Converter

### File Name

`number_converter.py`

### Python Program

```python
# Number Converter
# Converts a decimal number into binary and hexadecimal.

number = int(input("Enter a decimal number: "))

binary = bin(number)
hexadecimal = hex(number)

print("Decimal number:", number)
print("Binary representation:", binary)
print("Hexadecimal representation:", hexadecimal)
```

### Command Used

```bash
python3 number_converter.py
```

### Testing the Program

**Test 1: Input = 10**

```text
Enter a decimal number: 10
Decimal number: 10
Binary representation: 0b1010
Hexadecimal representation: 0xa
```

**Test 2: Input = 25**

```text
Enter a decimal number: 25
Decimal number: 25
Binary representation: 0b11001
Hexadecimal representation: 0x19
```

**Test 3: Input = 100**

```text
Enter a decimal number: 100
Decimal number: 100
Binary representation: 0b1100100
Hexadecimal representation: 0x64
```

### Python Functions Used

- `input()` accepts a number from the user.
- `int()` converts the input into an integer.
- `bin()` converts the decimal number into binary.
- `hex()` converts the decimal number into hexadecimal.
- `print()` displays the results.

**Observation:** The program successfully converted all three positive decimal numbers into binary and hexadecimal representations.

---

## Task 5.4: How Is Text Stored?

Computers store text using character-encoding standards.

### ASCII Decimal Codes

| Character | ASCII Decimal Code |
|---|---:|
| Uppercase A | 65 |
| Lowercase a | 97 |

### Why Do Computers Need Character Encoding?

Computers store text as binary data, so they need character-encoding standards to represent each character with a defined numeric value. ASCII represents a basic set of characters, while UTF-8 supports a much wider range of characters and symbols from different languages.

**Example of a character outside basic ASCII:** ₹ (Indian Rupee symbol).

---

## Commands Used

| Command | Purpose |
|---|---|
| `python3` | Opens Python interactive mode |
| `bin(13)` | Converts decimal to binary |
| `int('1010', 2)` | Converts binary to decimal |
| `hex(31)` | Converts decimal to hexadecimal |
| `int('1F', 16)` | Converts hexadecimal to decimal |
| `touch number_converter.py` | Creates the Python file |
| `code number_converter.py` | Opens the file in VS Code |
| `python3 number_converter.py` | Runs the converter |

---

## Final Conclusion

In this mission, I learned how computers represent numbers using decimal, binary and hexadecimal systems. I performed manual conversions and verified them using Python's built-in functions. I also created and tested a Python number converter that converts decimal values into binary and hexadecimal. Finally, I learned how character encoding standards such as ASCII and UTF-8 allow computers to store and represent text.

**Mission 5 completed.**