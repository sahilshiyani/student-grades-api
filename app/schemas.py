from pydantic import BaseModel, Field

class StudentBase(BaseModel):
    name: str = Field(..., description='Alice')
    score: float = Field(..., ge=0, le=100, description='Student score between 0 and 100')

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    grade: str

    class Config:
        form_attributes = True
