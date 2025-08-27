# TODO: CRIAR TÍTULO

TODO: Digitar uma pequena introdução para o artigo.

---

## Este texto não é para iniciantes com NeoVim

Neste tutorial, vou assumir que você já tem algum conhecimento sobre o `nvim`. Porém, vou deixar
alguns vídeos que podem ser úteis para você sobre meu ambiente Dev e comandos Unix que são muito
usados em conjunto com o `nvim`:

- [Ambiente de Desenvolvimento Dev 2025](https://youtu.be/mhudacg8f_A?si=3EvlUS0SsOrLGmUZ)
- [Comandos Unix que todo programador deveria saber](https://youtu.be/UQBAytRBNiM?si=pOfQNmAeGxvv3vgP)

---

## Pare de usar tanto `hjkl`

Eu sei que você já deve saber disso, mas não existem apenas os comandos `hjkl` para mover o cursor
no `vim` (ou `nvim` tanto faz). Eu também sofro desse mal e estou tentando mudando aos poucos.

Por exemplo:

- `w` - move para o início da próxima palavra
- `W` - move para o início da próxima palavra pulando pontuações
- `b` - move para o início da palavra anterior
- `B` - move para o início da palavra anterior pulando pontuações
- `e` - move para o final da próxima palavra
- `E` - move para o final da próxima palavra pulando pontuações
- `ge` - move para o final da palavra anterior
- `gE` - move para o final da palavra anterior pulando pontuações

Isso não é tão impressionante, mas já aumenta MUITO a velocidade que você se move dentro do
buffer.

---

### Combinações

Agora, se o trecho anterior ainda não te impressionou, vamos combinar o que vimos com outras
coisas.

- Quero selecionar 4 palavras para frente: `v4e`
- Quero selecionar a palavra abaixo do cursor mais 3 palavras para trás: `viwo3b`

No primeiro comando, `v` entra no modo `VISUAL`, `4` conta o que vier na frente, no caso `e` (da
lista anterior). O problema desse comando é que o ponto de partida é onde o cursor está, isso pode
pegar metade de palavras.

O segundo comando já une um monte de coisa. O `viw` entra no modo visual e seleciona a palavra
abaixo do cursor de ponta a ponta. Já o `o` inverte a posição do cursor na seleção, se está no
final vai para o início e vice versa. Por fim, `3b` move o cursor para o início da palavra
anterior 3 vezes (3 palavras para trás).

O mais interessante desses comandos é que ambos te deixam com uma seleção, então `y` (yank) copia,
`d` apaga, `c` apaga e entra no modo de edição... Enfim, permite você fazer o que quiser com a
seleção. Por exemplo, `viwo3bd` apaga 4 palavras para trás (a que está abaixo do cursor e 3 para
trás).

Se você quer mais precisão, onde o número bate certinho com a quantidade de palavras, é só mudar a
fórmula. Olha lá na lista anterior e veja o que isso aqui faz: `veo3b`?

Se você está no meio de uma palavra, `v` entra no `VISUAL`, `e` vai para o final da palavra atual,
`o` inverte o cursor da seleção, `3b` vai para o início das 3 palavras anteriores (atual mais
duas). Em resumo, `veo3b` seleciona 3 palavras para trás a partir do meio a palavra atual.

---

## Text Objects? Como uso isso?

Se você não sabe disso, provavelmente vai viciar nos comandos que vou te mostrar nessa parte. Bora
lá!

O `vim` tem o conceito de "Text Objects". Todo mundo lança esse termo como se fosse algo
extremamente óbvio, e claramente não é (já que estou pesquisando isso nesse exato momento para te
falar).

O fato é que "Text Object" é um conceito que descreve uma região do texto definida de acordo com a
lógica do texto em questão! (pareceu que sei do que estou falando? Nem eu entendi a frase!)

Brincadeiras à parte, no meu entendimento, Text Object indica uma ação que pode ser feita de forma
bidirecional ao invés de apenas em uma direção, como é o caso de `hjkl` ou até os `w`, `b`, `e`
... que vimos antes. Calma, calma... Antes de me xingar, eu já vou fazer você entender isso,
continua lendo que estamos indo há algum lugar com isso...

---

### Inner (`i`) ou Around (`a`)?

Você já viu isso antes! Eu até te mostrei um exemplo na parte anterior, com `viw`.

O `iw` é um Text Object e significa `Inner Word`, mas também poderia ser `vaw`. Nesse caso, o `aw`
também é um Text Object que significa `Around Word`. A diferença entre `i` e `a` está na forma de
seleção. O `i` envolve o que está **DENTRO** e o `a` também envolve o que está **POR VOLTA**.

Nada como um exemplo para tirar essa sua dúvida... Eu te falei que ia fazer você entender,
confia...

Considere o texto:

```text
Otávio Miranda "NÃO SABE" muito de VIM.
```

Se eu colocar o meu cursor em qualquer lugar dessa frase ANTES das aspas duplas, posso pressionar
`vi"` e ele vai selecionar as palavras **NÃO SABE**. Como eu estava te explicando antes, o `iw`
significa `Inner Word`, consequentemente o `i"` significa `Inner "` (dentro de aspas duplas).

Quando digitei `vi"` ele simplesmente tentou encontrar o primeiro par de aspas duplas para frente
do meu cursor e selecionou o que estava dentro delas.

Se eu usar `va"`, o que vai acontecer é que ele vai selecionar `Around "` e isso indica que as
aspas também devem ser incluídas, não apenas o que está dentro delas. As aspas estão **POR VOLTA**
do que você está selecionando. Entendeu?

E o negócio de bidirecional? Bom, coloque seu cursor entre as duas palavras e pressione `vi"`.
Viu? Seleção para trás e para frente!

Quem faz a mágica aqui são essas duas letras: `i` e `a`. Elas podem ser combinadas com várias
coisas para fazer movimentos bidirecionais no texto. Isso significa que eu posso estar em qualquer
lugar do texto que estou tentando selecionar que o `nvim` vai usar tudo para trás e para frente do
meu cursor para fazer a seleção completa. É por isso que `viw` seleciona uma palavra inteira
independente de onde estiver seu cursor naquela palavra.

Alguns exemplos que podem ser combinados com `i` ou `a` são:

- `w` - Word (palavra)
- `s` - Sentence (frase)
- `p` - Paragraph (Parágrafo)
- `t` - Tags
- `(` ou `b` - Dentro de parênteses
- `[` - Dentro de colchetes
- `{` - Dentro de chaves
- `'` - Dentro de aspas simples
- `"` - Dentro de aspas duplas

Pode escolher qualquer um dos caracteres acima e fazer o teste.

Por exemplo, olha esse `JSON`:

```json
[
  { "nome": "Otávio", "sobrenome": "Miranda" },
  { "nome": "Ana", "sobrenome": "Maria" },
  { "nome": "Xuxa", "sobrenome": "Silva" }
]
```

Com o seu cursor em QUALQUER lugar dentro dos colchetes, ao pressionar `vi[`, o conteúdo inteiro
**DENTRO** deles será selecionado. Se pressionar `va[`, além do conteúdo, ambos `[` e `]` também
serão incluídos na seleção.

Também temos as chaves no JSON. E é a mesma ideia, de qualquer lugar por dentro de qualquer chave,
ao digitar `vi{`, on conteúdo inteiro daquela chave específica será selecionado. Enfim, testa
aí... Acho que já entendemos isso!

---

### Mas e o `v`? Nunca muda?

Muda sim, é que eu não queria te fazer editar ou apagar algum texto, então a opção mais segura é
`v`, que trabalha na seleção. Além disso é mais fácil de ver o que está acontecendo.

Mas já que você fica insistindo aí, você pode usar qualquer um desses:

- `c` - change (apaga e entra no modo de edição)
- `d` - delete (apaga)
- `y` - yank (copia o texto para o registro)
- `~` - Faz toggle entre maiúsculo e minúsculo
- `g~` - Faz toggle entre maiúsculo e minúsculo
- `gu` - Transforma em minúsculo
- `gU` - Transforma em maiúsculo
- `zf` - Define um trecho para fazer fold

Ok, ok... mais exemplos... Vamos usar o JSON e dessa vez faz aí comigo. Vamos tentar com `gU`.
Quero tudo dentro dos colchetes em maiúsculo.

```json
[
  { "nome": "Otávio", "sobrenome": "Miranda" },
  { "nome": "Ana", "sobrenome": "Maria" },
  { "nome": "Xuxa", "sobrenome": "Silva" }
]
```

Posicione seu cursor entre os colchetes e pressione `gUi[`, e... Voilà...

```json
[
  { "NOME": "OTÁVIO", "SOBRENOME": "MIRANDA" },
  { "NOME": "ANA", "SOBRENOME": "MARIA" },
  { "NOME": "XUXA", "SOBRENOME": "SILVA" }
]
```

---
