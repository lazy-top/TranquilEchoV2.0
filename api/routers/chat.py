
import asyncio
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from models import Message
from services.langchain.Models import getqf
router = APIRouter(    
    prefix="/chat",
    tags=["chat"],
    responses={404: {"message": "Not found"}},
    )

@router.post("/start")
async def stream_chat(message: Message):
    qfModel=getqf()
    if(message.content==" " or len(message.content)>1000):
        return {"message":"content is too long"}
    async def stream_data(content:str):
      async for chunk in qfModel.astream(content):
        yield f"data: {chunk}\n\n".encode()
    return StreamingResponse(stream_data(message.content),status_code=200,media_type="text/event-stream")