
class Color:


    def __init__(self, r: int, g: int, b: int):

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("Valores RGB invalidos. Coloca valores entre 0 y 255.")

        self._r = r
        self._g = g
        self._b = b

    def __str__(self) -> str:
        return f"{self._r}, {self._g}, {self._b}"

    @staticmethod
    def from_string(color_str: str):
        r, g, b = map(int, color_str.split(','))
        return Color(r, g, b)
