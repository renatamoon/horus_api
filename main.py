# STANDARD IMPORTS
from http import HTTPStatus
from flask import Flask, Response
from loguru import logger

# PROJECT IMPORTS
from src.domain.response.response_model import ResponseModel
from src.domain.enums.status_code.status_code import InternalCode


app = Flask("Horus API")


@app.route("/get_all_laptops")
def get_all_laptops() -> Response:

    result = 0

    try:
        response = ResponseModel(
            success=True,
            result=result,
            code=InternalCode.SUCCESS
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except ValueError as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="Value Error cause by a random reason",
            code=InternalCode.INVALID_PARAMS,
        ).build_http_response(status=HTTPStatus.BAD_REQUEST)
        return response

    except Exception as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="UNEXPECTED ERROR",
            code=InternalCode.INTERNAL_SERVER_ERROR,
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response
