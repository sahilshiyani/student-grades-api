Student Records API
This is a FastAPI-based RESTful API for managing student records with JWT authentication. It allows users to perform CRUD operations (Create, Read, Update, Delete) on student records, including storing student names, scores, and automatically calculated grades in an SQLite database.
How to Run
Prerequisites

Python 3.8+
pip (Python package manager)
Virtual environment (recommended)

Setup Instructions

Clone the Repository or Copy Files

Ensure all provided files (auth.py, crud.py, database.py, main.py, models.py, schemas.py, requirements.txt) are in the same directory.


Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies

Install the required packages using the provided requirements.txt:pip install -r requirements.txt


The requirements.txt contains:fastapi
uvicorn
sqlalchemy
pydantic
passlib[bcrypt]
python-jose
pytz




Run the Application

Start the FastAPI server using Uvicorn:uvicorn main:app --reload


The API will be available at http://127.0.0.1:8000.


Access the API

Open a browser or API client (e.g., Postman, cURL) to interact with the endpoints.
Visit http://127.0.0.1:8000/docs for the interactive Swagger UI to test the API.



Notes

The application uses an SQLite database (students.db) that will be created automatically in the project directory.
The default user for testing is:
Username: butler
Password: password123


Replace the SECRET_KEY in auth.py with a secure key in production.

Example Input/Output
1. Login (Obtain JWT Token)
Endpoint: POST /loginInput:
curl -X POST "http://127.0.0.1:8000/login" -d "username=butler&password=password123"

Output:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

2. Access Protected Route
Endpoint: GET /protectedInput:
curl -X GET "http://127.0.0.1:8000/protected" -H "Authorization: Bearer <access_token>"

Output:
{
  "message": "Hello butler, you have access!"
}

3. Create a Student
Endpoint: POST /studentsInput:
curl -X POST "http://127.0.0.1:8000/students" -H "Content-Type: application/json" -d '{"name": "Alice", "score": 85.5}'

Output:
{
  "name": "Alice",
  "score": 85.5,
  "id": 1,
  "grade": "B"
}

4. Get All Students
Endpoint: GET /studentsInput:
curl -X GET "http://127.0.0.1:8000/students"

Output:
[
  {
    "name": "Alice",
    "score": 85.5,
    "id": 1,
    "grade": "B"
  }
]

5. Get a Specific Student
Endpoint: GET /students/{student_id}Input:
curl -X GET "http://127.0.0.1:8000/students/1"

Output:
{
  "name": "Alice",
  "score": 85.5,
  "id": 1,
  "grade": "B"
}

6. Delete a Student
Endpoint: DELETE /students/{student_id}Input:
curl -X DELETE "http://127.0.0.1:8000/students/1"

Output:
{
  "detail": "Student deleted"
}

Concepts Practiced

FastAPI Framework: Building a RESTful API with automatic OpenAPI documentation.
JWT Authentication: Implementing secure user authentication with JSON Web Tokens.
SQLAlchemy ORM: Managing database operations with an Object-Relational Mapper.
SQLite Database: Using a lightweight database for persistent storage.
Pydantic Models: Defining and validating data structures for API requests and responses.
Dependency Injection: Using FastAPI's Depends for managing database sessions and authentication.
Password Hashing: Securely hashing passwords with passlib and bcrypt.
CRUD Operations: Implementing Create, Read, Update, Delete functionality for student records.
Error Handling: Managing HTTP exceptions for invalid inputs or unauthorized access.
Type Hints: Using Python type annotations for better code clarity and IDE support.
