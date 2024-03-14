
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
import os
from dotenv import load_dotenv

load_dotenv()
qianfan_apikey = os.getenv("QIANFAN_AK")
qianfan_scretkey = os.getenv("QIANFAN_SK")
os.environ["QIANFAN_AK"] = qianfan_apikey
os.environ["QIANFAN_SK"] = qianfan_scretkey
def getqf()->QianfanLLMEndpoint:
    QianfanLLM= QianfanLLMEndpoint(streaming=True,
                                model="ERNIE-Bot-turbo",)
    return QianfanLLM

