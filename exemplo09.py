#
# Hello World!
#
class Animal: ...


class Cat(Animal): ...


def wants_cats(cats: list[Cat]) -> None: ...
def delivers_cats() -> list[Cat]: ...
def delivers_animals() -> list[Animal]: ...


a: list[Animal] = []
c: list[Cat] = []

wants_cats(delivers_cats())
wants_cats(delivers_animals())

# Isso é porque bool é um subtipo de int (0 e 1)
# Covariância -> int -> bool
boolean: int = 0
boolean = False
boolean = True
boolean = "False"  # Error: Isso é subtipo de str (Literal["False"])
