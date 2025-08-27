# Cadê a eficiência? Pare URGENTE de usar `hjkl` no NeoVim!

Esse texto não é pra você, é para o eu do futuro (presente, sei lá). Sou eu tentando ver se
aprendo a parar de ficar jogando pac-man no NeoVim e começo a usar uns comandos mais eficientes do
que `hjkl`.

Você também tá jogando né? To te vendo, hein!

---

## Vamos combinar, não somos mais iniciantes

Se você caiu aqui sem saber nem abrir o `nvim`, parabéns, você clicou errado. Aqui eu vou assumir
que você já não troca mais o `j` com o `k`.

**Lembrete:** Só para te lembrar, `j` vai para cima e o `k` vai para baixo, OK 🤔? Isso... faz
isso mesmo... volta e lê de novo para não esquecer!

E pra não dizer que não ajudo, segue uns vídeos que podem salvar tua vida digital em algum
momento:

- [Ambiente de Desenvolvimento Dev 2025](https://youtu.be/mhudacg8f_A?si=3EvlUS0SsOrLGmUZ)
- [Comandos Unix que todo programador deveria saber](https://youtu.be/UQBAytRBNiM?si=pOfQNmAeGxvv3vgP)

---

## Pare de usar tanto `hjkl`

Sim, eu sei. Você já ouviu isso, mas precisa entrar na tua cabeça: **não existem só `hjkl` no
Vim.**

Eu também viciei nisso aí, mas estou tentando ficar limpo graças a Deus. Já foram 2 segundos sem
usar `hjkl` porque eu estou no modo `INSERT` digitando isso... Um passo de cada vez (aí meu Deus,
eu vou ter que salvar agora).

`:w`, `Enter`, `o` e `Enter` e estamos nessa linha que você está lendo (mais 30 segundos sem
`hjkl`).

Vamos falar sério agora. Olha aí abaixo alguns comandos que não são nada complicados de usar e vão
acelerar o seu pac-man para navegar no código (me conta quem você tá achando que é o pac-man que
eu falo toda hora?).

E outra, você só vai saber se eu estou zoando se testar isso aí:

- `w` - vai pro início da próxima palavra
- `W` - vai pro início da próxima palavra ignorando pontuação
- `b` - volta pro início da palavra anterior
- `B` - idem, mas ignorando pontuação
- `e` - vai pro final da próxima palavra
- `E` - idem, mas ignorando pontuação
- `ge` - final da palavra anterior
- `gE` - final da palavra anterior ignorando pontuação

Sozinho isso não parece nada demais, né não? Mas isso é por que você ainda não entrou no modo
normal e segurou o `w` enquanto tentava ler o código seguindo o cursor. Se ainda não fez, faz o
teste aí.

---

### Combinações - Vamos juntar seus dois neurônios

Você sabe que dá para combinar um operador (`v`, `y`, `c`, `d`, ...) com um número para fazer algo
útil, né? Tipo: `d2l` ou `d2h`.

É disso que eu estou falando, `d` (operador para deletar), `2` quantidade, `l` e `h` (sem
comentários, estou limpo já fazem 5 minutos).

Mais exemplos pra gente ficar ninja juntos:

- Quero selecionar 4 palavras pra frente: `v4e` (simples, fala verdade?)
- Quero selecionar a palavra atual e mais 3 pra trás: `viwo3b` (o que qui foi isso?)

Bora entender... No primeiro, `v` abre o modo VISUAL, `4` é a contagem e `e` é o movimento.

Simples, mas o ruim desse comando é que pode cortar o meio da palavra dependendo de onde seu
cursor estiver. Se você está no meio da palavra, vai a metade da primeira palavra. O resto vai
certinho. Isso me dá uma certa ansiedade.

Mas... _"você pode sentar aqui e conversar com nós só um pouquinho,
[meu preciosssso](https://www.valinor.com.br/6377)"_. Deixa que eu te explico a magia do segundo
comando:

- `viw` - pega a palavra inteira onde o cursor está (guarda essa informação que
  [ela vai voltar](youtube.com/watch?v=KgAZWXqK7Ac))
- `o` - inverte a posição do cursor na seleção (isso aqui é genial)
- `3b` - volta 3 palavras

Pronto, seleção feita. E seleção no Vim vai te permitir fazer um milhão de outras coisas, como:

- `y` - copia
- `d` - apaga
- `c` - apaga e já te joga no modo INSERT

Exemplo: `viwo3bd` - isso apaga 4 palavras pra trás de onde o cursor está.

Vamos ver se você está é "bão memo", digita `viwo3bd` sem olhar no teclado.

Show! Tá esperando os parabéns? Parabéns então...

---

### Quer precisão? Tem também

Se você gosta das coisas certinhas, onde o número bate bonitinho com a quantidade de palavras, a
fórmula pode mudar (cadê aqueles neurônios que a gente adora?).

Um exemplo:

`veo3b`

A explicando:

- `v` - entra no VISUAL.
- `e` - vai pro final da palavra atual.
- `o` - inverte a seleção (já falei que isso é genial né?).
- `3b` - volta 3 palavras.

Em resumo, este comando seleciona 3 palavras pra trás, mesmo que você comece do meio de uma
palavra.

**`o` no modo VISUAL é tipo a Mitsuri Kanroji**

Eu já falei umas 3 vezes que o `o` no modo VISUAL é lindo demais, não é? A função dele é inverter
o cursor da seleção. Entenda...

Qualquer seleção que você faz, o cursor vai na direção que você começou. Olha a seta que desenhei
tentando imitar uma seleção (ficou ó 👌):

```text
Estou selecionando isso.
      ----------->
```

Se não entendeu, a intenção era mostrar que eu selecionei a palavra "selecionando". Comecei pelo
"s" e fui até o "o".

Mas agora, se eu quero selecionar "Estou", não daria.

Entra a Mitsuri Kanroji (o `o` se você se esqueceu). Ao pressionar `o` no modo VISUAL, o cursor
inverte a posição permitindo que você vá na direção oposta.

Outra sacada inteligente: às vezes eu seleciono algo só para inverter o cursor de posição (isso
não é zoeira). Após inverter, desativo o modo VISUAL e ganho um cursor no outro lado do texto.
Quero voltar do outro lado de novo? Digita `gv` para refazer a última seleção, aperta a Mitsuri
Kanroji e você sai do outro lado. Dá para fazer um ping-pong com o cursor indo de um lado para
outro em trechos grandes de código.

De nada! Não precisa me agradecer, isso é só preguiça mesmo...

---

## Text Objects? Como uso isso?

Se você não sabe disso, provavelmente vai viciar nos comandos que vou te mostrar agora. Bora lá!

O `vim` tem o conceito de "Text Objects". Todo mundo fala desse termo como se fosse óbvio, mas não
é (tanto que eu tô pesquisando agora pra fingir que sei também).

A real é que "Text Object" descreve uma região do texto definida pela **lógica do texto** em vez
de só "pra frente" ou "pra trás". (Ficou bonito? Nem eu entendi a frase, mas tá boa der ler então
deixa aí.)

Brincadeiras à parte: Text Object é basicamente um **movimento bidirecional**. Diferente de
`hjkl`, `w`, `b`, `e`... que só andam pra um lado, os text objects entendem o contexto todo.

Calma, calma, relaxa, respira... vou te explicar isso... Vamos lá...

---

### Inner (`i`) ou Around (`a`)?

Você já viu isso antes! Eu até mostrei lá em cima com `viw`.

- `iw` = **Inner Word**
- `aw` = **Around Word**

A diferença é simples:

- `i` pega só o **dentro**.
- `a` pega o **dentro e o que envolve** (espaço, aspas, parênteses).

Nada como um exemplo pra você entender perfeitamente. Veja o texto:

```text
Otávio Miranda "NÃO SABE" muito de VIM.
```

Se o cursor estiver **antes das aspas** e você digitar `vi"`, ele seleciona só **NÃO SABE**. Por
quê? Porque `i"` = `Inner "` (o que está dentro de aspas duplas).

Se usar `va"`, aí sim ele seleciona **"NÃO SABE"** com aspas e tudo. `a` = `Around` (por volta).

E o negócio do bidirecional? Faz um teste aí, coloca o cursor **no meio das palavras** e manda
`vi"`. Ele não só vai pra frente como também pra trás, fechando a seleção completa.

Quem faz essa mágica são justamente essas duas letras: `i` e `a`. Eles funcionam com vários
objetos diferentes do texto:

- `w` - palavra
- `s` - sentença
- `p` - parágrafo
- `t` - tags
- `(` ou `b` - parênteses
- `[` - colchetes
- `{` - chaves
- `'` - aspas simples
- `"` - aspas duplas

Pode brincar com qualquer um desses.

---

### Exemplo Prático com JSON

Da uma boa olhada nesse JSON:

```json
[
  { "nome": "Otávio", "sobrenome": "Miranda" },
  { "nome": "Ana", "sobrenome": "Maria" },
  { "nome": "Xuxa", "sobrenome": "Silva" }
]
```

Se o cursor estiver **dentro dos colchetes**, digita `vi[` e ele seleciona só o conteúdo entre `[`
e `]`. Já com `va[`, ele seleciona conteúdo e os colchetes.

Mesma ideia pras chaves. Em qualquer lugar dentro de uma delas:

- `vi{` - só o conteúdo.
- `va{` - conteúdo e `{}`.

Testa aí e vê como a seleção fica certinha sem precisar ficar caçando caractere.

---

### Mas e o `v`? Nunca muda?

Muda sim, eu só não queria te fazer apagar sem querer nada importante, então o `v` é a opção mais
segura, entra no modo VISUAL, você enxerga o que tá fazendo e não faz nenhuma burrada.

Mas já que você fica insistindo, pode usar qualquer um desses (tem outros também):

- `c` - change (apaga e já entra no INSERT)
- `d` - delete (apaga)
- `y` - yank (copia pro registro)
- `~` - alterna maiúsculo/minúsculo
- `g~` - idem acima, mas mais nerd
- `gu` - transforma em minúsculo
- `gU` - transforma em MAIÚSCULO
- `zf` - define um trecho pra fold (fechar código)

Tá bom, tá bom... mais exemplos, né? Bora usar o JSON de novo. Dessa vez quero fazer ele ficar
tudo em maiúsculo.

```json
[
  { "nome": "Otávio", "sobrenome": "Miranda" },
  { "nome": "Ana", "sobrenome": "Maria" },
  { "nome": "Xuxa", "sobrenome": "Silva" }
]
```

Posiciona o cursor dentro dos colchetes e digita: `gUi[` E... Voilà. Aprecie O GRITO DO MEU JSON:

```json
[
  { "NOME": "OTÁVIO", "SOBRENOME": "MIRANDA" },
  { "NOME": "ANA", "SOBRENOME": "MARIA" },
  { "NOME": "XUXA", "SOBRENOME": "SILVA" }
]
```

Eu não tenho mais brincadeirinha não, vai para o próximo trecho que to com pressa.

---

## Buscas com `f`, `F`, `t`, `T`, `/` e `?`

Eu sei, o texto tá enorme e eu já estou ficando aflito. Mas calma, essa é a última cartada. Depois
eu faço outro com mais comandos geniais.

Às vezes, em vez de ficar jogando pac-man 🕹️ com o cursor, você quer ir **direto** naquele
caractere.

Pra isso você pode usar os comandos inline:

- `f` - busca caractere pra frente na linha
- `F` - busca caractere pra trás na linha
- `t` - igual ao `f`, mas para um caractere ANTES do encontrado
- `T` - igual ao `F`, mas para um caractere DEPOIS do encontrado
- `;` - repete última busca pra frente
- `,` - repete última busca pra trás

Exemplo:

```text
O Cavaleiro Branco - "Até meus ossos estão enregelados", comentou Gimli...
```

- Do começo da linha, digita `f-` - o cursor pula para o traço.
- Agora `f"` - pula pra primeira aspa.
- Agora `;` - repete e vai pra próxima aspa.
- Agora `,` - volta pra anterior.

Simples, genial e viciante.

Quer algo útil? `"_vf"`

Explicando:

- `_` - vai para o primeiro caractere da linha
- `v` - VISUAL mode
- `f"` - busca a primeira aspa

Ou seja: **seleciona tudo do começo da linha até a primeira aspa**. Faz o teste depois com `F`,
`t` e `T` pra sentir a diferença.

---

## Movendo na linha e no arquivo

Promessa é dívida: último trecho. Tá acabando... estamos nos acréscimos.

Só os básicos de navegação e "teleporte" do cursor:

- `gg` - topo do arquivo
- `G` - final do arquivo
- `^` - início da linha
- `$` - final da linha
- `_` - primeiro caractere não-vazio da linha
- `g_` - último caractere não-vazio da linha

Agora meu último combo genial pra você. Digita aí: `VggoGd`

Me conta o que achou nos comentários.

---

## Acabouuuuuuu! Acabouuuuuu!!! Chora Galvão!!!

É isso. Não tenho conclusão, não tenho call-to-action, não vendo nada, não tenho reflexão final.
Só o silêncio constrangedor do pós-artigo.

Beijos, me liga!

---
