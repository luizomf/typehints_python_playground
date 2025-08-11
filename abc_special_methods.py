from collections.abc import AsyncIterator, Awaitable, Iterable, Iterator
from typing import Any, Self, TypeVar

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
K = TypeVar("K")
V = TypeVar("V")

# ----------------------------------------
# Container
# ----------------------------------------


def __contains__(self, item: object) -> bool:
    """x in obj — verifica se item está no container."""


# ----------------------------------------
# Hashable
# ----------------------------------------


def __hash__(self) -> int:
    """hash(obj) — usado em sets e chaves de dict."""


# ----------------------------------------
# Iterable / Iterator
# ----------------------------------------


def __iter__(self) -> Iterator[T_co]:
    """iter(obj) — início da iteração (for ... in obj)."""


def __next__(self) -> T_co:
    """next(iterator) — retorna o próximo elemento."""


# ----------------------------------------
# Reversible
# ----------------------------------------


def __reversed__(self) -> Iterator[T_co]:
    """reversed(obj) — iteração inversa."""


# ----------------------------------------
# Sized
# ----------------------------------------


def __len__(self) -> int:
    """len(obj) — tamanho do container."""


# ----------------------------------------
# Callable
# ----------------------------------------


def __call__(self, *args: object, **kwargs: object) -> object:
    """obj(...) — invoca a instância como função."""


# ----------------------------------------
# Sequence / Mapping
# ----------------------------------------


def __getitem__(self, key: int) -> T_co:
    """obj[i] — acesso por índice."""


def __getitem__(self, s: slice) -> "Sequence[T_co]":
    """obj[a:b:c] — acesso por slice."""


def __getitem__(self, key: K) -> V:
    """obj[key] — acesso por chave (Mapping)."""


# ----------------------------------------
# MutableSequence / MutableMapping
# ----------------------------------------


def __setitem__(self, key: int, value: T) -> None:
    """obj[i] = v — atribuição por índice."""


def __setitem__(self, s: slice, value: Iterable[T]) -> None:
    """obj[a:b] = iterable — atribuição por slice."""


def __setitem__(self, key: K, value: V) -> None:
    """obj[key] = v — atribuição por chave (Mapping)."""


def __delitem__(self, key: int | slice) -> None:
    """del obj[i] / del obj[a:b] — remove por índice ou slice."""


def __delitem__(self, key: K) -> None:
    """del obj[key] — remove por chave (Mapping)."""


# ----------------------------------------
# MutableSequence
# ----------------------------------------


def __iadd__(self, values: Iterable[T]) -> Self:
    """obj += iterable — concatenação in-place."""


# ----------------------------------------
# Set
# ----------------------------------------


def __le__(self, other: "Set[T]") -> bool:
    """obj <= other — subconjunto."""


def __lt__(self, other: "Set[T]") -> bool:
    """obj < other — subconjunto próprio."""


def __ge__(self, other: "Set[T]") -> bool:
    """obj >= other — superconjunto."""


def __gt__(self, other: "Set[T]") -> bool:
    """obj > other — superconjunto próprio."""


def __eq__(self, other: object) -> bool:
    """obj == other — igualdade."""


def __ne__(self, other: object) -> bool:
    """obj != other — desigualdade."""


def __and__(self, other: "Set[T]") -> "Set[T]":
    """obj & other — interseção."""


def __or__(self, other: "Set[T]") -> "Set[T]":
    """obj | other — união."""


def __sub__(self, other: "Set[T]") -> "Set[T]":
    """obj - other — diferença."""


def __xor__(self, other: "Set[T]") -> "Set[T]":
    """obj ^ other — diferença simétrica."""


def __rsub__(self, other: "Set[T]") -> "Set[T]":
    """other - obj — diferença (refletida)."""


def __rxor__(self, other: "Set[T]") -> "Set[T]":
    """other ^ obj — diferença simétrica (refletida)."""


# ----------------------------------------
# MutableSet
# ----------------------------------------


def __ior__(self, other: Iterable[T]) -> Self:
    """obj |= iterable — união in-place."""


def __iand__(self, other: Iterable[T]) -> Self:
    """obj &= iterable — interseção in-place."""


def __ixor__(self, other: Iterable[T]) -> Self:
    """obj ^= iterable — diferença simétrica in-place."""


def __isub__(self, other: Iterable[T]) -> Self:
    """obj -= iterable — diferença in-place."""


# ----------------------------------------
# Awaitable
# ----------------------------------------


def __await__(self) -> Iterator[Any]:
    """await obj — protocolo awaitable."""


# ----------------------------------------
# AsyncIterable / AsyncIterator / AsyncGenerator
# ----------------------------------------


def __aiter__(self) -> AsyncIterator[T_co]:
    """async for x in obj — início de iteração assíncrona."""


def __anext__(self) -> Awaitable[T_co]:
    """async for — retorna próximo item."""


# ----------------------------------------
# Buffer (PEP 688)
# ----------------------------------------


def __buffer__(self, flags: int, /) -> memoryview:
    """memoryview(obj) — cria interface de buffer."""
