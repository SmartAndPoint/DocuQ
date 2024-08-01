from typing import List
from abc import ABC, abstractmethod


class Embedder(ABC):
    @abstractmethod
    def invoke(self) -> List[float]:
        pass
