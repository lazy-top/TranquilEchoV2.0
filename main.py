from fastapi import  Depends, FastAPI, HTTPException
from api.routers import  chat
from core import models
from sqlalchemy.orm import Session
from core.database import SessionLocal



app=FastAPI(
    title="TranquilEchoV2.0API",
    description="TranquilEchoV2.0API",
    version="2.0.0",
responses={404: {"message": "Not found"}},
)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app.include_router(chat.router)
@app.get("/")
def read_root(user_id: int = 3, db: Session = Depends(get_db)):
    try:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=400, message="User not found")
        return {"message": f"Hello {db_user.name}"}
    except Exception as e:
        # 捕获其他异常，以防止程序崩溃
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, message="Internal server error")

