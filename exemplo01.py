from collections.abc import Callable
from typing import Final, Literal, Protocol, overload

CONSTANTE = "Seu valor será deve ser esse"
constante: Final = "valor"  # Literal["valor"]
constante2: Literal["valor"] = "valor"  # constante implícita

# You always should select de widest possible type
# for example: Sequence[str] is wider than List[str]
# You can use # type: ignore to completely supress erros
# With pyright you can use # pyright: ignore or # pyright: basic to change behaviour


@overload
def do_sum(x: int, y: int) -> int: ...
@overload
def do_sum(x: float, y: float) -> float: ...
def do_sum(x: float, y: float) -> float:
    return x * y


abc = do_sum(1, 2)


class Func[**P, R](Protocol):
    __name__: str

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R: ...


def decor[**P, R](
    *,
    verbose: bool = True,
) -> Callable[[Func[P, R]], Callable[P, R]]:
    def params(
        cb: Func[P, R],
    ) -> Callable[P, R]:
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            if verbose:
                print(f"Function: {cb.__name__!r} decorated")
            return cb(*args, **kwargs)

        return inner

    return params


def add(x: float, y: float) -> float:
    return x + y


@decor(verbose=True)
def add3(x: float, y: float) -> float:
    return x + y


add2 = decor(verbose=True)(add)

result1 = add(1, 2)
result2 = add2(1, 2)
result3 = add3(1, 2)

print(f"{result1= }")
print(f"{result2= }")
print(f"{result3= }")
