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

Se `B` é subtipo de `A`, `B` é `A` (`B` is `A`). Mas `A` nunca por ser `B`,
porque `B` pode ter coisas mais específicas que `A`.

Analogia: um `Cachorro` é um subtipo de um `Animal`, mas um `Animal` não é um
subtipo de `Cachorro`. O `Cachorro` pode latir, mas nem todo `Animal` pode
latir.

Subtipagem nominal é quando um tipo é subtipo de outro tipo via herança. A
relação `é um` significa `Cachorro` é um `Animal`. Nesse caso, `Cachorro` herda
de animal.

Subtipagem estrutural é quando um tipo tem os atributos requeridos em um
protocolo, mas podem não ter relação entre si.

Um tipo `t1` é constistente com um tipo `t2` se `t1` for um subtipo de `t2`. O
contrário não é verdadeiro.

```python
# Consider: Address and MySubAddress(Address)
address: Address
address = MySubAddress("a", 123)  # OK! MySubAddress is a subtype of Address

sub_address: MySubAddress
sub_address = Address("a", 123)  # Error! The inverse relation is not safe
```

`Any` pode ser considerado um tipo que aceita qualquer valor e assume ter
qualquer atributo ou método. Ele é um tipo estrutural especial, usado para
desativar temporariamente a verificação de tipos.

Já `object` é o tipo base nominal de todas as classes em Python, todo valor é um
`object`.

A diferença é que você pode passar um `Any` onde se espera um `int`, uma `str`,
ou qualquer outro tipo, sem erro; mas não pode passar um `object` onde se espera
um `int`, porque o `object` não garante os métodos e atributos do `int`.

- Um genérico pode ter variância: ser covariant ou contravariant
- Um genérico invariant é um container que aceita `T` e apenas `T`
