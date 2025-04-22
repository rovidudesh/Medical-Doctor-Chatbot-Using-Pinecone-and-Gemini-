from langchain.document_loaders import PyPDFLoader , DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

#Exracting Data from the PDF File
def load_pdf(file_path):
    loader = DirectoryLoader(file_path ,
                             glob="**/*.pdf",
                             loader_cls=PyPDFLoader)
    data = loader.load()
    return data

#Splitting the text into chunks
def split_text(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(data)
    return text_chunks

#downloading the huggingface model for embeddings
def download_huggingface_model():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",)
    return embeddings

