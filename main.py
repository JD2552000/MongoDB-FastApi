from fastapi import FastAPI, HTTPException
from database import create_student, delete_student, get_all_students, get_student_by_id, update_student

app = FastAPI()

@app.post("/students/")
def create(student_data: dict):
    new_student_id = create_student(student_data)
    return {"message": "Student created successfully", "student_id": new_student_id}

@app.get("/students/{student_id}")
def read_by_id(student_id: str):
    student = get_student_by_id(student_id)
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}")
def update(student_id: str, student_data: dict):
    if update_student(student_id, student_data):
        return {"message": "Student updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete(student_id: str):
    if delete_student(student_id):
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
    
@app.get("/students/")
def read_all():
    students = get_all_students()
    return students