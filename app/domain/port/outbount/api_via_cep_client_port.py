from abc import ABC, abstractmethod

class IApiViaCepClientPort(ABC):
    @abstractmethod
    def find_endereco_by_cep(self, cep):
        pass
