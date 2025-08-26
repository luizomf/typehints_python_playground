from collections.abc import Callable
from functools import wraps

from utils import cyan_print, sep_print

################################################################################
#
# ParamSpec com closures e decorators em geral
#
# Vamos ver exemplos:
#
################################################################################

# Exemplo de um decorator ruim


def simple_decorator_bad[R](func: Callable[..., R]) -> Callable[..., R]:
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> R:
        return func(*args, **kwargs)

    return wrapper


################################################################################

# Exemplo de um decorator bom


def simple_decorator[R, **P](func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        cyan_print(f"{func.__name__!r} will be executed")

        result = func(*args, **kwargs)

        cyan_print(f"{func.__name__!r} was be executed")
        return result

    return wrapper


################################################################################

# Funções toscas de exemplo


@simple_decorator
def add(x: int, y: int, /) -> int:
    return x + y


@simple_decorator
def keyword_only(*, value: str) -> str:
    return value


################################################################################


if __name__ == "__main__":
    sep_print()

    add_result = add(1, 2)
    cyan_print(f"{add_result = }")

    keyword_only_result = keyword_only(value="Wow")
    cyan_print(f"{keyword_only_result = }")

    sep_print()

################################################################################
