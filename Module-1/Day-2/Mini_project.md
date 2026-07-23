# Module 1 - Day 2 Mini Project

## Project Name

Simple Calculator

## Objective

Create a Python program that accepts two numbers from the user and performs basic arithmetic operations.

## Requirements

- Take two numbers as input.
- Convert the input into integers using type casting.
- Display:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Modulus
  - Floor Division
  - Exponent

## Example Code

```python
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Addition :", num1 + num2)
print("Subtraction :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division :", num1 / num2)
print("Modulus :", num1 % num2)
print("Floor Division :", num1 // num2)
print("Exponent :", num1 ** num2)
```

## Expected Output

```text
Enter First Number: 20
Enter Second Number: 5

Addition : 25
Subtraction : 15
Multiplication : 100
Division : 4.0
Modulus : 0
Floor Division : 4
Exponent : 3200000
```

## Learning Outcome

- Learned how to take user input.
- Practiced type casting using `int()`.
- Understood arithmetic operators.
- Built a simple calculator using Python.