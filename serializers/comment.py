from pydantic import BaseModel

class CommentSchema(BaseModel):
  id: int
  content: str
  tea_id:int

  class Config:
    orm_mode = True
