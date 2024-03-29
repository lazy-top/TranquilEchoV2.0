
import json
from fastapi import APIRouter, WebSocket, Request

from services.langchain.Services.personService import agent_executor
from fastapi.responses import HTMLResponse
from services.langchain.Services.personService import agent_executor
router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Chat not found"}},
)

@router.websocket("/start")
async def stream_chat(websocket: WebSocket):
    """Start a new chat session."""
    await websocket.accept()
    await websocket.send_json({"role":"ai",
                               "content":"你好，我是你的私人心理咨询师，你有什么问题，我都能为你解答。"})
    while True:
        try:
            message = await websocket.receive_text()
            message=json.loads(message)
            message= message['content']
            # 这里可以添加处理消息的逻辑,流式返回数据

            async for chunk in agent_executor.stream( {"input":message}):
             yield chunk
             websocket.send_json({"role":"ai",
                               "content":chunk})
             print(chunk)
  
        except Exception as e:
            print("聊天功能：{}".format(e))
            await websocket.send_json({
                "role":"system",
                "content":f'Error: {e}'
            })
            websocket.close()
            break
    return

@router.get("/ui_chat", response_class=HTMLResponse)
async def ui(request: Request, chat_id: str):
    """
    返回聊天UI模板的HTTP响应。

    参数:
    - request: Request对象，表示客户端的HTTP请求。
    - chat_id: 字符串，表示聊天的唯一标识符。

    返回值:
    - HTMLResponse对象，包含聊天界面的HTML内容。
    """
    # 从文件系统中读取并返回静态HTML文件的内容
    return HTMLResponse(open("static/html/chat.html",encoding='utf-8').read())