# STANDARD IMPORTS
from typing import Any
from decouple import config

# THIRD PART IMPORTS
from loguru import logger

from src.domain.exceptions.exceptions import DataNotInsertedOnDatabase
# PROJECT IMPORTS
from src.infrastructure.mongo_db.infrastructure import MongoDBInfrastructure


class LaptopMongoRepository:
    infra = MongoDBInfrastructure
    database = config("MONGODB_DATABASE_NAME")
    collection = config("MONGODB_COLLECTION")

    @classmethod
    async def __get_collection(cls):
        mongo_client = cls.infra.get_client()
        try:
            database = mongo_client[cls.database]
            collection = database[cls.collection]
            return collection
        except Exception as error:
            message = (
                f"UserRepository::__get_collection::Error when trying to get collection"
            )
            logger.error(
                error=error,
                message=message,
                database=cls.database,
                collection=cls.collection,
            )
            raise error

    @classmethod
    async def save_laptops_on_database(
            cls,
            laptop_database: list
            ):

        collection = await cls.__get_collection()
        was_inserted = await collection.insert_many(
            laptop_database
        )

        if not was_inserted.matched_count == 1:
            raise DataNotInsertedOnDatabase

        return bool(was_inserted)
