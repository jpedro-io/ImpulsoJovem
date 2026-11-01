#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as páginas dos verbetes e a página Formação (Escola Impulso)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import _gerar as G
from verbete_dados import V, TRILHAS
try:
    from verbete_amplia import AMPLIA
except Exception:
    AMPLIA = {}

TRILHA_INFO = [
    ("1", "Ideias: de onde vêm as palavras que a gente usa"),
    ("2", "Nossa história: o Brasil que produziu a gente"),
    ("2B", "Minas Gerais: o estado que produziu a nossa região"),
    ("3", "Ditadura militar: 21 anos, ato por ato"),
    ("4", "O mundo: o que aconteceu fora que mexeu aqui"),
    ("5", "Quem já lutou: movimentos sociais"),
    ("6", "Como o poder funciona (e como a gente usa)"),
]

def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))

por_trilha = {}
for v in V:
    por_trilha.setdefault(v["tr"], []).append(v)

def vizinhos(v):
    irmaos = por_trilha[v["tr"]]
    i = irmaos.index(v)
    ant = irmaos[i - 1] if i > 0 else None
    prox = irmaos[i + 1] if i < len(irmaos) - 1 else None
    return ant, prox

# ─────────────────────────────────────────────── páginas de verbete
for v in V:
    ant, prox = vizinhos(v)
    datas = "".join(f"<div><h3>{esc(d[0])}</h3><p>{esc(d[1])}</p></div>" for d in v["datas"])
    paragrafos = "".join(f"<p>{esc(p)}</p>" for p in v["txt"])
    extras_txt = AMPLIA.get(v["slug"], [])
    extras = "".join(f"<p>{esc(p)}</p>" for p in extras_txt)
    minutos = max(4, round(sum(len(x) for x in v["txt"] + extras_txt) / 450))
    fontes = "".join(f"<li>{esc(f)}</li>" for f in v["f"])
    leia = "".join(f'<li><a href="verbete-{esc(s)}.html">{esc(t)}</a></li>' for t, s in v["leia"])
    nav_ant = (f'<a class="botao botao--mini" href="verbete-{ant["slug"]}.html">← {esc(ant["t"])}</a>'
               if ant else '')
    nav_prox = (f'<a class="botao botao--mini botao--vermelho" href="verbete-{prox["slug"]}.html">{esc(prox["t"])} →</a>'
                if prox else '')

    corpo = f"""<main id="conteudo">
  <article class="secao">
    <div class="envelope">
      <nav class="migalha" aria-label="Você está aqui">
        <a href="formacao.html">Formação</a> · {esc(TRILHAS[v["tr"]])} · Verbete {esc(v["n"])}
      </nav>

      <div class="verbete">
        <h1>{esc(v["t"])}</h1>
        <p class="fina">{minutos} min de leitura · atualizado em novembro de 2026</p>

        <div class="datas">{datas}</div>

        {paragrafos}{extras}

        <div class="caixa mt-5">
          <p class="olho">Conceito-chave</p>
          <p class="mb-0">{esc(v["c"])}</p>
        </div>

        <div class="caixa caixa--preta mt-5">
          <p class="olho olho--vermelho">Levar pra roda</p>
          <p class="mb-0">Verbete é base, não ponto final. Leva pra reunião do núcleo, discorda, pergunta:
          formação aqui não é leitura solitária, é conversa com quem está na mesma luta.</p>
        </div>

        <h2 class="mt-6">Fontes</h2>
        <ol class="fontes">{fontes}</ol>

        <h2 class="mt-6">Leia também</h2>
        <ul>{leia}</ul>

        <hr class="separador">
        <div class="acoes">
          {nav_ant}
          <a class="botao botao--mini" href="formacao.html">Todas as trilhas</a>
          {nav_prox}
        </div>
      </div>
    </div>
  </article>
</main>
"""
    html = (G.head(f"{v['t']} | Formação · Impulso Jovem",
                   f"{esc(v['c'])} Verbete da {TRILHAS[v['tr']]} da Escola Impulso.")
            + G.cabecalho("formacao.html") + corpo + G.rodape() + G.fim())
    G.escrever(f"verbete-{v['slug']}.html", html)

# ─────────────────────────────────────────────── página Formação
blocos = []
total = 0
for num, titulo in TRILHA_INFO:
    itens = por_trilha[num]
    total += len(itens)
    lis = "".join(
        f'<li><a href="verbete-{esc(x["slug"])}.html">{esc(x["t"])}</a></li>' for x in itens)
    meta = f"{len(itens)} verbetes" if len(itens) != 4 else "4 verbetes"
    blocos.append(f"""<details class="trilha"{' open' if num == '1' else ''}>
  <summary>
    <span class="trilha__num">{num}</span>
    <span class="trilha__titulo">{esc(titulo)}</span>
    <span class="trilha__meta">{meta}</span>
  </summary>
  <div class="trilha__corpo">
    <ul>{lis}</ul>
  </div>
</details>""")

corpo_formacao = f"""<main id="conteudo">
  {G.faixa()}
  <section class="secao">
    <div class="envelope">
      <p class="rotulo">Formação · Escola Impulso</p>
      <h1>Formação não é ler muito.<br>É <em>entender</em> o que acontece.</h1>
      <p class="entrada largura-texto mt-4">Sete trilhas, {total} verbetes, todos escritos e no ar: da palavra
      que a gente usa até como cobrar o poder público. Cada verbete tem três a cinco minutos de leitura,
      datas, conceito-chave e as fontes no fim.</p>

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
          <p class="largura-texto">143 livros da pasta do movimento, com busca por título ou autor,
          capa, resumo e o link que abre o arquivo direto no Drive.</p>
          <a class="acao" href="biblioteca.html">Abrir a Biblioteca Virtual {G.ico("seta")}</a>
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
"""
html = (G.head(f"Formação — Escola Impulso: {total} verbetes | Movimento Impulso Jovem",
               f"Formação não é ler muito, é entender o que acontece com a gente. Sete trilhas e {total} verbetes escritos: ideias, história do Brasil e de Minas, o mundo, movimentos sociais e como o poder funciona.")
        + G.cabecalho("formacao.html") + corpo_formacao + G.rodape() + G.fim())
G.escrever("formacao.html", html)
print("verbetes gerados:", len(V), "| total anunciado:", total)
