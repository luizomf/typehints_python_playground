# O Princípio da Substituição de Liskov (LSP)

## A Definição Formal (Por Barbara Liskov)

A definição original, proposta por Barbara Liskov em 1988, é um pouco mais
acadêmica:

> "What is wanted here is something like the following substitution property: If
> for each object `o1` of type `S` there is an object `o2` of type `T` such that
> for all programs `P` defined in terms of `T`, the behavior of `P` is unchanged
> when `o1` is substituted for `o2`, then `S` is a subtype of `T`."

**Nota:** pode ler quantas vezes quiser, tome seu tempo 🤣.

O que eu entendo do que ela dizer é o seguinte:

`S` é um subtipo de `T` somente se **qualquer programa** que foi escrito para
funcionar com objetos do tipo `T` continue funcionando **exatamente da mesma
forma** se você passar para ele um objeto do tipo `S`, sem que o programa nem
"perceba" a troca.

Ela está falando do **comportamento** dos objetos e não dos tipos. Você poderia
escrever um programa com tipagem perfeita e ainda "quebrar" o LSP.

O programa não pode ser surpreendido pelo comportamento do subtipo.

## Vamos às regras

Para que o comportamento não seja alterado, um "bom subtipo" (`S`) deve aderir a
um contrato estabelecido pela sua superclasse (`T`). Esse contrato é definido
por um conjunto de regras:

### Assinaturas dos Métodos:

- Os tipos dos parâmetros dos métodos no subtipo devem ser os mesmos ou mais
  abstratos (contravariantes) que na superclasse.
- O tipo de retorno no subtipo deve ser o mesmo ou mais específico (covariante)
  que na superclasse.
- O subtipo não pode lançar exceções que não sejam subtipos das exceções
  lançadas pela superclasse.

### Pré-condições (o que a função exige para rodar):

- **Regra:** Uma pré-condição de um método no subtipo não pode ser mais forte
  (mais restritiva) que a da superclasse.
- **Tradução:** O filho não pode ser mais exigente que o pai. Se o método do pai
  aceita qualquer número (`int`), o método do filho não pode passar a exigir
  apenas números positivos.

### Pós-condições (O que a função promete entregar no final):

- **A Regra:** Uma pós-condição de um método no subtipo não pode ser mais fraca
  que a da superclasse.
- **Tradução:** O filho tem que cumprir todas as promessas do pai, e pode até
  prometer mais, mas nunca menos.

### Invariantes (As verdades que devem ser sempre mantidas pela classe):

- **A Regra:** Os invariantes da superclasse devem ser preservados pelo subtipo.
- **Tradução:** As regras internas e o estado consistente da classe pai não
  podem ser quebrados pelo filho.
- **Conexão com o Exemplo:** **É exatamente aqui que o `Square` falha!** O
  "invariante" de `Rectangle` (uma de suas verdades internas) é que sua largura
  e altura são propriedades independentes. A classe `Square`, para manter seu
  próprio invariante ("os lados devem ser sempre iguais"), quebra o invariante
  da sua superclasse. E é essa quebra de invariante que surpreende a função
  `use_rectangle`.
