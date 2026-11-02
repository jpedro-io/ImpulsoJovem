#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regera biblioteca.html a partir da pasta de livros do Drive.

Entradas: ../.tmp/catalogo_bruto.json (id, nome, slug da capa, bytes)
          ../.tmp/catalogo.py       (fichas: título, autor, ano, área, licença, resumo)
Saída:    biblioteca.html
"""
import json, os, sys, unicodedata, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import _gerar as G

TMP = "/home/user/.tmp"
spec = importlib.util.spec_from_file_location("cat", f"{TMP}/catalogo.py")
cat = importlib.util.module_from_spec(spec); spec.loader.exec_module(cat)
bruto = json.load(open(f"{TMP}/catalogo_bruto.json", encoding="utf-8"))

AREAS = ["Todos", "Teoria", "História", "Brasil", "Mundo", "Economia",
         "Raça e gênero", "Educação", "Trabalho", "Literatura", "Relatórios"]

def esc(t):
    """Escapa texto pra HTML (títulos e resumos têm &, aspas e afins)."""
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))

def sem_acento(t):
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn").lower()

def peso(bytes_):
    if not bytes_:
        return ""
    if bytes_ >= 1_000_000:
        return f"{bytes_/1_000_000:.1f} MB".replace(".", ",")
    return f"{max(1, round(bytes_/1000))} KB"

livros = []
for i, arq in enumerate(bruto):
    ficha = cat.DADOS.get(i)
    if not ficha or "dup" in ficha:
        continue
    livros.append(dict(
        id=arq["id"], slug=arq["capa"], bytes=arq["bytes"],
        t=ficha["t"], a=ficha.get("a", ""), y=ficha.get("y", ""),
        area=ficha.get("area", "Teoria"), li=ficha.get("li", "Edição comercial"),
        r=ficha.get("r", "")
    ))

livros.sort(key=lambda l: sem_acento(l["t"]))
print("livros na estante:", len(livros))

def cartao(l):
    link = f"https://drive.google.com/file/d/{l['id']}/view"
    meta = " · ".join(x for x in [esc(l["a"]), esc(l["y"]), f"<b>{esc(l['li'])}</b>", "PDF", peso(l["bytes"])] if x)
    return f"""<article class="livro" data-livro data-titulo="{esc(sem_acento(l['t']))}" data-autor="{esc(sem_acento(l['a']))}" data-area="{esc(l['area'])}">
  <a class="livro__capa-link" href="{link}" target="_blank" rel="noopener noreferrer" tabindex="-1" aria-hidden="true"><img class="livro__capa" src="assets/capas/{l['slug']}.jpg" alt="" width="104" height="148" loading="lazy" decoding="async"></a>
  <div>
    <h3><a href="{link}" target="_blank" rel="noopener noreferrer">{esc(l['t'])}</a></h3>
    <p class="livro__meta">{meta}</p>
    <p>{esc(l['r'])}</p>
    <div class="livro__acoes">
      <a class="botao botao--mini botao--vermelho" href="{link}" target="_blank" rel="noopener noreferrer">Abrir no Drive {G.ico("abrir")}</a>
      <button class="copiar" type="button" data-copiar="{link}" data-copiar-ok="Link copiado" title="Copia o endereço do livro">{G.ico("copiar")} Copiar link</button>
    </div>
  </div>
</article>"""

filtros = "".join(
    f'<button class="filtro" type="button" data-filtro="{a}" aria-pressed="{"true" if a=="Todos" else "false"}">{a}</button>'
    for a in AREAS
)

corpo = f"""<main id="conteudo">
  {G.faixa()}
  <section class="secao">
    <div class="envelope">
      <div class="cabeca__grade">
        <div>
          <p class="rotulo">Formação · Biblioteca Virtual</p>
          <h1>Biblioteca<br><em>Virtual</em></h1>
        </div>
        <p class="mb-0">{len(livros)} arquivos da pasta do movimento, um por ficha: capa, resumo e o
        link que abre o livro direto no Drive — não a pasta, o livro.</p>
      </div>

      <div class="busca" role="search">
        <div class="busca__campo">
          <label class="oculto-visual" for="campo-busca">Buscar por nome do livro ou de quem escreveu</label>
          {G.ico("busca")}
          <input id="campo-busca" type="search" name="q" placeholder="Buscar por livro ou autor"
                 autocomplete="off" data-busca>
        </div>
      </div>

      <div class="filtros" role="group" aria-label="Filtrar por assunto">{filtros}</div>

      <p class="contagem" data-contagem aria-live="polite">{len(livros)} livros na estante</p>

      <div class="grade-livros" data-estante>
{chr(10).join(cartao(l) for l in livros)}
        <p class="vazio" data-vazio hidden>Nada com esse nome na estante. Tenta outra palavra ou abre a pasta completa do Drive.</p>
      </div>

      <noscript><p class="aviso mt-4">A busca e os filtros precisam de JavaScript. Todos os
      {len(livros)} livros estão listados nesta página e cada botão abre o arquivo direto no Drive.</p></noscript>

      <div class="duas-colunas mt-6">
        <div class="caixa">
          <p class="olho olho--vermelho">Como funciona</p>
          <ol class="mb-0">
            <li>A ficha traz capa, autor, ano, licença e o peso do arquivo.</li>
            <li>O botão abre o PDF daquele livro no Drive, em outra aba.</li>
            <li>Sem cadastro, sem senha, sem espera.</li>
          </ol>
        </div>
        <div class="caixa caixa--preta">
          <p class="olho olho--vermelho">Tem um livro pra indicar?</p>
          <p>Manda o arquivo ou o link no direct do Instagram. A gente confere, monta a ficha e põe
          seu nome como quem indicou.</p>
          <div class="acoes">
            <a class="botao botao--mini botao--vermelho" href="{G.INSTAGRAM_DM}" target="_blank" rel="noopener noreferrer">{G.ico("instagram")} Chamar no direct</a>
            <a class="botao botao--mini botao--claro" href="{G.DRIVE_PASTA}" target="_blank" rel="noopener noreferrer">Ver a pasta completa</a>
          </div>
        </div>
      </div>

      <p class="nota-pe">A estante é o retrato da pasta do movimento: entram obras em domínio público,
      material aberto do próprio movimento e edições que a gente estuda. Onde o livro ainda tem
      direitos, o PDF é cópia de estudo — se puder, compre a edição e prestigie quem publicou.
      As capas são a primeira página de cada arquivo.</p>
    </div>
  </section>
</main>
"""

html = (G.head(
    f"Biblioteca Virtual — {len(livros)} livros para baixar | Movimento Impulso Jovem",
    f"Estante com {len(livros)} livros da pasta do movimento: teoria, história, Brasil, mundo, economia, raça e gênero. Busca por título ou autor, capa, resumo e link direto pro arquivo.")
    + G.cabecalho("biblioteca.html") + corpo + G.rodape() + G.fim())

G.escrever("biblioteca.html", html)

# lista de capas usadas, pra conferir o que sobrou na pasta
usadas = {l["slug"] for l in livros}
sobrando = sorted(set(f[:-4] for f in os.listdir(f"{AQUI}/assets/capas") if f.endswith(".jpg")) - usadas)
print("capas sem uso:", len(sobrando), sobrando[:8])
