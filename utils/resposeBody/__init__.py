from dataclasses import dataclass
@dataclass
class ResponseJson:
    """ResponseJson class"""
    status: int = 200
    message: str = "success"
    data: dict = None
    def response_json_success(status: int = 200, message: str = "success", data: dict = None) -> ResponseJson:
        """response_json function"""
        return ResponseJson(status, message, data)
    def response_json_error(status: int = 400, message: str = "error", data: dict = None) -> ResponseJson:
        """response_json_error function"""
        return ResponseJson(status, message, data)