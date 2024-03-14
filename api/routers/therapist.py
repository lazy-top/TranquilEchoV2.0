from fastapi import APIRouter
from utils import R_error,R_success, check_email, check_phone, check_username,get_db,authenticate_therapist
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
    db=get_db()
    if db.query(Therapist).filter(Therapist.email==therapist.email).first():
        return R_error("邮箱已注册")
    db.query(Therapist).add(therapist)
    db.commit()
    db.refresh(therapist)
    return R_success()  #注册

@router.post("/login")
def login(therapist:Therapist):
    if not check_email(therapist.email) or not therapist.password or not check_username(therapist.username) or not  check_phone(therapist.phone_number):
        return R_error("格式错误")
    authenticate_therapist(get_db,therapist.email,therapist.password)
    return R_success() #登录

@router.post("/me")
def getTherapist(token):
    return R_success()


