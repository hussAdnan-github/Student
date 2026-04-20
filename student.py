from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware # 1. استيراد المكتبة

app = FastAPI()

# 2. إعدادات الـ CORS لتسمح لـ React بالوصول
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int 
    name: str
    grade: int

students = [
    Student(id=1, name='mogammed', grade=90),
    Student(id=2, name='hussain', grade=80)
]

# الحصول على الطلاب
@app.get('/student')
async def read_student():
    return students

# إضافة طالب جديد
@app.post('/student')
async def add_student(listStudent: Student):
    students.append(listStudent)
    return listStudent # أرجعت الكائن مباشرة ليكون JSON صحيح

# تحديث بيانات طالب
@app.put('/student/{student_id}')
async def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student   
    
    raise HTTPException(status_code=404, detail="Student not found")

# حذف طالب
@app.delete('/student/{student_id}')
async def delete_student(student_id: int):
    target_student = next((s for s in students if s.id == student_id), None)
    if target_student:
        students.remove(target_student)
        return {"message": "success delete"}
        
    raise HTTPException(status_code=404, detail="Student not found")