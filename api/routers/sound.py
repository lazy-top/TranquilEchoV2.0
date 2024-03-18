import io
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from services.soundModel.fastSay import fast_say
router = APIRouter(    
    prefix="/audio",
    tags=["audio"],
    responses={404: {"message": "Not found"}},
    )
@router.get("/stream_fast_audio", summary="快速生成语音功能。")
#获取所要说的内容
async def stream_fast_audio(text:str):
    filename=fast_say(text)
    # 读取音频文件
    with open(filename, "rb") as audio_file:
        audio_data = audio_file.read()
    
    # 将音频数据流式传输到客户端
    return StreamingResponse(io.BytesIO(audio_data), media_type="audio/mp3")

@router.get("/stream_real_audio", summary="生成真实语音功能。")
async def stream_real_audio(text:str):
    filename=fast_say(text)
    # 读取音频文件
    with open(filename, "rb") as audio_file:
        audio_data = audio_file.read()
    
    # 将音频数据流式传输到客户端
    return StreamingResponse(io.BytesIO(audio_data), media_type="audio/mp3")