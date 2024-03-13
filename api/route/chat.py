from api import app
from utils.resposeBody import ResponseJson
@app.get("/chat",response_model=ResponseJson)
def chat():
    return ResponseJson.response_json_success()