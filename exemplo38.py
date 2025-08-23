from collections.abc import Sequence
from typing import TypeIs

from utils import cyan_print, sep_print

################################################################################
#
# TypeIs e TypeGuard - Precisamos de Guarda-costas?
#
# Obs.: a PEP 724 menciona que devemos usar mais `TypeIs` em nosso dia a dia,
# mas usar `TypeGuard` e ocasiões específicas. Isso por que ambas são para fazer
# quase a mesma coisa.
#
# `TypeIs` é um tipo usado para Type Narrowing. Criamos uma função que recebe
# pelo menos um argumento e retorna `bool`. O Type Hint de retorno da função
# fica como `TypeIs[T]` (onde T é o tipo afunilado). Se a função retorna `True`,
# o tipo é afunilado para `T`. Se retornar `False`, o tipo é o mesmo do primeiro
# argumento.
# A função pode receber mais argumentos, porém o primeiro é onde estamos
# trabalhando o tipo.
# Na prática, `TypeIs[T]` deve ser consistente com `isinstance()`.
#
################################################################################


def is_str(value: object) -> TypeIs[str]:
    return isinstance(value, str)


def is_number(value: object) -> TypeIs[float | int]:
    return isinstance(value, float | int)


################################################################################


def make_str_upper(values: Sequence[object]) -> list[str]:
    values_str: list[str] = []
    for value in values:
        if not is_str(value):
            continue
        value.upper()
        values_str.append(value.upper())
    return values_str


def filter_numbers(values: Sequence[object]) -> list[float]:
    new_values: list[float] = []
    for value in values:
        if not is_number(value):
            continue
        new_values.append(value)
    return new_values


################################################################################


if __name__ == "__main__":
    sep_print()

    mixed = [1, "a", 2, 3, "b", 1.5, 4j + 1, "c", True]

    mixed_upper = make_str_upper(mixed)
    cyan_print(f"{mixed=}")
    cyan_print(f"{mixed_upper=}")
    sep_print()

    mixed_upper = filter_numbers(mixed)
    cyan_print(f"{mixed=}")
    cyan_print(f"{mixed_upper=}")
    sep_print()

################################################################################
