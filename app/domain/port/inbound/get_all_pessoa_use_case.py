from abc import ABC, abstractmethod

class IGetAllPessoaUseCase(ABC):
    @abstractmethod
    def get_all_pessoa(self) -> list[dict[str, str]]:
        pass