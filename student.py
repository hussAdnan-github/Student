from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student (BaseModel):
    id : int 
    name : str
    grade : int

students = [
    Student(
        id=1 , name='mogammed' , grade=90
    ),
    Student(
        id=2 , name='hussain' , grade=80
    )
]

# get student
@app.get('/student')
async def read_student():
    return students
    

@app.post('/student/')
async def add_student(listStudent : Student):
    students.append(listStudent)

    return{
        listStudent
    }

from fastapi import HTTPException

@app.put('/student/{student_id}')
async def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student   
    
    # هذه الرسالة تظهر فقط بعد انتهاء الحلقة (Loop) دون إيجاد الطالب
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete('/student/{student_id}')
async def delete_student(student_id: int):
    
    
    
    target_student = next((s for s in students if s.id == student_id), None)
    if target_student:
        students.remove(target_student)
        return {"message": "success delete"}
        
    raise HTTPException(status_code=404, detail="Student not found")