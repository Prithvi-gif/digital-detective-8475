
# Number Converter
# Converts a decimal number into binary and hexadecimal.

number = int(input("Enter a decimal number: "))

binary = bin(number)
hexadecimal = hex(number)

print("Decimal number:", number)
print("Binary representation:", binary)
print("Hexadecimal representation:", hexadecimal)
