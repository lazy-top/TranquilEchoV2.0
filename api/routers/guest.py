from fastapi import APIRouter
from models import Guest
from utils import R_success,R_error, create_access_token
router = APIRouter(    
    prefix="/guest",
    tags=["guest"],
    responses={404: {"message": "Not found"}},
    )
#实现游客登录获取token的功能
@router.post("/login")
def login(guest:Guest):
    """游客登录获取token"""
    if(not guest.guest_bool):
        return R_error()
    token =create_access_token(data={"sub": 'guest'})
    return R_success("Bear  {}".format(token))
