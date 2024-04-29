from fastapi import APIRouter,Depends
from .. import schemas,database
from sqlalchemy.orm import Session
from ..repository import user

router=APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db=database.get_db

@router.post('/',response_model=schemas.ShowUser,tags=['Users'])
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser,tags=['Users'])
def get_user(id,db:Session=Depends(get_db)):
    return user.show(id,db)
