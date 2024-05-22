

class BaseAppException(Exception):

    def __init__(self, message: str = "", code: int = 0):
        super().__init__(message)
        self._message: str = message
        self._code: int = code

    def get_message(self) -> str:
        return self._message

    def get_code(self) -> int:
        return self._code