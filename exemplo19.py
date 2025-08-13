#
# Mais exemplo de parâmetros de tipo
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

import string
from collections.abc import Hashable, MutableMapping
from secrets import SystemRandom

from utils import cyan_print, sep_print


# O hash do dicionário é um número calculado pelo __hash__ que serve como
# identificador rápido do conteúdo de algumas estruturas de dados como
# dict e set.
# O hash nunca deve mudar, por isso os valores para a chave precisam ser imutáveis.
def invert_mapping[K: str, V: Hashable](
    mapping: MutableMapping[K, V],
) -> MutableMapping[V, K]:
    return {v: k for k, v in mapping.items()}


def generate_password(
    *,
    unwanted_chars: str = "\"'\\@/",
    lower_qtd: int = 3,
    upper_qtd: int = 3,
    digits_qtd: int = 3,
    punctuation_qtd: int = 3,
) -> str:
    """
    Simple password generator

    Parameters:
        unwanted_chars (str): a string with characters that should not be added
        lower_qtd (int): quantity of lower case letters
        upper_qtd (int): quantity of upper case letters
        digits_qtd (int): quantity of digits letters
        punctuation_qtd (int): quantity of punctuation characters letters

    Returns:
        str: a string with the generated password
    """
    rand = SystemRandom()

    sum_of_props = sum((lower_qtd, upper_qtd, digits_qtd, punctuation_qtd))

    safe_chars = string.digits + string.ascii_letters
    lowers = rand.choices(string.ascii_lowercase, k=lower_qtd)
    uppers = rand.choices(string.ascii_uppercase, k=upper_qtd)
    digits = rand.choices(string.digits, k=digits_qtd)
    punctuation = rand.choices(string.punctuation, k=punctuation_qtd)
    extras = "".join(rand.choices(safe_chars, k=len(unwanted_chars)))

    list_password = [*lowers, *uppers, *digits, *punctuation]

    string_password = "".join(
        [
            c
            if c not in unwanted_chars
            else f"{extras[rand.randint(0, len(extras) - 1)]}"
            for c in list_password
        ],
    )

    missing = sum_of_props - len(string_password)
    string_password = list(
        string_password if missing <= 0 else string_password + extras[:missing],
    )
    rand.shuffle(string_password)

    return "".join(string_password)


if __name__ == "__main__":
    password = generate_password(
        lower_qtd=3,
        upper_qtd=3,
        digits_qtd=3,
        punctuation_qtd=3,
    )

    sep_print()

    dict1 = {
        "a": "1",
        "b": "2",
        "c": (1, 2),
    }
    inverted1 = invert_mapping(dict1)

    cyan_print(inverted1)

    sep_print()
