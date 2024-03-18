


from  langchain.document_loaders  import DirectoryLoader,TextLoader
from langchain.text_splitter import  CharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
def read():
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

load_dotenv()
# 设置环境变量或直接在代码中指定OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "你的OpenAI API密钥"
qianfan_apikey = os.getenv("QIANFAN_AK")
qianfan_scretkey = os.getenv("QIANFAN_SK")
# 加载PDF文件并提取文本
def load_pdf_texts(pdf_folder):
    texts = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            pdf_reader = PdfReader(pdf_path)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            texts.append(text)
    return texts

# 处理文本，生成嵌入向量，并构建知识库
def create_pdf_knowledge_base(texts,index_name: str):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    embeddings = QianfanEmbeddingsEndpoint()
    chunks = []
    for text in texts:
        chunks.extend(text_splitter.split_text(text))
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    knowledge_base.save_local(index_name)
    return knowledge_base
def load_pdf_knowledge_base(index_name: str,embeddings):
    knowledge_base=FAISS.load_local(index_name,embeddings)
    return knowledge_base
# 创建代理
def create_agent(knowledge_base):
    llm = getqf()
    agent = initialize_agent(
        tools=[],
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    # 注意：这里需要根据实际情况调整代理的配置和使用
    return agent


