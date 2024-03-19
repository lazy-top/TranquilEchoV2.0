
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
import os
from dotenv import load_dotenv

load_dotenv()
qianfan_apikey = os.getenv("QIANFAN_AK")
qianfan_scretkey = os.getenv("QIANFAN_SK")
os.environ["QIANFAN_AK"] = qianfan_apikey
os.environ["QIANFAN_SK"] = qianfan_scretkey
def getqf()->QianfanLLMEndpoint:
    """
    初始化并返回一个千帆LLM终端点。
    
    参数:
    - 无
    
    返回值:
    - QianfanLLMEndpoint: 一个配置为使用ERNIE-Bot-turbo模型，并启用流处理的千帆LLM终端点实例。
    """
    QianfanLLM= QianfanLLMEndpoint(streaming=True,
                                model="ERNIE-Bot-turbo",)
    return QianfanLLM
