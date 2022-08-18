# STANDARD IMPORTS
from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 0
    INVALID_PARAMS = 10
    DATA_NOT_FOUND = 99
    INTERNAL_SERVER_ERROR = 100

    def __repr__(self):
        return self.value
