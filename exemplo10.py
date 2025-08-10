#
# Covariância e contravariância em Genéricos padrão
#
# Doc: https://docs.python.org/3/library/collections.abc.html
#
# Muitos genéricos são "collections", ou seja, podem ter algum tipo que vem de
# fora, como vimos em: `list[T]`, `tuple[T]`, `Iterable[T]` e outros.
# Então, como poderíamos saber se `C[T2]` também é um subtipo de `C[T1]`?
# Para distinguir isso precisamos das características da "collection" e de como
# ela será usada.
# Aqui entra em ação a variância: covariância, contravariância e invariância.
#
# Observação: variância pode ser escolhida pelo desenvolvedor ou inferida
# automaticamente. Voltaremos nesse assunto em aulas futuras, mas aqui estamos
# falando das collections existentes em collections.abc.
#
# `C`=Collection ### `T`=Tipo ### `Tn`=Tipo enumerado ### `<:`=é subtipo de.
#
# Considerando `T2 <: T1`, o que acontece com `C` de acordo com a variância?
#
# Se `C` é `covariant`: a hierarquia é mantida, `C[T2]` é subtipo de `C[T1]`. \
# É intuitivo: `T2` <: `T1` então `C[T2]` <: `C[T1]`. \
# Geralmente aparece em retornos e tipos imutáveis (outputs).
#


# Vamos ver um exemplo simples:
# - `tuple` como collection `C[T]`
# - Por padrão, `tuple` é imutável, portanto covariante (CO é o intuitivo)
# - Para `T2`, podemos usar o `bool`, porque no Python `bool` é subtipo de `int`
# - Para `T1`, podemos usar então o supertipo `int`.
# Então temos exatamente o exemplo: `bool <: int` e `tuple[bool] <: tuple[int]`
#
# TypeAlias
type C[T] = tuple[T, ...]  # Tupla com um ou mais Ts

# Código
integer_box: C[int] = 0, 1, 1, 0  # C[T1]
boolean_box: C[bool] = False, True, True, False  # C[T2]

# Se é a collection é covariante, posso usar o subtipo no lugar do supertipo
# integer_box = boolean_box  # Isso não gera erros


def get_integers() -> C[int]:
    return True, True, False, False  # Isso também funciona normalmente


# Por conta disso:
a, b, c, d = get_integers()
# Se eu usar o retorno como int, funciona:
print(a + b + c + d)  # 2
# Se eu usar o retorno como bool funciona:
is_admin, is_logged, *_ = get_integers()
print(f"{is_admin = }, {is_logged = }")
