from fastapi import FastAPI , Query
from enum import Enum

app = FastAPI();


@app.get('/')

def Hi():
    return {
        "message" : "hello word"
    }

@app.get('/user/1' , include_in_schema=False)
async def Admin_user():
    return{
        "messege" : "this admin user"
    }
    
@app.get('/user/{user_id}')
async def addUsers(user_id : int ):
    return{
        "name" : user_id
    }
@app.get('/calculate')
def calculate(w : float  = Query(... , gt=20 , lt=200 , description="asdsadsa") 
              
              , h : float = Query(... , gt= 20 , lt=200 , description="sadsadsa")):
    bmi = w / (h *2)
    if bmi < 18.5 :
        message = "لجيك نقص في الوزن"
    elif  18.5 <= bmi < 30 :
        message = "لديك وزن طبيعي"
    elif 30 < bmi <= 40 :
        message = "لديك وزن زيادة"
    else :
        message  = "good"

    return{
        "bmi" : bmi ,
        "message" : message
    }
class UsersList(str , Enum):
    admin = 1
    manager = 2
    user = 3
 
@app.get('/{user_type}/{user_id}')
async def get_user_type(user_type : UsersList , user_id):
    return{
        "user" : {user_type.name , user_id}
    }



