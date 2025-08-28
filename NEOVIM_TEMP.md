# Testando os comandos

Aqui nós temos um parágrafo de texto simples que pode não ter sentido nenhum. São apenas palavras
para conseguirmos executar comandos do NeoVim.

```python
def simple_decorator[R, **P](func: Callable[P, R]) -> Callable[Concatenate[str, P], R]:
    @wraps(func)
    def wrapper(whatever: str, *args: P.args, **kwargs: P.kwargs) -> R:
        cyan_print(f"{whatever=!r}", f"{func.__name__!r} will be executed")

        result = func(*args, **kwargs)

        cyan_print(f"{whatever!r}", f"{func.__name__!r} will be executed")
        return result

    return wrapper


@simple_decorator
def add(x: int, y: int, /) -> int:
    return x + y


@simple_decorator
def keyword_only(*, value: str) -> str:
    return value

def simple_decorator[R, **P](func: Callable[P, R]) -> Callable[Concatenate[str, P], R]:
    @wraps(func)
    def wrapper(whatever: str, *args: P.args, **kwargs: P.kwargs) -> R:
        cyan_print(f"{whatever=!r}", f"{func.__name__!r} will be executed")

        result = func(*args, **kwargs)

        cyan_print(f"{whatever!r}", f"{func.__name__!r} will be executed")
        return result

    return wrapper


@simple_decorator
def add(x: int, y: int, /) -> int:
    return x + y


@simple_decorator
def keyword_only(*, value: str) -> str:
    return value
```
