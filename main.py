from fastapi import FastAPI

app = FastAPI()     #object

students = [
    {"id": 1, "name": "John Doe", "age": 20},
    {"id": 2, "name": "Jane Smith", "age": 22},
    {"id": 3, "name": "Alice Johnson", "age": 19},
    {"id": 4, "name": "Bob Brown", "age": 21},
]

@app.get("/test")   # with decorator we can create a route /test     
def tet():
    return "server is working"

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def add_student(student: dict):
    student_id = len(students) + 1
    student["id"] = student_id
    students.append(student)
    return student

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"error": "Student not found"}


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: dict): 
    for student in students:
        if student["id"] == student_id:
            student.update(updated_student)
            return student
    return {"error": "Student not found"}
