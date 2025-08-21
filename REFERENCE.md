# Referência das aulas

## Aulas já gravadas

Já gravei isso:

- Type Hints no Python: Do BÁSICO ao AVANÇADO - Aula 1
- Type Hints em Funções e Callable no Python - Aula 2
- Type Hints em Classes e Herança (Tipagem Nominal) - Aula 3
- Type Hints em Classes com ABC, Dataclass, Self, ClassVar e mais - Aula 4
- Entenda Covariância, Contravariância e Invariância com Genéricos ABC no Python - Aula 5
- Aprenda a implementar um Genérico com Sequence (ABC) - Aula 6
- Entenda o Princípio da Substituição de Liskov (LSP) - Aula 7
- TypeVar e Funções Genéricas no Python 3.13 (Nova Sintaxe, PEP 695) - Aula 8
- Classes Genéricas e TypeVar no Python 3.13 - Aula 9
- Protocol e Structural Subtyping no Python 3.13 - Aula 10
- Composição de Protocolos e o Interface Segregation Principle (SOLID) - Aula 11
- Protocol x ABC + Padrão de projeto Template Method no Python - Aula 12
- Callback Protocols no Python: do básico ao avançado - Aula 13
- TypedDict - CHEGA de dicionários com tipagem fraca em Python - Aula 14

## O que ainda falta

Montei essa ordem no chute, não sei se seria a melhor.

- **NewType**
- **TypeGuard & TypeIs**
- **ParamSpec & Concatenate**
- **TypeVarTuple & Unpack**
- **Callback Protocols + ParamSpec (avanço)**
- **Never & NoReturn**
- **Outras coisas específicas**

## 1) ParamSpec & Concatenate — Decorators que preservam assinatura

**Título:** Decorators Tipados com ParamSpec & Concatenate (PEP 612) **Foco:** como não perder a
assinatura original em decorators; adicionar args antes/depois. **Exemplo-âncora:**

- `retry[T, P](fn: Callable[P, T]) -> Callable[P, T]` (preserva parâmetros).
- `with_request[P, R](fn: Callable[P, R]) -> Callable[Concatenate[Request, P], R]` para
  middlewares web. **Gotchas:** diferença de `ParamSpec` vs `TypeVar`; onde usar
  `.args`/`.kwargs`; evitar “decorator sem wrapper”.

---

## 2) Callback Protocols + ParamSpec (parte 2)

**Título:** Callback Protocols Avançados: ParamSpec na prática **Foco:** contrato nomeado com
`__call__` **e** `ParamSpec` para “embrulhar” qualquer callable sem perder tipos.
**Exemplo-âncora:**

- `Around[P, R]: Protocol` →
  `def __call__(self, fn: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R`
- `with_logging(around: Around[P, R], fn: Callable[P, R]) -> Callable[P, R]` **Gotchas:**
  `Callable[..., R]` vs preservação com `P`; quando `Callable` é suficiente.

---

## 3) TypedDict moderno — Required/NotRequired/total e ReadOnly

**Título:** TypedDict no Mundo Real: Required, NotRequired e total=False (PEP 655) **Foco:**
modelar payloads/JSON, campos obrigatórios e opcionais, migração incremental. **Exemplo-âncora:**

- `class User(TypedDict, total=False): id: int; name: Required[str]; email: NotRequired[str]`
- “validação leve” + `match/case` em responses. **Gotchas:** `total` vs `Required/NotRequired`;
  `dict` normal aceitanto extras; quando preferir `dataclass`/Pydantic.

> Se quiser, inclua **`ReadOnly`** para campos imutáveis (em 3.13 está disponível; historicamente
> veio do `typing_extensions`).

---

## 4) TypeGuard & TypeIs — Afunilamento de tipos sob medida

**Título:** Ensine o Checker a Pensar: TypeGuard e TypeIs **Foco:** criar guardas de tipo para
APIs dinâmicas. **Exemplo-âncora:**

- `def is_non_empty_str(x: object) -> TypeGuard[str]: ...`
- `def is_status_ok(r: Response) -> TypeIs[Success]: return r["status"] == "ok"` **Gotchas:**
  diferença **TypeGuard** (aceita qualquer input) vs **TypeIs** (refina de A para B); cuidado com
  efeitos colaterais no guard.

---

## 5) NewType & “branding” — IDs com segurança

**Título:** NewType: IDs Seguros sem Custos em Runtime **Foco:** evitar trocar `UserId` por
`OrderId` por engano. **Exemplo-âncora:**

- `UserId = NewType("UserId", int)`, `OrderId = NewType("OrderId", int)`; funções que exigem o
  tipo certo. **Gotchas:** `NewType` não é subclasse real; conversão explícita; quando preferir
  `dataclass(frozen=True)`.

---

## 6) Never, NoReturn e exaustividade

**Título:** Never & NoReturn: Falhas, Aborts e Checagem Exaustiva **Foco:** modelar funções que
_não retornam_ e ramos impossíveis. **Exemplo-âncora:**

- `def fail(msg: str) -> NoReturn: raise RuntimeError(msg)`
- `match status: case "ok": ... case "error": ... case _: assert_never(status)` com
  `def assert_never(x: Never) -> NoReturn: ...` **Gotchas:** diferença sutil entre `NoReturn`
  (comportamento) e `Never` (tipo vazio).

---

## 7) Variadic Generics — TypeVarTuple & Unpack (PEP 646)

**Título:** Generics Variádicos: TypeVarTuple & Unpack **Foco:** shapes/tuplas de tamanho
variável, formatação, CSVs, pipelines. **Exemplo-âncora:**

- `def first[*Ts](t: tuple[*Ts]) -> Ts[0]: ...`
- `class Row[*Cols]: def __init__(self, *cols: *Cols): ...` **Gotchas:** quando faz sentido vs
  complicação gratuita; `Unpack` em `TypedDict` não existe (só `TypedDict` especial).

---

## 8) ReadOnly/Final/Override e propriedades imutáveis

**Título:** Imutabilidade e Contratos de Classe: ReadOnly, Final e Override **Foco:** congelar
atributos, impedir sobrescrita, garantir sobrescrita correta. **Exemplo-âncora:**

- `class Config: url: ReadOnly[str]`
- `@final` em métodos utilitários; `@override` (quando disponível) para evitar erros de
  assinatura. **Gotchas:** imutabilidade “só estática”; uso com Protocols (preferir `@property`
  read-only).

---

## 9) Bônus curto — LiteralString e segurança de APIs de formatação

**Título:** LiteralString: Strings Seguras para Formatação **Foco:** restringir APIs que recebem
padrões de formatação/SQL/templating. **Exemplo-âncora:**

- `def log(fmt: LiteralString, /, *args: object) -> None: ...` **Gotchas:** não “sanitiza”
  runtime; é defesa estática.

---
