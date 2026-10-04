import json
from fastapi import FastAPI

app = FastAPI()

# Load data from JSON file
with open("students.json", "r") as file:
    data = json.load(file)

students = data["students"]

Q
@app.get("/test")
def test():
    return "Server is working"


# Get all students
@app.get("/students")
def get_students():
    return students


# Add new student
@app.post("/students")
def add_student(student: dict):
    student_id = max([s["id"] for s in students], default=0) + 1

    student["id"] = student_id
    students.append(student)

    with open("students.json", "w") as file:
        json.dump({"students": students}, file, indent=4)

    return student


# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {"error": "Student not found"}


# Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: dict):

    for student in students:
        if student["id"] == student_id:

            student.update(updated_student)

            with open("students.json", "w") as file:
                json.dump({"students": students}, file, indent=4)

            return student

    return {"error": "Student not found"}


# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:
        if student["id"] == student_id:

            students.remove(student)

            with open("students.json", "w") as file:
                json.dump({"students": students}, file, indent=4)

            return {"message": "Student deleted successfully"}

    return {"error": "Student not found"}