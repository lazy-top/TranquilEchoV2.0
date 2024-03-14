from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
import os
from dotenv import load_dotenv
from fastapi import HTTPException
from langchain import hub
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, create_structured_chat_agent
from services.langchain.Tools import Knowledge_search
load_dotenv()

qianfan_apikey = os.getenv("QIANFAN_AK")
qianfan_scretkey = os.getenv("QIANFAN_SK")
os.environ["QIANFAN_AK"] = qianfan_apikey
os.environ["QIANFAN_SK"] = qianfan_scretkey
def getqf()->QianfanLLMEndpoint:
    QianfanLLM= QianfanLLMEndpoint(streaming=True,
                                model="ERNIE-Bot-turbo",)
    return QianfanLLM

if __name__ == "__main__":
    QianfanLLM=getqf()
    # prompt = hub.pull("hwchase17/structured-chat-agent")
    # memory = ConversationBufferMemory(memory_key="chat_history")
    # tools=[
    #     Knowledge_search
    # ]
    # qfModel=getqf()
    # agent = create_structured_chat_agent(qfModel, tools, prompt)
    # agent_executor = AgentExecutor(
    #     agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
    # )


    for chunk in QianfanLLM.stream("你是谁呢？"):
      print(chunk)