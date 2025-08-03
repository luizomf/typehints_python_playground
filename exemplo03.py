#
# Funções
#
# É necessário tipar todos os parâmetros e o retorno de funções.
#


def add(x, y):
    return x + y


def with_callback(x, y, callback):
    result = x + y
    callback(f"{result = }")
    return x + y


def with_args(*args):
    print(*args)


def with_kwargs(*args, **kwargs):
    print("Args:", *args)
    print("Kwargs:", kwargs)  # Desempacotar aqui vai dar problema
