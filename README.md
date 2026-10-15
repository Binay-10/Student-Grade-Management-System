# Student Grade Management System in Python

A console-based academic grading and performance evaluation system built using pure Python standard libraries. The system accepts student credentials and marks for five core computer science subjects, performs rigorous numerical and logic calculations (Total Marks, Percentage, 10-Point GPA, Letter Grade, and Subject-Wise Pass/Fail Evaluation), and renders a clean, professional ASCII grade report card.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Requirements](#technology-requirements)
4. [Grading Scheme & GPA Formula](#grading-scheme--gpa-formula)
5. [Project Directory Structure](#project-directory-structure)
6. [Core Python Concepts Demonstrated](#core-python-concepts-demonstrated)
7. [Installation & Execution Guide](#installation--execution-guide)
8. [Automated Testing](#automated-testing)
9. [Sample Program Execution](#sample-program-execution)
10. [Capturing Screenshots in VS Code](#capturing-screenshots-in-vs-code)
11. [Git & GitHub Submission Guide](#git--github-submission-guide)
12. [Assignment Rubric Checklist](#assignment-rubric-checklist)

---

## Project Overview

The **Student Grade Management System** is designed for college-level introductory Python curricula. It emphasizes clean software architecture, functional decomposition, input sanitization, and structured data representation without relying on third-party frameworks, external libraries, or databases.

The system evaluates student performance across five curriculum subjects:
1. **Python Programming**
2. **Data Structures**
3. **Database Systems**
4. **Web Development**
5. **Software Engineering**

---

## Features

- **Robust Input Validation:**
  - Prevents empty or whitespace-only student names and roll numbers.
  - Rejects non-numeric text, floating-point decimals, negative numbers, and marks exceeding 100 without crashing (`try...except ValueError`).
  - Gracefully prompts the user to re-enter invalid inputs until valid data is provided.
- **Dictionary & List Data Structures:**
  - Uses lists to iterate through canonical subject names.
  - Stores student records in nested dictionaries with clean key-value mapping.
- **Modular Functional Architecture:**
  - Independent functions with explicit parameters and return values (no global mutable state).
- **Decoupled Grading and Pass/Fail Logic:**
  - Letter grades are calculated from the overall percentage.
  - Pass/fail status requires a minimum passing threshold of **40 marks in every single subject**. If any subject score falls below 40, the student is marked as `FAILED`, even if their cumulative average is high.
- **Standardized 10-Point GPA:**
  - Evaluates GPA using the formula `GPA = Percentage / 10`, rounded and displayed to two decimal places.
- **ASCII Report Card:**
  - Formatted using Python f-strings with consistent column widths, right/left text alignment, and distinct ASCII section dividers.

---

## Technology Requirements

- **Operating System:** Windows 10/11, macOS, or Linux.
- **Python Version:** Python 3.10 or higher (Tested on Python 3.13).
- **Editor / IDE:** Visual Studio Code (VS Code) or any modern terminal.
- **Dependencies:** Strictly Python Standard Library (`typing`, `unittest`, `unittest.mock`, `io`, `sys`). No external pip dependencies required.

---

## Grading Scheme & GPA Formula

### 1. Letter Grade & Classification Scheme
The letter grade is determined based on the cumulative percentage score:

| Percentage Range | Letter Grade | Academic Classification |
|---|---|---|
| **90.00% – 100.00%** | **A+** | Outstanding |
| **80.00% – 89.99%** | **A** | Distinction |
| **70.00% – 79.99%** | **B** | Very Good |
| **60.00% – 69.99%** | **C** | Good |
| **Below 60.00%** | **F** | Fail |

### 2. GPA Calculation Formula
The Grade Point Average (GPA) is computed on a documented 10-point scale:

$$\text{GPA} = \frac{\text{Percentage}}{10.0}$$

*Example:* A percentage score of $89.00\%$ yields a GPA of $8.90 / 10.00$.

### 3. Subject-Level Pass / Fail Rule
- **Minimum Passing Threshold:** A student must score **at least 40 marks out of 100** in each of the 5 subjects.
- **Rule:** If $\text{marks} < 40$ in any subject, the status is automatically `FAILED`.
- **Decoupled Evaluation:** The letter grade reflects overall percentage, while the pass/fail status independently assesses subject-level competency. For example, a student scoring 35 in one subject and 95 in the remaining four achieves an 83.00% average (Grade A), but will receive a status of `FAILED`. Conversely, a student scoring exactly 40 in all five subjects achieves a 40.00% average (Grade F), but will receive a status of `PASSED`.

---

## Project Directory Structure

```text
Student-Grade-Management-System/
├── .gitignore                    # Standard Python gitignore (caches, virtualenvs, OS artifacts)
├── README.md                     # Comprehensive documentation & submission guide
├── student_grade_system.py       # Core application source code
├── test_student_grade_system.py  # Automated unit and integration test suite
└── screenshots/
    └── report_card.png           # Live execution screenshot of the terminal report card
```

---

## Core Python Concepts Demonstrated

1. **Functions & Parameter Passing:**
   - Pure functions (`calculate_total`, `calculate_percentage`, `calculate_gpa`, `calculate_grade`, `get_result`) receive explicit inputs and return typed outputs without relying on global variables.
2. **Data Structures:**
   - **Lists:** Canonical subject list (`DEFAULT_SUBJECTS`) used for deterministic iteration.
   - **Dictionaries:** Nested dictionary storing student metadata and subject-to-mark mappings.
3. **Loops & Control Flow:**
   - `while True` loops for bulletproof interactive input validation.
   - `for` loops for iterating through subjects and calculating totals.
   - `if...elif...else` branching for threshold classification and grading.
4. **Exception Handling:**
   - `try...except ValueError` to catch non-numeric inputs and prevent terminal crashes.
5. **Formatted Output with f-strings:**
   - Precision format specifiers (`{percentage:.2f}%`, `{gpa:.2f}`) and alignment widths (`{subject:<34}`, `{marks:>3}`) for professional ASCII layout.
6. **Program Entry Point:**
   - `if __name__ == "__main__":` idiom ensures modularity, allowing functions to be imported by test suites without triggering interactive execution.

---

## Installation & Execution Guide

### Step 1: Open the Project in VS Code
1. Launch **Visual Studio Code**.
2. Click **File > Open Folder...** and select the `Student-Grade-Management-System` folder.
3. Open an integrated terminal in VS Code using the shortcut:
   - **Windows / Linux:** ``Ctrl + ` `` (Backtick)
   - **macOS:** ``Cmd + ` ``

### Step 2: Verify Python Installation
Verify that Python 3.10+ is installed and accessible in your terminal:

```bash
python --version
```

> **Troubleshooting Python Launchers:**
> - If `python` is not recognized on Windows, try running:
>   ```powershell
>   py --version
>   # or
>   py -3 --version
>   ```
> - On macOS / Linux, run:
>   ```bash
>   python3 --version
>   ```

### Step 3: Run the Application
Execute the main program:

```bash
python student_grade_system.py
```

*(On Windows, you may also use `py student_grade_system.py`; on macOS/Linux use `python3 student_grade_system.py`)*

---

## Automated Testing

An automated test suite using Python's built-in `unittest` framework is included in `test_student_grade_system.py`.

### Run All Tests:
Execute the test runner from your VS Code terminal:

```bash
python -m unittest test_student_grade_system.py -v
```

### Verified Test Scenarios:
1. **Sample Scenario (Liam Anderson):** Validates total ($445/500$), percentage ($89.00\%$), GPA ($8.90$), Grade ($A$), and Status (`PASSED`).
2. **Perfect Score Scenario:** All subjects scored $100$ $\rightarrow$ Total $500$, $100.00\%$, GPA $10.00$, Grade $A+$, `PASSED`.
3. **Zero Score Scenario:** All subjects scored $0$ $\rightarrow$ Total $0$, $0.00\%$, GPA $0.00$, Grade $F$, `FAILED`.
4. **Grading Boundary Coverage:** Verifies boundary scores ($59\%$, $60\%$, $69.99\%$, $70\%$, $79.99\%$, $80\%$, $89.99\%$, $90\%$, $100\%$).
5. **High Percentage with Single Subject Failure:** Subject scored $35$ with four $95$s $\rightarrow$ $83.00\%$, Grade $A$, Status `FAILED`.
6. **Input Validation Recovery (Marks):** Mocked input verifying recovery from invalid text (`"invalid_text"`), negative marks (`-15`), and overflow marks (`105`).
7. **Input Validation Recovery (Strings):** Mocked input verifying recovery from empty (`""`) and whitespace (`"   "`) inputs.
8. **Threshold Pass Boundary:** Exactly $40$ in all five subjects $\rightarrow$ Total $200$, $40.00\%$, Grade $F$, Status `PASSED`.
9. **Report Card Visual Consistency:** Verifies header, delimiters, alignment, and fields in the rendered ASCII report card.

---

## Sample Program Execution

### Input Prompts:
```text
=== STUDENT GRADE REPORT GENERATOR ===

Enter Student Name: Liam Anderson
Enter Roll Number: PY-2026-042

Enter marks out of 100:
Python Programming: 94
Data Structures: 88
Database Systems: 91
Web Development: 85
Software Engineering: 87
```

### Generated Report Card:
```text
===============================================
           OFFICIAL GRADE REPORT CARD
===============================================
Student Name : Liam Anderson
Roll Number  : PY-2026-042
-----------------------------------------------
SUBJECT                         MARKS
-----------------------------------------------
Python Programming                94/100
Data Structures                   88/100
Database Systems                  91/100
Web Development                   85/100
Software Engineering              87/100
-----------------------------------------------
Total Marks : 445 / 500
Percentage  : 89.00%
GPA         : 8.90 / 10.00
Grade       : A (Distinction)
Status      : PASSED
===============================================
```

---

## Capturing Screenshots in VS Code

An authentic screenshot generated directly from program execution is located at `screenshots/report_card.png`.

To capture your own live screenshots of the program running in your VS Code editor:

### On Windows:
1. Run `python student_grade_system.py` in the VS Code integrated terminal and complete the prompts.
2. Press **`Win + Shift + S`** to open the Windows Snipping Tool.
3. Drag the selection box over the VS Code window showing both your code and the terminal output.
4. Save the screenshot as `report_card.png` inside the `screenshots/` directory.

### On macOS:
1. Run `python3 student_grade_system.py` in the VS Code terminal.
2. Press **`Cmd + Shift + 4`**, then press **`Spacebar`** to capture the VS Code window (or click-and-drag across the terminal).
3. Save the resulting image into `screenshots/report_card.png`.

---

## Git & GitHub Submission Guide

Follow these steps to initialize version control and push the project to your GitHub account:

### Step 1: Initialize Git Repository
In your project root directory (`Student-Grade-Management-System`), run:

```bash
git init
git status
```

### Step 2: Stage and Commit All Files
Stage the project files and make your initial commit:

```bash
git add .
git commit -m "feat: complete student grade management system with unit tests and docs"
```

### Step 3: Create a New Repository on GitHub
1. Open your browser and navigate to [https://github.com/new](https://github.com/new).
2. Set the **Repository name** to: `Student-Grade-Management-System`.
3. Set the visibility to **Public**.
4. **Do not** initialize with a README, .gitignore, or license (these already exist in your local project).
5. Click **Create repository**.

### Step 4: Link Remote Repository and Push
Copy the remote repository URL provided by GitHub and execute:

```bash
git branch -M main
git remote add origin https://github.com/<your-username>/Student-Grade-Management-System.git
git push -u origin main
```

*(Replace `<your-username>` with your actual GitHub username).*

---

## Assignment Rubric Checklist

| Requirement | Implementation Detail | Status |
|---|---|:---:|
| **Language & Environment** | Pure Python 3.10+ standard library; zero third-party packages | Verified |
| **Subjects (5 Core)** | Python Programming, Data Structures, Database Systems, Web Dev, Software Eng | Verified |
| **Data Structures** | List for canonical subjects; nested dictionary for student info & subject marks | Verified |
| **Input Validation** | Rejects blanks, invalid text, negative marks, and marks > 100 gracefully | Verified |
| **Calculation: Total** | `calculate_total(marks)` sums marks across all 5 subjects (out of 500) | Verified |
| **Calculation: Percentage** | `calculate_percentage(total, max_marks)` computes percentage (out of 100) | Verified |
| **Calculation: 10-Pt GPA** | `calculate_gpa(percentage)` applies $\text{Percentage} / 10$ to 2 decimal places | Verified |
| **Calculation: Grade** | `calculate_grade(percentage)` assigns A+, A, B, C, F per rubric scale | Verified |
| **Calculation: Pass/Fail** | `get_result(marks)` requires $\ge 40$ in all subjects; fails if any $< 40$ | Verified |
| **ASCII Report Card** | `generate_report_card(...)` produces aligned borders, headers, and fields | Verified |
| **Automated Tests** | `test_student_grade_system.py` contains 10 thorough test cases (100% pass) | Verified |
| **Visual Documentation** | `screenshots/report_card.png` captures clean execution output | Verified |
| **Clean Architecture** | Modular functions, PEP 8 compliance, docstrings, type annotations, `__main__` entry | Verified |
