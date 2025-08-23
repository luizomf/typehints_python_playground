# TypeIs vs TypeGuard (PEP 742 & 647)

**Tema:** Predicados de tipo em Python (narrowing controlado pelo usuário)

---

## Objetivo (para o aluno)

- Entender **o que** são `TypeIs` e `TypeGuard`.
- Saber **quando** usar cada um.
- Evitar **armadilhas** (predicados não _sound_).

---

## Definições rápidas

- **`TypeIs[T]`** → predicado _simples_ que garante que **um valor** é do tipo `T`. Também
  estreita o tipo no ramo `else` ("não é T").
- **`TypeGuard[T]`** → predicado _geral_ para garantir que **uma estrutura inteira** (lista, dict,
  união mais complexa) pode ser tratada como `T`.

> Regra de bolso: **Valor escalar/união simples → `TypeIs`**. **Coleção/estrutura → `TypeGuard`**.

---

## Árvore de decisão (rápida)

```
Quer refinar UM valor?
  └─ Sim → TypeIs[T]
Quer refinar UMA COLEÇÃO/ESTRUTURA inteira?
  └─ Sim → TypeGuard[T]
Checagem é 100% confiável?
  └─ Não → Não use nenhum; retorne bool normal
```

---

## Exemplos — `TypeIs` (3 casos)

### 1) Escalar simples

```python
from typing import TypeIs

def is_str(x: object) -> TypeIs[str]:
    return isinstance(x, str)

value: object = "hello"
if is_str(value):
    value.upper()  # value: str aqui
else:
    ...  # value: not str aqui
```

### 2) União discriminada (TypedDict + Literal)

```python
from typing import TypedDict, Literal, TypeIs

class Circle(TypedDict):
    kind: Literal["circle"]
    radius: float

class Rect(TypedDict):
    kind: Literal["rect"]
    w: float
    h: float

Shape = Circle | Rect

def is_circle(s: Shape) -> TypeIs[Circle]:
    return s.get("kind") == "circle"

shape: Shape = {"kind": "circle", "radius": 2.0}
if is_circle(shape):
    area = 3.14159 * shape["radius"] ** 2  # shape: Circle
else:
    area = shape["w"] * shape["h"]         # shape: Rect
```

### 3) `None` seguro com ramo `else` útil

```python
from typing import TypeIs

def is_none(x: object) -> TypeIs[None]:
    return x is None

maybe_id: int | None = 123
if is_none(maybe_id):
    ...  # aqui é None
else:
    assert maybe_id % 3 == 0  # aqui é int (não-None)
```

---

## Exemplos — `TypeGuard` (3 casos)

### 1) Lista homogênea

```python
from typing import TypeGuard

def is_str_list(xs: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in xs)

values: list[object] = ["a", "b", "c"]
if is_str_list(values):
    values.append("ok")  # values: list[str]
```

### 2) Dicionário com chaves **e** valores tipados

```python
from typing import TypeGuard

def is_dict_str_int(d: dict[object, object]) -> TypeGuard[dict[str, int]]:
    return all(isinstance(k, str) and isinstance(v, int) for k, v in d.items())

raw: dict[object, object] = {"age": 39, "lvl": 9000}
if is_dict_str_int(raw):
    reveal = raw["age"] + 1  # raw: dict[str, int]
```

### 3) Lista de união → lista específica (TypedDict)

```python
from typing import TypeGuard, TypedDict, Literal

class Circle(TypedDict):
    kind: Literal["circle"]
    radius: float

class Rect(TypedDict):
    kind: Literal["rect"]
    w: float
    h: float

Shape = Circle | Rect

def all_circles(xs: list[Shape]) -> TypeGuard[list[Circle]]:
    return all(x.get("kind") == "circle" and "radius" in x for x in xs)

shapes: list[Shape] = [
    {"kind": "circle", "radius": 2.0},
    {"kind": "circle", "radius": 1.5},
]

if all_circles(shapes):
    areas = [3.14159 * s["radius"] ** 2 for s in shapes]  # shapes: list[Circle]
```

---

## Armadilhas e boas práticas

- **Soundness**: a função deve **garantir** o tipo declarado. Se houver dúvida/heurística, **não
  use** `TypeIs/TypeGuard`.
- **Retorno é `bool`**: os predicados retornam `True/False` de verdade (não invente outros tipos
  retornados).
- **`TypeIs` é ponto-a-ponto**: pense nele como um `isinstance` "tipado" para um valor.
- **`TypeGuard` é estrutural**: valide **todos** os elementos/atributos necessários.
- **Nomeie como guard**: `is_*`, `has_*`, `looks_like_*`.

---

## Compatibilidade

- Python **3.13+**: `from typing import TypeIs, TypeGuard`.
- Python **< 3.13** (quando necessário): `from typing_extensions import TypeIs  # e/ou TypeGuard`.

---

## Cheatsheet (1 slide)

- **Use `TypeIs[T]`** quando o **valor** vira `T`.
- **Use `TypeGuard[T]`** quando a **estrutura inteira** vira `T`.
- **`else` útil**: `TypeIs` estreita também o ramo negativo ("não T").
- **Se não tiver 100% de certeza**, volte para `bool`.

---

## Notas para o instrutor (bullet points rápidos)

- Diga que `TypeIs` resolve o caso comum e foi pensado para ser mais intuitivo.
- Mostre que `TypeGuard` continua necessário para coleções e validações estruturais.
- Alerte: predicados mal escritos **enganam** o checker (não são verificados em tempo de tipo).
- Reforce a convenção de nomes (`is_*`) e o retorno `bool`.
- Dica final: teste com `pyright --verifytypes`/`mypy` e use `reveal_type` nos exemplos.
