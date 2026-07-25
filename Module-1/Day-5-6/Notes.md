# Module 1 - Day 6 Notes

# Functions in Python

## Introduction

A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we write it once inside a function and call it whenever required.

Functions make programs shorter, easier to understand, and easier to maintain.

---

# What is a Function?

A function is a named block of code that executes only when it is called.

### Why do we use Functions?

- Reduce code duplication.
- Improve readability.
- Make programs modular.
- Easy debugging.
- Code reusability.

---

# Creating a Function

### Syntax

```python
def function_name():
    statement
```

### Example

```python
def welcome():
    print("Welcome to Python")
```

---

# Calling a Function

A function runs only when it is called.

### Example

```python
def welcome():
    print("Welcome to Python")

welcome()
```

Output

```
Welcome to Python
```

---

# Parameters

Parameters are variables that receive values inside a function.

### Example

```python
def greet(name):
    print("Hello", name)
```

---

# Arguments

Arguments are the actual values passed while calling a function.

### Example

```python
greet("Bhanu")
```

---

# Return Statement

The return statement sends a value back to the caller.

### Example

```python
def add(a,b):
    return a+b

result = add(10,20)

print(result)
```

Output

```
30
```

---

# Built-in Functions

Python provides many built-in functions.

Examples

```python
print()

input()

len()

type()

int()

float()

str()

range()
```

---

# User-defined Functions

Functions created by the programmer.

### Example

```python
def square(num):
    return num*num
```

---

# Local Variable

A variable declared inside a function.

Example

```python
def demo():
    x = 10
    print(x)
```

---

# Global Variable

A variable declared outside a function.

Example

```python
name = "Bhanu"

def show():
    print(name)
```

---

# Advantages

- Reusable code.
- Better readability.
- Easy maintenance.
- Faster debugging.
- Modular programming.

---

# Disadvantages

- Too many functions may reduce readability.
- Function calls have a small execution overhead.

---

# Real-Time Applications

- Login Systems
- OTP Verification
- Banking Systems
- Calculator
- Student Management
- Shopping Cart
- Payment Gateway
- Email Verification

---

# Important Commands

```python
def

return

print()

input()

len()

type()
```

---

# Summary

- Functions are reusable blocks of code.
- Functions are created using the def keyword.
- Parameters receive values.
- Arguments are values passed to functions.
- The return statement sends a value back to the caller.
- Python provides built-in and user-defined functions.