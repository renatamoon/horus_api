# STANDARD IMPORTS
from http import HTTPStatus
from aioflask import Flask
from flask import Response
from loguru import logger

# PROJECT IMPORTS
from src.domain.response.response_model import ResponseModel
from src.domain.enums.status_code.status_code import InternalCode
from src.repositories.laptop_repository.repository import LaptopMongoRepository
from src.services.web_scraping.service import GetLaptopsService
from src.domain.exceptions.exceptions import (
    DataNotInsertedOnDatabase,
    NoDataWasFoundOnDatabase,
    SyncPlaywrightError
)


app = Flask("Horus API")


@app.route("/put/save_laptops")
async def insert_laptops_on_database() -> Response:
    try:
        laptops = await GetLaptopsService.get_laptops()
        response = LaptopMongoRepository.save_laptops_on_database(
            laptops=laptops
        )

        response = ResponseModel(
            success=True,
            message="DATA WAS DULLY INSERTED ON DATABASE",
            result=response,
            code=InternalCode.SUCCESS
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except SyncPlaywrightError as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="ERROR WHEN TRYING TO SCRAP DATA FROM WEBSITE",
            code=InternalCode.PLAYWRIGHT_ERROR,
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except DataNotInsertedOnDatabase as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="DATA NOT INSERTED ON DATABASE",
            code=InternalCode.DATA_NOT_INSERTED_ON_DATABASE,
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except ValueError as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="VALUE ERROR CAUSED BY A RANDOM REASON",
            code=InternalCode.VALUE_ERROR,
        ).build_http_response(status=HTTPStatus.BAD_REQUEST)
        return response

    except Exception as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="AN UNEXPECTED ERROR HAS OCCURRED",
            code=InternalCode.INTERNAL_SERVER_ERROR,
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response


@app.route("/get_all_laptops")
async def get_all_laptops() -> Response:

    try:
        laptops_response = LaptopMongoRepository.find_laptops_on_database()

        response = ResponseModel(
            success=True,
            result=laptops_response,
            code=InternalCode.SUCCESS
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except NoDataWasFoundOnDatabase as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="VALUE ERROR CAUSED BY A RANDOM REASON",
            code=InternalCode.DATA_NOT_FOUND,
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except ValueError as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="VALUE ERROR CAUSED BY A RANDOM REASON",
            code=InternalCode.VALUE_ERROR,
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
