# Comandos NeoVim para movimentar melhor no texto

- `hjkl` - Já eliminamos isso para mover o cursor

## Na horizontal

- `w` - vai pro início da próxima palavra
- `W` - vai pro início da próxima palavra ignorando pontuação
- `b` - volta pro início da palavra anterior
- `B` - idem, mas ignorando pontuação
- `e` - vai pro final da próxima palavra
- `E` - idem, mas ignorando pontuação
- `ge` - final da palavra anterior
- `gE` - final da palavra anterior ignorando pontuação
- `f` - busca caractere pra frente na linha
- `F` - busca caractere pra trás na linha
- `t` - igual ao `f`, mas para um caractere ANTES do encontrado
- `T` - igual ao `F`, mas para um caractere DEPOIS do encontrado
- `;` - repete última busca pra frente
- `,` - repete última busca pra trás
- `_` e `^` - Vai para o primeiro caractere não vazio da linha
- `0` - Vai para o início da linha
- `$` - Vai para o final da linha
- `g_` - Vai para o último caractere não vazio da linha

---

## Operadores

Lembrete: operadores precisa de movimento

- `d` - delete (apaga)
- `v` - visual (seleção)
- `c` - change (apaga e já entra no INSERT)
- `y` - yank (copia pro registro)
- `~` - ALTERNA MAIÚSCULO/MINÚSCULO
- `g~` - idem acima, mas mais nerd
- `gu` - transforma em minúsculo
- `gU` - transforma em MAIÚSCULO
- `zf` - define um trecho pra fold (fechar código)

## Não operadores

- `p` ou `P` - colar depois ou antes
- `x` ou `X` - apagar caractere abaixo do cursor para frente ou para trás
- `r` ou `R` alterar caractere ou vários caracteres abaixo do cursor
- `o` ou `O` - nova linha depois ou antes
- `J` - Juntar linhas

`r` e `R` você consegue repetir.

---

## Combinações:

Ao combinar comandos, é possível especificar a quantidade com um número:

- `d2l` - Apague dois caracteres para a direita (sim, `l` do `hjkl`)
- `v5h` - Selecione 5 caracteres para a esquerda (sim, `h` do `hjkl`)
- `elyb` - Copia uma palavra inteira sem text objects (depende muito de onde está o cursor)
- `^vg_` - Vai para o primeiro caractere da linha e seleciona até o último
- `0v3g_` - Vai para o início da linha e seleciona 3 linhas até o último caractere
- `veo3b` - Seleciona três palavra para trás
- `gU3w` - Faz as 3 próximas palavras ficarem com letra maiúscula
- `gU3w` - Faz as 3 próximas palavras ficarem com letra maiúscula

---

## Text Objects

Operador + `i` (inner) ou `a` (around) + qualquer um abaixo:

- `w` - palavra
- `s` - sentença
- `p` - parágrafo
- `t` - tags
- `(` ou `b` - parênteses
- `[` - colchetes
- `{` - chaves
- `'` - aspas simples
- `"` - aspas duplas

Exemplos:

- `vi[` - Visual DENTRO (i) dos colchetes
- `va[` - Visual POR VOLTA (a) dos colchetes
- `yi{` - Yank DENTRO (i) das chaves
- `ya{` - Visual POR VOLTA (a) das chaves
- `ci"` - Change DENTRO (i) das aspas
- `ca"` - Change POR VOLTA (a) das aspas

```json
[
  { "nome": "Otávio", "sobrenome": "Miranda" },
  { "nome": "Ana", "sobrenome": "Maria" },
  { "nome": "Xuxa", "sobrenome": "Silva" }
]
```

---

## Visual Mode

- `v` - Já sabemos
- `V` - para a linha inteira
- `Ctrl + v` - Visual em bloco (use `I` e `A` para edição, depois `ESC`)
- `o` - Inverte a posição do cursor

```javascript
const items = [
  // TODO: Adicionar mais itens
  'item_1',
  'item_2',
  'item_3',
];
```

---

## Repetições

- `.` - Repete a última alteração

---

## Marks

- `m[a-z]` - Cria uma marcação no local onde você está.
- `:delmark a` - Apaga a marcação `a`
- `:delmarks a-z` - Apaga todas as marcações
- `'[a-z]` - Vai para a linha da marcação

---

## Buscas mais complicadas

- `*` - Encontra a próxima ocorrência da palavra sob o cursor
- `#` - Encontra a ocorrência anterior da palavra sob o cursor
- `g*` e `g#` - Funcionam como \* e #, mas procuram por partes da palavra
- `/` - Busca para frente
- `?` - Busca para trás

---

## Movendo a janela

- `Ctrl + e` - Move linhas para cima mantendo o cursor na posição
- `Ctrl + y` - Move linhas para baixo mantendo o cursor na posição
- `zt` - Move a linha do cursor para o topo
- `zz` - Move a linha do cursor para o meio
- `zb` - Move a linha do cursor para o rodapé

---
