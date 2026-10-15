"""
Student Grade Management System
================================
A console-based academic grading and performance evaluation tool built in Python.
Calculates total marks, percentage, 10-point GPA, letter grade, and pass/fail status
for five core computer science subjects and displays a clean ASCII report card.

Features:
- Robust input validation (non-empty strings, whole-number marks 0-100).
- Modular architecture with clean parameter passing.
- 10-point GPA calculation and letter grading scheme.
- Standalone subject-level pass/fail evaluation (minimum 40 marks required in each).
- Clean, professional ASCII report card formatting using f-strings.
"""

from typing import Dict, List, Tuple, Union

# List of subjects included in the curriculum
DEFAULT_SUBJECTS: List[str] = [
    "Python Programming",
    "Data Structures",
    "Database Systems",
    "Web Development",
    "Software Engineering",
]

# Academic grading scale reference
# 90-100%  -> A+ (Outstanding)
# 80-89.99% -> A  (Distinction)
# 70-79.99% -> B  (Very Good)
# 60-69.99% -> C  (Good)
# Below 60% -> F  (Fail)
GRADE_CLASSIFICATIONS: Dict[str, str] = {
    "A+": "Outstanding",
    "A": "Distinction",
    "B": "Very Good",
    "C": "Good",
    "F": "Fail",
}

PASSING_MARK_PER_SUBJECT: int = 40
MAX_MARK_PER_SUBJECT: int = 100


def calculate_total(marks: Union[Dict[str, int], List[int]]) -> int:
    """
    Calculate the sum of marks obtained across all subjects.

    Parameters:
        marks (dict or list): Subject-to-marks mapping or list of integer marks.

    Returns:
        int: Total marks obtained.
    """
    if isinstance(marks, dict):
        return sum(marks.values())
    return sum(marks)


def calculate_percentage(total: Union[int, float], max_marks: Union[int, float] = 500) -> float:
    """
    Calculate the percentage score based on total marks and maximum possible marks.

    Parameters:
        total (int or float): Total marks obtained.
        max_marks (int or float): Maximum achievable marks across all subjects (default: 500).

    Returns:
        float: Percentage score (0.0 to 100.0).
    """
    if max_marks <= 0:
        return 0.0
    return round((total / max_marks) * 100, 2)


def calculate_gpa(percentage: Union[int, float]) -> float:
    """
    Calculate Grade Point Average (GPA) using a documented 10-point scale.

    Formula:
        GPA = Percentage / 10

    Parameters:
        percentage (int or float): Percentage score (0.0 to 100.0).

    Returns:
        float: GPA score on a 10.00 scale rounded to 2 decimal places.
    """
    return round(percentage / 10.0, 2)


def calculate_grade(percentage: Union[int, float]) -> str:
    """
    Determine the letter grade based on the overall percentage.

    Grading Scheme:
        90.00% - 100.00% : A+
        80.00% - 89.99%  : A
        70.00% - 79.99%  : B
        60.00% - 69.99%  : C
        Below 60.00%     : F

    Parameters:
        percentage (int or float): Percentage score.

    Returns:
        str: Letter grade ('A+', 'A', 'B', 'C', or 'F').
    """
    if percentage >= 90.0:
        return "A+"
    elif percentage >= 80.0:
        return "A"
    elif percentage >= 70.0:
        return "B"
    elif percentage >= 60.0:
        return "C"
    else:
        return "F"


def get_grade_classification(grade: str) -> str:
    """
    Retrieve the descriptive academic classification for a letter grade.

    Parameters:
        grade (str): Letter grade ('A+', 'A', 'B', 'C', 'F').

    Returns:
        str: Academic classification description.
    """
    return GRADE_CLASSIFICATIONS.get(grade, "Unknown")


def get_result(marks: Union[Dict[str, int], List[int]]) -> str:
    """
    Determine overall pass/fail status based on individual subject marks.

    Rule:
        A student must secure at least 40 marks in EVERY subject to pass.
        If any single subject has fewer than 40 marks, the status is 'FAILED',
        regardless of how high the overall percentage is.

    Parameters:
        marks (dict or list): Subject marks mapping or list of marks.

    Returns:
        str: 'PASSED' if all subject marks >= 40, else 'FAILED'.
    """
    scores = marks.values() if isinstance(marks, dict) else marks
    for mark in scores:
        if mark < PASSING_MARK_PER_SUBJECT:
            return "FAILED"
    return "PASSED"


def generate_report_card(
    student: Dict[str, Union[str, Dict[str, int]]],
    total: int,
    percentage: float,
    gpa: float,
    grade: str,
    status: str,
) -> str:
    """
    Generate a formatted ASCII official grade report card.

    Parameters:
        student (dict): Student dictionary containing 'name', 'roll_number', and 'marks'.
        total (int): Total marks obtained out of 500.
        percentage (float): Overall percentage score.
        gpa (float): Calculated GPA on 10.00 scale.
        grade (str): Letter grade (e.g. 'A').
        status (str): Pass/fail status ('PASSED' or 'FAILED').

    Returns:
        str: Neatly aligned ASCII report card string.
    """
    classification = get_grade_classification(grade)
    max_total = len(student["marks"]) * MAX_MARK_PER_SUBJECT

    border_outer = "=" * 47
    border_inner = "-" * 47

    lines = [
        border_outer,
        "           OFFICIAL GRADE REPORT CARD",
        border_outer,
        f"Student Name : {student['name']}",
        f"Roll Number  : {student['roll_number']}",
        border_inner,
        f"{'SUBJECT':<32}MARKS",
        border_inner,
    ]

    for subject, mark in student["marks"].items():
        lines.append(f"{subject:<34}{mark}/{MAX_MARK_PER_SUBJECT}")

    lines.extend([
        border_inner,
        f"Total Marks : {total} / {max_total}",
        f"Percentage  : {percentage:.2f}%",
        f"GPA         : {gpa:.2f} / 10.00",
        f"Grade       : {grade} ({classification})",
        f"Status      : {status}",
        border_outer,
    ])

    report = "\n".join(lines)
    return report


def get_valid_string(prompt: str) -> str:
    """
    Prompt the user for a non-empty string with leading/trailing spaces stripped.

    Parameters:
        prompt (str): Text prompt to display to user.

    Returns:
        str: Non-empty validated string.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [Error] Input cannot be blank. Please enter a valid value.")


def get_valid_mark(subject: str) -> int:
    """
    Prompt the user to enter a whole-number mark (0 to 100) for a subject.
    Re-prompts gracefully if user enters non-integer text or out-of-range values.

    Parameters:
        subject (str): Name of the subject.

    Returns:
        int: Validated integer mark between 0 and 100 inclusive.
    """
    while True:
        raw_input = input(f"{subject}: ").strip()
        try:
            mark = int(raw_input)
            if 0 <= mark <= MAX_MARK_PER_SUBJECT:
                return mark
            print(f"  [Error] Marks must be between 0 and {MAX_MARK_PER_SUBJECT}. You entered: {mark}")
        except ValueError:
            print("  [Error] Invalid input! Please enter a valid whole number (integer).")


def get_student_input(subjects: List[str] = DEFAULT_SUBJECTS) -> Dict[str, Union[str, Dict[str, int]]]:
    """
    Collect student personal details and marks for all subjects.

    Parameters:
        subjects (list): List of subject names.

    Returns:
        dict: Student information dictionary.
    """
    print("\n=== STUDENT GRADE REPORT GENERATOR ===\n")
    name = get_valid_string("Enter Student Name: ")
    roll_number = get_valid_string("Enter Roll Number: ")

    print("\nEnter marks out of 100:")
    marks: Dict[str, int] = {}
    for subject in subjects:
        marks[subject] = get_valid_mark(subject)

    student: Dict[str, Union[str, Dict[str, int]]] = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
    }
    return student


def main() -> None:
    """
    Main orchestration function:
    1. Collects and validates student input.
    2. Performs academic calculations (total, percentage, GPA, grade, pass/fail status).
    3. Generates and displays the official ASCII report card.
    """
    # Step 1: Collect student details and subject marks
    student = get_student_input(DEFAULT_SUBJECTS)

    # Step 2: Perform calculations
    total = calculate_total(student["marks"])
    max_marks = len(student["marks"]) * MAX_MARK_PER_SUBJECT
    percentage = calculate_percentage(total, max_marks)
    gpa = calculate_gpa(percentage)
    grade = calculate_grade(percentage)
    status = get_result(student["marks"])

    # Step 3: Generate and display the report card
    report_card = generate_report_card(
        student=student,
        total=total,
        percentage=percentage,
        gpa=gpa,
        grade=grade,
        status=status,
    )

    print()
    print(report_card)


if __name__ == "__main__":
    main()
