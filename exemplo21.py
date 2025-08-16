#
# Classes Genéricas e TypeVar no Python 3.13 (Nova Sintaxe) - Aula 9
#
# A tipagem de Classes Genéricas ou Generic Classes seguem o mesmo padrão das
# funções genéricas que vimos na aula anterior. Defina um type parameter na
# classe e automaticamente ela se tornará uma classe genérica com a nova sintaxe
# da PEP 695 (>=3.12).
#

# No exemplo abaixo tenho um MutableMapping que está fixado com chave e valor.
# Nosso trabalho é tornar este mapping em uma classe genérica que aceite
# parâmetros de tipo (type parameter) para que ela possa ser usada com os
# tipos que cumprem o objetivo.
# O objetivo final é ter a possibilidade de inverter chave e valor.
# Lembre-se: chave precisa ser hashable (imutável).

# ⚠️ Pontos de atenção


from collections.abc import Hashable, Iterator, MutableMapping

from utils import cyan_print, sep_print


class MyMutableDict[K: Hashable, V: Hashable](MutableMapping[K, V]):
    def __init__(self, *args: tuple[K, V]) -> None:
        self._data: dict[K, V] = dict(args)

    # Não tem como inverter esse dicionário
    # Preciso retornar [int, str], mas minha classe aceita [str, int]
    def inv(self) -> MutableMapping[V, K]:  # Esse retorno pode ser mais específico
        inverted = {v: k for k, v in self._data.items()}
        return MyMutableDict(*tuple(inverted.items()))

    def __iter__(self) -> Iterator[K]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key: K) -> V:
        return self._data[key]

    def __setitem__(self, key: K, value: V) -> None:
        self._data[key] = value

    def __delitem__(self, key: K) -> None:
        del self._data[key]

    def __repr__(self) -> str:
        attrs = [f"{k}={v!r}" for k, v in self._data.items()]
        cls_name = type(self).__name__
        return f"{cls_name}({', '.join(attrs)})"


if __name__ == "__main__":
    data1 = ("chave1", 1), ("chave2", 2)
    data2 = (1, "chave1"), (2, "chave2")
    data3 = (1, [1, 2, 3]), (2, [4, 5, 6])  # ⚠️

    my_dict1 = MyMutableDict(*data1)
    my_dict2 = MyMutableDict(*data2)
    my_dict3 = MyMutableDict(*data3)  # ⚠️

    sep_print()

    cyan_print(my_dict1)
    cyan_print(my_dict1.inv())
    cyan_print()
    cyan_print(my_dict2)
    cyan_print(my_dict2.inv())
    cyan_print()
    cyan_print(my_dict3)  # ⚠️
    cyan_print(my_dict3.inv())  # ⚠️

    sep_print()
