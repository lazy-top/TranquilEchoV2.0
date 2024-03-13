from fastapi import APIRouter
router = APIRouter(    
    prefix="/chat",
    tags=["chat"],
    responses={404: {"message": "Not found"}},
    )
@router.get("/send")
def chat():
    return [{"username": "Rick"}, {"username": "Morty"}]


