import csv
from functools import reduce

# File paths for input and output CSV files
FILEPATH = 'students.csv'
G_FILEPATH = 'graded_students.csv'

def is_valid_score(score):
    """Check if a score is a valid float between 0 and 100 (inclusive).

    Args:
        score: The score to validate (string or numeric).

    Returns:
        bool: True if the score is a float between 0 and 100, False otherwise.
    """
    try:
        score_value = float(score)
        return 0 <= score_value <= 100
    except (ValueError, TypeError):
        return False

def read_grades(file_path):
    """Read student names and scores from a CSV file, filtering valid scores.

    Args:
        file_path (str): Path to the input CSV file with 'name' and 'score' columns.

    Returns:
        list: List of dictionaries with 'name' and 'score' (as float) for valid rows.

    Raises:
        FileNotFoundError: If the input file is not found.
        ValueError: If the CSV file lacks required columns.
    """
    students = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            # Verify required columns
            if reader.fieldnames is None or not all(col in reader.fieldnames for col in ['name', 'score']):
                raise ValueError("CSV file must have 'name' and 'score' columns")
            
            # Process each row and filter valid scores
            for row in reader:
                if is_valid_score(row['score']):
                    students.append({'name': row['name'], 'score': float(row['score'])})
                else:
                    print(f"Skipping invalid score '{row['score']}' for student {row['name']}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    return students

def calculate_grade(score):
    """Calculate a letter grade based on a numeric score.

    Args:
        score (float): The numeric score to convert to a letter grade.

    Returns:
        str: The letter grade ('A', 'B', 'C', 'D', 'E', or 'F').

    Note:
        Grading scale:
        - A: 90–100
        - B: 80–89
        - C: 70–79
        - D: 60–69
        - E: 50–59
        - F: Below 50
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'F'

def write_grades(students, file_path):
    """Write student data with grades to a CSV file.

    Args:
        students (list): List of dictionaries with 'name', 'score', and 'grade' keys.
        file_path (str): Path to the output CSV file.

    Raises:
        IOError: If there's an error writing to the file.
    """
    try:
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ['name', 'score', 'grade']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")

def main():
    """Main function to process student grades and generate output CSV."""
    # Read and filter student data
    students = read_grades(FILEPATH)
    
    if not students:
        print("No valid student data found.")
        return
    
    # Add grades to each student using dictionary comprehension
    graded_students = [
        {**student, 'grade': calculate_grade(student['score'])}
        for student in students
    ]
    
    # Filter students who passed (grade != 'F')
    passed_students = [student for student in graded_students if student['grade'] != 'F']
    
    # Calculate average score of passed students using reduce
    if passed_students:
        average_score = reduce(lambda x, y: x + float(y['score']), passed_students, 0) / len(passed_students)
        print(f"Average score of passed students: {average_score:.2f}")
    
    # Write graded students to output CSV
    write_grades(graded_students, G_FILEPATH)
    print(f"Grades written to {G_FILEPATH}")

if __name__ == "__main__":
    main()