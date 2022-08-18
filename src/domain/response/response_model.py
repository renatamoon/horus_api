# STANDARD IMPORTS
from json import dumps
from flask import Response

# PROJECT IMPORTS
from src.domain.enums.status_code.status_code import InternalCode


class ResponseModel:
    def __init__(
        self, success: bool, code: InternalCode, message: str = None, result: any = None
    ):
        self.success = success
        self.code = code.value
        self.message = message
        self.result = result
        self.response = self.to_dumps()

    def to_dumps(self) -> str:
        response_model = dumps(
            {
                "result": self.result,
                "message": self.message,
                "success": self.success,
                "internal_code": self.code,
            }
        )
        self.response = response_model
        return response_model

    def build_http_response(
        self, status: int, mimetype: str = "application/json"
    ) -> Response:
        http_response = Response(
            self.response,
            mimetype=mimetype,
            status=status,
        )
        return http_response
