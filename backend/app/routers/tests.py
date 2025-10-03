from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from .. import db, models
from ..crud import get_current_user

router = APIRouter()

@router.post('/')
def submit_test(payload: dict, user = Depends(get_current_user)):
    # payload should contain: score, percentage, diagnosis, answers
    t = models.IshiharaTest(user_id=user.id, score=payload.get('score'), percentage=payload.get('percentage'), diagnosis=payload.get('diagnosis'), answers=str(payload.get('answers')))
    with Session(db.engine) as session:
        session.add(t)
        session.commit()
        session.refresh(t)
        return t

@router.get('/')
def list_tests(user = Depends(get_current_user)):
    with Session(db.engine) as session:
        results = session.exec("SELECT * FROM ishiharatest WHERE user_id = :uid", {'uid': user.id}).all()
        return results
