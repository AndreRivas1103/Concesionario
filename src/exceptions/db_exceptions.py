

from src.exceptions.base_exception import BaseAppException

class DatabaseException(BaseAppException):
    pass

class PhoneNumberRepeated(DatabaseException):
    pass

class NoFoundPhoneNumber(DatabaseException):
    pass

class NoFoundUser(DatabaseException):
    pass