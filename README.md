📚 Student Grade Manager
A Python project that reads student names and scores from a CSV file, filters valid scores (0–100), assigns letter grades, calculates the average score of passing students, and writes the results to a new CSV file.
📂 Project Structure
student-grade-manager/
├── grade_manager.py    # Main script for processing grades
├── students.csv        # Input CSV with student names and scores
├── graded_students.csv # Output CSV with names, scores, and grades
├── README.md           # Project documentation

🎯 Features

Input CSV Processing: Reads students.csv with name and score columns.
Score Validation: Filters scores to ensure they are numeric and between 0 and 100 (inclusive).
Grade Calculation: Assigns letter grades based on the score:
A: 90–100
B: 80–89
C: 70–79
D: 60–69
E: 50–59
F: Below 50


Passing Students: Identifies students with grades A–E and calculates their average score.
Output CSV: Writes results to graded_students.csv with name, score, and grade columns.
Functional Programming: Uses list/dictionary comprehensions and reduce for processing.

🛠️ How to Run

Ensure you have Python 3.6+ installed.
Create a students.csv file with the following format:name,score
Alice,85
Bob,67
Charlie,92
Diana,49
Eve,76
Frank,abc
Grace,105
Henry,-5


Place students.csv in the same directory as grade_manager.py.
Run the script:python grade_manager.py


Check the output:
Console output shows invalid score warnings and the average score of passing students.
graded_students.csv contains the filtered students with their grades.



Example Output
Console Output:
Skipping invalid score 'abc' for student Frank
Skipping invalid score '105' for student Grace
Skipping invalid score '-5' for student Henry
Average score of passed students: 80.00
Grades written to graded_students.csv

Output CSV (graded_students.csv):
name,score,grade
Alice,85.0,B
Bob,67.0,D
Charlie,92.0,A
Diana,49.0,F
Eve,76.0,C

📜 Script Overview

is_valid_score(score): Validates if a score is a float between 0 and 100.
read_grades(file_path): Reads students.csv, filters valid scores, and returns a list of dictionaries.
calculate_grade(score): Converts a numeric score to a letter grade (A–F).
write_grades(students, file_path): Writes student data with grades to graded_students.csv.
main(): Orchestrates the process, using comprehensions and reduce to filter and compute averages.

💡 Dependencies

Standard Python libraries: csv, functools (for reduce).
No external packages required.

🏷️ Topics

Python
CSV Processing
List/Dictionary Comprehensions
Functional Programming (reduce)
Error Handling
File I/O

📄 License
This project is licensed under the MIT License.