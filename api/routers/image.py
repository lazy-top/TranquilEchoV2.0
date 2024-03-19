from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
router = APIRouter(    
    prefix="/image",
    tags=["image"],
    responses={404: {"message": "Not found"}},
    )
@router.post("/create",summary="根据相关的提示词获取图片流")
def sendImageStream(prompt:str):
    """ 获取图片的流式数据通过提示词 """



    return [{"username": "Rick"}, {"username": "Morty"}]
@router.get('/vr',response_class=HTMLResponse)
async def vr(request: Request, chat_id: str):
    """
    返回聊天UI模板的HTTP响应。

    参数:
    - request: Request对象，表示客户端的HTTP请求。
    - chat_id: 字符串，表示聊天的唯一标识符。

    返回值:
    - HTMLResponse对象，包含聊天界面的HTML内容。
    """
    # 从文件系统中读取并返回静态HTML文件的内容
    return HTMLResponse(open("static/html/vr.html",encoding='utf-8').read())