#
# Genéricos padrão em Collections ABC
#
# Doc: https://docs.python.org/3/library/collections.abc.html
#
# Como vimos antes, podemos usar as coleções padrão do Python para tipagem. Ou
# seja: `list[T]`, `dict[K, V]`, `tuple[T, ...]`, etc...
# Mas, isso deixa o meu código fixado no tipo escolhido. Uma função que recebe
# uma `list[str]` só pode receber `list[str]` e nada mais... E daí?
#
# Isso vai contra o Princípio da Robustez ou Lei de Postel, que diz:
#
# "Seja liberal no que você aceita, e conservador no que você retorna."
#
# Em resumo: para parâmetros que recebemos, devemos usar o tipo mais abstrato,
# enquanto nos retornos usamos valores mais restritos.
#
# Isso faz muito sentido quando você pensa em como um código funciona. Se uma
# função aceita algo que você pode percorrer (iterável), uma lista cumpre o
# papel, mas restringe todos os outros tipos que podem ser percorridos.
# Por outro lado, se uma função diz que vai retornar uma lista, o desenvolvedor
# que vai usar a função saberá os métodos que pode usar nessa lista sem quebrar
# o programa.
#


from collections.abc import Iterable


# Antes: def concat(items: list[str]) -> str:
def concat(items: Iterable[str]) -> str:
    return "".join(items)


items_list = ["a", "b", "c"]
items_str = "abc"
items_tuple = "a", "b", "c"
items_set = {"a", "b", "c"}
items_dict = {"a": None, "b": None, "c": None}

list_result = concat(items_list)  # só isso era aceitável
str_result = concat(items_str)  # Antes: Não aceitava
tuple_result = concat(items_tuple)  # Antes: Não aceitava
set_result = concat(items_set)  # Antes: Não aceitava
dict_result = concat(items_dict)  # Antes: Não aceitava

print(f"{list_result = !r}")
print(f"{str_result = !r}")
print(f"{tuple_result = !r}")
print(f"{set_result = !r}")
print(f"{dict_result = !r}")
