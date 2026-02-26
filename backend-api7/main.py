from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Running"}

@app.post("/students/")
def create_student(name: str, career: str):
    db: Session = SessionLocal()
    student = models.Student(name=name, career=career)
    db.add(student)
    db.commit()
    db.refresh(student)
    db.close()
    return student

@app.get("/students/")
def get_students():
    db: Session = SessionLocal()
    students = db.query(models.Student).all()
    db.close()
    return students
