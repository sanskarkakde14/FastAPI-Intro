from pydantic import BaseModel
from typing import List, Optional
#pydantic models
class Blog(BaseModel):
    title: str
    body: str

class BlogBase(Blog):
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[BlogBase]=[]
    class Config():
        orm_mode=True

#for updated response its a pydantic model that is added to urls for particularization of data
class ShowBlog(BaseModel):
    title:str
    body: str
    creator: ShowUser
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str

class TokenData(BaseModel):
    email:Optional[str]=None