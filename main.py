
from fastapi import  Depends, FastAPI, HTTPException
import uvicorn
from api.routers import  chat,guest,image,therapist,video
from core import models
from sqlalchemy.orm import Session
from core.database import SessionLocal

from uvicorn.config import LOGGING_CONFIG

LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelprefix)s %(message)s"

app=FastAPI(
    title="TranquilEchoV2.0API",
    description="TranquilEchoV2.0API",
    version="2.0.0",
responses={404: {"message": "Not found"}},
)

# Dependency

app.include_router(chat.router)
app.include_router(therapist.router)
app.include_router(guest.router)
# app.include_router(user.router)
app.include_router(image.router)
app.include_router(video.router)

if __name__ =='__main__': 
    uvicorn.run(
            app='main:app',
            host="127.0.0.1",
            reload=True,
            port=8000,
        )
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/")
# def read_root(user_id: int = 3, db: Session = Depends(get_db)):
#     try:
#         db_user = db.query(models.User).filter(models.User.id == user_id).first()
#         if db_user is None:
#             raise HTTPException(status_code=400, detail="User not found")
#         return {"message": f"Hello {db_user.username}"}
#     except Exception as e:
#         # 捕获其他异常，以防止程序崩溃
#         raise HTTPException(status_code=500, detail="Internal server error{}".format(e))

