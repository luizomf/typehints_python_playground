#
# Tipos mais flexíveis e úteis
#
# Union, Optional, TYPE_CHEKCKING, Sequence, Iterable, Iterator
#
# - TYPE_CHEKCKING - só na tipagem, não em runtime
# - Union - quando você precisa de mais de um tipo
# - Optional - Quando pode ou não existir um valor
# - Sequence - Quando é suprota dunder len e getitem
# - Iterable - Qualquer iterável (que vc usa com for)
# - Iterator - Um iterator que sabe iterar o iterável
#

from collections.abc import Generator


def generator(x: int = 20) -> Generator[int]:
    for i in range(x):
        yield i


generate: Generator[int] = generator(20)
print(list(generate))


def to_str(value):
    print("\nto_str")
    return str(value)


# valor = to_str(123)
# print(valor, type(valor))


def greet(name=None):
    print("\ngreet")
    if name is None:
        return "Olá, visitante"
    return f"Olá, {name}"


# print(greet("Luiz"))
# print(greet())


def show_items(items):
    items_type_name = items.__class__.__name__
    print(f"\nshow_items {items_type_name!r}", end=" ")

    for item in items:
        print(item, end=" ")

    print()


# show_items(["a", "b", "c"])
# show_items(("x", "y"))
# show_items({"z", "w"})
# show_items("xyz")

# generator = (letter for letter in "abcd")
# show_items(generator)


def print_dict(dados):
    print("\nprint_dict")

    for key in dados:
        valor = dados.get(key, "")
        print(key, valor)


pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
}

# print_dict(pessoa)
