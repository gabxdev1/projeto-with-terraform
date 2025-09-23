import uuid

from domain.model.pessoa import Pessoa
from domain.port.inbound.save_pessoa_use_case import ISavePessoaUseCase
from infra.adapter.api_via_cep_client import ApiViaCepClient
from infra.adapter.pessoa_dynamo_repository import PessoaDynamoRepository


class SavePessoaService(ISavePessoaUseCase):
    api_via_cep_client: ApiViaCepClient
    pessoa_dynamo_repository: PessoaDynamoRepository

    def __init__(self, api_via_cep_client, pessoa_dynamo_repository):
        self.api_via_cep_client = api_via_cep_client
        self.pessoa_dynamo_repository = pessoa_dynamo_repository

    def execute(self, nome: str, cep: str, numero: str) -> Pessoa:
        endereco = self.api_via_cep_client.find_endereco_by_cep(cep)

        id = str(uuid.uuid4())
        logradouro = endereco["logradouro"]
        bairro = endereco["bairro"]
        localidade = endereco["localidade"]
        uf = endereco["uf"]
        estado = endereco["estado"]
        regiao = endereco["regiao"]

        pessoaToSave = Pessoa(id, nome, cep, logradouro, bairro, localidade, uf, estado, regiao, numero)

        return self.pessoa_dynamo_repository.save(pessoaToSave)
