from pydantic import BaseModel
class Token(BaseModel):
    access_token: str
    token_type: str
class Guest(BaseModel):
    guest_bool:bool
class Therapist(BaseModel):
    username:str
    password:str
    email:str
    full_name:str
    phone_number:str
    title:str
    description:str
class Message(BaseModel):
    content:str
class User(BaseModel):
    username:str
    password:str
    email:str
    full_name:str
    phone_number:str