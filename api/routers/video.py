from fastapi import APIRouter
router = APIRouter(    
    prefix="/video",
    tags=["video"],
    responses={404: {"message": "Not found"}},
    )
@router.get("/send")
def chat():
    return [{"username": "Rick"}, {"username": "Morty"}]
