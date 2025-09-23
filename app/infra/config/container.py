import logging
from typing import Any, TypeVar, cast

logger = logging.getLogger()
logger.setLevel(logging.INFO)

T = TypeVar("T")


class Container:
    def __init__(self):
        self._instances: dict[str, Any] = {}

    def register_instance(self, name: str, instance: Any) -> None:
        self._instances[name] = instance

    def get_instance(self, name: str, type_: type[T]) -> T:
        return cast(T, self._instances[name])

container = Container()

def bootstrap() -> Container:
    from application.get_all_pessoa_service import GetAllPessoaService
    from application.save_pessoa_service import SavePessoaService
    from infra.adapter.api_via_cep_client import ApiViaCepClient
    from infra.adapter.pessoa_dynamo_repository import PessoaDynamoRepository

    logger.info("Bootstrapping...")

    api_via_cep_client = ApiViaCepClient()
    pessoa_dynamo_repository = PessoaDynamoRepository()
    save_pessoa_service = SavePessoaService(api_via_cep_client, pessoa_dynamo_repository)
    get_all_pessoa_service = GetAllPessoaService(pessoa_dynamo_repository)

    container.register_instance("api_via_cep_client", api_via_cep_client)
    container.register_instance("pessoa_dynamo_repository", pessoa_dynamo_repository)
    container.register_instance("save_pessoa_service", save_pessoa_service)
    container.register_instance("get_all_pessoa_service", get_all_pessoa_service)

    logger.info("Todos os beans foram carregados")

    return container
