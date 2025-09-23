import requests

from domain.port.outbount.api_via_cep_client_port import IApiViaCepClientPort


class ApiViaCepClient(IApiViaCepClientPort):
    def find_endereco_by_cep(self, cep):
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        if response.status_code == 400:
            raise ValueError("CEP inválido")

        data = response.json()

        if "erro" in data:
            raise ValueError("CEP inválido")

        return data
