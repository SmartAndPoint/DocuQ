from typing import List
from pydantic import BaseModel, Field


# Query request and answer


class Answer(BaseModel):
    text: str = Field(..., description="Text content of the answer")
    query: str = Field(..., description="Query that generated the answer")


class History(BaseModel):
    history: List[Answer] = Field(..., description="List of answers")


class Request(History):
    content: str = Field(..., description="Text content of the page")
    query: str = Field(..., description="Query to generate the answer")


class Response(Answer):
    pass
    # answer: Answer = Field(..., description="Answer generated")
    # query: str = Field(..., description="Query that generated the answer")


# Documents processing


class Document(BaseModel):
    name: str = Field(..., description="Name of the document")
    text: str = Field(..., description="Text content of the document")


class Documents(BaseModel):
    documents: List[Document]
