import bcrypt
def hash_password(password:str):
    #converting password in to bytes
    password_bytes=password.encode('utf-8')
    #converting bytes in to string form
    encoded_password=bcrypt.hashpw(password_bytes,bcrypt.gensalt())
    return encoded_password.decode('utf-8')
def verify_password(plain_password:str,hashed_password_from_db:str):
    new_password=plain_password.encode('utf-8')
    db_password=hashed_password_from_db.encode('utf-8')
    return bcrypt.checkpw(new_password,db_password)
print(hash_password("hi"))
print(verify_password("hi","$2b$12$XHRnDWYr6e/dhlSjIyWOHOrH9pMTxB/Hgz0Z1qoA7H/58up9OAXvK"))
