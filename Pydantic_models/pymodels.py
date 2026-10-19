from pydantic import BaseModel,EmailStr,Field,field_validator
from fastapi import HTTPException
class Users(BaseModel):
    email:EmailStr=Field(...,description="Enter your email address ",examples=["yousuf@gmail.com"])
    password:str=Field(...,description="Enter your password ",examples=["12345678"])
    @field_validator("password")
    def password_validator(cls,v):
        if len(v)<8:
            raise HTTPException(status_code=400,detail="Password must be at least 8 characters long",)
        else :
            return v

class Projects(BaseModel):
    uid:int=Field(...,description="Enter your user id ",examples=[1,2])

class Tasks(BaseModel):
    tid:int=Field(...,description="Enter your task id ",examples=[1,2])