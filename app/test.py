class BusinessRuleViolation(Exception):
    def __init__(self, meesage: str):
        super().__init__(meesage)


class ExternalServiceUnavailable(Exception):
    def __init__(self, meesage: str):
        super().__init__(meesage)


class ValidationError(Exception):
    def __init__(self, meesage: str):
        super().__init__(meesage)


class StartSagaUseCase:
    def execute(self):
        raise ValidationError("ValidationError test")



class ErrorPolicyHandler:
    def __init__(self):
        self.policies = {
            BusinessRuleViolation: self._handle_business_error,
            ExternalServiceUnavailable: self._handle_service_error,
            ValidationError: self._handle_validation_error
        }

    def handle(self, ex: Exception):
        handler = self.policies.get(type(ex), self._handle_unknown_error)
        handler(ex)

    def _handle_business_error(self, ex):

        print(f"{ex} - _handle_business_error")

    def _handle_service_error(self, ex):
        print(f"{ex} - _handle_service_error")

    def _handle_validation_error(self, ex):
        print(f"{ex} - _handle_validation_error")

    def _handle_unknown_error(self, ex):
        print(f"{ex} - _handle_unknown_error")


erro_handler = ErrorPolicyHandler()
start = StartSagaUseCase()

def lambda_handler():
    try:
        start.execute()
    except Exception as ex:
        erro_handler.handle(ex)

lambda_handler()
