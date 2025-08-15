Student Records API
  
This is a FastAPI-based RESTful API for managing student records with JWT authentication. It supports CRUD operations (Create, Read, Update, Delete) for student data, including names, scores, and automatically calculated grades, stored in an SQLite database.

🚀 Live API: [student-grades-api.onrender.com](https://student-grades-api.onrender.com)
📄 Swagger Docs: [student-grades-api.onrender.com/docs](https://student-grades-api.onrender.com/docs)

How to Run Locally (Optional)
The API is deployed on Render and accessible via the live URL above. Running locally with Uvicorn is optional and useful for development, testing, or debugging.
🔧 Prerequisites

Python 3.8+
pip (Python package manager)
Virtual environment (recommended)

🛠️ Setup Instructions

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
python-multipart




Run the Application Locally

Start the FastAPI server using Uvicorn:uvicorn main:app --reload


The API will be available locally at http://127.0.0.1:8000.


Access the API

Use a browser or API client (e.g., Postman, cURL) to interact with the endpoints.
Visit http://127.0.0.1:8000/docs for the local interactive Swagger UI or use the live Swagger Docs at student-grades-api.onrender.com/docs.



📝 Notes

The application uses an SQLite database (students.db) locally, which is separate from the Render deployment’s database.
The default user for testing is:
Username: butler
Password: password123


⚠️ Replace the SECRET_KEY in auth.py with a secure key in production, and ensure it’s configured in Render’s environment variables.

🌟 Example Requests & Responses
1. Root Endpoint
Request:
curl -X GET "https://student-grades-api.onrender.com/"

Response:
{
  "message": "Welcome to the Student Records API"
}

2. Login (Obtain JWT Token)
Request:
curl -X POST "https://student-grades-api.onrender.com/login" -d "username=butler&password=password123"

Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

3. Access Protected Route
Request:
curl -X GET "https://student-grades-api.onrender.com/protected" -H "Authorization: Bearer <access_token>"

Response:
{
  "message": "Hello butler, you have access!"
}

4. Create a Student
Request:
curl -X POST "https://student-grades-api.onrender.com/students" -H "Content-Type: application/json" -d '{"name": "Alice", "score": 85.5}'

Response:
{
  "name": "Alice",
  "score": 85.5,
  "id": 1,
  "grade": "B"
}

5. Get All Students
Request:
curl -X GET "https://student-grades-api.onrender.com/students"

Response:
[
  {
    "name": "Alice",
    "score": 85.5,
    "id": 1,
    "grade": "B"
  }
]

6. Get a Specific Student
Request:
curl -X GET "https://student-grades-api.onrender.com/students/1"

Response:
{
  "name": "Alice",
  "score": 85.5,
  "id": 1,
  "grade": "B"
}

7. Delete a Student
Request:
curl -X DELETE "https://student-grades-api.onrender.com/students/1"

Response:
{
  "detail": "Student deleted"
}

🧠 Concepts Practiced

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
