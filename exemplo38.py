import json
from pathlib import Path
from typing import Any, TypedDict, TypeGuard, cast

from utils import cyan_print, red_print, sep_print

################################################################################
#
# TypeGuard - Precisamos de Guarda-costas?
#
# Obs.: PEP 742 e 647 falam de TypeGuard e TypeIs. Focaremos em TypeGuard.
# Depois TypeIs.
#
# Comparação: No TypeScript, funções que fazem Type Guard, são chamadas de
# "Type Predicate" (ou Predicado de tipos). São funções especializadas em fazer
# "Type Narrowing" (ou afunilamento de tipo), assim como `isinstance` ou
# condicionais que afunilam tipos no Python.
#
# TypeGuard[T] e TypeIs[T] são ambas funções para "Type Predicate" no Python.
# As duas informam ao Type Checker que se seu retorno for verdadeiro, o tipo do
# objeto avaliado é `T`.
#
# Com a inclusão de TypeIs[T], TypeGuard[T] tenderá a ser menos usado, mas de
# acordo com a PEP 742 (sobre TypeIs), TypeGuard[T] vai continuar na linguagem.
#
################################################################################


class UserDict(TypedDict):
    firstname: str
    lastname: str
    age: int


def is_valid_dict(item: object) -> TypeGuard[UserDict]:
    if not isinstance(item, dict):
        return False

    item = cast("dict[str, Any]", item)  # isso é para o Pyright para de amolar

    if not isinstance(item.get("firstname"), str):
        return False

    if not isinstance(item.get("lastname"), str):
        return False

    return isinstance(item.get("age"), int)


################################################################################


if __name__ == "__main__":
    sep_print()

    input_file = Path("exemplo38.json").resolve()
    with input_file.open("r", encoding="utf8") as file:
        user_data = json.load(file)  # Any

    for user in user_data:
        if is_valid_dict(user):
            cyan_print("✅ VALID USER")
            cyan_print(f"{user['firstname']} {user['lastname']} {user['age']}")
        else:
            red_print("❌ INVALID DATA ❌")
            red_print(user.keys())

    sep_print()

################################################################################
