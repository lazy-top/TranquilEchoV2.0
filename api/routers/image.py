from fastapi import APIRouter
router = APIRouter(    
    prefix="/image",
    tags=["image"],
    responses={404: {"message": "Not found"}},
    )
@router.post("/get")
def sendImageStream():
    return [{"username": "Rick"}, {"username": "Morty"}]
