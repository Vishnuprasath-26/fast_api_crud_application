
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict


# User Registration
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)


# User Login
class UserLogin(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=100)


# Task Creation
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    description: Optional[str] = None
    status: str = Field(default="pending", max_length=30)
    priority: str = Field(default="medium", max_length=20)
    due_date: Optional[datetime] = None


# Task Update
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=150)
    description: Optional[str] = None
    status: Optional[str] = Field(default=None, max_length=30)
    priority: Optional[str] = Field(default=None, max_length=20)
    due_date: Optional[datetime] = None


# Task Response
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    due_date: Optional[datetime]
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)