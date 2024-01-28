[Voltar](../index.md)

links do youtube serão publicado quando estiverem disponíveis.

# Configuração do Ambiente

Uma parte muito importante para o desenvolvimento de software é uma configuração apropriada do ambiente de trabalho. Nesse tutorial vamos ensinar como instalar as ferramentas necessárias para fazer os trabalhos das disciplinas, e dar algumas dicas de configurações.

Vamos dividir os tutoriais específicos para sistemas operacionais em suas respectivas partes. Faremos um tutorial para Windows, maior e mais longo por necessitar mais atenção e dois pequenos para Ubuntu e Manjaro, por serem distribuições mais populares. 

Vale lembrar que muitas distribuições comuns como Debian ou Mint são semelhantes o suficiente ao Ubuntu para que o tutorial ainda seja útil.

## Teoria

Nessa seção falaremos sobre as ferramentas em um aspecto mais "agnóstico" de sistema operacional, que se aplica a qualquer um. Na seção de [tutoriais](#tutoriais) explicaremos como configurar seu ambiente de acordo com seu sistema operacional.

### As Ferramentas Necessárias

Para desenvolver um programa em qualquer linguagem, no mínimo você precisará de alguma ferramenta que traduz aquela linguagem para código de máquina. No caso de C, isso será um compilador (geralmente o `gcc`), mas outras linguagens também tem seus equivalentes. Java por exemplo necessita de um compilador (`javac`), e uma máquina virtual (JVM). Python precisa apenas do interpretador (chamado comumente apenas de `python`).

Além disso, você vai precisar instalar as outras ferramentas auxiliares, como o Make, git, Valgrind, GDB, que vão ser essenciais para desenvolver os programas localmente.

E por fim você vai precisar de um editor de texto. Aqui falaremos apenas de como instalar o editor mais popular, o [Microsoft](https://github.com/dessalines/essays/blob/master/microsoft.md) Visual Studio Code. Ele já vem com muitas funcionalidades úteis "direto da caixa", e contém um marketplace com ainda mais extensões, temas e outras ferramentas que vão ser úteis pro resto da carreira de vocês. Além disso, por ser hoje um dos produtos para desenvolvedores mais importantes da Microsoft, e [monopolisar](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-integrated-development-environment) o espaço de editores de texto, é improvável que ele seja descontinuado no futuro.

Para usuários de Linux, ensinaremos também como instalar o VSCodium, um _fork_ (utiliza o mesmo código base) do VSCode, que remove toda telemetria de código não-livre da Microsoft, e é realmente Open-Source. Ele é funcionalmente idêntico em todos os aspectos exceto no modo de instalar extensões.


### Gerenciador de Pacotes

Em um Sistema Operacional, um [gerenciador de pacotes](https://pt.wikipedia.org/wiki/Sistema_gestor_de_pacotes) é um sistema encarregado de baixar, instalar e configurar programas de forma centralizada e consistente. Esses sistemas garantem que o usuário está instalando uma versão oficial e confiável do programa, e automatiza o processo de atualizá-lo ou desinstalá-lo. Ele também garante que as dependências dos programas sejam baixadas junto com o programa, caso ele precise de alguma
biblioteca externa. Uma boa demonstração da necessidade disso é quando programas de Windows pedem para o usuário também instalar Java ou C++ Redistributable separadamente para o programa em si funcionar.

Hoje, todos os sistemas operacionais "principais" possuem algum tipo de gerenciador de pacotes. Por exemplo celulares Android utilizam primariamente a Play Store (e podem instalar o [F-Droid](https://f-droid.org/) para aplicativos open source), iPhones tem a App Store.

Como nossos ambientes de desenvolvimento necessitam de bastante estabilidade, e são muito sensíveis a configurações incompletas, é sempre recomendado instalar as ferramentas necessárias com esses gerenciadores de pacotes.

Para os sistemas Linux, existem vários gerenciadores de pacotes diferentes dependendo da distribuição usada, mas os principais são o `dpkg` do Debian e derivados (ou o `apt`, que é apenas um front-end mais fácil de usar desse gerenciador) e  `pacman` (extendido pelo `pamac`) para distribuições baseadas em Arch como Manjaro. Existem outros gerenciadores de pacotes mais específicos, como [Flatpak](https://flathub.org/pt-BR) e [Snap](https://snapcraft.io/), mas não falaremos sobre eles aqui.

Já para os sistemas Windows, existem dois gerenciadores de pacotes oficiais, a aplicação Microsoft Store e o programa da de linha de comando [WinGet](https://www.theregister.com/2020/05/28/appget_replaced_by_winget_says_dev/). Além deles, também existem outros gerenciadores de pacotes mantidos pela comunidade, como o Chocolatey e o Scoop.

Embora não tenhamos feito um tutorial para o MacOS, o seu gerenciador de pacotes oficial é a App Store. Mas como ela tem um foco maior em software comercial e é muito limitada em quem pode distribuir seu software, é essencial o uso da ferramenta mantida pela comunidade [Homebrew](https://brew.sh/).

### Editores de Texto

Como vocês vão programar em C, precisam de um editor de código competente. O nome "editor de texto" não expressa bem o quão complexo e completo um software desse tipo pode ser, então muitas pessoas chamam sistemas maiores de Integrated Development Environment ("Ambiente de Desenvolvimento Integrado"), ou só IDE. Um editor moderno não serve apenas para ler e escrever em um arquivo de texto com coloração de sintaxe, mas também para executar uma série de funcionalidades para facilitar o
desenvolvimento de programas. 

Em um lado do espectro, temos editores extremamente básicos como Gedit, Nano ou MS Notepad. Do outro, temos sistemas complexos e cheios de funcionalidades como VSCode, Vim, Emacs e o falecido [Atom](https://github.blog/2022-06-08-sunsetting-atom/).

A funcionalidade mais básica que vai além do conceito de "editor", é o sistema de "compilar e rodar", que hoje em dia vem incluso em quase todo editor de texto. Mas além disso existem várias outras ferramentas especificas de linguagem (geralmente agrupadas em algo chamado Language Server), que podem por exemplo verificar seu código por erros (conhecido como Linter) enquanto você escreve, auto-completar seu código de acordo com a estrutura escrita, e até refatorar o seu programa completamente.

Também existem extensões que integram ferramentas externas como Git, reduzindo o custo de mudança de contexto e adicionando representações visuais dos comandos de terminal. No geral, editores modernos são bem extensíveis, então se é algo programável, e existe demanda, provavelmente existe uma extensão que faz isso.


## Tutoriais

Aqui vamos mostrar como instalar e configurar os sistemas acima, e como utilizar os gerenciadores de pacotes de cada sistema caso mais ferramentas sejam necessárias. Vamos falar especificamente sobre o [Windows](https://www.youtube.com/watch?v=GmeGPudmSjs) e as distribuições de Linux [Ubuntu](https://pt.wikipedia.org/wiki/Ubuntu_(sistema_operacional)) e [Manjaro](https://pt.wikipedia.org/wiki/Manjaro_Linux).

### Ubuntu

O Ubuntu é uma distribuição de Linux baseada na distribuição clássica [Debian](https://en.wikipedia.org/wiki/Debian). Ele tem um foco em ser fácil para novatos do Linux, mesmo que as vezes sacrifique controle do usuário.

Por ser baseada no Debian, assim como a maioria das distribuições populares, os mesmos comandos que servem para Ubuntu devem servir no geral para a maioria dos casos. Algumas distribuições baseadas em Debian são Kali, Deepin, Nova, Mint e Elementary.

#### DPKG e APT



O sistema de pacotes do Debian é o [dpkg](https://www.dpkg.org/). Ele é um sistema extremamente limitado, podendo apenas instalar pacotes já baixados no formato `.deb`. Ele também não consegue baixar dependências em caso de necessidade por um pacote.

Para usar ele, você precisa executar os comandos no terminal, da seguinte forma.

```bash
sudo dpkg -i pacote.deb # instala o pacote com o nome pacote.deb
sudo dpkg -r nomepacote # desinstala pacote com esse nome
```

O comando `sudo` apenas força o resto do comando a rodar como admnistrador. Isso é necessário para utilizar qualquer sistema de gerenciamento de pacotes por questões de segurança.

No geral, ele não é muito útil para um usuário comum. Ao invés dele, a maioria dos usuários utilizam o sistema APT, que é um "front-end" para o dpkg.

O APT é um conjunto de ferramentas que extende e automatiza o processo de baixar um pacote, verificar as dependências e instalar com o dpkg. Ele ainda é utilizado pela linha de comando, mas possui comandos mais "amigáveis". Ele mantêm uma listagem de todos pacotes disponíveis na internet e suas versões.

Para utilizar o APT, o primeiro passo é sempre rodar o comando a seguir:

```bash
sudo apt-get update
```

Esse comando força o APT a atualizar a sua listagem de versões disponíveis. Embora não seja estritamente necessário, é uma boa forma de evitar instalar versões ultrapassadas de programas.

Para instalar algum programa, você vai precisar utilizar o comando a seguir:

```bash
sudo apt-get install nome_do_programa
```

Caso não haja erros, ele irá pedir uma confirmação, baixar todas as dependências e instalar o programa. Caso o processo seja abortado, o apt automaticamente retorna o sistema ao estado anterior à instalação, então não existe (muito) risco de acidentalmente corromper uma instalação.

Para atualizar e desintalar um programa, você deve usar os dois comandos a seguir espectivamente:

```bash
sudo apt-get upgrade nome_do_programa
sudo apt-get remove nome_do_programa
```

Caso você queira buscar o nome do programa que irá instalar, o apt-get possui um sistema de completação automática. Basta digitar o começo do pacote, e apertar a teclar `TAB`. Mas você pode também executar o comando a seguir para buscar por um pacote dado um pedaço do seu nome.

```bash
sudo apt-get search me_do_progra
```

Para obter mais informações sobre um pacote antes de instalar (principalmente para evitar pacotes com [nomes similares](https://superuser.com/questions/784258/whats-the-difference-between-docker-io-and-docker) mas funções bem diferentes), você pode listar mais informações sobre um pacote com:

```bash
sudo apt-get show nome_do_programa
```

#### Snap

Além do dpkg, existe também o sistema specificamente para sistemas derivados do Ubuntu, o [Snap](https://snapcraft.io/). Ele geralmente não vai estar presente em sistemas não-derivados do Ubuntu, mas pode ser instalado via apt-get

```bash
sudo apt-get install snapd
```

Ele também tem uma loja como interface gráfica.

```bash
sudo apt-get install snap-store
```

O Snap foi desenvolvido pela Canonical (empresa desenvolvedora do Ubuntu) para tentar criar uma loja de aplicativos semelhante à Windows Store. Embora seja um sistema [altamente controverso](https://hackaday.com/2020/06/24/whats-the-deal-with-snap-packages/), vamos focar apenas em como usar ele, e como ele é usado "por debaixo dos panos" no Ubuntu.

Para usar o snap, não é necessário atualizar a listagem como no APT. Basta executar os seguintes comandos:

```bash
sudo snap find nome_do_programa # busca o programa no repositório remoto
sudo snap install nome_do_programa # instala o programa
sudo snap remove nome_do_programa # desinstala o programa
sudo snap refresh # atualiza todos programas
```

Você também pode instalar aplicativos direto da loja. Basta abrir o programa Snap Store, procurar o pacote que quiser e clicar em instalar.

**inserir imagens**

#### Ubuntu/GNOME Software

A maioria das distribuições baseadas em Debian trazem instaladas consigo um programa gráfico chamado apenas "Software". Esse programa é um front-end que tenta centralizar todos os gerenciadores de pacotes, mas focando especificamente nos chamados "Aplicativos" (programas com interface gráfica). Para a maioria dos programas que vocês forem usar na vida de vocês, podem utilizar essa ferramenta, precisando apenas usar o terminal para intalar programas de terminal ou bibliotecas para
desenvolvimento.

**inserir imagens**

#### Como instalar ferramentas de desenvolvimento

Durante o a disciplina de ED, vocês irão precisar de um conjunto de ferramentas base para desenvolvimento, mas também é possível que precisem instalar alguns outros softwares de acordo com circunstancias.

### Manjaro

~~explicar sobre Manjaro ser Arch-based, e sobre o sistema rolling release~~

### Windows

~~Explicar tudo de Windows, muita coisa jesus~~
