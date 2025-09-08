import inspect
from abc import ABC, abstractmethod
from collections.abc import Callable
from functools import wraps
from typing import Annotated, get_args, get_type_hints

from utils import cyan_print, sep_print

p = cyan_print
s = sep_print

################################################################################
#
# Python Annotated: Exemplo simples!
#
# Dica: se vai fazer uma coisa complexa que outra lib já faz, usa ela. Isso
# pode se tornar muito complexo muito rápido.
#
################################################################################


def validate_annotated[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Decorator que valida o que for anotado com Annotated e Validator"""

    # Obtemos as annotations da função
    hints = get_type_hints(func, include_extras=True)
    # Isso vai nos ajudar a inspecionar a função
    signature = inspect.signature(func)

    @wraps(func)  # Boa prática 👍
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        # Agora podemos pegar os argumentos e seus valores
        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()

        # Se não encontrarmos nenhuma annotation, retornamos
        if not hints:
            return func(*args, **kwargs)

        # Loop nos nomes dos argumentos da função
        for arg_name in bound_arguments.arguments:
            # Se o nome que eu recebi aqui não está anotado, próximo...
            if arg_name not in hints:
                continue

            # Pego o valor do argumento
            value = bound_arguments.arguments[arg_name]
            # Pego os dados do argumento
            metadata = get_args(hints[arg_name])

            # Só vou conferir algo que tenha mais de um valor
            # o segundo valor pode ser um ou mais validadores
            if len(metadata) <= 1:
                continue

            # Pegamos o tipo e os possíveis validadores
            type_, *validators = metadata

            # Vamos passar em todos checando se são mesmo validadores
            for validator in validators:
                if not isinstance(validator, Validator):
                    continue

                # Se são, quero garantir que o tipo também está correto
                if not isinstance(value, type_):
                    msg = (
                        f"Argument {arg_name!r} should be of type {type_!r} "
                        f"in {func.__name__!r}. Got {type(value)!r}."
                    )
                    raise TypeError(msg)

                # E agora é só validar
                # Obs.: Já chequei o tipo, pyright não reconheceu
                validator.validate(value)  # pyright: ignore[reportUnknownMemberType]

        # Executamos a função original com os argumentos bonitinhos
        return func(*args, **kwargs)

    # Te dou uma nova função
    return wrapper


################################################################################


# Exemplo de uma hierarquia de validadores


class ValidationError(Exception):
    """Uma exceção com nome mais semântico"""


class Validator[T](ABC):
    """Contrato que os validadores prometem cumprir"""

    @abstractmethod
    def validate(self, value: T) -> T: ...


class IntRange(Validator[int]):
    """Valida um range de números"""

    def __init__(self, min_: int, max_: int) -> None:
        self.min = min_
        self.max = max_

    def validate(self, value: int) -> int:
        if value < self.min or value > self.max:
            msg = f"{value} is out of range ({self.min}, {self.max})"
            raise ValidationError(msg)

        return value


class StrMaxLength(Validator[str]):
    """Valida uma string com tamanho máximo"""

    def __init__(self, max_: int) -> None:
        self.max = max_

    @validate_annotated
    def validate(self, value: str) -> str:
        if len(value) > self.max:
            msg = f"{value!r} has more than {self.max} characters"
            raise ValidationError(msg)

        return value


################################################################################


@validate_annotated
def set_height(height: Annotated[int, IntRange(1, 100)]) -> int:
    """Set the widget height"""
    p(f"Height is set to {height}")
    return height


@validate_annotated
def set_app_name(
    name: Annotated[str, StrMaxLength(10)],
) -> str:
    """Change app name"""
    p(f"App name is now {name!r}")
    return name


################################################################################


if __name__ == "__main__":
    new_app_name = set_app_name(name="My App")
    new_height = set_height(height=1)


################################################################################
