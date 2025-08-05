#
# Classes
#
# Sua classe É um tipo por si só.
# É necessário tipar todos os parâmetros e o retorno de métodos de classe.
# Quando for necessário usar o tipo de uma classe sem ela estar definida, use
# __future__ ou coloque entre aspas.
#
from __future__ import annotations


def print_endereco(endereco):
    print(endereco.endereco_completo)


class Endereco:
    _cache = {}

    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    @property
    def endereco_completo(self):
        return f"{self.rua} {self.numero}"

    def mudar_rua(self, rua):
        self.rua = rua

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"{cls_name}({self.endereco_completo})"


# @dataclass
# class Pessoa:
#     nome:
#     sobrenome:
#     idade:
#     endereco:
#     genero = ""
#
#     @property
#     def endereco_completo(self):
#         return self.endereco.endereco_completo
#
#
# endereco = Endereco("Rua das flores", 22)
# pessoa = Pessoa("Otávio", "Miranda", 18, endereco)
#
# print(pessoa)
# print(pessoa.endereco_completo)
