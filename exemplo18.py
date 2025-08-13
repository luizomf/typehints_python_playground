#
# TypeVar é o modelo anterior
#
# Usaremos a nova sintaxe definida pela PEP 695 (Python >=3.12)
# https://docs.python.org/3/whatsnew/3.12.html#pep-695-type-parameter-syntax
#
# O modo anterior (que ainda pode ser usado) era definido com o seguinte:
#
# from typing import TypeVar
#
# 1. Unconstrained type variable (TypeVar livre)
# Pode ser substituído por qualquer tipo.
# _T = TypeVar("_T")  # novo [T]
#
# 2. Bounded type variable (TypeVar com upper bound)
# Só pode ser substituído por `str` ou subtipos de `str`.
# _U = TypeVar("_U", bound=str)  # novo [U: str]
#
# 3. Covariant type variable
# Usado em contextos de "produção" de valores (output),
# permite que subtipos sejam aceitos onde se espera o tipo base.
# _V_co = TypeVar("_V_co", covariant=True)  # PEP 695: variância inferida no uso
#
# 4. Contravariant type variable
# Usado em contextos de "consumo" de valores (input),
# permite que supertipos sejam aceitos onde se espera o subtipo.
# _W_contra = TypeVar("_W_contra", contravariant=True)  # PEP 695: variância inferida
#
# 5. Bounded type variable com união de tipos como bound
# Aceita apenas `str` ou `bytes` (ou subtipos de cada um).
# _X = TypeVar("_X", bound=str | bytes)  # novo [X: str | bytes]
#
# 6. Constrained type variable (TypeVar com restrições explícitas)
# Pode ser apenas `int` ou `str` (tipos exatos ou subtipos deles).
# _Y = TypeVar("_Y", int, str)  # novo [Y: (int, str)]
#
# 7. Default Type (TypeVar com tipo padrão)
# Se um tipo não for informado inicialmente, temos um tipo padrão `str`
# _Z = TypeVar("_Z", default=str)  # novo [Z = str]
