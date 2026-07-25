# Module 1 - Day 6 Mini Project

## Project Name

Simple Banking System

---

## Objective

Develop a Python program that simulates basic banking operations using functions.

---

## Concepts Covered

- Functions
- Parameters
- User Input
- if...elif...else
- return
- while Loop

---

## Requirements

The program should repeatedly display the following menu until the user exits.

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

---

## Code

```python
balance = 1000


def check_balance(balance):
    print(f"\nCurrent Balance: ₹{balance}\n")
    return balance


def deposit(balance):
    amount = float(input("Enter Deposit Amount: ₹"))

    if amount > 0:
        balance += amount
        print("Amount Deposited Successfully!\n")
    else:
        print("Invalid Amount\n")

    return balance


def withdraw(balance):
    amount = float(input("Enter Withdraw Amount: ₹"))

    if amount <= balance:
        balance -= amount
        print("Please Collect Your Cash.\n")
    else:
        print("Insufficient Balance!\n")

    return balance


while True:

    print("====== Banking System ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        check_balance(balance)

    elif choice == 2:
        balance = deposit(balance)

    elif choice == 3:
        balance = withdraw(balance)

    elif choice == 4:
        print("Thank You for Using Our Banking System!")
        break

    else:
        print("Invalid Choice\n")
```

---

## Expected Output

```text
====== Banking System ======

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter Your Choice: 1

Current Balance: ₹1000

Enter Your Choice: 2

Enter Deposit Amount: ₹500

Amount Deposited Successfully!

Enter Your Choice: 1

Current Balance: ₹1500

Enter Your Choice: 3

Enter Withdraw Amount: ₹300

Please Collect Your Cash.

Enter Your Choice: 1

Current Balance: ₹1200

Enter Your Choice: 4

Thank You for Using Our Banking System!
```

---

## Learning Outcome

- Created and called user-defined functions.
- Used parameters and return values.
- Built a menu-driven application.
- Applied loops, functions, and conditional statements together.
- Understood how functions improve code reusability and organization.