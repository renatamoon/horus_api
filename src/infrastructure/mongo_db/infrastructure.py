# THIRD PART IMPORTS
from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBInfrastructure:

    client = None

    @classmethod
    def get_client(cls):
        if cls.client is None:
            url = config("MONGO_CONNECTION_URL")
            cls.client = AsyncIOMotorClient(url)
        return cls.client
