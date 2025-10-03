from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from .. import db, models
from typing import List

router = APIRouter()

@router.get('/', response_model=List[models.Product])
def list_products():
    with Session(db.engine) as session:
        return session.exec(select(models.Product)).all()

@router.post('/')
def create_product(prod: models.Product):
    with Session(db.engine) as session:
        session.add(prod)
        session.commit()
        session.refresh(prod)
        return prod

@router.get('/{product_id}')
def get_product(product_id: int):
    with Session(db.engine) as session:
        prod = session.get(models.Product, product_id)
        if not prod:
            raise HTTPException(status_code=404, detail='Not found')
        return prod
