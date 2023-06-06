from typing import Any, Dict, List

from chromadb.config import Settings
from langchain.docstore.document import Document
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.vectorstores.base import VectorStore

from .embeddings import get_embeddings
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://a:b@cluster1.example.mongodb.net/?retryWrites=true&w=majority&tls=true"
MONGODB_DATABASE = ""
MONGODB_COLLECTION = ""
 # Connect to the MongoDB server
client = MongoClient(MONGO_URI)
# Get the collection
collection = client[MONGODB_DATABASE][MONGODB_COLLECTION]

def get_vectorstore(config: Dict[str, Any]) -> VectorStore:
    embeddings = get_embeddings(config)
    return MongoDBAtlasVectorSearch(
        collection, embeddings
    )


def get_vectorstore_from_documents(
    config: Dict[str, Any],
    documents: List[Document],
) -> VectorStore:
    embeddings = get_embeddings(config)
    vectorstore = MongoDBAtlasVectorSearch(collection, embeddings)
    vectorstore.add_documents(documents)
    return vectorstore
