from fastapi import APIRouter
router = APIRouter(    
    prefix="/user",
    tags=["user"],
    responses={404: {"message": "Not found"}},
    )
@router.get("/send")
def chat():
    return [{"username": "Rick"}, {"username": "Morty"}]
