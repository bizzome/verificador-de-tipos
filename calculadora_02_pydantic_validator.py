from pydantic import validate_call

class PydanticValidator:
    @validate_call
    def soma(self, num1: int, num2: int) -> int:
        return num1 + num2