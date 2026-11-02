#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as páginas HTML do site do Movimento Impulso Jovem.

Uso:  python3 _gerar.py
Sai:  os .html na raiz de site/

O site não depende deste arquivo pra funcionar — o HTML gerado é a entrega.
Este script existe só pra manter cabeçalho, menu e rodapé iguais em todas
as páginas. Se preferir editar na mão, edite os .html.
"""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ links
INSTAGRAM = "https://www.instagram.com/impulsojovem.33"
# abre a conversa no direct (o perfil recebe, e os admins passam o link do grupo)
INSTAGRAM_DM = "https://ig.me/m/impulsojovem.33"
DRIVE_PASTA = "https://drive.google.com/drive/folders/1hWb0P8qGGx9j6iSROzkyZiyYZ96MR_N7?usp=drive_link"
# ---------------------------------------------- formulário → e-mail
# Para onde vai cada resposta do formulário do site.
# EMAIL_FORM_1 é o destino principal; os outros dois entram como cópia (CC).
# Deixe vazio o que ainda não existe — o código só manda o que estiver preenchido.
EMAIL_FORM_1 = "joaopedrocampos452@gmail.com"
EMAIL_FORM_2 = ""   # ← segundo e-mail (opcional)
EMAIL_FORM_3 = ""   # ← terceiro e-mail (opcional)


def emails_cc():
    """Monta a lista de cópias do formulário com os e-mails preenchidos."""
    return ",".join(e.strip() for e in (EMAIL_FORM_2, EMAIL_FORM_3) if e.strip())


FORM_ACTION = f"https://formsubmit.co/{EMAIL_FORM_1}"
FORM_AJAX = f"https://formsubmit.co/ajax/{EMAIL_FORM_1}"

PIX_CHAVE = "33 98415-8262"
PIX_NOME = "Mateus de Sousa Costa"
PIX_BANCO = "Mercado Pago"

# ----------------------------------------------------------------- ícones
def ico(nome, tam=None):
    d = {
        "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/>',
        "whatsapp": '<path d="M20.5 11.6a8.5 8.5 0 0 1-12.7 7.5L4 20.5l1.4-3.7a8.5 8.5 0 1 1 15.1-5.2Z"/><path d="M8.8 9.2c0 3 2.5 5.5 5.5 5.5.5 0 1.2-.4 1.4-.9l-1.6-.9-.9.7c-1.1-.4-2-1.3-2.4-2.4l.7-.9-.9-1.6c-.5.2-.9.9-.9 1.4Z" fill="currentColor" stroke="none"/>',
        "busca": '<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/>',
        "abrir": '<path d="M8 16 16 8"/><path d="M9.5 8H16v6.5"/>',
        "copiar": '<rect x="9" y="9" width="11" height="11"/><path d="M15 5H5v10"/>',
        "menu": '<path d="M4 7h16"/><path d="M4 12h16"/><path d="M4 17h16"/>',
        "fechar": '<path d="M6 6l12 12"/><path d="M18 6 6 18"/>',
        "escuta": '<path d="M4 12a8 8 0 1 1 8 8"/><path d="M12 16v4"/>',
        "livro": '<path d="M4 5h7v14H4z"/><path d="M13 5h7v14h-7z"/>',
        "seta": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    }[nome]
    extra = f' width="{tam}" height="{tam}"' if tam else ""
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"{extra}>{d}</svg>')


def faixa():
    """Faixa vermelha rolante — decorativa, então fica escondida do leitor de tela."""
    itens = ["Juventude que participa", "Se posiciona", "E transforma",
             "Divisa Alegre", "Águas Vermelhas", "Escola Impulso", "Biblioteca livre"]
    meio = "".join(f'<span>{t}</span><i aria-hidden="true">★</i>' for t in itens)
    return (f'<div class="faixa-rolante" aria-hidden="true"><div class="faixa-rolante__trilha">'
            f'{meio}{meio}</div></div>')


NAV = [
    ("o-impulso.html", "O Impulso"),
    ("bandeiras.html", "Bandeiras"),
    ("formacao.html", "Formação"),
    ("biblioteca.html", "Biblioteca"),
    ("participe.html", "Contato"),
    ("apoie.html", "Apoie"),
]


# ------------------------------------------------------------- cabeçalho
def cabecalho(ativo):
    itens = []
    for arquivo, texto in NAV:
        atual = ' aria-current="page"' if arquivo == ativo else ""
        itens.append(f'<a class="topo__link" href="{arquivo}"{atual}>{texto}</a>')
    return f"""<header class="topo" data-menu="fechado">
  <div class="envelope topo__interno">
    <a class="marca" href="index.html">
      <img src="assets/img/punho.png" alt="" width="20" height="34">
      <span>IMPULSO</span>
    </a>
    <nav class="topo__nav" id="menu-principal" aria-label="Menu principal">
      {''.join(itens)}
    </nav>
    <div class="topo__acoes">
      <a class="botao botao--mini botao--desk" href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">
        {ico("instagram")} Instagram
      </a>
      <a class="botao botao--mini botao--vermelho" href="participe.html">Entrar</a>
      <button class="menu-botao" type="button" aria-expanded="false" aria-controls="menu-principal">
        {ico("menu")} <span class="menu-botao__texto">Menu</span>
      </button>
    </div>
  </div>
</header>"""


# ---------------------------------------------------------------- rodapé
def rodape():
    links = "".join(f'<a href="{a}">{t}</a>' for a, t in [
        ("o-impulso.html", "Núcleos"),
        ("participe.html", "Contato"),
        ("codigo-de-conduta.html", "Código de conduta"),
    ])
    return f"""<footer class="rodape">
  <div class="envelope">
    <div class="rodape__grade">
      <div>
        <span class="rodape__marca">IMPULSO JOVEM</span>
        <p class="rodape__frase">Juventude que participa, se posiciona e transforma.</p>
      </div>
      <a class="botao botao--mini botao--claro" href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">
        {ico("instagram")} Siga-nos no Instagram
      </a>
      <nav class="rodape__links" aria-label="Links do rodapé">{links}</nav>
    </div>
    <div class="rodape__base">
      <span>Divisa Alegre (MG) · Águas Vermelhas (MG) · desde outubro de {2026}</span>
      <span>Branco, preto e vermelho. Nenhum dado seu é vendido.</span>
    </div>
  </div>
</footer>"""


# ------------------------------------------------------------------ head
def head(titulo, descricao, raiz=""):
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<meta name="theme-color" content="#efe9d8">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Movimento Impulso Jovem">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:image" content="{raiz}assets/img/passeata-leques.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{raiz}favicon.ico" sizes="32x32">
<link rel="icon" href="{raiz}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{raiz}apple-touch-icon.png">
<link rel="manifest" href="{raiz}site.webmanifest">
<link rel="preload" href="{raiz}assets/fontes/Anton-Regular.ttf" as="font" type="font/ttf" crossorigin>
<link rel="preload" href="{raiz}assets/fontes/InstrumentSerif-Italic.ttf" as="font" type="font/ttf" crossorigin>
<link rel="preload" href="{raiz}assets/fontes/SourceSerif4-Regular.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="{raiz}assets/css/estilo.css">
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
"""


def fim(raiz=""):
    return f"""
<script src="{raiz}assets/js/site.js" defer></script>
</body>
</html>
"""


def escrever(arquivo, html):
    caminho = os.path.join(AQUI, arquivo)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(html)
    print("·", arquivo, len(html) // 1024, "KB")


# ===========================================================================
#  CONTEÚDO DAS PÁGINAS
# ===========================================================================
FOTOS = [
    ("assets/img/constituicao.jpg", "Jovem ergue a Constituição durante a caminhada, à noite, sob luz de poste."),
    ("assets/img/passeata-leques.jpg", "Trecho da passeata com leques coloridos levantados acima das cabeças."),
    ("assets/img/bandeira-brasil.jpg", "Pessoa carrega a bandeira do Brasil enrolada nos ombros no meio do ato."),
]


def bandeiras_resumo():
    itens = [
        ("01", "Educação que não se vende",
         "Escola pública forte, universidade e pesquisa financiadas, bolsa que sustenta quem é pobre. Contra voucher, militarização e corte na Capes, no CNPq e no Pé-de-Meia.",
         "bandeiras.html#educacao"),
        ("02", "Trabalho pra viver, não pra sobreviver",
         "Fim da escala 6x1, primeiro emprego com carteira e direitos, contra a precarização disfarçada de “flexibilidade”.",
         "bandeiras.html#trabalho"),
        ("03", "Nossa vida vale mais que o ódio",
         "Antirracismo, fim da misoginia e da LGBTfobia, contra a violência de Estado. Onde houver caso na região, o Impulso se manifesta, acompanha e cobra.",
         "bandeiras.html#vida"),
    ]
    cores = ["vermelho", "tinta", "ocre"]
    saida = []
    for i, (num, titulo, texto, link) in enumerate(itens):
        saida.append(f"""<a class="cartao-bandeira cartao-bandeira--{cores[i]}" href="{link}">
  <span class="cartao-bandeira__num">{num} · Bandeira</span>
  <h3>{titulo}</h3>
  <p>{texto}</p>
  <span class="cartao-bandeira__acao">Ler a bandeira {ico("seta")}</span>
</a>""")
    return "\n".join(saida)


# --------------------------------------------------------------- HOME
def pagina_home():
    fotos = "\n".join(
        f'<img src="{src}" alt="{alt}" width="1400" height="933" loading="lazy" decoding="async">'
        for src, alt in FOTOS
    )
    return head(
        "Movimento Impulso Jovem — juventude que participa, se posiciona e transforma",
        "Movimento de juventude de esquerda de Divisa Alegre e Águas Vermelhas (MG). Nascido em outubro de 2026 da união de estudantes e trabalhadores. A eleição acabou, o impulso continua."
    ) + cabecalho("index.html") + f"""
<main id="conteudo">
  <section class="heroi">
    <div class="envelope heroi__grade">
      <div>
        <p class="selo">Divisa Alegre · Águas Vermelhas (MG)</p>
        <h1>A eleição acabou.<br>O <em>impulso</em> continua.</h1>
        <p class="entrada">Movimento de juventude de esquerda de Divisa Alegre e Águas Vermelhas.
        Uniu estudantes e trabalhadores. Cresceu nas ruas.</p>
        <div class="heroi__acoes">
          <a class="botao botao--vermelho" href="participe.html">Entrar no movimento</a>
          <a class="botao" href="bandeiras.html">Ver as bandeiras</a>
        </div>
      </div>
      <div class="heroi__marca">
        <img src="assets/img/logo.png" alt="Logo do Movimento Impulso Jovem: punho erguido com a palavra IMPULSO" width="300" height="353">
      </div>
    </div>
  </section>

  {faixa()}

  <div class="dados">
    <p>Desde outubro de 2026</p>
    <p>Divisa Alegre e Águas Vermelhas (MG)</p>
    <p>54 verbetes na Escola</p>
    <p>143 livros na Biblioteca</p>
  </div>

  <section class="secao">
    <div class="envelope">
      <div class="grade-fotos" data-revelar>
        {fotos}
      </div>
      <p class="fina mt-3">Fotos da Caminhada pela Democracia, o primeiro ato público do movimento.</p>
    </div>
  </section>

  <section class="secao secao--curta">
    <div class="envelope">
      <div class="cabeca__grade">
        <div>
          <p class="rotulo">Nossas bandeiras</p>
          <h2>O que a gente <em>defende</em></h2>
        </div>
        <p class="mb-0"><a class="acao" href="bandeiras.html">Ver as seis {ico("seta")}</a></p>
      </div>
      <div class="grade-bandeiras mt-5" data-revelar>
        {bandeiras_resumo()}
      </div>
    </div>
  </section>

  <section class="secao secao--preta">
    <div class="envelope">
      <div class="cabeca__grade">
        <div>
          <p class="rotulo">Escola Impulso e Biblioteca</p>
          <h2>Formação pra <em>entender</em><br>e não repetir frase feita</h2>
        </div>
        <p class="mb-0">Duas ferramentas gratuitas: os verbetes da Escola, escritos por nós,
        e os livros da Biblioteca, em PDF, direto do Drive.</p>
      </div>
      <div class="tres-colunas mt-5" data-revelar>
        <div class="caixa">
          <p class="olho">01 · Escola</p>
          <h3>Sete trilhas, 54 verbetes</h3>
          <p>Da palavra “mais-valia” ao AI-5, tudo explicado em três a cinco minutos de leitura,
          com datas, conceito-chave e fontes no fim.</p>
          <p class="mb-0"><a class="acao" href="formacao.html">Começar a formação {ico("seta")}</a></p>
        </div>
        <div class="caixa">
          <p class="olho">02 · Ditadura militar</p>
          <h3>Ato por ato, de 1964 a 1985</h3>
          <p>Trilha nova: o que era um Ato Institucional, o que cada AI mudou e como o AI-5
          fechou o Congresso. Sem decoreba, com documento.</p>
          <p class="mb-0"><a class="acao" href="verbete-atos-institucionais.html">Ler o primeiro verbete {ico("seta")}</a></p>
        </div>
        <div class="caixa caixa--preta">
          <p class="olho olho--vermelho">03 · Biblioteca</p>
          <h3>143 livros, sem cadastro</h3>
          <p>Marx, Freire, Angela Davis, Florestan Fernandes e mais. Busca por título, autor
          ou tema — e o PDF abre no Drive, sem login.</p>
          <p class="mb-0"><a class="acao acao--claro" href="biblioteca.html">Abrir a estante {ico("seta")}</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="chamada chamada--vermelha">
    <div class="envelope chamada__grade">
      <div>
        <h2>A eleição passou.<br>O <em>movimento</em> ficou.</h2>
        <p>Se você é jovem de Divisa Alegre ou Águas Vermelhas e quer organizar o seu bairro,
        a sua escola ou a sua cidade, é aqui que começa. A gente responde em até 48 horas.</p>
      </div>
      <div class="acoes">
        <a class="botao botao--vermelho" href="participe.html">Falar com a gente</a>
        <a class="botao botao--claro" href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">{ico("instagram")} Instagram</a>
      </div>
    </div>
  </section>
</main>
""" + rodape() + fim()


# ------------------------------------------------------------ O IMPULSO
def pagina_impulso():
    return head(
        "O Impulso — quem somos | Movimento Impulso Jovem",
        "O Impulso nasceu em outubro de 2026, em Divisa Alegre e Águas Vermelhas (MG), da união de jovens estudantes e trabalhadores que defendiam as mesmas pautas. Nosso primeiro ato foi a Caminhada pela Democracia."
    ) + cabecalho("o-impulso.html") + f"""
<main id="conteudo">
  <section class="secao">
    <div class="envelope">
      <p class="rotulo">O Impulso</p>
      <h1>Uniu estudantes e<br>trabalhadores.<br>Cresceu nas <em>ruas</em>.</h1>

      <div class="grade-texto-foto mt-5">
        <div class="largura-texto">
          <p class="entrada">O Impulso Jovem nasceu em outubro de 2026, em Divisa Alegre e Águas Vermelhas,
          da <strong>união de jovens estudantes e trabalhadores das duas cidades</strong>.</p>
          <p>A gente não se conheceu em gabinete. A gente se uniu defendendo as mesmas pautas — e desde
          então não parou mais.</p>
          <p>Nosso primeiro ato foi a <strong>Caminhada pela Democracia</strong>. Depois dela não paramos:
          assumimos a defesa das pautas sociais, acolhemos minorias e todo tipo de gente, e escolhemos
          um lado — o da juventude, o dos trabalhadores, o de quem é tratado como sobra.</p>
          <div class="destaque">
            <p>Não temos tempo de estrada pra inventar. Temos uma cidade de cada lado da divisa,
            uma passeata no currículo e muito o que fazer.</p>
          </div>
        </div>
        <figure class="foto-lateral">
          <img src="assets/img/passeata-meio.jpg" alt="Pessoas caminhando juntas no meio da passeata, bandeiras ao fundo" width="1280" height="852" loading="lazy">
        </figure>
      </div>

      <h2 class="mt-6">Nossos princípios</h2>
      <ul class="principios">
        <li>Anticapitalista</li>
        <li>Antiracista</li>
        <li>Contra a LGBTfobia e a misoginia</li>
        <li>Ambientalista</li>
        <li>Antifascista</li>
      </ul>

      <h2 class="mt-6">Como nos organizamos</h2>
      <p class="largura-texto">Núcleos por cidade — Divisa Alegre e Águas Vermelhas — e três frentes de
      trabalho: <strong>formação</strong>, <strong>mobilização de redes sociais</strong> e
      <strong>militância</strong>. Cada núcleo se reúne na sua cidade e o que é decidido fica
      registrado, à vista de todo mundo.</p>

      <div class="tempo">
        <div>
          <h3>Out 2026</h3>
          <p>Fundação: união de jovens estudantes e trabalhadores das duas cidades.</p>
        </div>
        <div>
          <h3>Caminhada</h3>
          <p>Nosso primeiro ato público: a Caminhada pela Democracia.</p>
        </div>
        <div>
          <h3>Hoje</h3>
          <p>Defesa das pautas sociais, núcleos nas duas cidades e formação política.</p>
        </div>
      </div>

      <div class="acoes mt-6">
        <a class="botao botao--vermelho" href="participe.html">Falar com a gente</a>
        <a class="botao" href="{INSTAGRAM_DM}" target="_blank" rel="noopener noreferrer">{ico("instagram")} Chamar no direct</a>
      </div>
    </div>
  </section>
</main>
""" + rodape() + fim()


# ------------------------------------------------------------ BANDEIRAS
BANDEIRAS = [
    ("educacao", "01", "Educação que não se vende",
     "Escola pública forte, universidade e pesquisa financiadas, bolsa que sustenta quem é pobre. Contra voucher, militarização e corte na Capes, no CNPq e no Pé-de-Meia.",
     "A educação é o primeiro lugar onde a desigualdade é decidida. Quem não tem pai que pague cursinho depende de escola pública, de universidade pública e de bolsa que chegue antes da desistência. Por isso: nenhuma vaga, nenhum recurso e nenhuma bolsa a menos."),
    ("trabalho", "02", "Trabalho pra viver, não pra sobreviver",
     "Fim da escala 6x1, primeiro emprego com carteira e direitos, contra a precarização disfarçada de “flexibilidade”.",
     "Seis dias de trabalho para um de descanso não é rotina, é exaustão programada. Defendemos o fim da escala 6x1, o primeiro emprego com carteira assinada, e a recusa de chamar de “flexibilidade” o contrato que tira direito e transfere risco pra quem trabalha."),
    ("vida", "03", "Nossa vida vale mais que o ódio",
     "Antirracismo, fim da misoginia e da LGBTfobia, contra a violência de Estado. Onde houver caso na região, o Impulso se manifesta, acompanha e cobra.",
     "Ódio não é opinião. Racismo, misoginia e LGBTfobia matam gente da nossa idade todos os dias. Quando houver caso na região, o Impulso se manifesta, acompanha a pessoa e cobra de quem tem obrigação de proteger."),
    ("clima", "04", "Clima, floresta e povos indígenas",
     "Ambientalismo popular, não de rico: Amazônia em pé, terra indígena demarcada, contra garimpo ilegal e o agronegócio predatório. A crise climática é pauta de juventude porque é o nosso futuro sendo negociado.",
     "Ambientalismo popular, não de rico. A Amazônia em pé, a terra indígena demarcada, o fim do garimpo ilegal e do agronegócio predatório não são pauta distante: são a conta que a nossa geração vai pagar. É pauta nacional e é pauta nossa."),
    ("saude", "05", "Saúde é pública, e cuidar é político",
     "SUS forte, contra a Super PEC e o corte de verba. Inclui saúde mental da juventude: adoecimento não é fraqueza, é falta de política pública.",
     "SUS forte, contra a Super PEC e contra todo corte de verba que chega no posto do bairro. E saúde mental também é saúde: o adoecimento da juventude não é fraqueza individual, é falta de política pública."),
    ("democracia", "06", "Democracia e antifascismo",
     "Golpe não se repete. Ódio não é opinião. Quem é ameaçado ou demitido por se posicionar não fica sozinho.",
     "Golpe não se repete. Ódio não é opinião. E quem é ameaçado, constrangido ou demitido por se posicionar não fica sozinho: o movimento acompanha, registra e responde."),
]


def pagina_bandeiras():
    blocos = []
    for ancora, num, titulo, resumo, texto in BANDEIRAS:
        blocos.append(f"""<article class="bandeira" id="{ancora}">
  <span class="bandeira__num">{num}</span>
  <div class="bandeira__texto">
    <h2 class="mt-0">{titulo}</h2>
    <p><strong>{resumo}</strong></p>
    <p>{texto}</p>
  </div>
</article>""")
    return head(
        "Bandeiras — o que a gente defende | Movimento Impulso Jovem",
        "As seis bandeiras do Impulso Jovem: educação, trabalho, vida, clima, saúde pública e democracia. O que defendemos, o que estamos vendo e o que fazemos na prática."
    ) + cabecalho("bandeiras.html") + f"""
<main id="conteudo">
  <section class="secao">
    <div class="envelope">
      <p class="rotulo">Bandeiras</p>
      <h1>O que a gente<br><em>defende</em></h1>
      <p class="entrada">Seis bandeiras. Cada uma com o que defendemos, o que estamos vendo e o que
      fazemos na prática.</p>

      <div class="lista-bandeiras mt-5">
        {''.join(blocos)}
      </div>

      <div class="caixa mt-6">
        <h3>Notas e fatos</h3>
        <p class="mb-0">Cada bandeira puxa as notas e os fatos que já publicamos, com data e fonte.
        As notas saem primeiro no Instagram do movimento.</p>
        <div class="acoes mt-3">
          <a class="botao botao--mini botao--desk" href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">{ico("instagram")} Siga-nos no Instagram</a>
          <a class="botao botao--mini" href="{INSTAGRAM_DM}" target="_blank" rel="noopener noreferrer">{ico("instagram")} Chamar no direct</a>
        </div>
      </div>
    </div>
  </section>
</main>
""" + rodape() + fim()


# ------------------------------------------------------------- FORMAÇÃO
TRILHAS = [
    ("01", "Ideias: de onde vêm as palavras que a gente usa", "7 verbetes",
     ["Esquerda e direita", "Classe social", "Mais-valia", "Hegemonia", "Reforma ou revolução", "Estado", "Imperialismo"], True),
    ("02", "Nossa história: o Brasil que produziu a gente", "9 verbetes",
     ["Escravidão e quilombos", "Coronelismo", "Era Vargas", "Ditadura militar", "Diretas Já", "Constituinte de 1988", "Redemocratização", "2013", "8 de janeiro"], False),
    ("2B", "Minas Gerais: o estado que produziu a nossa região", "4 blocos",
     ["Minas política", "Minas econômica", "Minas social", "A divisa: Águas Vermelhas e Divisa Alegre"], False),
    ("03", "O mundo: o que aconteceu fora que mexeu aqui", "10 verbetes",
     ["Revolução Francesa", "1917", "Guerra Fria", "Imperialismo dos EUA", "Fascismo e antifascismo", "Muros e fronteiras", "Globalização", "ONU e FMI", "Guerras atuais", "América Latina"], False),
    ("04", "Quem já lutou: movimentos sociais", "9 verbetes",
     ["Estudantil", "Sindical", "MST", "Negro", "Feminista", "LGBTQIA+", "Indígena", "De bairro", "Pessoas com deficiência"], False),
    ("05", "Como o poder funciona (e como a gente usa)", "8 verbetes",
     ["Três poderes", "MP e Tribunal de Contas", "Orçamento público", "Partidos", "Coligação e quociente", "Câmara e Senado", "Como cobrar o poder público", "Audiência pública"], False),
]


def pagina_formacao():
    blocos = []
    for num, titulo, meta, itens, aberta in TRILHAS:
        lis = []
        for item in itens:
            if aberta and item == "Esquerda e direita":
                lis.append('<li><a href="verbete-esquerda-e-direita.html">De onde vem esquerda e direita</a></li>')
            else:
                lis.append(f"<li>{item}</li>")
        blocos.append(f"""<details class="trilha"{' open' if aberta else ''}>
  <summary>
    <span class="trilha__num">{num}</span>
    <span class="trilha__titulo">{titulo}</span>
    <span class="trilha__meta">{meta}</span>
  </summary>
  <div class="trilha__corpo">
    <ul>{''.join(lis)}</ul>
  </div>
</details>""")
    return head(
        "Formação — Escola Impulso | Movimento Impulso Jovem",
        "Formação não é ler muito, é entender o que acontece com a gente. Sete trilhas, 54 verbetes e blocos: de onde vem as palavras que a gente usa até como cobrar o poder público."
    ) + cabecalho("formacao.html") + f"""
<main id="conteudo">
  <section class="secao">
    <div class="envelope">
      <div class="cabeca__grade">
        <div>
          <p class="rotulo">Formação · Escola Impulso</p>
          <h1>Formação não é ler muito.<br>É entender o que acontece com a gente.</h1>
        </div>
        <p class="mb-0">Sete trilhas, 54 verbetes e blocos, na ordem de leitura: da palavra que a gente
        usa até como cobrar o poder público.</p>
      </div>

      <div class="trilhas mt-5">
        {''.join(blocos)}
      </div>

      <div class="caixa caixa--preta mt-5">
        <p class="olho olho--vermelho">Comece por aqui</p>
        <h2>De onde vem esquerda e direita</h2>
        <p>O primeiro verbete do site. Seis minutos de leitura, com as fontes no fim.</p>
        <a class="botao botao--vermelho" href="verbete-esquerda-e-direita.html">Abrir o verbete</a>
      </div>

      <div class="duas-colunas mt-6">
        <div>
          <p class="rotulo">Biblioteca Virtual</p>
          <h2>Livros pra ler de graça</h2>
          <p class="largura-texto">Página própria, com busca. Cada livro com capa, resumo e o link
          do arquivo, que fica aberto no Drive do movimento.</p>
          <a class="acao" href="biblioteca.html">Abrir a Biblioteca Virtual {ico("seta")}</a>
        </div>
        <div>
          <p class="rotulo">Como usar</p>
          <p class="largura-texto">Trilha é caminho, não prova. Comece pela 1, leia o verbete, volta
          pra próxima. Ninguém precisa ler tudo pra entrar na conversa — e ninguém vai ser cobrado
          na reunião por não ter lido.</p>
        </div>
      </div>
    </div>
  </section>
</main>
""" + rodape() + fim()


# ----------------------------------------------------------- BIBLIOTECA
LIVROS = [
    dict(slug="o-capital", titulo="O Capital", autor="Karl Marx", ano="1867", assunto="Teoria",
         licenca="Domínio público", peso="8,3 MB",
         resumo="A crítica da economia política em que o movimento se apoia: mercadoria, mais-valia e o que acontece com o trabalho quando ele vira preço.",
         link="https://drive.google.com/file/d/1oFaqDHg3XsNEcU4srRprRf7C_oyhEhXe/view"),
    dict(slug="origem-familia", titulo="A Origem da Família, da Propriedade Privada e do Estado",
         autor="Friedrich Engels", ano="1884", assunto="Teoria", licenca="Domínio público", peso="1,3 MB",
         resumo="Como a família, a propriedade e o Estado nasceram — e por que nenhum dos três existiu sempre.",
         link="https://drive.google.com/file/d/1OORFFXOmG1NdOvUNNpwFY1zn9qj4IKiF/view"),
    dict(slug="imperialismo", titulo="O Imperialismo, etapa superior do capitalismo",
         autor="Vladimir Lênin", ano="1917", assunto="Teoria", licenca="Domínio público", peso="2,0 MB",
         resumo="O texto de 1917 que explica por que a expansão do capital termina em domínio político e em guerra.",
         link="https://drive.google.com/file/d/1Ac9yRzXLQ8DKTWlc7yUSsMGPzuqdOnu8/view"),
    dict(slug="classe-trabalhadora", titulo="A Situação da Classe Trabalhadora na Inglaterra",
         autor="Friedrich Engels", ano="1845", assunto="História", licenca="Domínio público", peso="5,1 MB",
         resumo="A miséria de Manchester descrita por quem andou nas ruas: a primeira grande reportagem sobre a classe trabalhadora.",
         link="https://drive.google.com/file/d/1CqShQECZWI5gzbHROTj_6VHduiZAHobv/view"),
    dict(slug="capital-popular", titulo="O Capital: uma leitura popular", autor="Carlo Cafiero", ano="1879",
         assunto="Divulgação", licenca="Domínio público", peso="24,3 MB",
         resumo="A explicação de O Capital em linguagem direta, feita por um militante italiano. É o melhor primeiro livro da estante.",
         link="https://drive.google.com/file/d/1KOh5qgu5JulSXPd1ZCHdJXJfAkrjbesI/view"),
    dict(slug="socialista", titulo="Por que sou socialista", autor="Albert Einstein", ano="1949",
         assunto="Divulgação", licenca="Domínio público", peso="134 KB",
         resumo="Poucas páginas de 1949 em que o físico explica por que escolheu o socialismo. Curto e bom pra começar conversa.",
         link="https://drive.google.com/file/d/1sGUpedKs2P0YJLAjNa23xV1JUJK2CihP/view"),
]


def cartao_livro(l):
    import unicodedata
    def sem_acento(t):
        return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn").lower()
    return f"""<article class="livro" data-livro data-titulo="{sem_acento(l['titulo'])}" data-assunto="{l['assunto']}">
  <img class="livro__capa" src="assets/capas/{l['slug']}.jpg" alt="Capa de {l['titulo']}" width="104" height="148" loading="lazy" decoding="async">
  <div>
    <h3>{l['titulo']}</h3>
    <p class="livro__meta">{l['autor']} · {l['ano']} · <b>{l['licenca']}</b> · PDF · {l['peso']}</p>
    <p>{l['resumo']}</p>
    <a class="acao" href="{l['link']}" target="_blank" rel="noopener noreferrer">Abrir no Drive {ico("abrir")}</a>
  </div>
</article>"""


def pagina_biblioteca():
    assuntos = ["Todos", "Teoria", "História", "Divulgação"]
    filtros = "".join(
        f'<button class="filtro" type="button" data-filtro="{a}" aria-pressed="{"true" if a == "Todos" else "false"}">{a}</button>'
        for a in assuntos
    )
    return head(
        "Biblioteca Virtual — livros em domínio público | Movimento Impulso Jovem",
        "Estante de livros em domínio público e cartilhas do movimento. Busca por nome, capa, resumo e link direto pro arquivo no Drive, sem cadastro."
    ) + cabecalho("biblioteca.html") + f"""
<main id="conteudo">
  <section class="secao">
    <div class="envelope">
      <div class="cabeca__grade">
        <div>
          <p class="rotulo">Formação · Biblioteca Virtual</p>
          <h1>Biblioteca<br>Virtual</h1>
        </div>
        <p class="mb-0">Livros, clássicos e cartilhas pra ler de graça. Cada ficha tem capa, resumo e o
        link do arquivo. O site não guarda o livro: aponta pra ele.</p>
      </div>

      <div class="busca" role="search">
        <div class="busca__campo">
          <label class="oculto-visual" for="campo-busca">Buscar por nome do livro</label>
          {ico("busca")}
          <input id="campo-busca" type="search" name="q" placeholder="Buscar por nome do livro"
                 autocomplete="off" data-busca>
        </div>
      </div>

      <div class="filtros" role="group" aria-label="Filtrar por assunto">{filtros}</div>

      <p class="contagem" data-contagem aria-live="polite">{len(LIVROS)} livros na estante</p>

      <div class="grade-livros" data-estante>
        {''.join(cartao_livro(l) for l in LIVROS)}
        <p class="vazio" data-vazio hidden>Nenhum livro com esse nome na estante do site. A pasta do
        Drive do movimento tem mais de cem títulos.</p>
      </div>

      <noscript><p class="aviso mt-4">A busca e os filtros precisam de JavaScript. Todos os livros
      estão listados nesta página e o link de cada um abre direto no Drive.</p></noscript>

      <div class="duas-colunas mt-6">
        <div class="caixa">
          <p class="olho olho--vermelho">Como funciona</p>
          <ol class="mb-0">
            <li>A ficha traz capa, resumo e licença.</li>
            <li>O arquivo fica na pasta pública do Drive do movimento.</li>
            <li>O link abre o livro em outra aba. Sem cadastro, sem senha.</li>
          </ol>
        </div>
        <div class="caixa caixa--preta">
          <p class="olho olho--vermelho">Tem um livro pra indicar?</p>
          <p>Manda o arquivo ou o link no direct do Instagram. A gente confere a licença, publica a
          ficha e põe seu nome como quem indicou.</p>
          <div class="acoes">
            <a class="botao botao--mini botao--vermelho" href="{INSTAGRAM_DM}" target="_blank" rel="noopener noreferrer">{ico("instagram")} Chamar no direct</a>
            <a class="botao botao--mini botao--claro" href="{DRIVE_PASTA}" target="_blank" rel="noopener noreferrer">Ver a pasta completa</a>
          </div>
        </div>
      </div>

      <p class="nota-pe">Só entra obra em domínio público, com licença aberta ou material do próprio
      movimento. Livro que ainda tem direitos, a ficha indica onde comprar ou pegar emprestado. As
      capas são desenhadas pelo movimento quando o arquivo não tem capa.</p>
    </div>
  </section>
</main>
""" + rodape() + fim()


# ------------------------------------------------------------- PARTICIpe
def pagina_participe():
    cc = emails_cc()
    cc_hidden = f'<input type="hidden" name="_cc" value="{cc}">' if cc else ""
    return head(
        "Contato — fale com a gente | entre no movimento | Impulso Jovem",
        "Fale com a gente: preencha o formulário e a resposta chega no e-mail do movimento, com retorno em até 48 horas. Para entrar no grupo, chame no direct do Instagram. Divisa Alegre e Águas Vermelhas (MG)."
    ) + cabecalho("participe.html") + f"""
<main id="conteudo">
  <section class="secao">
    <div class="envelope grade-texto-foto">
      <div>
        <p class="rotulo">Contato · fale com a gente</p>
        <h1>Não precisa saber discurso.<br>Precisa <em>querer</em>.</h1>
        <p class="entrada">Escreve aqui e a gente responde em até 48 horas, no WhatsApp que você
        deixar. Se preferir falar agora, chama no direct do Instagram — é por lá que os admins passam o
        link do grupo.</p>

        <form class="formulario" data-formulario name="participe" method="post"
              action="{FORM_ACTION}" data-endpoint="{FORM_AJAX}" novalidate>
          <input type="hidden" name="_subject" value="Novo cadastro no site do Impulso Jovem">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_captcha" value="false">
          {cc_hidden}
          <p class="oculto-visual"><label>Não preencha: <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></p>

          <div class="campo">
            <label class="campo__label" for="nome">Nome</label>
            <input id="nome" name="nome" type="text" autocomplete="name" placeholder="Como te chamamos"
                   aria-describedby="erro-nome" required>
            <p class="erro" id="erro-nome" role="alert"></p>
          </div>

          <div class="campo">
            <label class="campo__label" for="cidade">Cidade</label>
            <input id="cidade" name="cidade" type="text" autocomplete="address-level2"
                   placeholder="Divisa Alegre, Águas Vermelhas ou outra" aria-describedby="erro-cidade" required>
            <p class="erro" id="erro-cidade" role="alert"></p>
          </div>

          <div class="campo">
            <label class="campo__label" for="whatsapp">WhatsApp com DDD</label>
            <p class="campo__ajuda" id="ajuda-whatsapp">Só usamos pra te chamar. Ex.: (33) 99999-0000</p>
            <input id="whatsapp" name="whatsapp" type="tel" inputmode="numeric" autocomplete="tel"
                   placeholder="33 99999-0000" aria-describedby="ajuda-whatsapp erro-whatsapp" required>
            <p class="erro" id="erro-whatsapp" role="alert"></p>
          </div>

          <div class="campo">
            <label class="campo__label" for="faz">O que você faz</label>
            <input id="faz" name="faz" type="text" placeholder="Estudo, trabalho, os dois">
          </div>

          <p class="aviso"><strong>Uso dos seus dados:</strong> nome, cidade, WhatsApp e o que você faz
          são enviados por e-mail para o movimento, pelo serviço FormSubmit. Usamos só para falar do
          movimento e avisar dos encontros: nada é vendido nem compartilhado. Para sair, é só pedir
          no próprio WhatsApp.</p>

          <div class="retorno" tabindex="-1" role="status" aria-live="polite"></div>

          <button class="botao botao--vermelho" type="submit">
            <span class="botao__giro" aria-hidden="true"></span>
            <span class="botao__texto">Enviar mensagem</span>
          </button>
        </form>
      </div>

      <aside class="aside--fixo">
        <h2 class="olho">Como entrar</h2>

        <div class="caixa mb-4">
          <h3>Entrar no grupo</h3>
          <p>O link do grupo não fica público. Chama no direct do Instagram que a gente manda.</p>
          <a class="acao" href="{INSTAGRAM_DM}" target="_blank" rel="noopener noreferrer">Chamar no Instagram {ico("abrir")}</a>
        </div>

        <div class="caixa mb-4">
          <h3>Trabalhar numa frente</h3>
          <p class="mb-0">Formação · Mobilização de redes sociais · Militância</p>
        </div>

        <div class="caixa caixa--preta">
          <h3>O que acontece depois</h3>
          <ol class="mb-0">
            <li>Sua mensagem chega no e-mail do movimento.</li>
            <li>A gente responde em até 48 horas, no WhatsApp que você deixou.</li>
            <li>Se quiser o link do grupo, ele vem por aqui.</li>
          </ol>
        </div>
      </aside>
    </div>
  </section>
</main>
""" + rodape() + fim()


# ----------------------------------------------------------------- APOIE
def pagina_apoie():
    return head(
        "Apoie — nem todo apoio é dinheiro | Movimento Impulso Jovem",
        "Habilidade, espaço e material: o que o movimento precisa antes de caixa. PIX do Impulso Jovem, chave, nome e banco à vista."
    ) + cabecalho("apoie.html") + f"""
<main id="conteudo">
  <section class="secao">
    <div class="envelope">
      <p class="rotulo">Apoie</p>
      <h1>Nem todo apoio<br>é <em>dinheiro</em></h1>
      <p class="entrada">O que o movimento precisa hoje, antes de caixa: gente com tempo, profissão e material.</p>

      <div class="lista-bandeiras">
        <div class="bandeira">
          <span class="bandeira__num">01</span>
          <div class="bandeira__texto">
            <h3>Habilidade</h3>
            <p>Advogado, designer, professor, gente que sabe dirigir, gravar vídeo ou fazer planilha.</p>
          </div>
        </div>
        <div class="bandeira">
          <span class="bandeira__num">02</span>
          <div class="bandeira__texto">
            <h3>Espaço e material</h3>
            <p>Sala pra reunião, impressão, som emprestado, carona pros atos.</p>
          </div>
        </div>
        <div class="bandeira">
          <span class="bandeira__num">03</span>
          <div class="bandeira__texto">
            <h3>Caixa, com transparência</h3>
            <p>Entra no PIX único do movimento e a prestação de contas fica publicada nesta mesma página.</p>
          </div>
        </div>
      </div>

      <div class="faixa-pix">
        <div class="envelope pix pix--unica">
          <div>
            <p class="olho olho--vermelho">Pix do movimento · caixa único</p>
            <p class="pix__chave">{PIX_CHAVE}</p>
            <p class="pix__dados">Chave telefone · {PIX_NOME} · {PIX_BANCO}</p>
            <p class="pix__dados">Cai no caixa das duas cidades. A prestação de contas fica publicada nesta página.</p>
            <div class="acoes mt-3">
              <button class="botao botao--vermelho" type="button" data-copiar="+5533984158262">{ico("copiar")} Copiar a chave Pix</button>
            </div>
          </div>
        </div>
      </div>

      <h2 class="mt-6">Materiais e redes do movimento</h2>
      <p class="largura-texto">Baixa o material, imprime, cola no muro — e acompanha a gente onde a coisa acontece.</p>
      <div class="tres-colunas mt-4">
        <div class="caixa">
          <img src="assets/img/wordmark.png" alt="Wordmark IMPULSO em vermelho" width="240" height="89" loading="lazy">
          <h3 class="mt-3">Logo do movimento</h3>
          <p class="fina">Punho e palavra, em PNG com fundo transparente.</p>
          <a class="botao botao--mini" href="assets/img/punho.png" download>Baixar o punho</a>
        </div>
        <div class="caixa">
          <h3>Segue no Instagram</h3>
          <p class="fina">É onde o movimento aparece primeiro: ato, pauta, bastidor e o que rola na região.</p>
          <a class="botao botao--mini botao--vermelho" href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">{ico("instagram")} @impulsojovem.33</a>
        </div>
        <div class="caixa caixa--preta">
          <h3>Sem dinheiro?</h3>
          <p>Manda habilidade, espaço ou material. Chama no direct do Instagram que a gente combina o que serve.</p>
          <a class="botao botao--mini botao--claro" href="{INSTAGRAM_DM}" target="_blank" rel="noopener noreferrer">{ico("instagram")} Chamar no direct</a>
        </div>
      </div>
    </div>
  </section>
</main>
""" + rodape() + fim()


# ----------------------------------------------------- CÓDIGO DE CONDUTA
PROIBIDOS = [
    ("01", "Racismo e injúria racial", "Cor, origem, religião de matriz africana, cabelo, sotaque. Piada não é piada."),
    ("02", "LGBTfobia", "Contra lésbicas, gays, bissexuais, travestis e pessoas trans. Nome social é o nome da pessoa."),
    ("03", "Misoginia e violência contra a mulher", "Física, psicológica, sexual, patrimonial ou moral. Nenhuma delas é assunto privado."),
    ("04", "Assédio sexual e moral", "No movimento, no trabalho e na escola. Sempre tem alguém usando poder pra constranger."),
    ("05", "Capacitismo", "Tratar pessoa com deficiência como incapaz, esconder ou não adaptar o espaço e a fala."),
    ("06", "Humilhação e intimidação sistemática", "Bullying, exposição e piada repetida que rebaixa alguém. Repetição não é brincadeira."),
]

LEIS = [
    ("Racismo", "Lei 7.716/1989 tipifica os crimes de preconceito de raça ou de cor. A Constituição (art. 5º, XLII) diz que racismo é crime inafiançável e imprescritível, punido com reclusão. Desde a Lei 14.532/2023, a injúria racial é tratada como racismo."),
    ("LGBTfobia", "Em 2019 o STF (ADO 26 e MI 4733) enquadrou homofobia e transfobia na Lei 7.716/1989, até o Congresso legislar sobre o tema. O nome social é garantido pelo Decreto 8.727/2016 na administração pública — e é regra aqui dentro também."),
    ("Misoginia e violência contra a mulher", "A Lei 11.340/2006 (Maria da Penha) define cinco formas de violência: física, psicológica, sexual, patrimonial e moral. A Lei 13.104/2015 colocou o feminicídio como qualificadora do homicídio; a Lei 14.188/2021 criou o crime de violência psicológica e o Sinal Vermelho."),
    ("Assédio sexual e moral", "Assédio sexual é crime pelo art. 216-A do Código Penal, desde a Lei 10.224/2001. Assédio moral no trabalho é falta grave do empregador e pode ser cobrado na Justiça do Trabalho (CLT, art. 483)."),
    ("Capacitismo", "Lei 13.146/2015 (Lei Brasileira de Inclusão) e Lei 7.853/1989, que tipifica crimes contra pessoas com deficiência, inclusive por recusa de acesso, de informação e de comunicação."),
    ("Humilhação e intimidação", "Lei 13.185/2015 define a intimidação sistemática (bullying) e obriga escolas e clubes a prevenir. O constrangimento ilegal está no art. 146 do Código Penal."),
    ("Tortura e violência de Estado", "Lei 9.455/1997 tipifica a tortura, inclusive quando praticada por agente público. O art. 5º, III, da Constituição proíbe tortura e tratamento desumano."),
]


def pagina_conduta():
    proibidos = "".join(
        f"""<div class="bandeira" id="proibido-{n}">
  <span class="bandeira__num">{n}</span>
  <div class="bandeira__texto"><h3>{t}</h3><p>{d}</p></div>
</div>""" for n, t, d in PROIBIDOS
    )
    leis = "".join(
        f"""<div class="lei">
  <span class="lei__num">{i:02d}</span>
  <p class="lei__tema">{tema}</p>
  <p>{texto}</p>
</div>""" for i, (tema, texto) in enumerate(LEIS, 1)
    )
    return head(
        "Código de conduta | Movimento Impulso Jovem",
        "O que o Impulso não aceita, o que esperamos de quem está junto, o que acontece quando o caso é crime e a lei que existe atrás de cada regra."
    ) + cabecalho("codigo-de-conduta.html") + f"""
<main id="conteudo">
  <section class="secao">
    <div class="envelope">
      <p class="rotulo">Documento público</p>
      <h1>Código de<br><em>conduta</em></h1>

      <div class="duas-colunas mt-5">
        <div>
          <p class="entrada">O Impulso nasceu em outubro de 2026, da união de jovens estudantes e
          trabalhadores de Divisa Alegre e Águas Vermelhas que defendiam as mesmas pautas. Um movimento
          assim só se sustenta se a mesma régua valer pra dentro e pra fora: o lugar que cobra o mundo
          é o lugar onde ninguém pode ser tratado como sobra.</p>
          <p>Vale nas reuniões, nos atos, nos espaços do movimento, nas redes e em qualquer lugar onde
          alguém esteja representando o Impulso — pra quem chega agora e pra coordenação.</p>
        </div>
        <div>
          <h2 class="olho">O que a gente espera de quem está aqui</h2>
          <ol>
            <li>Chamar cada pessoa pelo nome que ela usa.</li>
            <li>Escutar antes de responder e não falar pela pessoa.</li>
            <li>Não expor quem trouxe um assunto delicado.</li>
            <li>Dividir tarefa e crédito: trabalho invisível também é trabalho.</li>
            <li>Corrigir quando erra, sem repetir a cena.</li>
          </ol>
        </div>
      </div>

      <h2 class="mt-6" id="o-que-nao-tem-espaco">O que não tem espaço aqui</h2>
      <div class="lista-bandeiras">
        {proibidos}
      </div>

      <div class="caixa caixa--alerta mt-5">
        <h3>Quando o caso é crime</h3>
        <p class="mb-0">O movimento não julga no lugar da Justiça: acompanha a pessoa até a delegacia,
        ajuda a registrar o boletim e a chegar na Defensoria Pública e no Ministério Público. Procurar
        a polícia ou a Defensoria é um direito seu — com ou sem a gente.</p>
        <p class="nota-pe">190 polícia · 100 direitos humanos · 180 central de atendimento à mulher</p>
      </div>

      <h2 class="mt-6" id="a-lei">O que a lei diz</h2>
      <p class="largura-texto">Nada aqui foi inventado pelo movimento: cada item acima já é crime ou
      ilícito previsto na lei brasileira.</p>
      <div class="mt-4">
        {leis}
      </div>
      <p class="nota-pe">Resumo de leitura, não é consulta jurídica. Em caso de dúvida, procure a
      Defensoria Pública.</p>
    </div>
  </section>
</main>
""" + rodape() + fim()


# --------------------------------------------------------------- VERBETE
def pagina_verbete():
    raiz = ""
    return head(
        "De onde vem esquerda e direita | Formação · Impulso Jovem",
        "Verbete da trilha 1 da Escola Impulso: de onde vêm as palavras esquerda e direita, o que elas resumem hoje e por que isso importa pra gente."
    ) + cabecalho("formacao.html") + f"""
<main id="conteudo">
  <article class="secao">
    <div class="envelope">
      <nav class="fina mb-4" aria-label="Você está aqui">
        <a href="formacao.html">Formação</a> · Trilha 1 — Ideias · Verbete 01
      </nav>

      <div class="verbete">
        <h1>De onde vem<br>esquerda e direita</h1>
        <p class="fina">6 min de leitura · atualizado em novembro de 2026</p>

        <div class="datas">
          <div><h3>1789</h3><p>Na Assembleia Francesa, os deputados se dividem: direita do rei, esquerda da igualdade.</p></div>
          <div><h3>1848</h3><p>O Manifesto Comunista dá à esquerda o vocabulário da classe trabalhadora.</p></div>
          <div><h3>1917</h3><p>A Revolução Russa divide a esquerda: reforma ou revolução.</p></div>
        </div>

        <p>Em 1789, quando os deputados do Terceiro Estado se juntaram para escrever as novas regras da
        França, eles se sentaram em lugares diferentes da Assembleia. A direita da mesa ficavam os que
        defendiam o rei, os privilégios da nobreza e o voto por ordem. A esquerda, os que queriam
        igualdade de direitos, fim dos privilégios e voto por cabeça.</p>

        <p>As palavras nasceram daí: de um lugar na sala. Ninguém as inventou como teoria — elas
        descrevem onde cada um estava sentado numa disputa muito concreta, sobre quem pagava imposto
        e quem mandava.</p>

        <p>Depois disso, o eixo andou pelo mundo e mudou de conteúdo várias vezes. Em 1848, com o
        Manifesto Comunista, a esquerda ganhou o vocabulário da classe trabalhadora. Em 1917, com a
        Revolução Russa, ela se dividiu: de um lado quem acreditava em conquistar direitos pela
        eleição e pela reforma, do outro quem defendia a revolução. As duas continuam se chamando de
        esquerda.</p>

        <div class="caixa mt-5">
          <p class="olho">Conceito-chave</p>
          <p class="mb-0">Esquerda e direita não são partidos nem nomes de pessoas. São duas posturas
          diante da desigualdade.</p>
        </div>

        <h2 class="mt-6">Hoje</h2>
        <p>Hoje a distinção mais usada é a do cientista político Norberto Bobbio: esquerda e direita se
        diferenciam pelo que cada uma faz com a desigualdade. A esquerda tende a tratar a desigualdade
        como algo a corrigir; a direita tende a tratá-la como natural, necessária ou inevitável.</p>

        <div class="caixa caixa--preta mt-5">
          <p class="olho olho--vermelho">Por que isso importa pra gente hoje</p>
          <p class="mb-0">Chamar alguém de “esquerdista” como ofensa só funciona quando a pessoa não sabe
          de onde vem a palavra. Saber que ela nasceu de gente que queria igualdade de direitos é a
          melhor resposta que existe — e é mais forte que xingar de volta.</p>
        </div>

        <h2 class="mt-6">Fontes</h2>
        <ol class="fontes">
          <li>BOBBIO, Norberto. <em>Direita e esquerda</em>. São Paulo: Editora Unesp.</li>
          <li>HOBSBAWM, Eric. <em>A Era das Revoluções (1789–1848)</em>. Paz e Terra.</li>
          <li>MARX, Karl; ENGELS, Friedrich. <em>Manifesto Comunista</em> (1848), domínio público.</li>
          <li>Assembleia Nacional da França — página de história da Revolução.</li>
        </ol>

        <h2 class="mt-6">Leia também</h2>
        <ul>
          <li><a href="verbete-esquerda-e-direita.html">O que é fascismo (e o que não é)</a></li>
          <li><a href="verbete-esquerda-e-direita.html">Reforma ou revolução</a></li>
          <li><a href="biblioteca.html">O Manifesto Comunista, na Biblioteca Virtual</a></li>
        </ul>

        <hr class="separador">
        <div class="acoes">
          <a class="botao botao--vermelho" href="participe.html">Falar com a gente</a>
          <a class="botao" href="formacao.html">Voltar pras trilhas</a>
        </div>
      </div>
    </div>
  </article>
</main>
""" + rodape() + fim()


# ------------------------------------------------------------------ 404
def pagina_404():
    return head(
        "Página não encontrada | Movimento Impulso Jovem",
        "Essa página não existe. Volta pro começo e segue o movimento."
    ) + cabecalho("") + f"""
<main id="conteudo">
  <section class="secao">
    <div class="envelope">
      <p class="rotulo">Erro 404</p>
      <h1>Essa página<br>não <em>existe</em>.</h1>
      <p class="entrada">O endereço mudou, ou nunca existiu. O movimento continua no mesmo lugar.</p>
      <div class="acoes">
        <a class="botao botao--vermelho" href="index.html">Voltar pra Home</a>
        <a class="botao" href="bandeiras.html">Ver as bandeiras</a>
      </div>
    </div>
  </section>
</main>
""" + rodape() + fim()


# ------------------------------------------------------------------ main
if __name__ == "__main__":
    escrever("index.html", pagina_home())
    escrever("o-impulso.html", pagina_impulso())
    escrever("bandeiras.html", pagina_bandeiras())
    # formacao.html e os verbetes são gerados por _verbetes.py
    # biblioteca.html é gerado por _biblioteca.py, a partir da pasta do Drive
    escrever("participe.html", pagina_participe())
    escrever("apoie.html", pagina_apoie())
    escrever("codigo-de-conduta.html", pagina_conduta())
    escrever("404.html", pagina_404())
