from collections.abc import Callable
from functools import wraps
from typing import Concatenate

from utils import cyan_print, sep_print

################################################################################
#
# ParamSpec com Concatenate
#
# PEP 695: ParamSpec and Concatenate remain unchanged and are not directly
# expressible with the new syntax.
#
################################################################################


def simple_decorator[R, **P](func: Callable[P, R]) -> Callable[Concatenate[str, P], R]:
    @wraps(func)
    def wrapper(whatever: str, *args: P.args, **kwargs: P.kwargs) -> R:
        cyan_print(f"{whatever=!r}", f"{func.__name__!r} will be executed")

        result = func(*args, **kwargs)

        cyan_print(f"{whatever!r}", f"{func.__name__!r} will be executed")
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

    add_result = add("WHATEVER", 1, 2)
    cyan_print(f"{add_result = }")

    keyword_only_result = keyword_only("FIRST", value="Wow")
    cyan_print(f"{keyword_only_result = }")

    sep_print()

################################################################################
