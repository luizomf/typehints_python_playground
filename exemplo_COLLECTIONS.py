#
# Tipos mais flexíveis e úteis
#
# Union, Optional, TYPE_CHEKCKING, Sequence, Iterable, Iterator
#
# - TYPE_CHEKCKING - só na tipagem, não em runtime
# - Union - quando você precisa de mais de um tipo
# - Optional - Quando pode ou não existir um valor
# - Sequence[T] - Quando é suprota dunder len e getitem
# - Iterable[T] - Qualquer iterável (que você usa com for, tem iter)
# - Iterator[T] - Um iterator que sabe iterar o iterável (tem dunder iter e next)
# - Sized - Tem dunder len (len)
# - Container[T] - Tem dunder contains (in e not in)
# - Collection[T] - Tem dunder len, iter e contains
#
# Você pode ver todos em:
# https://docs.python.org/3/library/collections.abc.html
#


def generator(x=20):
    for i in range(x):
        yield i


generate = generator(20)
# print(list(generate))


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
