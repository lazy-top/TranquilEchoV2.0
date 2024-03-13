def R_success(data: dict = None) -> dict:
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