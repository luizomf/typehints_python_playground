#
# Genéricos padrão em Collections ABC
#
# Doc: https://docs.python.org/3/library/collections.abc.html
#
# Abstract Base Classes (ABCs), são classes abstratas que implementam alguns
# métodos abstratos e te dão outros gratuitamente (mixins). Isso significa que
# você pode implementar suas próprias coleções como preferir.
#
# Variância:
# Valores imutáveis são covariantes (posso retornar algo mais específico)
#
from __future__ import annotations

from collections.abc import Sequence
from typing import overload, override


class ReadOnlyList[T](Sequence[T]):
    def __init__(self, *args: T) -> None:
        super().__init__()
        self._data = args

    @overload
    def __getitem__(self, key: int) -> T: ...
    @overload
    def __getitem__(self, key: slice) -> ReadOnlyList[T]: ...
    @override
    def __getitem__(self, key: int | slice) -> T | ReadOnlyList[T]:
        # Ao meu ver, estamos caindo nesse "problema"
        # https://peps.python.org/pep-0673/#use-in-generic-classes
        if isinstance(key, float | int):
            return self._data[key]
        return ReadOnlyList(*self._data[key])

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        values = ", ".join(f"{i}={v!r}" for i, v in enumerate(self._data))
        return f"{self.__class__.__name__}({values})"


f2 = ReadOnlyList(1, 2, 3, "a", "b")
f3 = f2[1:2]

l1 = ReadOnlyList(1, 2, 3)
print(l1[0])
print(l1[0:2])

l1 = ReadOnlyList("ABC", 1, 22, "DEF", "GHI")
print(l1[0])
print(l1[0:2])
