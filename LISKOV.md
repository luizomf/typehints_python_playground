# O Princípio da Substituição de Liskov (LSP)

## A Definição Formal (Barbara Liskov, 1988)

Em 1988, Barbara Liskov formalizou o princípio de forma bastante acadêmica:

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
funcionar com objetos do tipo `T` continuar operando **exatamente da mesma forma** quando receber
um objeto do tipo `S`, sem "perceber" a troca.

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

_Em Python, o `Callable` já é contravariante nos argumentos e covariante nos retornos._

---

#### Lembrete rápido sobre variância:

```text
Covariância (saídas / retornos):
S <: T
Container[S] <: Container[T]

Contravariância (entradas / parâmetros):
S <: T
Container[T] <: Container[S]

Invariância:
S <: T
Container[S] != Container[T]
```

---

### Pré-condições

Pré-condições estão relacionadas aos parâmetros de entrada (ou inputs).

- **Regra:** O subtipo **não pode** ser mais restritivo que o tipo base.
- **Exemplo:** Se a classe pai aceita "qualquer inteiro", o filho não pode exigir "apenas inteiros
  positivos".

Por quê? Se o subtipo colocar mais barreiras, código que antes funcionava com o tipo base pode
falhar. Isso pode acontece mesmo que a tipagem bata perfeitamente.

```python
# Tipagem perfeita
class SizedProtocol:
    def __len__(self) -> int:
        return len(self._data)

class BadSized(SizedProtocol):
    def __len__(self) -> int:
        return len(self._data) - 1 # sutil, mas em algum momento vai dar -1


bad_sized = BadSized()
size = len(bad_sized) # -1
```

---

### Pós-condições (o que o método promete entregar)

- **Regra:** O subtipo **não pode** entregar menos do que o tipo base prometeu.
- **Exemplo:** Se o pai promete "retornar sempre um número positivo", o filho não pode retornar
  negativos.

Observação: Você pode **prometer mais** que o pai, mas nunca menos.

```python
class Base:
    def get_positive_int(self) -> int:
        return 42  # Sempre positivo

class Sub(Base):
    def get_positive_int(self) -> int:
        return -1  # 🚫 Quebrou a promessa

b: Base = Sub()
print(b.get_positive_int())  # Cliente espera positivo, recebe negativo
```

---

### Invariantes (verdades que sempre se mantêm)

**Regra:** O subtipo deve manter todos os invariantes do tipo base.

**Exemplo:**

- Tipo base (`BankAccount`): valor da conta não fica negativo.
- Subtipo (`OverdraftAccount`): fica negativo.

Resultado: o subtipo quebrou a invariante do tipo base.

```python
class BankAccount:
    def __init__(self) -> None:
        self.balance = 0.0

class OverdraftAccount(BankAccount):
    def __init__(self) -> None:
        super().__init__()
        self.balance = -100.0  # 🚫 invariante quebrado
```

---

## Por que isso importa?

O LSP é fácil de quebrar sem perceber. Não é preciso "herança do mal", um simples detalhe já
quebra o contrato.

Exemplo: [`liskov2.py`](liskov2.py)

```python
class MediaPlayer:
    max_volume = 100

class FancyMediaPlayer(MediaPlayer):
    # Limita volume a 90 "para proteger os ouvidos"
```

Problemas:

1. **Pré-condição mais restritiva:** não aumenta acima de 90.
2. **Pós-condição mais fraca:** não atinge o máximo prometido (100).
3. **Invariante quebrado:** `max_volume` deixa de ser realmente o volume máximo atingível.

Resultado: código que confiava no contrato do `MediaPlayer` pode falhar, mesmo que a tipagem
esteja correta.

---
