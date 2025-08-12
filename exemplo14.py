#
# Testing
# Any, Optional
#


from collections.abc import Hashable, Mapping, Sized

from utils import cyan_print, sep_print


class MySized:
    def __len__(self) -> int:
        return 42


def get_size(container: Sized) -> int:
    return len(container)


s1 = 1, 2, 3
s2 = [1, 2, 3]
s3 = MySized()

print(get_size(s1))
print(get_size(s2))
print(get_size(s3))


def invert_mapping[K, V](mapping: Mapping[K, V]) -> Mapping[V, K]:
    new_mapping: Mapping[V, K] = {}

    for key, value in mapping.items():
        if not isinstance(value, Hashable):
            msg = f"{value!r} is not hashable"
            raise TypeError(msg)

        new_mapping[value] = key

    return new_mapping


d1 = {
    "a": 1,
    "b": (1, 2),
}
d2 = invert_mapping(d1)

sep_print()


cyan_print(d1)
cyan_print(d2)

sep_print()
