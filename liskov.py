#
# O princípio da substituição de Liskov
#
#
from utils import cyan_print, green_print, sep_print


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._width: float = width
        self._height: float = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float) -> None:
        self._width = width

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height

    @property
    def area(self) -> float:
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, width: float) -> None:
        self._width: float = width
        super().__init__(self.width, self.width)
        # Mudou o comportamento e uma invariante super

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float) -> None:
        self._width = width
        self._height = width
        # Mudou o comportamento de novo

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height
        self._width = height
        # Mudou o comportamento mais uma vez


def use_rectangle(rectangle: Rectangle) -> None:
    sep_print()
    cyan_print(f"w={rectangle.width}, h={rectangle.height}, a={rectangle.area}")

    new_width = 10
    new_height = 5
    new_area = new_width * new_height

    rectangle.width = new_width
    rectangle.height = new_height

    cyan_print(f"w={rectangle.width}, h={rectangle.height}, a={rectangle.area}")

    assert rectangle.area == new_area, "Deu ruim"

    green_print("✅ TEST PASSED")


if __name__ == "__main__":
    rectangle = Rectangle(20, 20)
    square = Square(20)

    use_rectangle(rectangle)
    use_rectangle(square)

    sep_print()
