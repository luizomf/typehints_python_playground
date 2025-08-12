# O Princípio da Substituição de Liskov (LSP)

A Definição Formal de Barbara Liskov é bastante acadêmica:

> "What is wanted here is something like the following substitution property: If for each object
> `o1` of type `S` there is an object `o2` of type `T` such that for all programs `P` defined in
> terms of `T`, the behavior of `P` is unchanged when `o1` is substituted for `o2`, then `S` is a
> subtype of `T`."

Tradução literal:

> "O que se quer aqui é algo como a seguinte propriedade de substituição: se, para cada objeto
> `o1` do tipo `S`, existe um objeto `o2` do tipo `T`, de forma que, para todos os programas `P`
> definidos em termos de `T`, o comportamento de `P` permanece inalterado quando `o1` é
> substituído por `o2`, então `S` é um subtipo de `T`."

**Tradução livre:** `S` é subtipo de `T` **somente** se **qualquer programa** escrito para
funcionar com objetos do tipo `T` continuar se comportando **exatamente da mesma forma** quando
receber um objeto do tipo `S`, sem "perceber" a troca.

O ponto central: **não basta a tipagem bater, o comportamento também precisa ser compatível**.
Você pode ter um código perfeito para o type checker e mesmo assim quebrar o LSP se violar o
contrato do tipo base.

---

## Como verificar se o LSP está sendo respeitado

Um checklist clássico é baseado em três pontos: **pré-condições**, **pós-condições** e
**invariantes**. Se qualquer um for quebrado, o LSP também é.

---

### Assinaturas de métodos

- **Parâmetros:** No subtipo, devem ser **iguais ou mais genéricos** (**contravariantes**).
- **Retorno:** No subtipo, devem ser **iguais ou mais específicos** (**covariantes**).
- **Exceções:** O subtipo não deve lançar exceções que não sejam subtipos das lançadas pela
  superclasse.

Em Python, o `Callable` já é contravariante nos argumentos e covariante nos retornos.

E para saber qual exceção é subtipo de outra, veja a
[hierarquia de exceptions](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
do Python.

---

#### Lembrete rápido sobre variância:

Falamos sobre este assunto no vídeo
[Genéricos ABC, Covariância, Contravariância e Invariância no Python - Aula 5](https://youtu.be/26BdcuNAlys).
Mas só como um lembrete:

```text
Contravariância (entradas / parâmetros):
S <: T
Container[T] <: Container[S]

Covariância (saídas / retornos):
S <: T
Container[S] <: Container[T]

Invariância:
S <: T
Container[S] != Container[T]
```

---

### Pré-condições (inputs / parâmetros)

Pré-condições estão relacionadas aos parâmetros de entrada (ou inputs).

- **Regra:** O subtipo **não pode** ser mais restritivo que o tipo base.
- **Exemplo:** Se a classe pai aceita um container iterável com qualquer objeto interno de
  entrada, o filho não pode exigir uma lista de strings.

Por quê? Se o subtipo colocar mais barreiras, código que antes funcionava com o tipo base pode
falhar. Isso pode acontecer mesmo que a tipagem funcione perfeitamente.

Exemplo:

```python
class Tags:
    def __init__(self, tags: set[str]) -> None:
        self._tags = tags

    # Contrato amplo: aceita qualquer objeto
    def __contains__(self, item: object) -> bool:
        return item in self._tags  # Para tipo "errado", retorna False


class StrictTags(Tags):
    # 🚫 Pré-condição mais restritiva: agora só aceita str
    def __contains__(self, item: object) -> bool:
        if not isinstance(item, str):
            raise TypeError("item must be str")
        return item in self._tags


# Cliente escrito para o tipo base:
def has_tag(t: Tags, q: object) -> bool:
    return q in t


t1 = Tags({"python", "types"})
t2 = StrictTags({"python", "types"})

print(has_tag(t1, 123))  # False (ok no contrato do base)
print(has_tag(t2, 123))  # 💥 TypeError — subtipo ficou mais restritivo
```

No código acima, `Tags` aceita que qualquer `object` seja utilizado com `__contains__` (`in` e
`not in`). Mas `StrictTags` impõe que apenas `str` pode ser utilizado. O type checker não reclama,
mas o comportamento mudou, quebrando a pré-condição da classe base.

---

### Pós-condições (retorno / output)

- **Regra:** O subtipo **não pode** entregar menos do que o tipo base prometeu.
- **Exemplo:** Se o pai promete "retornar sempre um número positivo", o filho não pode retornar
  negativos.

Observação: Você pode **prometer mais** que o pai, mas nunca menos.

Um exemplo de algo que só retorna positivos no Python é o `__len__`. Este método é chamado ao usar
`len()` para saber quantos itens existem no container. Ou o container está vazio (0 itens) ou tem
elementos. Ele nunca terá uma quantidade negativa de itens.

```python
# Tipagem perfeita, mas pós-condição violada
class SizedProtocol:
    def __init__(self, data: list[int]) -> None:
        self._data = data

    def __len__(self) -> int:
        return len(self._data)  # Sempre >= 0 (contrato implícito do Python)

class BadSized(SizedProtocol):
    def __len__(self) -> int:
        return len(self._data) - 1  # 🚫 Pode gerar valor negativo (sutil)


bad_sized = BadSized([])  # Vazio, então seria zero, mas será -1
size = len(bad_sized)     # ValueError: __len__() should return >= 0
```

---

### Invariantes (verdades que sempre se mantêm)

**Regra:** O subtipo deve manter todos os invariantes do tipo base.

**Exemplo:**

```python
class DatabaseConfig:
    def __init__(self, dsn: str) -> None:
        self._dsn = dsn

    @property
    def dsn(self) -> str:
        return self._dsn


class MySqlDatabaseConfig(DatabaseConfig):
    def __init__(self, host: str, user: str, password: str, db: str) -> None:
        # Não tem DSN, mas força herança para "reaproveitar" métodos
        self.host = host
        self.user = user
        self.password = password
        self.db = db

        # Apenas inicializa a base com valor vazio (quebrando a invariante)
        super().__init__("")


def connect(cfg: DatabaseConfig) -> None:
    # Cliente depende da invariante DatabaseConfig.dsn
    print("Connecting to:", cfg.dsn)


cfg_bad = MySqlDatabaseConfig(host="", user="root", password="", db="app")
connect(cfg_bad)  # ❌ imprime DSN vazio; quebra a invariante
```

No exemplo acima, `DatabaseConfig` foi projetada para trabalhar com `dsn` como parte obrigatória.
O subtipo herda a classe mas ignora essa regra, inicializando com valor vazio. Isso quebra o
contrato implícito de que `dsn` sempre está configurado.

Uma forma de resolver seria:

- Extrair métodos compartilhados para outra classe/módulo, evitando herança forçada.
- Padronizar todas as subclasses para realmente usarem `dsn` no mesmo formato.

---

## Por que isso importa?

O LSP é fácil de quebrar sem perceber. Não é preciso "herança do mal" nem mudar tipagem — um
simples detalhe de lógica já quebra o contrato. Muitos desses bugs são sutis e podem viver
despercebidos por anos… até que um dia 💥💥💥.

---
