import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from datetime import date
from database import engine
import models
import schemas
import database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Example user data store (in-memory for simplicity)
users_db = []


# User model
class User(BaseModel):
    user_id: Optional[int] = None
    name: str
    dob: date
    email: str
    immigration_reason: Optional[bool] = None
    institution: Optional[str] = None
    interests: Optional[str] = None
    address: str


@app.get("/")
async def root():
    return {"message": "User Management API"}


@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", response_model=schemas.User, status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
