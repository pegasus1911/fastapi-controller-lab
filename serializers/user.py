from pydantic import BaseModel

class UserSchema(BaseModel):
    username:str
    email:str
    password:str


    class Config:
        orm_mode=True


class UserResposeSchema(BaseModel):
    username:str
    email:str


    class config:
        orm=True