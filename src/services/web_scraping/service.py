# STANDARD IMPORTS
import random as rd

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import SyncPlaywrightError
from src.transport.playwright.transport import GetScrapFromWebsite


class GetLaptopsService:

    @classmethod
    def __get_laptops_dictionary(
            cls, laptops: list
    ) -> list:

        laptops_list = [

        ]

        for laptop in laptops:
            brand = laptop[0:6]
            description = laptop[7:-1]

            laptop_dict = {
                'laptop_id': rd.randrange(5, 100),
                'brand': brand,
                'description': description
            }

            laptops_list.append(laptop_dict)

        return laptops_list

    @classmethod
    async def get_laptops(cls) -> list:

        laptops = await GetScrapFromWebsite.get_laptops_from_website()

        if not laptops:
            raise SyncPlaywrightError

        laptops_list = cls.__get_laptops_dictionary(
            laptops=laptops
        )

        return laptops_list
