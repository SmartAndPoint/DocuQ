import asyncio
from typing import AsyncGenerator, Dict, Any
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from src.entity.models import Documents, Request, Response


class DocuQ:
    def __init__(self) -> None:
        self.app = FastAPI()
        self.app.post("/generate")(self.generate)
        self.app.post("/documents", response_model=Response)(self.processing_documents)

    async def generate(self, input_data: Request) -> StreamingResponse:
        stream = stub_stream(input_data.content)
        return StreamingResponse(stream, media_type="text/event-stream")

    async def processing_documents(self, documents: Documents) -> Dict[str, str]:
        return {"message": "Documents received"}


async def stub_stream(text) -> AsyncGenerator[str, Any]:
    words = text.split()
    for word in words:
        await asyncio.sleep(0.2)  # Simulating a delay
        yield f"{word} "
