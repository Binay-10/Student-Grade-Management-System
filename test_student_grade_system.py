"""
Unit and Integration Tests for Student Grade Management System
=============================================================
Automated test suite covering:
1. Normal sample calculations (Liam Anderson scenario).
2. Boundary scenarios (all 100s, all 0s, all 40s).
3. Grading boundaries (59%, 60%, 70%, 80%, 90%, 100%).
4. Subject-level pass/fail rule (fail if any subject < 40 despite high percentage).
5. Validation logic (empty strings, non-numeric input, out-of-range marks).
6. Report card layout and field consistency.
"""

import io
import unittest
from unittest.mock import patch

from student_grade_system import (
    DEFAULT_SUBJECTS,
    calculate_total,
    calculate_percentage,
    calculate_gpa,
    calculate_grade,
    get_grade_classification,
    get_result,
    generate_report_card,
    get_valid_string,
    get_valid_mark,
    get_student_input,
)


class TestStudentGradeSystem(unittest.TestCase):
    """Test suite for Student Grade Management System."""

    # -------------------------------------------------------------------------
    # Scenario 1: Normal input matching prompt sample (Liam Anderson)
    # -------------------------------------------------------------------------
    def test_sample_scenario_liam_anderson(self):
        """Verify calculations match the exact prompt sample."""
        marks = {
            "Python Programming": 94,
            "Data Structures": 88,
            "Database Systems": 91,
            "Web Development": 85,
            "Software Engineering": 87,
        }
        total = calculate_total(marks)
        percentage = calculate_percentage(total, 500)
        gpa = calculate_gpa(percentage)
        grade = calculate_grade(percentage)
        status = get_result(marks)

        self.assertEqual(total, 445)
        self.assertEqual(percentage, 89.00)
        self.assertEqual(gpa, 8.90)
        self.assertEqual(grade, "A")
        self.assertEqual(get_grade_classification(grade), "Distinction")
        self.assertEqual(status, "PASSED")

    # -------------------------------------------------------------------------
    # Scenario 2: All subjects scored 100 (Perfect Score)
    # -------------------------------------------------------------------------
    def test_all_subjects_100(self):
        """Verify calculations when all subject scores are 100."""
        marks = {subject: 100 for subject in DEFAULT_SUBJECTS}
        total = calculate_total(marks)
        percentage = calculate_percentage(total, 500)
        gpa = calculate_gpa(percentage)
        grade = calculate_grade(percentage)
        status = get_result(marks)

        self.assertEqual(total, 500)
        self.assertEqual(percentage, 100.00)
        self.assertEqual(gpa, 10.00)
        self.assertEqual(grade, "A+")
        self.assertEqual(get_grade_classification(grade), "Outstanding")
        self.assertEqual(status, "PASSED")

    # -------------------------------------------------------------------------
    # Scenario 3: All subjects scored 0 (Minimum Score)
    # -------------------------------------------------------------------------
    def test_all_subjects_zero(self):
        """Verify calculations when all subject scores are 0."""
        marks = {subject: 0 for subject in DEFAULT_SUBJECTS}
        total = calculate_total(marks)
        percentage = calculate_percentage(total, 500)
        gpa = calculate_gpa(percentage)
        grade = calculate_grade(percentage)
        status = get_result(marks)

        self.assertEqual(total, 0)
        self.assertEqual(percentage, 0.00)
        self.assertEqual(gpa, 0.00)
        self.assertEqual(grade, "F")
        self.assertEqual(get_grade_classification(grade), "Fail")
        self.assertEqual(status, "FAILED")

    # -------------------------------------------------------------------------
    # Scenario 4: Grading boundaries (59, 60, 70, 80, 90 percent)
    # -------------------------------------------------------------------------
    def test_grading_boundaries(self):
        """Verify letter grades and classifications at exact grade threshold boundaries."""
        test_cases = [
            (0.0, "F", "Fail"),
            (59.0, "F", "Fail"),
            (59.99, "F", "Fail"),
            (60.0, "C", "Good"),
            (69.99, "C", "Good"),
            (70.0, "B", "Very Good"),
            (79.99, "B", "Very Good"),
            (80.0, "A", "Distinction"),
            (89.99, "A", "Distinction"),
            (90.0, "A+", "Outstanding"),
            (95.5, "A+", "Outstanding"),
            (100.0, "A+", "Outstanding"),
        ]
        for percentage, expected_grade, expected_classification in test_cases:
            with self.subTest(percentage=percentage):
                grade = calculate_grade(percentage)
                classification = get_grade_classification(grade)
                self.assertEqual(grade, expected_grade)
                self.assertEqual(classification, expected_classification)

    # -------------------------------------------------------------------------
    # Scenario 5: One subject below 40 while overall percentage is high
    # -------------------------------------------------------------------------
    def test_high_percentage_but_one_subject_failed(self):
        """Verify student fails if any subject is < 40 despite high overall average."""
        marks = {
            "Python Programming": 35,  # Failed subject (< 40)
            "Data Structures": 95,
            "Database Systems": 95,
            "Web Development": 95,
            "Software Engineering": 95,
        }
        total = calculate_total(marks)
        percentage = calculate_percentage(total, 500)
        gpa = calculate_gpa(percentage)
        grade = calculate_grade(percentage)
        status = get_result(marks)

        self.assertEqual(total, 415)
        self.assertEqual(percentage, 83.00)
        self.assertEqual(gpa, 8.30)
        self.assertEqual(grade, "A")
        self.assertEqual(status, "FAILED")

    # -------------------------------------------------------------------------
    # Scenario 6 & 7: Input validation for marks (text, negative, > 100)
    # -------------------------------------------------------------------------
    @patch("builtins.input", side_effect=["invalid_text", "ten", "-15", "105", "85"])
    def test_get_valid_mark_validation_recovery(self, mock_input):
        """Verify invalid text, negative marks, and marks > 100 are rejected until valid."""
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            valid_mark = get_valid_mark("Python Programming")
            self.assertEqual(valid_mark, 85)
            output = fake_out.getvalue()
            self.assertIn("Invalid input! Please enter a valid whole number", output)
            self.assertIn("Marks must be between 0 and 100", output)

    # -------------------------------------------------------------------------
    # Scenario 8: Empty student name or roll number validation
    # -------------------------------------------------------------------------
    @patch("builtins.input", side_effect=["", "   ", "Liam Anderson"])
    def test_get_valid_string_validation_recovery(self, mock_input):
        """Verify empty and whitespace-only strings are rejected until valid."""
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            valid_name = get_valid_string("Enter Student Name: ")
            self.assertEqual(valid_name, "Liam Anderson")
            output = fake_out.getvalue()
            self.assertIn("Input cannot be blank", output)

    # -------------------------------------------------------------------------
    # Scenario 9: Student scoring exactly 40 in every subject
    # -------------------------------------------------------------------------
    def test_exactly_passing_marks_in_all_subjects(self):
        """Verify scoring exactly 40 in every subject results in PASSED with Grade F."""
        marks = {subject: 40 for subject in DEFAULT_SUBJECTS}
        total = calculate_total(marks)
        percentage = calculate_percentage(total, 500)
        gpa = calculate_gpa(percentage)
        grade = calculate_grade(percentage)
        status = get_result(marks)

        self.assertEqual(total, 200)
        self.assertEqual(percentage, 40.00)
        self.assertEqual(gpa, 4.00)
        self.assertEqual(grade, "F")
        self.assertEqual(get_grade_classification(grade), "Fail")
        self.assertEqual(status, "PASSED")

    # -------------------------------------------------------------------------
    # Additional Integration Test: Full get_student_input and report card layout
    # -------------------------------------------------------------------------
    @patch("builtins.input", side_effect=["Liam Anderson", "PY-2026-042", "94", "88", "91", "85", "87"])
    def test_get_student_input(self, mock_input):
        """Verify get_student_input correctly packages user input into dictionary structure."""
        with patch("sys.stdout", new=io.StringIO()):
            student = get_student_input(DEFAULT_SUBJECTS)
            self.assertEqual(student["name"], "Liam Anderson")
            self.assertEqual(student["roll_number"], "PY-2026-042")
            self.assertEqual(student["marks"]["Python Programming"], 94)
            self.assertEqual(student["marks"]["Data Structures"], 88)
            self.assertEqual(student["marks"]["Database Systems"], 91)
            self.assertEqual(student["marks"]["Web Development"], 85)
            self.assertEqual(student["marks"]["Software Engineering"], 87)

    def test_generate_report_card_layout(self):
        """Verify report card string format contains all mandatory details and borders."""
        student = {
            "name": "Liam Anderson",
            "roll_number": "PY-2026-042",
            "marks": {
                "Python Programming": 94,
                "Data Structures": 88,
                "Database Systems": 91,
                "Web Development": 85,
                "Software Engineering": 87,
            },
        }
        report = generate_report_card(
            student=student,
            total=445,
            percentage=89.0,
            gpa=8.9,
            grade="A",
            status="PASSED",
        )

        # Check headers and borders
        self.assertIn("OFFICIAL GRADE REPORT CARD", report)
        self.assertIn("Student Name : Liam Anderson", report)
        self.assertIn("Roll Number  : PY-2026-042", report)
        self.assertIn("Python Programming", report)
        self.assertIn("94/100", report)
        self.assertIn("Total Marks : 445 / 500", report)
        self.assertIn("Percentage  : 89.00%", report)
        self.assertIn("GPA         : 8.90 / 10.00", report)
        self.assertIn("Grade       : A (Distinction)", report)
        self.assertIn("Status      : PASSED", report)


if __name__ == "__main__":
    unittest.main()
