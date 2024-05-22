"""Este módulo define la clase `Car`, que representa un automóvil en el sistema.
La clase "Car" almacena información sobre un automóvil."""

from dataclasses import dataclass
from typing import Optional

from src.utils.color import Color

@dataclass
class Car:

    _type: Optional[str] = None
    _rim: Optional[str] = None
    _engine_displacement: Optional[int] = None
    _color: Optional[Color] = None

    def get_type(self) -> str:
        return self._type

    def get_rim(self) -> str:
        return self._rim

    def get_internal_color(self) -> Color:
        return self._color

    def get_engine_displacement(self) -> str:
        return self._engine_displacement
    
