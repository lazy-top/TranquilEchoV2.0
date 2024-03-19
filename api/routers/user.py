import datetime
from fastapi.responses import HTMLResponse
import datetime
import json
import shutil
from fastapi import APIRouter,  File,  Request, UploadFile, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
router = APIRouter(    
    prefix="/user",
    tags=["user"],
    responses={404: {"message": "Not found"}},
    )

@router.get("/ui_group", response_class=HTMLResponse)
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
    return HTMLResponse(open("static/html/group.html",encoding='utf-8').read())





connected_users = {}

class Message(BaseModel):
    content: str
    message_type: str
@router.websocket("/group/{user_id}")
async def websocket_endpoint(user_id: str, websocket: WebSocket):
    await websocket.accept()
    connected_users[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            message["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await broadcast_message(message)
    except WebSocketDisconnect:
        del connected_users[user_id]
        await websocket.close()

async def broadcast_message(message: dict):
    for user, user_ws in connected_users.items():
        await user_ws.send_text(json.dumps(message))

@router.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    """上传文件到服务器。"""
    print(file.filename)
    with open(f"uploaded_files/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}