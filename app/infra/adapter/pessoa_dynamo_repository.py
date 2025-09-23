from dataclasses import asdict

import boto3

from domain.model.pessoa import Pessoa
from domain.port.outbount.pessoa_repository_port import IPessoaRepositoryPort

class PessoaDynamoRepository(IPessoaRepositoryPort):

    def __init__(self):
        self.table = boto3.resource('dynamodb').Table("tb_pessoa")

    def save(self, pessoa: Pessoa) -> Pessoa:
        self.table.put_item(Item=asdict(pessoa))

        return pessoa

    def find_all(self) -> list[dict[str, str]]:
        response = self.table.scan()

        return response.get("Items", [])
