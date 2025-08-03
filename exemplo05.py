#
# Tipos mais flexíveis e úteis
#
# Union, Optional, TYPE_CHEKCKING, Sequence, MutableSequence, Iterable, Mapping,
# MutableMapping
#


from collections.abc import Iterable


def to_str(value: str | int) -> str:
    print("\nto_str")
    return str(value)


valor = to_str(123)
print(valor, type(valor))


def greet(name: str | None = None) -> str:
    print("\ngreet")
    if name is None:
        return "Olá, visitante"
    return f"Olá, {name}"


print(greet("Luiz"))
print(greet())


def show_items(items: Iterable[str]) -> None:
    items_type_name = items.__class__.__name__
    print(f"\nshow_items {items_type_name!r}", end=" ")

    for item in items:
        print(item, end=" ")

    print()


show_items(["a", "b", "c"])
show_items(("x", "y"))
show_items({"z", "w"})
show_items("xyz")

generator = (letter for letter in "abcd")
show_items(generator)


def print_dict(dados: dict[str, str]) -> None:
    print("\nprint_dict")

    for key in dados:
        valor = dados.get(key, "")
        print(key, valor)


pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
}

print_dict(pessoa)
