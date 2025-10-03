from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlmodel import Session, select
from .. import models, db
from ..crud import create_user, authenticate_user, create_access_token

router = APIRouter()

class RegisterIn(BaseModel):
    email: str
    full_name: str | None = None
    password: str
    is_optometrist: bool = False

@router.post('/register')
def register(payload: RegisterIn):
    user = create_user(payload.email, payload.password, payload.full_name, payload.is_optometrist)
    return {"id": user.id, "email": user.email}

class LoginIn(BaseModel):
    email: str
    password: str

@router.post('/login')
def login(data: LoginIn):
    user = authenticate_user(data.email, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    token = create_access_token({'sub': str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
