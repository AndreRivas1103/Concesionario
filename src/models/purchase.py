"""Este módulo define la clase 'pre-compra', que se representa en el sistema."""

from src.models.user import User
from src.models.car import Car

class Purchase:

    TYPES_CAR: tuple[str] = ('Deportivo', 'Camioneta', 'Automovil')
    TYPES_RIM: tuple[str] = ('Deportivos', 'Invierno', 'Sencillos', 'Fibra de Carbono')
    ENGINE_DISPLACEMENT: tuple[int] = (1000, 1500, 2000, 2500, 3000, 3500)
    PAY_METHODS: tuple[str] = ("Cheque", "Efectivo", "Transferencia", "Tarjetas")
    SEDES: tuple[str] = ("Medellín", "Cali", "Bogotá", "Pereira")

    def __init__(self, user: User = None, car: Car = None, pay_method: str = None) -> None:
        self._user: User = user
        self._car: Car = car
        self._payment_method: str = pay_method
