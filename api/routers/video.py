from fastapi import APIRouter
router = APIRouter(    
    prefix="/video",
    tags=["video"],
    responses={404: {"message": "Not found"}},
    )
@router.get("/get")
def sendVedioStream():
    return [{"username": "Rick"}, {"username": "Morty"}]
