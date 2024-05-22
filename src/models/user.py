"""Este módulo define la clase `Usuario`, que representa un usuario en el sistema."""

class User:

    def __repr__(self) -> str:
        return f"id: {self._id_number}, name: {self._name}, phone_number: {self._phone_number}"

    def __init__(self, name: str = None, phone_number: int = None, number_id: str = None):

        self._name: str = name
        self._phone_number: int = phone_number
        self._id_number: str = number_id

    def get_name(self) -> str:

        return self._name

    def get_id(self) -> str:

        return self._id_number

    def get_number(self) -> str:

        return self._phone_number
