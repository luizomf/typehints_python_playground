import inspect
from collections.abc import Callable
from functools import wraps

from utils import cyan_print, sep_print

################################################################################
#
# ParamSpec com Decorator Factory - o micro pydantic mais pobre
#
# Um "Decorator Factory" é um decorator que recebe argumentos. Ou seja, é um
# decorator com uma camada a mais de funções.
#
# Estrutura:
# - A função factory recebe parâmetros e devolve o decorator.
# - O decorator recebe a função-alvo e devolve o wrapper.
# - O wrapper envolve a função-alvo, executando lógica extra antes/depois.
#
# Fluxo completo:
# decor_factory(...) -> decorator -> wrapper -> SUA FUNÇÃO
#
# Se não houver factory (decorator puro), o fluxo é direto:
# decorator -> wrapper -> SUA FUNÇÃO
#
################################################################################

# Isso aqui é a tipagem de um decorator
# É uma função que recebe uma função e retorna outra função
# Só fiz isso porque o nome tava longo demais, dificulta a leitura.
# A propósito, isso é um Type Alias genérico
type D[**P, R] = Callable[[Callable[P, R]], Callable[P, R]]
type Types = type | tuple[type, ...]


# Factory
def validate_types[**P, R](**types: Types) -> D[P, R]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        # Isso vai ler os nomes dos parâmetros da função original
        func_sig = inspect.signature(func)

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Isso liga os args e kwargs aos nomes dos parâmetros
            # Mais simples: liga parâmetros a argumentos.
            bound_args = func_sig.bind(*args, **kwargs).arguments

            for param, arg in bound_args.items():
                if param not in types:
                    continue

                type_ = types[param]
                if isinstance(type_, tuple):
                    type_name = ", ".join([f"{t.__name__!r}" for t in type_])
                    type_name = " or ".join(type_name.rsplit(", ", 1))
                else:
                    type_name = type_.__name__

                if not isinstance(arg, types[param]):
                    msg = f"{param!r} must be of type {type_name}"
                    raise TypeError(msg)

            return func(*args, **kwargs)

        return wrapper

    return decorator


################################################################################

# Funções toscas de exemplo


@validate_types(x=int, y=(int, float))
def add(x: int, y: int, /) -> int:
    return x + y


@validate_types(value=str)
def keyword_only(*, value: str) -> str:
    return value


@validate_types(x=int, y=int, whatever=str, value=(str,))
def mixed(x: int, y: int, /, whatever: str, *, value: str) -> str:
    return f"{x=!r} {y=!r} {whatever=!r} {value=!r}"


################################################################################


if __name__ == "__main__":
    sep_print()

    add_result = add(1, 2)
    cyan_print(f"{add_result=!r}")

    keyword_only_result = keyword_only(value="Wow")
    cyan_print(f"{keyword_only_result=!r}")

    mixed_result = mixed(1, 2, "abc", value="valor")
    cyan_print(f"{mixed_result=!r}")

    sep_print()

################################################################################
