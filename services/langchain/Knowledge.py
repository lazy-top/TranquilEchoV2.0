
from  langchain.document_loaders  import DirectoryLoader,TextLoader,WebBaseLoader
from langchain.text_splitter import  CharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
def split_text():
    """ 
加载目录中的文本文件，并将每个文本分割成小块。
使用DirectoryLoader从指定目录加载所有txt文件，然后使用CharacterTextSplitter将文本分割为指定大小的块。
"""
    loader = DirectoryLoader(
        path="./Knowledge/resources/txt",
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        sample_size=100,
        show_progress=True,
        randomize_sample=True,
        sample_seed=42,
    )
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=100,chunk_overlap=0)
    split_documents = text_splitter.split_documents(documents)

import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.baidu_qianfan_endpoint import QianfanEmbeddingsEndpoint
from langchain.vectorstores import FAISS
from langchain.agents import AgentType, initialize_agent,create_vectorstore_agent
from dotenv import load_dotenv
from services.langchain.Models import getqf

# 加载环境变量配置
load_dotenv()

# 从环境变量中获取千帆API的密钥
qianfan_apikey = os.getenv("QIANFAN_AK")
qianfan_scretkey = os.getenv("QIANFAN_SK")

# 加载指定文件夹中的PDF文件，并提取其中的文本内容
# @param pdf_folder: 存储PDF文件的文件夹路径
# @return: 包含所有PDF文本内容的列表
def load_pdf_texts(pdf_folder):
    texts = []
    # 遍历文件夹中的所有文件
    for filename in os.listdir(pdf_folder):
        # 仅处理以.pdf为后缀的文件
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)  # 拼接完整路径
            pdf_reader = PdfReader(pdf_path)  # 初始化PDF阅读器
            text = ""
            # 提取每页的文本内容，并合并为文档的完整文本
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            texts.append(text)  # 将提取的文本添加到列表中
    return texts

# 处理文本，生成嵌入向量，并构建知识库
def create_pdf_knowledge_base(texts,index_name: str):
    """
    从一系列文本创建一个PDF知识库。
    
    参数:
    - texts: 一个包含多个文本的列表，这些文本将被用来创建知识库。
    - index_name: 字符串，表示知识库的索引名称，用于保存和加载知识库。
    
    返回值:
    - knowledge_base: 创建的知识库对象。
    """
    # 初始化文本分割器和嵌入模型
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    embeddings = QianfanEmbeddingsEndpoint()
    
    chunks = []  # 用于存储分割后的文本块
    for text in texts:
        chunks.extend(text_splitter.split_text(text))  # 分割文本并收集块
    
    # 使用文本块和嵌入模型创建知识库
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    
    # 本地保存知识库
    knowledge_base.save_local(index_name)
    
    return knowledge_base

def load_pdf_knowledge_base(index_name: str,embeddings):
    """
    加载一个已经保存的PDF知识库。
    
    参数:
    - index_name: 字符串，知识库的索引名称，用于加载知识库。
    - embeddings: 嵌入模型，与知识库创建时使用的模型一致。
    
    返回值:
    - knowledge_base: 加载的知识库对象。
    """
    # 从本地加载知识库
    knowledge_base=FAISS.load_local(index_name,embeddings)
    
    return knowledge_base
# 创建代理
def create_agent(knowledge_base):
    """
    创建一个基于知识库的代理。

    参数:
    - knowledge_base: 知识库，代理将利用这个知识库进行问题解答和决策。

    返回值:
    - agent: 初始化后的代理对象，准备用于进行对话或任务执行。
    """
    llm = getqf()  # 获取语言模型
    agent = initialize_agent(
        tools=[],
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # 设定代理类型为零样本反应描述
        verbose=True  # 设定为详细模式，以便观察代理的初始化过程
    )
    # 注意：这里需要根据实际情况调整代理的配置和使用
    return agent

def load_web_url(url):
    """
    加载并处理指定网页的URL。

    参数:
    - url: 要加载的网页的URL地址。

    返回值:
    - all_splits: 网页内容被分割成的多个片段列表，每个片段适合进一步处理。
    """
    loader = WebBaseLoader(url)  # 创建网页加载器
    data = loader.load()  # 加载网页数据

    # 创建文本分割器，用于将网页内容分割成合适的片段
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 384, chunk_overlap = 0, separators=["\n\n", "\n", " ", "", "。", "，"])
    all_splits = text_splitter.split_documents(data)  # 实际执行分割