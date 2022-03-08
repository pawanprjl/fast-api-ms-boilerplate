from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.db import engine
from . import models, crud, schemas


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/user"
)


@router.get('/')
async def get_all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db=db)


@router.post('/create/')
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
