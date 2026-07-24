# Module 1 - Day 3 Mini Project

## Project Name

Student Information & Result Management System

---

## Objective

Develop a Python program that accepts student details, performs string operations, and determines the student's result and grade using conditional statements.

---

## Concepts Covered

- Variables
- User Input
- Type Casting
- Strings
- String Methods
- String Formatting
- if Statement
- if...elif...else Statement

---

## Requirements

The program should:

1. Accept Student Name.
2. Accept College Name.
3. Accept Branch.
4. Accept Roll Number.
5. Accept Marks.
6. Display student details using string methods.
7. Display:
   - Student Name in Title Case.
   - College Name in Uppercase.
   - Branch in Lowercase.
   - Length of Student Name.
8. Calculate Grade.
9. Display Pass or Fail.

---

## Code

```python
name = input("Enter Student Name: ")
college = input("Enter College Name: ")
branch = input("Enter Branch: ")
roll = input("Enter Roll Number: ")
marks = int(input("Enter Marks: "))

print("\n========== STUDENT DETAILS ==========")
print("Name :", name.title())
print("College :", college.upper())
print("Branch :", branch.lower())
print("Roll Number :", roll)
print("Characters in Name :", len(name))

print("\n========== RESULT ==========")

if marks >= 90:
    grade = "A"
    result = "Pass"
elif marks >= 75:
    grade = "B"
    result = "Pass"
elif marks >= 50:
    grade = "C"
    result = "Pass"
else:
    grade = "F"
    result = "Fail"

print("Marks :", marks)
print("Grade :", grade)
print("Result :", result)

print(f"\nCongratulations {name.title()}! Your Grade is {grade}.")
```

---

## Expected Output

```text
Enter Student Name: bhanu prakash
Enter College Name: vvit
Enter Branch: Cyber Security
Enter Roll Number: 23