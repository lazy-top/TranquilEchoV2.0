# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 11:19
#聊天功能实现
# @File    : ChatService.py
# @Software: PyCharm

# import asyncio
from fastapi import HTTPException
from langchain import hub
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, create_structured_chat_agent
from services.langchain.Models import getqf
from services.langchain.Tools import Knowledge_search
"""
CRISPE Prompt Framework提示词模板:
能力与角色: 请输入你希望大模型扮演怎样的角色。

背景信息: 请输入背景信息和上下文。

指令: 请输入你希望大模型具体执行的任务。

输出风格: 请输入期望大模型生成内容的风格。 例如：我希望你能以详细且专业的方式回答我

输出范围： 请输入期望大模型生成内容的风格。

"""
prompt = hub.pull("hwchase17/structured-chat-agent")
memory = ConversationBufferMemory(memory_key="chat_history")
tools=[
    Knowledge_search
]
qfModel=getqf()
agent = create_structured_chat_agent(qfModel, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

async def run(content:str):
    for event in agent_executor.astream_events(
        {"input": content},
        version="v1",
    ):
        kind = event["event"]
        if kind == "on_chain_start":
            if (
                event["name"] == "Agent"
            ):  # Was assigned when creating the agent with `.with_config({"run_name": "Agent"})`
                print(
                    f"Starting agent: {event['name']} with input: {event['data'].get('input')}"
                )
        elif kind == "on_chain_end":
            if (
                event["name"] == "Agent"
            ):  # Was assigned when creating the agent with `.with_config({"run_name": "Agent"})`
                print()
                print("--")
                print(
                    f"Done agent: {event['name']} with output: {event['data'].get('output')['output']}"
                )
        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                # Empty content in the context of OpenAI means
                # that the model is asking for a tool to be invoked.
                # So we only print non-empty content
                yield f"data: {content}".encode()
        elif kind == "on_tool_start":
            print("--")
            print(
                f"Starting tool: {event['name']} with inputs: {event['data'].get('input')}"
            )
        elif kind == "on_tool_end":
            print(f"Done tool: {event['name']}")
            print(f"Tool output was: {event['data'].get('output')}")
            print("--")
        


# return None
# async def run(content: str):
#      """流式响应"""
 
#      return agent_executor.iter(content)

# # 定义一个异步回调处理器
# class AsyncCallbackHandler(AsyncIteratorCallbackHandler):
#     content: str = ""
#     final_answer: bool = False

#     async def on_llm_new_token(self, token: str, **kwargs) -> None:
#         self.content += token
#         if self.final_answer:
#             self.queue.put_nowait(token)
#         elif ";" in self.content:
#             self.final_answer = True
#             self.content = ""

#     async def on_llm_end(self, response, **kwargs) -> None:
#         if self.final_answer:
#             self.content = ""
#             self.final_answer = False
#             self.done.set()
#         else:
#             self.content = ""

# # 初始化LangChain agent
# AGENT = agent_executor # 初始化您的LangChain agent
# AGENT.callbacks = AsyncCallbackHandler()
# # 定义一个生成器函数，用于创建流式响应
# async def create_gen(history, stream_it: AsyncCallbackHandler):
#     task = asyncio.create_task(AGENT.acall(history))
#     async for token in stream_it.aiter():
#         yield token
#     await task


   
        






