# O Princípio da Substituição de Liskov (LSP)

## A Definição Formal (Por Barbara Liskov)

A definição original, proposta por Barbara Liskov em 1988, é bem "acadêmica":

> "What is wanted here is something like the following substitution property: If for each object
> `o1` of type `S` there is an object `o2` of type `T` such that for all programs `P` defined in
> terms of `T`, the behavior of `P` is unchanged when `o1` is substituted for `o2`, then `S` is a
> subtype of `T`."

> "O que se quer aqui é algo como a seguinte propriedade de substituição: se, para cada objeto
> `o1` do tipo `S`, existe um objeto `o2` do tipo `T`, de forma que, para todos os programas `P`
> definidos em termos de `T`, o comportamento de `P` permanece inalterado quando `o1` é
> substituído por `o2`, então `S` é um subtipo de `T`."

**Tradução livre:** `S` é um subtipo de `T` **somente** se **qualquer programa** escrito para
trabalhar com objetos do tipo `T` continuar funcionando **exatamente da mesma forma** quando
receber um objeto do tipo `S`, sem o programa "perceber" a troca.

Ou seja: não basta só _bater a tipagem_. O **comportamento** também precisa ser compatível. Você
pode ter um código 100% aceito pelo type checker e mesmo assim quebrar o LSP se violar o contrato
que o tipo base estabeleceu.

O ponto central é: **o cliente não pode ser surpreendido pelo comportamento do subtipo**.

---

## Como identificar se o LSP está sendo respeitado

Uma forma prática (e clássica) de avaliar isso é usando três regras: pré-condições, pós-condições
e invariantes.

Se qualquer uma delas for quebrada, o LSP também é.

### Assinaturas dos Métodos

- Os tipos dos parâmetros no subtipo devem ser **iguais ou mais genéricos** (contravariantes) do
  que no tipo base.
- O tipo de retorno deve ser **igual ou mais específico** (covariante).
- O subtipo não pode lançar exceções que não sejam subtipos das lançadas pela superclasse.

Em Python, o type checker ajuda aqui: `Callable` já é contravariante nos argumentos e covariante
nos retornos.

---

### Pré-condições (o que a função exige para rodar)

- **Regra:** O subtipo **não pode** ser mais restritivo do que o tipo base.
- **Tradução:** Se o pai aceita "qualquer número inteiro", o filho não pode exigir "apenas
  inteiros positivos".

Se o subtipo coloca mais obstáculos antes de executar, o cliente que antes funcionava com o tipo
base pode falhar.

---

### Pós-condições (o que a função promete entregar)

- **Regra:** O subtipo **não pode** enfraquecer as promessas do tipo base.
- **Tradução:** Se o pai promete "retornar sempre um número positivo", o filho não pode devolver
  números negativos.

Você pode **prometer mais** que o pai, mas nunca menos.

---

### Invariantes (verdades que sempre se mantêm)

- **Regra:** O subtipo precisa preservar todos os invariantes do tipo base.
- **Tradução:** As regras internas e o estado consistente do pai não podem ser quebrados pelo
  filho.

Exemplo: use o arquivo `liskov.py` para acompanhar.

`Square` herdando de `Rectangle`. O invariante do retângulo é que largura e altura são
independentes. O quadrado, para manter seu próprio invariante ("lados iguais"), quebra o do pai, e
aí qualquer código que espera alterar só a largura de um retângulo se surpreende.

---

## Por que isso importa?

O LSP é fácil de quebrar sem perceber. Não precisa fazer herança "do mal" nem mudar completamente
a lógica: basta alterar um detalhe e o contrato do tipo base já era.

Exemplo: use o arquivo `liskov2.py` para acompanhar.

`MediaPlayer`, a classe base promete que, se você chamar `increase_volume()` `max_volume` vezes, o
volume vai chegar ao máximo. No `FancyMediaPlayer`, a intenção era só "proteger os ouvidos" e
limitar o volume, mas isso:

- Colocou **pré-condição mais restritiva** (não aumenta após 90 em vez de 100).
- Entregou **pós-condição mais fraca** (não chega no valor prometido).
- Quebrou **invariante** (o `max_volume` deixou de ser realmente o volume máximo atingível).

Resultado: qualquer função que use a API do tipo base (`MediaPlayer`) e conte com esse contrato
pode falhar, mesmo que a tipagem esteja perfeita.

---
