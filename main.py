from fastapi import FastAPI,HTTPException,Depends
from Pydantic_models.pymodels import Users as pyUsers
from Database_models.models import Users as dbUsers
from database.connection import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import select,exists
from Security import hash_password, verify_password
app=FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user:pyUsers,db:Session=Depends(get_db)):

    existing_user = db.scalar(select(dbUsers.email).where(dbUsers.email==user.email))
    if existing_user is not None:
        raise HTTPException(status_code=400,detail="Email already registered")
    hashed_password=hash_password(user.password)
    new_user = dbUsers(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"Email has been registered",
                "email":new_user.email,
                "password":new_user.password,
                "uid":new_user.uid}
@app.post("/login")
def login(user:pyUsers,db:Session=Depends(get_db)):
    get_pwd_stmt=select(dbUsers.password).where(dbUsers.email==user.email)
    db_password = db.scalar(get_pwd_stmt)
    if db_password is None:
        raise HTTPException(status_code=400,detail="Email doesn't exist,Please register first")

    is_true=verify_password(user.password,db_password)
    if is_true:
        return {"message":"Login Successful",}
    else:
        raise HTTPException(status_code=400,detail="Wrong Password! Try again")



