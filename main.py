
import asyncio
from fastapi import  FastAPI
import uvicorn
from api.routers import  chat,guest,image,therapist,video
from uvicorn.config import LOGGING_CONFIG
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import StreamingResponse
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app=FastAPI(
    title="TranquilEchoV2.0API",
    description=
    """
TranquilEchoV2.0API

    

    """,
    version="2.0.0",
)

# Dependency

app.include_router(chat.router)
app.include_router(therapist.router)
app.include_router(guest.router)
# app.include_router(user.router)
app.include_router(image.router)
app.include_router(video.router)
# # 自定义日志配置
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "use_colors": True,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": "%(levelprefix)s %(client_addr)s - \"%(request_line)s\" %(status_code)s",
            "use_colors": True,
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "filename": "uvicorn_default.log",
            "encoding": "utf-8",
        },
        "access": {
            "formatter": "access",
            "class": "logging.FileHandler",
            "filename": "uvicorn_access.log",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"handlers": ["default"], "level": "INFO", "propagate": False},
    },
}
LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelprefix)s %(message)s"

def generate_chunks():
    """模拟一个无限循环生成数据的生成器函数"""
    counter = 0
    while counter<10:
        yield f"data chunk {counter}\n".encode()  # 注意这里返回的是字节流，通常需要编码成bytes
        counter += 1

@app.get("/")
async def stream_data():
    headers = {"Content-Type": "text/plain"}  # 设置响应头
    return StreamingResponse(generate_chunks(), headers=headers, status_code=200)

# 或者，如果你正在处理SSE：
@app.get("/sse")
async def sse_stream():
    headers = {"Content-Type": "text/event-stream"}
    async def event_stream():
        for i in range(10):  # 仅做演示，这里生成100个事件
            await asyncio.sleep(0.5)  # 模拟延迟
            yield f"data: {i}\n\n".encode()  # SSE数据格式要求每条数据前面加上"data: "，并以两个换行符结束
    return StreamingResponse(event_stream(), headers=headers, status_code=200)

if __name__ =='__main__': 
    uvicorn.run(
            app='main:app',
            host="127.0.0.1",
            reload=True,
            port=8000,
            # log_config=log_config,
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

