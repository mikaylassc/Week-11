# Week 11 Python Assignments

This repository contains my Week 11 assignments focused on error handling and debugging in Python.

## 📌 Overview

The goal of this week was to practice writing more reliable programs by:

* Handling invalid user input using `try` / `except`
* Identifying and fixing logical errors in functions
* Writing code that runs without crashing

---

## 📂 Files Included

### 1. `input_validation.py`

This program asks the user to enter a number and safely handles invalid input.

**Key Features:**

* Prompts user for input
* Converts input to an integer
* Uses `ValueError` to catch invalid entries
* Prevents program crashes

**Example Output:**

```
Enter a number: 10
You entered: 10
```

```
Enter a number: hello
Invalid input. Please enter a number.
```

---

### 2. `fix_logical_error.py`

This program fixes a logical error in a function that was originally performing subtraction instead of multiplication.

**Key Features:**

* Corrected `multiply()` function
* Uses proper multiplication logic
* Includes comments and basic error handling
* Prints the correct result

**Example Output:**

```
10
```

---

## 🛠️ How to Run the Programs

1. Open your terminal
2. Navigate to the project folder
3. Run either file using:

```
python3 input_validation.py
```

or

```
python3 fix_logical_error.py
```

---

## 💡 What I Learned

* How to use `try` / `except` to handle runtime errors
* The difference between syntax errors and logical errors
* How to debug and fix incorrect program behavior
* How to write safer, more user-friendly Python programs

---

