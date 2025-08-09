#
# Hello World!
#
from dataclasses import dataclass


@dataclass
class Animal:
    name: str


class Dog(Animal): ...


class Pitbull(Dog): ...


class Box[In, Out]:
    def __init__(self) -> None: ...

    def get(self, index: int) -> Out: ...

    def add(self, items: In) -> None: ...


def show_animals[In, Out](animals: Box[In, Out]) -> None:
    print(animals.get(1))
    print(animals.get(2))


if __name__ == "__main__":
    print()

    a1, d1, p1 = Animal("a1"), Dog("d1"), Pitbull("p1")
    box_of_animals = Box[int, Animal]()
    box_of_dogs = Box[Animal, int]()

    show_animals(box_of_animals)
    show_animals(box_of_dogs)

    print()
