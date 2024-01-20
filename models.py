from sqlalchemy import Column, Integer, String, Date, Boolean
from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dob = Column(Date)
    email = Column(String, unique=True, nullable=False)
    immigration_reason = Column(Boolean)
    institution = Column(String)
    interests = Column(String)
    address = Column(String)