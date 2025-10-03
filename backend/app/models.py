from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False)
    full_name: Optional[str]
    hashed_password: str
    is_admin: bool = False
    is_optometrist: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    tests: List["IshiharaTest"] = Relationship(back_populates="user")

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str]
    price_cents: int = 0
    currency: str = 'INR'
    sku: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class IshiharaTest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    # Relationship back to User
    user: Optional["User"] = Relationship(back_populates="tests")
    score: Optional[int]
    percentage: Optional[int]
    diagnosis: Optional[str]
    answers: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"
