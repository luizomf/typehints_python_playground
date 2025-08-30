# Gemini vs. Codex: A Batalha das IAs no Terminal para Corrigir Legendas

Recentemente, decidi fazer um experimento um pouco diferente: colocar duas das mais poderosas
ferramentas de IA para desenvolvedores, o Gemini da Google e o Codex da OpenAI, em uma batalha
direta no meu terminal. O objetivo? Ver qual delas se sairia melhor em uma tarefa que, para mim, é
comum e um tanto desafiadora: a revisão técnica de legendas geradas automaticamente.

A ideia não é apenas declarar um vencedor, mas compartilhar um método que tenho aprimorado para
extrair os melhores resultados possíveis dessas ferramentas, usando prompts detalhados em Markdown
para guiar a IA.

## O Desafio: Corrigindo a Fúria do Whisper

Se você já usou ferramentas de transcrição automática como o Whisper da OpenAI, sabe que elas são
fantásticas, mas nem sempre perfeitas, especialmente com jargões técnicos. Em um dos meus vídeos,
a transcrição estava cheia de pequenas pérolas, como:

- **"Jungle"** em vez de **"Django"**
- **"Salary"** em vez de **"Celery"**
- **"SQL Alchemy"** (separado) em vez de **"SQLAlchemy"**

Corrigir isso manualmente em um arquivo de quase 2.000 linhas e mais de 7.500 palavras é um
trabalho tedioso. Além disso, é crucial não quebrar a estrutura do arquivo `.srt`, com seus
timestamps e sequências numéricas. Qualquer alteração errada pode dessincronizar toda a legenda.

Este é um desafio perfeito para uma IA: requer compreensão de contexto técnico, atenção aos
detalhes e a capacidade de seguir instruções rígidas de formatação.

## Minha Estratégia: O Prompt Detalhado em Markdown

Em vez de simplesmente pedir "corrija este arquivo", eu criei um "template de trabalho" em um
arquivo Markdown. Essa abordagem permite que eu seja extremamente específico sobre o que a IA deve
e, mais importante, não deve fazer.

A estrutura do meu prompt se parece com isto:

```markdown
# Você é um revisor técnico de legendas SRT geradas automaticamente.

A legenda foi transcrita por uma IA (Whisper) e pode conter **erros em termos técnicos de
programação**.

---

### Seu trabalho principal é:

- Corrigir palavras erradas com base no **contexto técnico e geral**.
- **Preservar o estilo e estrutura original** do texto.
- **Preservar sequência, timestamps e quebras de linha**.
- Gerar um relatório final detalhando o que foi feito.

---

### O que você não pode fazer:

- Alterar o bloco SRT.
- Alterar o timestamp.
- Adicionar notas, observações ou qualquer texto que não seja o SRT corrigido.
- Gerar imagens. Sua resposta deve ser em texto.
```

Essa clareza é fundamental. Eu instruo a IA a gerar não apenas o arquivo corrigido, mas também um
relatório (`.log`) de tudo o que foi alterado. Esse log é meu controle de qualidade e me ajuda a
entender os padrões de erro da transcrição, além de manter o contexto para futuras interações.

## A Batalha no Terminal

Com os prompts `gemini.md` e `codex.md` prontos, preparei o campo de batalha no meu terminal
usando `tmux` com duas sessões lado a lado.

Para quem quiser replicar, a instalação é simples:

**Codex (OpenAI):**

```bash
npm i -g @openai/codex
```

**Gemini (Google):** Eu rodo diretamente com `npx` para ter sempre a versão mais recente.

```bash
npx @google/gemini-cli
```

Com ambos os CLIs prontos, enviei o mesmo comando para cada um, referenciando seu respectivo
arquivo de prompt e o arquivo de legenda.

## Os Resultados: Quem se Saiu Melhor?

Ambos foram incrivelmente rápidos. Em poucos minutos, cada IA concluiu a tarefa, gerando o arquivo
`_fixed.srt` e o relatório de alterações, exatamente como eu pedi.

Os relatórios mostraram que ambos identificaram e corrigiram os principais erros:

- `Neovim`
- `Django`
- `Celery`
- `SQLAlchemy`
- `FastAPI`

Fiquei impressionado com a capacidade do Codex de até mesmo diferenciar quando eu falava "Vim" (o
editor) de "vi" (o comando de Text Object no Neovim). O Gemini, por sua vez, forneceu um relatório
mais verboso e detalhado, categorizando os tipos de erro do Whisper.

Mas, ao fazer um `diff` entre os dois arquivos corrigidos, a história ficou mais interessante. Não
houve um vencedor claro.

- Em alguns trechos, o **Codex** foi mais fiel ao que eu realmente falei, enquanto o Gemini tentou
  "corrigir" uma repetição minha.
- Em outros, o **Gemini** acertou a capitalização de um termo (`Cyan`) que o Codex errou.

Cada um cometeu pequenos deslizes em lugares diferentes.

## Conclusão: O Vencedor é o Método

No final, a maior lição não foi sobre qual IA é superior, mas sobre o poder da metodologia. Ao
fornecer um prompt claro, detalhado e estruturado em um arquivo Markdown, consegui resultados de
alta qualidade de _ambas_ as ferramentas.

Essa abordagem transforma a IA de um assistente imprevisível em um parceiro de trabalho confiável
e consistente. O segredo não está em apenas pedir, mas em como pedir.

Se você trabalha com IAs no seu dia a dia, recomendo fortemente que experimente essa técnica. Crie
seus próprios templates de prompt para tarefas repetitivas. A precisão e a consistência dos
resultados podem te surpreender.
