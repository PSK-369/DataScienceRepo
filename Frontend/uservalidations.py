from fastapi import FastAPI,HTTPException,status 
from pydantic import BaseModel,field_validator,model_validator,Field
from typing import List,Dict,Set,Optional,Any

app=FastAPI(title='auth form',version='1.0.0',summary='User authetication Form') 

class userClass(BaseModel):
    username: str = Field(...,description='Username')
    password: str = Field(...,description='password')

    @field_validator("username")
    @classmethod 
    def username_lengthcheck(cls,user:str):
        if len(user) <=2:
            raise HTTPException(status_code=400,detail='username length is not matched')
        return {"message":"Username length is matched"}

    @field_validator('username')
    @classmethod
    def username_gmailcheck(cls,gmail:str):
        if "@gmail.com" in gmail:
            return {"message":"@gmail.com is present"}
        raise HTTPException(status_code=400,detail='@gmail.com is missed')

    @field_validator('password')
    @classmethod
    def password_lengthcheck(cls,pass1:str):
        if len(pass1) < 5:
            raise HTTPException(status_code=400,detail="password length is not matched < 5 you entered")
        return {"message": "password length is matched"}

    @field_validator('password')
    @classmethod
    def password_qualitycheck(cls,pass2:str):
        str1="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*"
        if str1 in pass2:
            return {"message":"password quality check is success"}
        raise HTTPException(status_code=400,detail="password quanlity check is failed")

store=List[userClass]=[]
@app.get("/")
def health_check():
    return {"healthcheck":"passed"}

@app.get("/username/{username}")
def username_present_check(username:str):
    for old_id in store:
        if username == old_id:
            return {"message":"username is already presnet"}
        raise HTTPException(status_code=200,detail="username is not present")
    