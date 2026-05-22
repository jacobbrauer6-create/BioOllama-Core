import abc
class BaseMemory(abc.ABC):
    @abc.abstractmethod
    def retrieve(self, category: str) -> str: pass