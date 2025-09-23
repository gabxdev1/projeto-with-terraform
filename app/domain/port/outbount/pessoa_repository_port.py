from abc import ABC, abstractmethod

class IPessoaRepositoryPort(ABC):
    @abstractmethod
    def save(self, pessoa):
        pass

    @abstractmethod
    def find_all(self):
        pass
