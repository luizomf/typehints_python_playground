#
# O que é um "Callable" em Python?
# De forma simples, "callable" é qualquer coisa que pode ser "chamada", ou
# seja, executada usando parênteses `()`.
#
# Os exemplos mais comuns são:
#   - Funções (que criamos com `def`)
#   - Métodos (funções dentro de classes)
#   - As próprias Classes (para criar instâncias `MinhaClasse()`)
#   - Objetos que implementam o método especial `__call__`
#
# Descrevendo Assinaturas com `typing.Callable`
#
# Além de tipar os parâmetros e o retorno de uma função, às vezes precisamos
# dizer que uma variável ou um parâmetro é, ele mesmo, "do tipo função".
#
# Isso é muito comum em cenários mais avançados, como em decoradores ou em
# funções que recebem outras funções como argumento (conhecidas como
# "Higher-Order Functions" ou "HOF").
#
# Para esses casos, usamos o tipo especial `Callable` do módulo `collections.abc`.
# Ele nos permite criar um "contrato" ou uma "etiqueta" que descreve
# exatamente qual tipo de função esperamos receber.
#
# Agora, vamos ver tudo isso na prática!
#


def with_callback(
    x,
    y,
    callback,
) -> int:
    result = x + y
    callback(f"{result = }")
    return x + y


with_callback(2, 2, print)


def with_args(*args):
    print(*args)


def with_kwargs(*args, **kwargs):
    print("Args:", *args)
    print("Kwargs:", kwargs)  # Desempacotar aqui vai dar problema
