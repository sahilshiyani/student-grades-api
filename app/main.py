from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database, schemas, crud

app = FastAPI(title="Student Records API")

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def root():
    return {"message": "Welcome to the Student Records API"}

@app.get("/students", response_model=list[schemas.Student])
def read_students(db: Session = Depends(database.get_db)):
    return crud.get_students(db)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(database.get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    return crud.create_student(db, student)

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(database.get_db)):
    success = crud.delete_student(db, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}
