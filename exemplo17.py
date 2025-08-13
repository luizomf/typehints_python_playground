#
# TypeVar, parâmetro de tipos e Generics
#
# Usaremos a nova sintaxe definida pela PEP 695 (Python >=3.12)
# https://docs.python.org/3/whatsnew/3.12.html#pep-695-type-parameter-syntax
#
# Definições:
# `class Person[T]: ...` - O `T` significa "type parameter" ou "type variable"
# `Person[str]('John')` - O `str` entre colchete significa "type argument"
#
# Type variable (TypeVar) é um parâmetro de tipo que atua como um símbolo para
# um tipo ainda não conhecido. Seu valor será substituído por um tipo concreto
# durante a verificação estática ou inferência de tipos.
#
# Atualmente podemos usar os colchetes para definir uma TypeVar implicitamente.
# Com isso, não é mais necessário importar TypeVar e/ou Generic para definir um
# genérico parametrizado.
#
# DOC: NÃO MISTURAR A VERSÃO NOVA COM A VERSÃO ANTIGA NOS SEUS TIPOS.
#

from collections.abc import Iterable, Sequence

from utils import cyan_print, sep_print


def filter_by_type[T](items: Iterable[object], type_: type[T]) -> list[T]:
    return [item for item in items if isinstance(item, type_)]


def reverse_in_groups[T](items: Sequence[T], *, group_size: int = 2) -> list[T]:
    # [expressão for externo if opcional for interno if opcional ...]
    return [
        group
        for index in range(0, len(items), group_size)
        for group in reversed(items[index : index + group_size])
    ]


if __name__ == "__main__":
    mixed1 = ["a", "b", 1, 2, 3, {10, 20}]

    sep_print()

    cyan_print(reverse_in_groups(mixed1, group_size=2))

    sep_print()

    strings = filter_by_type(mixed1, str)
    integers = filter_by_type(mixed1, int)

    # cyan_print(strings)
    # cyan_print(integers)

    sep_print()
