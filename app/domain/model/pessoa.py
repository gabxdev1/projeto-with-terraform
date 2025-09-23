from dataclasses import dataclass

@dataclass
class Pessoa:
    id: str
    nome: str
    cep: str
    logradouro: str
    bairro: str
    localidade: str
    uf: str
    estado: str
    regiao: str
    numero: str