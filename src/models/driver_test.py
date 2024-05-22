"""Este módulo define la clase `DriverTest`, que representa una cita para el test de conducción
en el sistema."""


import datetime
from src.models.user import User
from src.models.car import Car


class DriverTest:

    def __init__(self, day: datetime.date = None,
                 hour: datetime.time = None,
                 user: User = None,
                 car: Car = None,
                 number_id: int = None):
        self._day: datetime.date = day
        self._hour: datetime.time = hour
        self._user: User = user
        self._car: Car = car
        self._id: int = number_id

    def get_id(self) -> int:
        return self._id
