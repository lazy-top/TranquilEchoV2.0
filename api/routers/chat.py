from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models import Message
from services.langchain.Services.ChatService import run
router = APIRouter(    
    prefix="/chat",
    tags=["chat"],
    responses={404: {"message": "Not found"}},
    )


@router.get("/start")
async def stream_chat():
    return StreamingResponse(run("你是谁呢？"), media_type="text/event-stream")