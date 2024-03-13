from pydantic import BaseModel, EmailStr
class User(BaseModel):
    email: EmailStr
    password: str
    name: str
    phone_number: str
class UserIn(BaseModel):
    email: EmailStr
    password: str
    repassword: str
    name: str
    phone_number: str

class UserOut(BaseModel):
    email: EmailStr
    password: str
    name: str
    phone_number: str
