import sys
from typing import Never, NoReturn

from utils import cyan_print, sep_print

################################################################################
#
# Never vs NoReturn: Qual é a DIFERENÇA em Python? (Aula 18)
#
# Ambos, `Never` e `NoReturn` indicam um "Bottom Type" (um tipo que é subtipo de
# todos os outros tipos). Se você entendeu tudo até aqui, vai perceber que o
# "Bottom Type" é o extremo oposto do `object`, que é um "Top Type".
#
# Obs.: `Any` também é um "Top Type", mas ele desliga o Type Checker.
#
# Como `Never` e `NoReturn` são subtipos de todos os outros tipos, eles não
# podem ser nenhum tipo. Isso é estranho, mas isso acontece muito no código.
# Por exemplo: uma função que lança uma exceção ou usa `sys.exit()` para terminar
# o programa, NUNCA RETORNA UM VALOR (ambos `Never` e `NoReturn` funcionariam aqui).
#
# Qual a diferença? O nome... Ficaria estranho adicionar o nome `NoReturn` em
# um local onde você não está retornando nada. Mas hoje em dia, ambos são
# tratados de forma equivalente pelos Type Checkers.
#
################################################################################


def quit_program() -> NoReturn:  # mais "clássico" para retorno
    # Nada abaixo dessa função será executado
    sys.exit(0)


def no_return_func() -> NoReturn:
    # Nada abaixo dessa função será executado
    raise RuntimeError


def never() -> Never:
    # Nada abaixo dessa função será executado
    raise RuntimeError


def ask_user() -> Never:  # mais "didático" fora do retorno
    while True:
        answer = input("Digite algo")
        exit_words = "q", "quit"

        if answer.lower() in exit_words:
            cyan_print("Bye 👋")
            quit_program()
            print("Isso é impossível")

        cyan_print(f"ECHO: {answer}")

    print("Isso é impossível")


if __name__ == "__main__":
    sep_print()

    should_run = True

    if should_run:
        print("Seu script vai rodar normal")
    else:
        # Proposital
        never()  # Olha só que nome estranho
        print("Isso é impossível")

    sep_print()

################################################################################
