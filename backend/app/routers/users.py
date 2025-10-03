from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from .. import db, models
from typing import List

router = APIRouter()

@router.get('/', response_model=List[models.User])
def list_users():
    with Session(db.engine) as session:
        users = session.exec(select(models.User)).all()
        return users
