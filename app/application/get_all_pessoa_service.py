from domain.port.inbound.get_all_pessoa_use_case import IGetAllPessoaUseCase
from domain.port.outbount.pessoa_repository_port import IPessoaRepositoryPort


class GetAllPessoaService(IGetAllPessoaUseCase):
    pessoa_dynamo_repository: IPessoaRepositoryPort

    def __init__(self, pessoa_dynamo_repository):
        self.pessoa_dynamo_repository = pessoa_dynamo_repository

    def get_all_pessoa(self) -> list[dict[str, str]]:
        return self.pessoa_dynamo_repository.find_all()
