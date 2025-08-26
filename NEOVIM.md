# Por que eu migrei para o NeoVim

Resolvi anotar aqui os motivos que me fizeram trocar tantas vezes de editor até acabar no NeoVim.
E, sinceramente, acho difícil sair daqui de novo.

---

## Minha trajetória até o NeoVim

Eu não tinha a menor intenção de voltar para o NeoVim. E digo "voltar" porque já tinha me
aventurado com **vi** e **vim** quando trabalhava com administração de redes.

Depois disso, passei a usar o **PyCharm da JetBrains**, na época em que estava escrevendo muitos
scripts em Python. A quantidade de recursos me encantou. O PyCharm já criava o ambiente virtual,
apontava violações da **PEP 8**, mostrava erros antes mesmo de rodar o código... Muita coisa que
aprendi no início com Python veio direto das mensagens do PyCharm.

---

### O Django apareceu, e junto vieram HTML, CSS e JS

Um belo dia, a empresa em que eu trabalhava decidiu usar **Django** para um serviço interno. Nós,
da área de redes (no caso, eu), tivemos que aprender na marra.

Depois de algumas leituras na documentação, percebi que era mais simples do que parecia. Eu já
estava confortável com Python, escrevendo scripts para gerenciamento de servidores, então a curva
de aprendizado não foi tão dolorosa.

Com o tempo, o projeto cresceu e comecei a usar bastante o **VS Code** para editar **JavaScript,
HTML e CSS** (na época o jQuery reinava). Eu não pagava o PyCharm, que também não tinha suporte
decente para HTML e CSS (se não me falha a memória). Resultado: usar dois editores pesados ao
mesmo tempo era uma péssima ideia. Além de consumir muitos recursos, era chato ficar alternando
entre ferramentas para montar o código.

---

### VS Code only

Depois de muito apanhar tentando usar dois editores, aprendi a configurar o **VS Code** de um
jeito que ele ficou praticamente um **PyCharm turbinado**, e até melhor em alguns pontos graças às
extensões.

A partir daí, tudo passou para o VS Code: linguagens, testes automatizados, Code Runner com o
botãozinho de play para rodar código... tudo mesmo. Inclusive criei um **tema próprio** para o VS
Code que acabou bombando, já passou dos **200 mil downloads**.

### VS Code fica "pesadão"

O problema é que o VS Code devora memória. Teve um dia em que percebi ele consumindo **10GB de
RAM** só por estar com duas instâncias abertas (uma em cada monitor), várias abas e ainda gravando
aula.

Isso não seria tão grave se eu não precisasse rodar, ao mesmo tempo:

- **Parallels** com Windows (para dar suporte aos alunos),
- **OBS** gravando a tela,
- e claro, o próprio VS Code.

Com 32GB de RAM, a máquina simplesmente não aguentava. O mouse ficava picotando, a digitação tinha
aquele **delay irritante de milissegundos**, e programar assim era tortura.

Se você já passou por isso, sabe: é como ter alguém arranhando seu cérebro com unhas de aço. Dói
na alma, e eu percebia esse incômodo até nas aulas que gravava.

### Conheça o Zed (escrito em Rust)

Você sabe como é: quando alguém fala que algo é feito em **Rust**, no fundo tá dizendo "isso aqui
é rápido e seguro pra caramba, irmão" Pois é, pensei a mesma coisa.

Na tentativa de resolver o problema do VS Code consumindo tudo, acabei caindo em algum Reddit onde
citaram o **Zed**. Nunca tinha ouvido falar, achei que era furada, mas fui ver no YouTube o que a
galera dizia. Adivinha? "É escrito em Rust, então é rápido e seguro". Resolvi testar.

Para minha surpresa, eu estava desenvolvendo uma aplicação com **Next.js + TypeScript**, e tudo
que precisei fazer foi instalar o Zed. Nada de caçar extensão, nada de configuração chata.
Funcionou de primeira.

O consumo? Uns **400MB de RAM** com tudo rodando. Comentei até em vídeo no meu canal que não
usaria o Zed em tempo integral, que ficaria no VS Code fora das gravações...

Mas a história começou a se repetir (PyCharm e VS Code, agora VS Code e Zed). No fim, optei pelo
**Zed** e segui desenvolvendo nele.

---

### Use Vim Motions, sem tirar as mãos do teclado

No fim de um dia de trabalho eu sempre sentia dores no ombro direito. Já desconfiava que era por
ficar indo e voltando do teclado para o mouse (spoiler: era exatamente isso). Quando descobri que
o **Zed** já vinha com **Vim Motions** por padrão, resolvi testar.

Configurei, comecei a usar e… **MEU DEUS, SOCORRO!**

No primeiro dia eu parecia alguém que nunca tinha visto um teclado. Tentava digitar no _NORMAL
MODE_, confundia seta pra cima com seta pra baixo, usava o mouse o tempo todo... mas insisti.

A primeira aula que tentei gravar com Vim Motions foi um desastre. Eu não conseguia **falar e
digitar ao mesmo tempo**. Antes, era natural: eu escrevia o código e já ia explicando. Mas agora
ficava pensando: "pra copiar isso eu uso `dd`, `yip` ou `cc`?". Preciso raciocinar antes de cada
comando.

Com o tempo fui melhorando, mas a memória muscular me sabotava. Bastava alguns segundos de
distração e lá iam os dedinhos para as teclas erradas, a mão para o mouse, e eu me perguntando por
que nada aparecia na tela.

Isso durou pelo menos um mês. Mas nesse meio tempo aconteceu algo estranho: **eu queria digitar
mais!** Comecei a ver tutoriais de Vim Motions no YouTube e toda vez que alguém digitava eu sentia
vontade de praticar também.

Solução? Voltei a escrever no meu blog em **Markdown** usando Zed + Vim Motions. Isso me ajudou a
ganhar precisão.

Com o tempo fiquei confortável. Só que percebi uma coisa: quase todos os tutoriais que eu assistia
eram de **NeoVim**. Eu só replicava no Zed o que via os outros fazendo no NeoVim.

---

### Já sei Vim Motions, que venha o NeoVim! Só que não...

Aqui caberia um meme:

**Expectativa**: "Dominei hjkl, tô pronto pro NeoVim". **Realidade**: "NeoVim é um editor de
terminal, fio!".

E sim, o NeoVim é como o **Nano**, **Vi** ou **Vim**: roda direto no terminal. Isso significa:
nada de explorador de arquivos, botõezinhos ou interface bonitinha. O que você tem são buffers e
um monte de `~` na tela.

Na primeira vez que instalei o NeoVim, nem consegui abrir. Eu não sabia que ele era um editor de
terminal, fiquei procurando ícone no menu de aplicativos do sistema. Quando percebi, desisti na
hora. Achei que seria só instalar, abrir e configurar. Mágica.

Voltei correndo pro Zed, de rabo entre as pernas.

---

### Segunda tentativa: agora vai! (Só que não…)

Na segunda tentativa fui atrás de tutoriais para configurar. Achei um vídeo e comecei a seguir.
Mas logo vi a realidade: para colocar um **LSP** funcionando, precisava escrever dezenas de linhas
de Lua, baixar meio mundo de repositórios no GitHub... e mesmo assim não havia garantia de ficar
igual ao tutorial, porque cada pessoa gosta de uma configuração diferente.

Resultado: pensei comigo mesmo: _"se for assim para cada linguagem, vou viver configurando o
editor e meu código nunca vai sair do papel"_.

E desisti de novo.

---

### Terceira vez: aqui foi um charme!

O problema das minhas primeiras tentativas é que eu queria configurar tudo na mão, e isso só
funciona se você já entende bem o que está fazendo.

Um belo dia, vagando pela internet, encontrei um projeto chamado **lazy.nvim**, do Folke. É um
**gerenciador de plugins para NeoVim**. Resolvi instalar e testar. Pelo nome "lazy", já parecia
exatamente o que eu precisava.

O que me encantou foi a simplicidade: uma configuração mínima no `init.lua`, e a partir daí basta
criar arquivos `.lua` separados para cada coisa. No meu primeiro teste, criei um `personal.lua` e
coloquei minhas configs antigas, alguns keymaps, até um `print` em Lua só pra brincar. Fechei,
abri o NeoVim e... **BOOM!** Tudo funcionando de primeira, sem erros.

Isso me animou demais. Desde então, fui montando minha própria configuração do NeoVim com o
**lazy.nvim**, e sigo assim até hoje.

---

## Resumo da ópera

Minha chegada ao NeoVim não foi das melhores, mas também não foi forçada. Acho que foi destino: um
editor pesado e uma dor no ombro me empurraram direto para ele, e aqui estou.

Aliás, este texto está sendo escrito em **Markdown no NeoVim**. Inclusive, de acordo com o
contador de palavras que eu mesmo programei em Lua só porque sim, já estamos em torno de 1300
palavras (agora um pouco mais).

Se você quiser usar o NeoVim por algum motivo específico, já aviso: o começo é difícil. Mas se
acontecer com você o que aconteceu comigo, logo vai perceber que programar (ou até escrever
textos) nele é uma experiência viciante. Faz o teste.

Obs.: eu não sei absolutamente tudo sobre NeoVim. Mas sei que gosto de usar. E isso, pra mim, já
basta.
