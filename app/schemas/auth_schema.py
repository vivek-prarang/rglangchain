from email.policy import default
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

class RegistrationRequest(BaseModel):
    mobile: str = Field(..., min_length=10, max_length=15)
    username: str = Field(..., min_length=3, max_length=255)
    password: str = Field(..., min_length=8, max_length=255)


class RegistrationResponse(BaseModel):
    mobile: str
    username: str
    created_at : Optional[str] = None
    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=255)
    password: str = Field(..., min_length=8, max_length=255)

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

