from sqlalchemy import Column,Integer, String
from .base import BaseModel
from passlib.context import CryptContext

pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')
class UserModel(BaseModel):
    __table__='users'
     
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    email=Column(String,Unique=True)

    password_hash=Column(String,nullable=True)

    def set_password(self,password:str):
        self.password_hash=pwd_context.hash(password)
