from collections.abc import Callable

################################################################################
#
# ParamSpec e Concatenate no Python: Você PRECISA DISSO Para Closures! (Aula17)
#
# Parameter Specification (ou o ParamSpec) serve para representar a lista
# completa de parâmetros de uma função. Ele guarda TUDO o que é relacionado aos
# parâmetros, como tipo, ordem, posicionais, opcionais, etc.
# Ao capturar a assinatura, você consegue passar seus dados adiante para outros
# locais. Assim, quando sua função passar por dentro de outra, os tipos dos
# parâmetros podem ser mantidos.
#
# Vamos ver exemplos:
#
################################################################################

# Exemplo onde uma função passa dentro de outra e perde a tipagem dos parâmetros.


def identity_bad[R](func: Callable[..., R]) -> Callable[..., R]:
    return func


def add(x: float, y: float, /) -> float:
    return x + y


add_ = identity_bad(add)  # add_(...) -> float: perdemos a tipagem dos parâmetros

################################################################################

# Mesmo exemplo, mas agora usando Parameter Specification


def indentity_good[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    return func


def multiply(x: float, y: float, /) -> float:
    return x * y


multiply_ = indentity_good(multiply)  # multiply_ permanece exatamente igual

################################################################################
