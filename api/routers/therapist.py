from fastapi import APIRouter
router = APIRouter(    
    prefix="/therapist",
    tags=["therapist"],
    responses={404: {"message": "Not found"}},
    )
@router.get("/send")
def therapist():
    return [{"username": "Rick"}, {"username": "Morty"}]
