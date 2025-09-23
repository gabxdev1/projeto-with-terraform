import json
import logging
from dataclasses import asdict

from domain.port.inbound.get_all_pessoa_use_case import IGetAllPessoaUseCase
from domain.port.inbound.save_pessoa_use_case import ISavePessoaUseCase
from infra.config.container import bootstrap, container

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bootstrap()


def lambda_handler(event, context):
    print(event, context)
    logger.info(f"Received event: {json.dumps(event, indent=2)}")
    logger.info(f"Received context: {context}")

    if event['httpMethod'] == 'GET':
        try:
            response = container.get_instance("get_all_pessoa_service", IGetAllPessoaUseCase).get_all_pessoa()

            return {"statusCode": 200, "body": json.dumps({"data": response}, ensure_ascii=False),
                    "headers": {"Content-Type": "application/json"}}
        except Exception as ex:
            return {"statusCode": 400, "body": json.dumps({"error": str(ex)}, ensure_ascii=False),
                    "headers": {"Content-Type": "application/json"}}

    if event['httpMethod'] == 'POST':
        try:
            body = json.loads(event['body'])

            nome = body.get('nome')
            cep = body.get('cep')
            numero = body.get('numero')

            if not (nome and cep and numero):
                return {"statusCode": 400,
                        "body": json.dumps({"error": "Campos obrigatórios: nome, cep, numero"}, ensure_ascii=False),
                        "headers": {"Content-Type": "application/json"}}

            saved_pessoa = container.get_instance("save_pessoa_service", ISavePessoaUseCase).execute(nome, cep, numero)

            return {"statusCode": 200, "body": json.dumps(asdict(saved_pessoa), ensure_ascii=False),
                    "headers": {"Content-Type": "application/json"}}
        except Exception as ex:
            return {"statusCode": 400, "body": json.dumps({"error": str(ex)}, ensure_ascii=False),
                    "headers": {"Content-Type": "application/json"}}

    return {"statusCode": 400, "body": json.dumps({"error": "Método não suportado"}, ensure_ascii=False),
            "headers": {"Content-Type": "application/json"}}
