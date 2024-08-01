from typing import List
from abc import ABC, abstractmethod

from src.entity.models import History


class AnswerGenerator(ABC):
    @abstractmethod
    def invoke(
        self,
        documents: List[str],
        page_content: str,
        history: History,
        query: str,
    ) -> str:
        pass
