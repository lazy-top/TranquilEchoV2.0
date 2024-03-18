
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from core.database import SessionLocal
import re
from passlib.context import CryptContext
from requests import Session
from core.models import User
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
import os
import models
from models import Guest
load_dotenv()
def R_success(data: dict|str|object = None) -> dict:
    return {
        "code": 200,
        "msg": "操作成功",
        "data": data,
    }
def R_error(msg: str = "操作失败") -> dict:
    return {
        "code": 400,
        "msg": msg,
        "data": None,
    }

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES =int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    创建访问令牌。
    
    参数:
    - data: 包含令牌信息的字典。
    - expires_delta: 令牌过期时间的偏移量。如果提供，将按此偏移量计算令牌的过期时间；否则，默认为15分钟。

    返回值:
    - 返回编码后的JWT令牌字符串。
    """
    to_encode = data.copy()  # 复制待编码的数据
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta  # 计算自定义过期时间
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # 默认15分钟后过期
    to_encode.update({"exp": expire})  # 添加过期时间到数据中
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # 编码数据为JWT令牌
    return encoded_jwt

def authenticate_user(db: Session, email: str, password: str):
    """
    验证用户登录。
    
    参数:
    - db: 数据库会话实例。
    - email: 用户的电子邮件地址。
    - password: 用户提供的密码。
    
    返回值:
    - 如果验证成功，返回True；否则返回False。
    """
    user = db.query(User).filter(User.email == email).first()  # 根据电子邮件查询用户
    if not user:  # 如果用户不存在，返回False
        return False
    if not verify_password(password, user.hashed_password):  # 验证密码是否匹配
        return False
    return True
def authenticate_therapist(db: Session, email: str, password: str):
    """
    验证咨询师登录。
    
    参数:
    - db: 数据库会话实例。
    - email: 用户的电子邮件地址。
    - password: 用户提供的密码。
    
    返回值:
    - 如果验证成功，返回True；否则返回False。
    """
    therapist = db.query(therapist).filter(User.email == email).first()  # 根据电子邮件查询
    if not therapist:  # 如果用户不存在，返回False
        return False
    if not verify_password(password, therapist.hashed_password):  # 验证密码是否匹配
        return False
    return True

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    异步函数，用于获取当前用户的身份验证信息。
    
    参数:
    - token (str): 依赖于oauth2_scheme的令牌，用于用户身份验证。
    
    返回值:
    - username (str): 验证成功后返回的用户用户名。
    
    抛出:
    - HTTPException: 如果无法验证令牌的有效性，将抛出此异常。
    """
    # 准备用于认证失败时返回的异常信息
    credentials_exception = HTTPException(
        status_code=500,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # 尝试使用JWT解码令牌以获取用户信息
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            # 如果解码后没有找到用户名，抛出认证异常
            raise credentials_exception
        return(username)
    except JWTError:
        # 如果JWT解码过程中出现错误，抛出认证异常
        raise credentials_exception


async def get_current_guest_user(token: str = Depends(oauth2_scheme)) -> Guest:
    
    return Guest(username="admin", email="admin@example.com", admin_code="secret")

async def get_current_admin_user(token: str = Depends(oauth2_scheme)) -> models.User:
  
    return models.User(username="user", email="user@example.com")
def get_db():
    """
    获取数据库会话实例。
    
    使用SessionLocal创建一个数据库会话实例，尝试使用该实例进行操作。
    当操作完成后，无论操作是否成功，都会确保数据库会话被关闭。
    
    返回值:
        db: SessionLocal类型的数据库会话实例，可用于执行数据库操作。
    """
    db = SessionLocal()  # 创建数据库会话实例
    try:
        yield db  # 将数据库会话实例作为生成器的元素返回，供调用者使用
    finally:
        db.close()  # 确保在函数退出时关闭数据库会话


def check_email(email):
    """
    检查邮箱地址是否有效。
    
    参数:
    email: 字符串，待检查的邮箱地址。
    
    返回值:
    布尔值，如果邮箱地址有效返回True，否则返回False。
    """
    # 类型检查
    if not isinstance(email, str):
        return False

    # 使用正则表达式检查邮箱格式
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        return False

    # 所有检查通过，邮箱有效
    return True

def check_username(username):
    """
    检查用户名是否有效。
    
    参数:
    username: 字符串，待检查的用户名。
    
    返回值:
    布尔值，如果用户名有效返回True，否则返回False。
    """
    # 检查用户名是否符合规定格式
    if re.match(r'^[0-9a-zA-Z]{6,16}$', username):
        return True
    else:
        return False
def check_password(password):
    """
    检查密码强度和格式。
    
    参数:
    password: 字符串，待检查的密码。
    
    返回值:
    返回 True 如果密码满足以下条件：
    - 由6到16个数字或字母组成；
    否则返回 False。
    """
    if re.match(r'^[0-9a-zA-Z]{6,16}$', password):
        return True
    else:
        return False

def check_phone(phone):
    """
    检查电话号码格式是否正确。
    
    参数:
    phone: 字符串，待检查的电话号码。
    
    返回值:
    返回 True 如果电话号码满足以下条件：
    - 以1开头，后面跟着3、4、5、7或8，再接着9个数字；
    否则返回 False。
    """
    if re.match(r'^1[34578]\d{9}$', phone):
        return True
    else:
        return False
#身份证格式检查
def check_idcard(idCard):
    if re.match(r'^\d{17}[\dX]$', idCard):
        return True
    else:
        return False