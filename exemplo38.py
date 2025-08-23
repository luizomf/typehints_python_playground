from collections.abc import Mapping
from typing import Any, TypedDict, TypeGuard

from utils import cyan_print, sep_print

################################################################################
#
# TypeIs e TypeGuard - Precisamos de Guarda-costas?
#
# Obs.: PEPs 484/742
#
# No TypeScript, funções que fazem Type Guard, são chamadas de "Type Predicate"
# (ou Predicado de tipos). São funções especializadas em fazer "Type Narrowing"
# (ou afunilamento de tipo), assim como `isinstance` ou condicionais que
# afunilam tipos no Python.
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
# Boas práticas
#
# - Nomeie como guard: is_*, has_*, looks_like_*.
# - Seja sound: a função tem que garantir o tipo que promete. Nada de “achismo”.
# - Use TypeIs para escalar/união simples; TypeGuard para refinar coleções/estruturas.
# - Evite truques: se o retorno real é só bool, não declare TypeIs/TypeGuard.
#
################################################################################


class HasFirstName(TypedDict):
    firstname: str


class HasLastName(TypedDict):
    lastname: str


class HasFullName(HasFirstName, HasLastName, total=False): ...


def has_full_name(user: Mapping[Any, Any]) -> TypeGuard[HasFullName]:
    return bool(user.get("firstname") and user.get("lastname"))


################################################################################


def print_user_info(user: Mapping[Any, Any]) -> None:
    if has_full_name(user):
        # Tipo de user aqui é: HasFullName
        cyan_print(user["firstname"], user["lastname"])
        return

    # Tipo de user aqui é: Mapping[Any, Any]
    cyan_print("NOT A USER")


################################################################################


if __name__ == "__main__":
    sep_print()

    user = {
        "firstname": "Luiz",
        "lastname": "Otávio",
        "age": 18,
    }
    print_user_info(user)  # Luiz Otávio

    # if has_full_name(user):
    #     reveal_type(user)  # HasFullName

    sep_print()

    any_dict = {
        "lastname": "Otávio",
        "age": 18,
    }
    print_user_info(any_dict)  # NOT A USER

    sep_print()

################################################################################
