#
# Classes
#
# Sua classe É um tipo por si só.
# É necessário tipar todos os parâmetros e o retorno de métodos de classe.
# Quando for necessário usar o tipo de uma classe sem ela estar definida, use
# __future__ ou coloque entre aspas.
#

from dataclasses import dataclass


def print_endereco(endereco: "Endereco") -> None:
    print(endereco.endereco_completo)


class Endereco:
    def __init__(self, rua: str, numero: int) -> None:
        self.rua = rua
        self.numero = numero

    @property
    def endereco_completo(self) -> str:
        return f"{self.rua} {self.numero}"

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f"{cls_name}({self.endereco_completo})"


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int
    endereco: Endereco
    genero: str = ""

    @property
    def endereco_completo(self) -> str:
        return self.endereco.endereco_completo


endereco = Endereco("Rua das flores", 22)
pessoa = Pessoa("Otávio", "Miranda", 18, endereco)

print(pessoa)
print(pessoa.endereco_completo)
