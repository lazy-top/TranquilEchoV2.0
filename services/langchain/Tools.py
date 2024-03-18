from langchain.agents import tool
@tool
def Knowledge_search(query: str) -> str:
    """一个帮助用户搜索关于心理知识的工具，并且能处理以下情况：
    1. 用户输入了关于心理学的相关概念，返回对应的知识
    2. 用户输入了心理学的关键词，返回对应的知识
    """
    try:
        # 对输入进行简单的清理和标准化
        query = query.strip().lower()

        # 模拟从知识库中搜索的过程
        # 注意：在实际应用中，这里可能会是数据库查询或网络请求
        # 为了演示，这里使用一个静态的知识返回
        knowledge = "这是关于 {} 的心理学知识".format(query)

        return knowledge

    except Exception as e:
        # 异常处理：记录错误并返回一个友好的错误信息
        return "很抱歉，搜索过程中发生了一些错误，请稍后再试。"
@tool
def GetDanger(query: str) -> str:
    """这个是一个工具用于分析用户输入内容是否包含严重心理状况的内容."""
    return f"Results for query {query}"


# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 11:19
# 网页搜索工具
# @File    : WebSearch.py
# @Software: PyCharm

from langchain.agents import tool
from langchain.chains.llm_requests import LLMRequestsChain
import urllib.parse

# 定义搜索引擎的基URL作为常量
SEARCH_URL = 'https://cn.bing.com/search?q='

@tool
def web_search(query: str) -> str:
    """一个帮助用户搜索最近的状况或者相关知识的web搜索工具."""
    # 对查询字符串进行编码，防止URL注入
    encoded_query = urllib.parse.quote(query)
    # 使用编码后的查询构建搜索URL
    search_url = f'{SEARCH_URL}{encoded_query}'
    
    try:
        # 使用LLMRequestsChain进行搜索
        result = LLMRequestsChain(llm_chain=getqf(), input_key=search_url)
    except Exception as e:
        # 在发生异常时处理，例如可以返回一个错误消息或记录日志
        # 此处为示例，具体实现应根据实际需求决定
        print(f"An error occurred during the web search: {e}")
        result = "Search failed due to an error."

    return result