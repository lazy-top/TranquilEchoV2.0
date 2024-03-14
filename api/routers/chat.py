from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models import Message
from services.langchain.Services import ChatService
router = APIRouter(    
    prefix="/chat",
    tags=["chat"],
    responses={404: {"message": "Not found"}},
    )
@router.post("/start")
async def chat(message:Message):
    headers = {"Content-Type": "text/event-stream"}
    return StreamingResponse(ChatService.run(message.content), headers=headers, status_code=200)


