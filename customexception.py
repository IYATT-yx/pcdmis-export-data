import logging

class CustomException(Exception):
    WARNING: int = logging.WARNING
    ERROR: int = logging.ERROR
    CRITICAL: int = logging.CRITICAL

    def __init__(self, message: str, type: int):
        self.message = message
        super().__init__(self.message)
        self.typeValue = type

    def type(self) -> int:
        return self.typeValue