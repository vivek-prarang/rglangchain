from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Users
from app.schemas import LoginRequest, LoginResponse, RegistrationResponse,RegistrationRequest
router = APIRouter()

@router.post("/login/", response_model=LoginResponse)
def login( login_request: LoginRequest, db: Session = Depends(get_db)):
    try:
        user=db.query(Users).filter_by(
                username=login_request.username,
                password=login_request.password
            ).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password."
            )
        return LoginResponse(access_token="dummy_token", token_type="bearer")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during login."
        )
    return LoginResponse(access_token="Login successful", token_type="dummy_token")


@router.post("/register/", response_model=RegistrationResponse)
def register(registration_request: RegistrationRequest, db: Session = Depends(get_db)):
    user=db.query(Users).filter_by(
            username=registration_request.username,
            mobile=registration_request.mobile
        ).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or password already exists."
        )
    try:
        user=Users(
            mobile=registration_request.mobile,
            username=registration_request.username,
            password=registration_request.password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during registration."
        )

    return RegistrationResponse(
        mobile=user.mobile,
        username=user.username,
        created_at=user.created_at.isoformat()
    )
