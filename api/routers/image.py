from fastapi import APIRouter
router = APIRouter(    
    prefix="/image",
    tags=["image"],
    responses={404: {"message": "Not found"}},
    )
@router.post("/create",summary="根据相关的提示词获取图片流")
def sendImageStream(prompt:str):
    """ 获取图片的流式数据通过提示词 """



    return [{"username": "Rick"}, {"username": "Morty"}]
