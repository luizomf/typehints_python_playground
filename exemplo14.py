#
# Liskov Substitution Principle ou Princípio da substituição de Liskov
#
# Artigo: https://www.otaviomiranda.com.br/2025/liskov-substitution-principle-lsp-solid/
#
# Pré-condições: O subtipo não pode ser mais restritivo que o tipo base.
# Contravariância = C[A] <: C[B]
# Pós-condições: O subtipo não pode entregar menos do que o tipo base prometeu.
# Covariância = C[B] <: C[A]
# Invariantes: O subtipo deve manter todos os invariantes do tipo base.
# Invariância = C[A] != C[B]
#
from utils import sep_print


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> int:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, width: int) -> None:
        super().__init__(width, width)


def use_rectangle(r: Rectangle) -> None:
    print(r.width, r.height, r.area)


if __name__ == "__main__":
    rectangle = Rectangle(20, 10)
    square = Square(10)

    use_rectangle(rectangle)
    use_rectangle(square)

    sep_print()
