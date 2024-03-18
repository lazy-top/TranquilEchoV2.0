

from fastapi import APIRouter, WebSocket
from fastapi.responses import StreamingResponse
from models import Message
from utils import R_error
from services.langchain.Services.personService import run

router = APIRouter(    
    prefix="/chat",
    tags=["chat"],
    responses={404: {"message": "Not found"}},
    )

@router.websocket("/start")
async def stream_chat(websocket: WebSocket):
    """start chat"""
    if(message.content==" " or len(message.content)>1000):
        return R_error('格式错误')
    return StreamingResponse(run(message.content),status_code=200,media_type="text/event-stream")