#This file is used to initialize the Pinecone vector store and load the PDF file and run the functions created in the helper.py file.

#Initializing the Pinecone vector store
from dotenv import load_dotenv
from pinecone.grpc import PineconeGRPC as Pinecone
import os
from src.helper import load_pdf, split_text, download_huggingface_model
from langchain_pinecone import PineconeVectorStore

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

exctracted_data = load_pdf('data/')
text_chunks = split_text(exctracted_data)
embeddings = download_huggingface_model()


index_name = "doctorbot"

pc = Pinecone(PINECONE_API_KEY)
index = pc.Index(index_name)

# Create the Pinecone vector store index if its not already created
# docsearch = PineconeVectorStore.from_documents(
#     documents=text_chunks,
#     embedding=embeddings,
#     index_name=index_name,
# )

