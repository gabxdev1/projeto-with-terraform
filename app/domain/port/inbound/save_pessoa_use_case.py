from abc import ABC, abstractmethod

from domain.model.pessoa import Pessoa


class ISavePessoaUseCase(ABC):
    @abstractmethod
    def execute(self, nome: str, cep: str, numero: str) -> Pessoa:
        pass