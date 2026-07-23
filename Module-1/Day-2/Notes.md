# Module 1 - Day 2 Notes

## 1. Operators

### What is it?

Operators are special symbols that perform operations on variables and values.

### Why do we use them?

Operators help us perform calculations, compare values, assign values, and combine multiple conditions.

---

## 2. Arithmetic Operators

### What is it?

Arithmetic operators perform mathematical calculations.

### Why do we use them?

They are used to perform mathematical operations in programs.

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 10 + 5 = 15 |
| - | Subtraction | 10 - 5 = 5 |
| * | Multiplication | 10 × 5 = 50 |
| / | Division | 10 / 5 = 2.0 |
| % | Modulus (Remainder) | 10 % 3 = 1 |
| // | Floor Division | 10 // 3 = 3 |
| ** | Exponent (Power) | 2 ** 3 = 8 |

---

## 3. Assignment Operator

### What is it?

The assignment operator (`=`) stores a value inside a variable.

### Why do we use it?

It allows us to save data in memory and reuse it throughout the program.

### Example

```python
age = 21
```

---

## 4. Comparison Operators

### What is it?

Comparison operators compare two values and return either **True** or **False**.

### Why do we use them?

They help us make decisions in programs using conditions.

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not Equal to |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal to |
| <= | Less Than or Equal to |

---

## 5. Logical Operators

### What is it?

Logical operators combine or modify conditions.

### Why do we use them?

They are used when checking multiple conditions in a program.

| Operator | Meaning |
|----------|---------|
| and | Returns True if both conditions are True |
| or | Returns True if at least one condition is True |
| not | Reverses the result |

---

## 6. User Input

### What is it?

The `input()` function accepts data entered by the user.

### Why do we use it?

It makes programs interactive by allowing users to enter their own values.

### Example

```python
name = input("Enter your name: ")
```

**Note:** The `input()` function always returns a string.

---

## 7. Type Casting

### What is it?

Type casting converts one data type into another.

### Why do we use it?

Since `input()` returns a string, we convert it to the required data type before performing calculations.

### Common Type Casting Functions

- `int()` – Converts to Integer
- `float()` – Converts to Float
- `str()` – Converts to String
- `bool()` – Converts to Boolean

### Example

```python
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))
```

---

# Summary

- Operators perform operations on values.
- Arithmetic operators perform mathematical calculations.
- Assignment operators store values in variables.
- Comparison operators compare values.
- Logical operators combine conditions.
- `input()` accepts user input.
- Type casting converts one data type into another.