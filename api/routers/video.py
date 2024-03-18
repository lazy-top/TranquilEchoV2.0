from typing import List
from fastapi import APIRouter
router = APIRouter(    
    prefix="/video",
    tags=["video"],
    responses={404: {"message": "Not found"}},
    )
@router.post("/create",summary="根据提示词生成相关的视频流")
def send_video_stream() -> List[dict]:
    return [{"username": "Rick"}, {"username": "Morty"}]
