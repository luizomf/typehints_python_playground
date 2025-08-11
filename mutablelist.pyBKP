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

from collections.abc import Iterable, MutableSequence
from typing import cast, overload, override


class MutableContainer[T](MutableSequence[T]):
    def __init__(self, *data: T) -> None:
        super().__init__()
        self._data: list[T] = list(data) if data else []

    def insert(self, index: int, value: T) -> None:
        self._data.insert(index, value)
        print(self._data)

    @overload
    def __getitem__(self, key: int) -> T: ...
    @overload
    def __getitem__(self, key: slice) -> MutableContainer[T]: ...
    @override
    def __getitem__(self, key: int | slice) -> T | MutableContainer[T]:
        if isinstance(key, int):
            return self._data[key]
        return MutableContainer(*self._data[key])

    @overload
    def __setitem__(self, index: int, value: T) -> None: ...
    @overload
    def __setitem__(self, index: slice, value: Iterable[T]) -> None: ...
    @override
    def __setitem__(self, index: int | slice, value: T | Iterable[T]) -> None:
        size = len(self._data)

        if isinstance(index, slice):
            if not isinstance(value, Iterable):
                raise TypeError

            self._data[index] = value
            return

        if index <= size:
            value = cast("T", value)
            self._data.append(value)
            return

        raise IndexError

    def __delitem__(self, index: int | slice) -> None:
        del self._data[index]

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        values = ", ".join(f"{i}={v!r}" for i, v in enumerate(self._data))
        return f"{self.__class__.__name__}({values})"


l1: MutableContainer[int | str] = MutableContainer("Zero")
