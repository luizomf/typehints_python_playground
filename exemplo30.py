import re
from datetime import _TzInfo, datetime
from typing import Protocol, overload

from utils import cyan_print, sep_print

################################################################################
#
# TypeVar com callback protocol
#
# Também é possível usar `TypeVar` com protocols. Isso permite que você faça a
# assinatura da sua função de forma mais dinâmica. Assim, os tipos podem variar
# de acordo com o contexto.
# No exemplo abaixo, tenho um Protocol super simples. A intenção é receber sempre
# um atributo nomeado chamado `value` com tipo `T` e retornar `R`.
# Ambos `T` e `R` são `TypeVars` ou Type Parameters dinâmicos.
#
################################################################################

# Essa expressão regular será usada para limpar vírgulas.
# Ela seleciona o seguinte:
# - `\s*` - zero ou mais espaços
# - `,` - a vírgula
# - `\s*` - zero ou mais espaços
# Tenho curso grátis sobre isso aqui:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr
RE_COMMA_SPACE = re.compile(r"\s*,\s*")


################################################################################

# Vamos definir o nosso `Protocol` que aceita tipos parametrizados (`TypeVar`).


class TypeCaster[T, R](Protocol):
    def __call__(self, *, value: T) -> R: ...


################################################################################

# Agora podemos definir nossas funções que cumprem o contrato.


def to_str(*, value: object) -> str:
    """Recebe qualquer coisa e converte em string"""

    return str(value)


def str_to_list(*, value: str) -> list[str]:
    """Recebe uma string e tenta converter em lista"""

    clean_value = RE_COMMA_SPACE.sub(value, ",")
    return [v.strip() for v in RE_COMMA_SPACE.split(clean_value) if v.strip()]


def wrong_kw_name(text: str) -> str:
    """❌ Esse argumento nomeado está com nome errado"""

    return text


################################################################################

# Por fim vamos definir algo que "usa" o nosso `Protocol` e testamos se nossas
# funções passam na tipagem. Perceba que aqui estamos realmente usando as nossas
# funções como callback (fazendo o nome callback protocol valer).


def run_type_caster[T, R](value: T, type_caster: TypeCaster[T, R]) -> R:
    """Recebe um valor, um type_caster e executa tudo"""

    return type_caster(value=value)


class Strptime(Protocol):
    def __call__(self, date_string: str, format: str, /) -> datetime: ...


class FromTimestamp(Protocol):
    def __call__(self, timestamp: float, tz: _TzInfo | None = ...) -> datetime: ...


class DateMaker(Protocol):
    @overload
    def __call__(
        self,
        value: str,
        *,
        in_format: str | None = None,
    ) -> Strptime: ...
    @overload
    def __call__(
        self,
        value: tuple[int, ...],
        *,
        in_format: None = None,
    ) -> type[datetime]: ...
    @overload
    def __call__(
        self,
        value: float,
        *,
        in_format: None = None,
    ) -> FromTimestamp: ...


@overload
def date_maker(
    value: str,
    *,
    in_format: str | None = None,
) -> Strptime: ...
@overload
def date_maker(
    value: tuple[int, ...],
    *,
    in_format: None = None,
) -> type[datetime]: ...
@overload
def date_maker(
    value: float,
    *,
    in_format: None = None,
) -> FromTimestamp: ...
def date_maker(
    value: str | tuple[int, ...] | float,
    in_format: str | None = None,
) -> Strptime | FromTimestamp | type[datetime]:
    if isinstance(value, str):
        if not in_format:
            msg = f"You must inform the date format for {value!r}"
            raise ValueError(msg)

        return datetime.strptime

    if isinstance(value, tuple):
        if not value:
            msg = "Cannot create a date with empty tuple"
            raise ValueError(msg)

        return datetime

    return datetime.fromtimestamp


################################################################################

# Bora testar tudo


if __name__ == "__main__":
    sep_print()

    # o mesmo que datetime()
    date1 = date_maker((1, 1, 1))
    # o mesmo que datetime.strptime()
    date2 = date_maker("2025-08", in_format="%Y-%m")
    # o mesmo que datetime.fromtimestamp(1755696515.035976)
    date3 = date_maker(1755696515.035976)

    cyan_print(f"{date1 = }")
    cyan_print(f"{date2 = }")
    cyan_print(f"{date3 = }")


################################################################################
