# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 11:19
#聊天功能实现
# @File    : ChatService.py
# @Software: PyCharm


from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_core.callbacks.base import BaseCallbackManager
from langchain.agents import initialize_agent


from Models import QianfanModel

from utils import Knowledge_search
"""
CRISPE Prompt Framework提示词模板:
能力与角色: 请输入你希望大模型扮演怎样的角色。

背景信息: 请输入背景信息和上下文。

指令: 请输入你希望大模型具体执行的任务。

输出风格: 请输入期望大模型生成内容的风格。 例如：我希望你能以详细且专业的方式回答我

输出范围： 请输入期望大模型生成内容的风格。

"""
myStreamHandler=MyChainStreamHandler()
memory = ConversationBufferMemory(memory_key="chat_history")
tools=[
    Knowledge_search
]
qfModel=CreateModel()
xihai = initialize_agent(tools, qfModel, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=False, memory=memory,handle_parsing_errors=True,callback_manager=BaseCallbackManager([myStreamHandler]))
class ChatService:
    def run(content):
     """流式响应"""
     text=xihai(content)
     print(text)
     return myStreamHandler.generate_tokens()
   
        






