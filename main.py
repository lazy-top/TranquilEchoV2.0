from fastapi import  FastAPI
from api.routers import  chat
app=FastAPI(
    title="TranquilEchoV2.0API",
    description="TranquilEchoV2.0API",
    version="2.0.0",

)
app.include_router(chat.router)
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}