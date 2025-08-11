#
# ReadOnlyList
#

from collections.abc import Iterator, Sequence
from typing import overload, override


class ReadOnlyList[ROValue](Sequence[ROValue]):
    def __init__(self, *args: ROValue) -> None:
        self._data: dict[int, ROValue] = {}
        self._index = 0
        self._next_index = 0
        self._add_initial_values(*args)

    def _add_initial_values(self, *args: ROValue) -> None:
        for arg in args:
            self._data[self._index] = arg
            self._index += 1

    @overload
    def __getitem__(self, index: int) -> ROValue: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[ROValue]: ...
    @override
    def __getitem__(self, index: int | slice) -> ROValue | Sequence[ROValue]:
        if isinstance(index, slice):
            data_slice = list(self._data.values())[index]
            return ReadOnlyList(*data_slice)
        return self._data[index]

    def __len__(self) -> int:
        return self._index

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs_str = ", ".join([f"{v!r}" for v in self._data.values()])
        return f"{cls_name}({attrs_str})"

    def __iter__(self) -> Iterator[ROValue]:
        return self

    def __next__(self) -> ROValue:
        if not self._data or self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1

        return value


if __name__ == "__main__":
    list1 = ReadOnlyList("a", 0, 1, 2, 3, 4, 5, {"a", "b", "c"})
    print(list1)
