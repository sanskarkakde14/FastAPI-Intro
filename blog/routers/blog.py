from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,models,database,oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router=APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db=database.get_db

@router.get('/',response_model=List[schemas.ShowBlog],tags=['Blogs'])
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    
@router.post('/',status_code=status.HTTP_201_CREATED,tags=['Blogs'])
def create(request: schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['Blogs'])
def destroy(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
    
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
def update(id:int,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['Blogs'])
def show(id:int,response:Response,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id,db)

