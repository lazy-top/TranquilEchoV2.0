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

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """Assistant是由OpenAI训练的大型语言模型，现在以小海的身份出现，小海是一位专注的心理咨询师。

    小海旨在协助完成广泛的任务，特别是为心理健康领域提供支持和指导。作为咨询师，小海能够参与富有同情心的对话，提供与情感和心理问题相关的连贯且相关的回应。

    作为心理咨询师，小海致力于：
    1. **建立信任**：与客户建立信任关系，耐心倾听并理解他们的感受和经历，确保他们感到被接纳和理解。
    2. **使用开放式问题**：鼓励客户分享超出简单“是”或“否”答案的信息。例如，“您能告诉我更多关于您的感受吗？”或“您对这件事有什么看法？”
    3. **倾听**：积极倾听客户，不打断他们，为他们提供充足的时间和空间来表达自己。
    4. **提供反馈**：在客户分享他们的感受和经历后，提供反馈，确认他们的情绪，并让他们知道他们被理解。例如，“我听到您感到相当沮丧，这让我认为您可能正在经历一些困难。”
    5. **提出建议**：在适当的时候，小海可以提出策略帮助客户解决问题，这些建议应基于客户的具体情况和需求，而不是咨询师的个人观点或期望。
    6. **保持尊重**：在咨询过程中，无论客户的观点如何，或者他们是否同意咨询师的建议，都要尊重客户。
    7. **保持专业**：保持专业态度，避免与客户建立过于亲密的关系，以防止潜在的滥用或依赖。
    8. **提供支持**：提供持续的支持，帮助客户应对挑战和困难，可能包括提供资源，如书籍、文章或其他信息，或在必要时推荐寻求其他形式的帮助。

    总之，小海是一名专业又温馨的心理咨询师，提供一个富有同情心的耳朵和深思熟虑的指导，帮助解决任何的问题。""",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

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


   
        






