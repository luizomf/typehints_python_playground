# Estudo de Type Hints

PEPs para reler (a fontes das informações):

- PEP 483 - The Theory of Type Hints - [link](https://peps.python.org/pep-0483/)
- PEP 484 - Type Hints - [link](https://peps.python.org/pep-0484/)
- PEP 544 - Protocols (Estrutural) [link](https://peps.python.org/pep-0544/)
- \*PEP 585 - Generics Std Collections [link](https://peps.python.org/pep-0585/)
- PEP 612 - Parameter Spec [link](https://peps.python.org/pep-0612/)
- PEP 695 - Type Parameter Syntax [link](https://peps.python.org/pep-0695/)

Documentações interessantes (pode ajudar com a didática):

- [typing doc](https://docs.python.org/3/library/typing.html)
- [Collections ABCs doc](https://docs.python.org/3/library/typing.html)
- [Índice de typing](https://typing.python.org/en/latest/index.html)
- [Mypy doc](https://mypy.readthedocs.io/en/stable/kinds_of_types.html)
- [Wiki Pylance](https://github.com/microsoft/pylance-release/wiki/Covariance-and-Contravariance)

Não importantes, mas me ajudam a entender como as pessoas ensinam isso:

- [Polimorfismo paramétrico](https://pt.wikipedia.org/wiki/Polimorfismo_param%C3%A9trico)
- [Teoria dos tipos](https://pt.wikipedia.org/wiki/Teoria_dos_tipos)
- [Variance](https://www.youtube.com/watch?v=FdFBYUQCuHQ&t=77s&ab_channel=ChristopherOkhravi)
- [Extremamente básico](https://realpython.com/python-type-checking/)

## Notas

`Any` pode ser considerado um tipo que aceita qualquer valor e assume ter qualquer atributo ou
método. Ele é um tipo estrutural especial, usado para desativar temporariamente a verificação de
tipos.

Já `object` é o tipo base nominal de todas as classes em Python, todo valor é um `object`.

A diferença é que você pode passar um `Any` onde se espera um `int`, uma `str`, ou qualquer outro
tipo, sem erro; mas não pode passar um `object` onde se espera um `int`, porque o `object` não
garante os métodos e atributos do `int`.

## Covariância e contravariância (Covariance e Contravariance)

Este foi o
[conteúdo mais intuitivo que encontrei](https://github.com/microsoft/pylance-release/wiki/Covariance-and-Contravariance)
a respeito de covariância e contravariância em Python.

Vamos usar os exemplos do conteúdo acima levemente modificados para testes:

```python
class Animal:
    def is_alive(self) -> bool: ...


class Dog(Animal):
    def bark(self, sound: str) -> None: ...


class Pitbull(Dog): ...


class Box[T]:
    def add(self, *items: T) -> None: ...
```

### PEP 483

vib - seleciona o que está entre parênteses. \
vip - seleciona o parágrafo.

Se um tipo `t2` é um subtipo de `t1`, então um construtor de um tipo genérico `GenType` é chamado
de:

- Covariante se `GenType[t2]` é um subtipo de `GenType[t1]` para todos os `t1` e `t2`.
- Contravariante se `GenType[t1]` é um subtipo de `GenType[t2]` para todos os `t1` e `t2`.
- Invariante se nenhuma das opções acima.

O exemplo que usaram:

```python
def cov(x: float) -> float:
    return 2*x

def contra(x: float) -> float:
    return -x

def inv(x: float) -> float:
    return x*x
```

Se `x1 < x2`, então sempre `cov(x1) < cov(x2)`, e `contra(x2) < contra(x1)`.

Se `x1 é subtipo de x2`, então sempre `Cov[x1] é subtipo de Cov[x2]` (covariância), e
`Contra[x2] é subtipo de Contra[x1]` (contravariância).

### Sobre `Callable`

- Se o tipo `T` só aparece em retorno → tende a ser covariante.
- Se `T` só aparece em parâmetro de entrada, tende a ser contravariante.
- Se aparece nos dois lados (ou em posições "mistas") → fica invariante

```python
from dataclasses import dataclass

@dataclass
class Animal: ...
class Dog(Animal): ...
class Pitbull(Dog): ...

class Producer[T]:
    def get(self) -> T: ...  # T só em retorno => covariante
    # nada de put(T) aqui, pra não “poluir” a variância

def wants_animals(p: Producer[Animal]) -> None: ...

dogs: Producer[Dog]
pits: Producer[Pitbull]

wants_animals(dogs)   # OK (Producer[Dog] <: Producer[Animal])
wants_animals(pits)   # OK (Producer[Pitbull] <: Producer[Animal])
```

### Covariância

Covariância geralmente indica que o tipo é seguro na saída (output), mas não seguro na entrada
(input).

Um exemplo de input e output seria um `Callable[[Input], Output]`, onde `Input` são os argumentos
e o `Output` o retorno. Então a covariância ocorre no retorno.

Se um tipo `Dog` é subtipo de `Animal`, então um tipo `Box[Dog]` é um subtipo de `Box[Animal]`
(esse cenário é intuitivo).

Se uma função tem que retornar `Box[Animal]`, então é aceitável retornar `Box[Dog]`.

Covariância sobe na árvore de tipos, como em `Animal` -> `Dog` -> `Pitbull`.

### Contravariância

Contravariante geralmente indica que o tipo é seguro na entrada (input).

Se um tipo `Dog` é um subtipo de `Animal`, então um tipo `Box[Animal]` é um subtipo de `Box[Dog]`
(isso é muito contra intuitivo).

Em Python isso ocorre com `Callable`, que é covariante no retorno e contravariante nos argumentos.

A dica da PEP 483 é que você deve usar tipos mais abrangentes nos argumentos e mais específicos
nos retornos.

Ainda seguindo exemplos da PEP 483, `Callable[[A], None]` seria subtipo de `Callable[[B], None]`.

Contravariância desce na árvore de tipos, como em `Animal` -> `Dog` -> `Pitbull`.

### Invariante

Invariante significa que não varia. Nem covariante nem contravariante. Se o tipo é `T`, então só
`T` é aceito. Esse foi bem mais simples.

Geralmente, tipos mutáveis são invariantes.
