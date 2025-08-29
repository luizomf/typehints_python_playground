Title: Codex CLI aprovado: revisando legendas SRT do Whisper com precisão (relatório + SEO)

Subtitle: Um workflow prático com prompt em Markdown, comparação rápida com Gemini/Claude e
entrega de arquivos prontos (SRT corrigido, log detalhado e SEO para YouTube)

Hoje eu coloquei o Codex CLI (OpenAI) à prova em uma tarefa que costuma desafiar várias LLMs:
revisar tecnicamente uma legenda SRT gerada automaticamente pelo Whisper — mantendo timestamps,
quebras de linha e estilo do texto. O objetivo foi corrigir termos de programação e nomes de
ferramentas que o Whisper frequentemente erra, sem reescrever frases inteiras.

Contexto e por que isso importa

- Whisper é excelente para transcrever, mas tropeça em termos técnicos (nomes de ferramentas,
  modelos, siglas).
- Em workflows reais, eu preciso de uma legenda pronta para publicar: corrigida, com estrutura SRT
  intacta e sem “criatividade” adicional.
- Já fiz isso antes com Gemini via API (quebrando em chunks) e também testei com outras LLMs;
  agora quis ver se o Codex CLI segurava essa bronca.

O que eu pedi para o Codex fazer Montei um prompt em Markdown (CODEX.md) descrevendo exatamente o
trabalho:

- Corrigir termos técnicos e ortografia com base no contexto do vídeo.
- Preservar estrutura SRT: timestamps, numeração e quebras de linha.
- Não reformular frases inteiras; apenas ajustes necessários.
- Gerar três saídas:
  - Transcrição corrigida: 04_FINAL_fixed.srt
  - Relatório de correções: CODEX_LOG.md
  - SEO para YouTube: YOUTUBE.md (título e descrição)

Resultados e destaques

- Precisão técnica: corrigiu nomes como “Claude” (onde estava “Cloud”), padronizou “Neovim” (em
  vez de “Neovin/NeoVim”), normalizou “ChatGPT” (em vez de “chat e pt”) e trocou “underline” por
  “underscore” quando o contexto era o caractere “\_”.
- Estrutura mantida: timestamps, numeração e quebras preservados — do jeito que um editor de vídeo
  espera.
- Tempo de execução: semelhante ao que vejo com outras LLMs em tarefas desse porte (na casa de
  minutos, variando com tamanho e complexidade).
- Entrega pronta: além do SRT corrigido, já sai o relatório com o que mudou e um SEO básico para
  publicar o vídeo rapidamente.

Mini‑tutorial (para você reproduzir)

- Instale o Codex CLI e faça login.
- Escreva um arquivo CODEX.md com regras claras (o que pode e o que não pode alterar).
- Aponte para o SRT original e peça:
  - Correções técnicas sem alterar a estrutura SRT.
  - Geração do arquivo corrigido, relatório e SEO.
- Valide a saída:
  - Abra o vídeo no VLC e carregue a legenda corrigida (04_FINAL_fixed.srt).
  - Faça um spot‑check em termos técnicos e formatação.
- Publique:
  - Vídeo + 04_FINAL_fixed.srt no YouTube.
  - Use YOUTUBE.md como base de título/descrição.
  - Envie este artigo no Substack com os links.

O que eu aprendi no processo

- Prompts melhoram muito quando viram “contratos” em Markdown (regras explícitas e nomes de
  arquivos de saída).
- Pedir um relatório (CODEX_LOG.md) é ouro: documenta as decisões e vira contexto para iterações
  futuras.
- Para tarefas longas, o gargalo costuma ser tokens e latência — nada fora do usual aqui.

Assista e baixe (links definitivos)

- Vídeo: [INSERIR_LINK_YOUTUBE]
- Legenda corrigida (SRT): 04_FINAL_fixed.srt
- Relatório de correções: CODEX_LOG.md
- SEO (título/descrição YouTube): YOUTUBE.md

Call to action Se curtir esse tipo de conteúdo (LLMs aplicadas a workflows reais, automação para
criadores e devs), me diga! Estou considerando rodar uma LLM local para explorarmos mais cenários.
Seu feedback decide os próximos vídeos e artigos.
