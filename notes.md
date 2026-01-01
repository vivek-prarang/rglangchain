<!-- Alembic -->
Alembic migration ke liye pehle packages install kiye (sqlalchemy, alembic, aur MySQL ke liye pymysql), phir SQLAlchemy Base banaya (DeclarativeBase), us Base se models (jaise Users, Profiles) define kiye, uske baad ek central file (app/db/base.py) me sab models import kiye taaki Base.metadata populate ho, phir alembic init karke alembic/env.py me Base import kiya aur target_metadata = Base.metadata set kiya, saath hi database URL configure kiya, aur finally alembic revision --autogenerate se migration generate karke alembic upgrade head se database me tables create kiye.

<!-- Database Connection -->
Database connection ke liye SQLAlchemy engine create kiya gaya, jo settings.database_url se database URL lekar connection establish karta hai. SessionLocal session manager bhi define kiya gaya hai jo database transactions manage karta hai.

<!-- Models Definition -->
Models define karne ke liye SQLAlchemy ORM ka use kiya gaya hai. Do models
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, scoped_session
from sqlalchemy import create_engine
<!-- all imports from sqlalchemy -->
from app.core.config import settings
Base = declarative_base()
engine = create_engine(settings.database_url)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    profiles = relationship("Profiles", back_populates="owner")
