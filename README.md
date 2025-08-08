# typehists_pg

PEPs para ler:

PEP 484 - Type Hints: O início de tudo. https://peps.python.org/pep-0484/  
PEP 544 - Protocols: Introduz a tipagem estrutural.
https://peps.python.org/pep-0544/  
PEP 612 - Parameter Specification Variables: A introdução do ParamSpec e
Concatenate. https://peps.python.org/pep-0612/

https://typing.python.org/en/latest/index.html  
https://mypy.readthedocs.io/en/stable/kinds_of_types.html  
https://realpython.com/python-type-checking/

## Notas

`Any` pode ser considerado um tipo que aceita qualquer valor e assume ter
qualquer atributo ou método. Ele é um tipo estrutural especial, usado para
desativar temporariamente a verificação de tipos.

Já `object` é o tipo base nominal de todas as classes em Python, todo valor é um
`object`.

A diferença é que você pode passar um `Any` onde se espera um `int`, uma `str`,
ou qualquer outro tipo, sem erro; mas não pode passar um `object` onde se espera
um `int`, porque o `object` não garante os métodos e atributos do `int`.

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

### Covariância

Covariância geralmente indica que o tipo é seguro na saída (output), mas não
seguro na entrada (input).

Um exemplo de input e output seria um `Callable[[Input], Output]`, onde `Input`
são os argumentos e o `Output` o retorno. Então a covariância ocorre no retorno.

Se um tipo `Dog` é subtipo de `Animal`, então um tipo `Box[Dog]` é um subtipo de
`Box[Animal]` (esse cenário é intuitivo).

Se uma função tem que retornar `Box[Animal]`, então é aceitável retornar
`Box[Dog]`.

Covariância sobe na árvore de tipos, como em `Pitbull` -> `Dog` -> `Animal`.

### Contravariância

Contravariante geralmente indica que o tipo é seguro na entrada (input).

Se um tipo `Dog` é um subtipo de `Animal`, então um tipo `Box[Animal]` é um
subtipo de `Box[Dog]` (isso é muito contra intuitivo).

Em Python isso ocorre com `Callable`, que é covariante no retorno e
contravariante nos argumentos.

A dica da PEP 483 é que você deve usar tipos mais abrangentes nos argumentos e
mais específicos nos retornos.

Ainda seguindo exemplos da PEP 483, `Callable[[A], None]` seria subtipo de
`Callable[[B], None]`.

Contravariancia desce na árvore de tipos, como em `Animal` -> `Dog` ->
`Pitbull`.

### Invariante

Invariante significa que não varia. Nem covariante nem contravariante. Se o tipo
é `T`, então só `T` é aceito. Esse foi bem mais simples.

Geralmente, tipos mutáveis são invariantes.
