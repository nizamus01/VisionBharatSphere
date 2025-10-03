from sqlmodel import Session, select
from . import db, models
import bcrypt
from jose import jwt
from datetime import datetime, timedelta
import os

# Use bcrypt directly to avoid passlib backend detection issues in some environments
SECRET_KEY = os.environ.get('VBS_SECRET','changeme123')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

def hash_password(password: str):
    if isinstance(password, str):
        password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

def verify_password(plain, hashed):
    if isinstance(plain, str):
        plain = plain.encode('utf-8')
    if isinstance(hashed, str):
        hashed = hashed.encode('utf-8')
    try:
        return bcrypt.checkpw(plain, hashed)
    except Exception:
        return False

def create_user(email, password, full_name=None, is_optometrist=False):
    with Session(db.engine) as session:
        existing = session.exec(select(models.User).where(models.User.email == email)).first()
        if existing:
            raise Exception('User exists')
        user = models.User(email=email, full_name=full_name, hashed_password=hash_password(password), is_optometrist=is_optometrist)
        session.add(user); session.commit(); session.refresh(user)
        return user

def authenticate_user(email, password):
    with Session(db.engine) as session:
        user = session.exec(select(models.User).where(models.User.email == email)).first()
        if not user: return None
        if not verify_password(password, user.hashed_password): return None
        return user

def create_access_token(data: dict, expires_delta: int|None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        uid = int(payload.get('sub'))
    except Exception:
        raise credentials_exception
    with Session(db.engine) as session:
        user = session.get(models.User, uid)
        if not user:
            raise credentials_exception
        return user
