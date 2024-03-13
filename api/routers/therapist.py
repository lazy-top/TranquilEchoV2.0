from fastapi import APIRouter
from utils import R_error,R_success, check_email, check_phone, check_username
from models import Therapist
router = APIRouter(    
    prefix="/therapist",
    tags=["therapist"],
    responses={404: {"message": "Not found"}},
    )
@router.post("/register")
def register(therapist:Therapist):
    if not check_email(therapist.email) or not therapist.password or not check_username(therapist.username) or not  check_phone(therapist.phone_number):
        return R_error("格式错误")
    return R_success()  #注册

@router.post("/login")
def login(therapist:Therapist):



    return R_success() #登录


