from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004",api_key=api_key)


def create_embeddings():
    documents_path = os.path.join(os.path.dirname(__file__), "documents")
    loader = DirectoryLoader(documents_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    document = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(document)

    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(chunks)

    return vector_store
