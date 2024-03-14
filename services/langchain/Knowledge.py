


from  langchain.document_loaders  import DirectoryLoader,TextLoader
from langchain.text_splitter import  CharacterTextSplitter
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

