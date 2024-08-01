from typing import List
from langchain_openai import OpenAIEmbeddings

from src.config.config import Config

class Embeddings:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.model_name = "text-embedding-3-small"
        self.embeddings = OpenAIEmbeddings(
            model=self.model_name,
            api_key=self.cfg.OPENAI_KEY # type: ignore
        )
        
    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        return self.embeddings.embed_documents(documents)
    
    def embed_query(self, query: str) -> List[float]:
        return self.embeddings.embed_query(query)
