#
# O princípio da substituição de Liskov
#


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width: int = width
        self._height: int = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self._width = width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = height

    @property
    def area(self) -> int:
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, width: int) -> None:
        super().__init__(width, width)

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self._width = width
        self._height = width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = height
        self._width = height


def use_rectangle(r: Rectangle) -> None:
    new_width = 20
    new_heigh = 40
    new_area = new_width * new_heigh

    r.width = new_width
    r.height = new_heigh

    assert r.area == new_area, "Por algum motivo, a área tá errada"

    print("\n✅ TEST PASSED \n")


if __name__ == "__main__":
    r = Rectangle(10, 5)
    s = Square(10)

    use_rectangle(r)
    use_rectangle(s)
