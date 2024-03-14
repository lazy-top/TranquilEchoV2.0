
from langchain_community.llms import QianfanLLMEndpoint
import os
from dotenv import load_dotenv
load_dotenv()
qianfan_apikey = os.getenv("QIANFAN_AK")
qianfan_scretkey = os.getenv("QIANFAN_SK")
def QianfanLLMCreateModel():
    os.environ["QIANFAN_AK"] = qianfan_apikey
    os.environ["QIANFAN_SK"] = qianfan_scretkey
    llm = QianfanLLMEndpoint(streaming=True,
                            model="ERNIE-Bot-turbo",
                            


                            )
    return llm
