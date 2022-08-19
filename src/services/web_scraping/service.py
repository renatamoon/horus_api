# PROJECT IMPORTS
from src.transport.playwright.transport import GetScrapFromWebsite


class GetLaptopsService:

    @classmethod
    def get_laptops(cls):

        laptops = GetScrapFromWebsite.get_laptops_from_website()

        database_laptops = [

        ]

        for laptop in laptops:
            brand = laptop[0:6]
            description = laptop[7:-1]

            laptop_dict = {
                'brand': brand,
                'description': description
            }

            database_laptops.append(laptop_dict)

        return database_laptops
