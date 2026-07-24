# Module 1 - Day 3 Notes

# Strings

## What is a String?

A string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' / """ """). Strings are used to store textual information such as names, emails, passwords, addresses, and messages.

### Syntax

```python
name = "Bhanu"
```

---

## Creating Strings

Strings can be created using either single quotes or double quotes.

### Example

```python
name = "Bhanu"
college = 'VVIT'
```

---

## String Indexing

Each character in a string has an index.

Positive indexing starts from 0.

```
P  y  t  h  o  n
0  1  2  3  4  5
```

Negative indexing starts from the end.

```
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

### Example

```python
word = "Python"

print(word[0])
print(word[-1])
```

---

## String Slicing

String slicing extracts a part of a string.

### Syntax

```python
string[start:end]
```

### Example

```python
word = "CyberSecurity"

print(word[0:5])
```

Output

```
Cyber
```

---

## String Methods

### upper()

Converts all letters to uppercase.

```python
name.upper()
```

### lower()

Converts all letters to lowercase.

```python
name.lower()
```

### title()

Converts the first letter of every word into uppercase.

```python
name.title()
```

### strip()

Removes spaces from both ends.

```python
text.strip()
```

### replace()

Replaces one word with another.

```python
text.replace("Python", "Java")
```

### split()

Splits a string into a list.

```python
text.split()
```

---

## String Formatting

Used to insert variables into strings.

### Example

```python
name = "Bhanu"

print(f"Welcome {name}")
```

---

# Conditional Statements

## What are Conditional Statements?

Conditional statements allow a program to make decisions based on conditions.

---

## if Statement

Executes a block of code only if the condition is True.

### Syntax

```python
if condition:
    statement
```

---

## if...else Statement

Executes one block if the condition is True and another block if it is False.

### Syntax

```python
if condition:
    statement
else:
    statement
```

---

## if...elif...else Statement

Used to check multiple conditions.

### Syntax

```python
if condition:
    statement
elif condition:
    statement
else:
    statement
```

---

## Nested if Statement

An if statement inside another if statement.

### Example

```python
if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

---

# Advantages

- Easy to process text.
- Helps make decisions.
- Improves application logic.
- Widely used in backend development.

---

# Real-Time Applications

- Login Authentication
- User Registration
- Student Result System
- Banking Applications
- E-Commerce Websites
- Chat Applications
- Search Functionality
- Form Validation