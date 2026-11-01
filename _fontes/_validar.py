# -*- coding: utf-8 -*-
"""Confere o site inteiro sem precisar de navegador.

Roda:  python3 _validar.py
Checa: páginas geradas, links internos, âncoras, ids repetidos,
       classes usadas no HTML que não existem no CSS, e arquivos citados.
"""
import os, re, sys, glob, collections

RAIZ = os.path.dirname(os.path.abspath(__file__))
HTML = sorted(glob.glob(os.path.join(RAIZ, "*.html")))
CSS = os.path.join(RAIZ, "assets/css/estilo.css")

problemas = []
texto = {}
for f in HTML:
    texto[os.path.basename(f)] = open(f, encoding="utf-8").read()

# ---------------------------------------------------------------- 1. páginas
esperadas = 10  # estáticas
ns = [os.path.basename(f) for f in HTML]
print(f"páginas: {len(ns)}  (estáticas {esperadas} + verbetes {len([n for n in ns if n.startswith('verbete-')])})")

# ------------------------------------------------- 2. links e âncoras internos
ids = {n: set(re.findall(r'\bid="([^"]+)"', h)) for n, h in texto.items()}
for nome, h in texto.items():
    for href in re.findall(r'href="([^"]+)"', h):
        if href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
            continue
        alvo, _, ancora = href.partition("#")
        alvo = alvo or nome
        if alvo.endswith(".html") or (not os.path.splitext(alvo)[1] and alvo):
            if alvo not in texto:
                problemas.append(f"{nome}: link para página inexistente → {href}")
            elif ancora and ancora not in ids[alvo]:
                problemas.append(f"{nome}: âncora inexistente → {href}")
        elif not os.path.exists(os.path.join(RAIZ, alvo)):
            problemas.append(f"{nome}: arquivo citado não existe → {href}")
    for src in re.findall(r'src="([^"]+)"', h):
        if src.startswith(("http", "data:")):
            continue
        if not os.path.exists(os.path.join(RAIZ, src)):
            problemas.append(f"{nome}: arquivo inexistente → {src}")

# -------------------------------------------------------- 3. ids repetidos
for nome, h in texto.items():
    repetidos = [i for i, c in collections.Counter(re.findall(r'\bid="([^"]+)"', h)).items() if c > 1]
    if repetidos:
        problemas.append(f"{nome}: id repetido → {', '.join(repetidos)}")

# ------------------------------------------------- 4. classes x CSS
css = open(CSS, encoding="utf-8").read()
no_css = set(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", re.sub(r"/\*.*?\*/", "", css, flags=re.S)))
usadas = collections.Counter()
for h in texto.values():
    for attr in re.findall(r'class="([^"]*)"', h):
        for c in attr.split():
            usadas[c] += 1
faltando = sorted(c for c in usadas if c not in no_css)
if faltando:
    problemas.append(f"classes sem CSS: {', '.join(faltando)}")
sem_uso = sorted(c for c in no_css - set(usadas)
                 if not c.startswith(("is-", "atraso-", "js-")) and len(c) > 3)
print(f"classes sem uso no CSS (só aviso): {', '.join(sem_uso) if sem_uso else 'nenhuma'}")

# ----------------------------------------------------- 5. essenciais por página
for nome, h in texto.items():
    for marca in ('<title>', 'name="description"', 'href="assets/css/estilo.css"', 'src="assets/js/site.js"', 'id="conteudo"'):
        if marca not in h:
            problemas.append(f"{nome}: falta {marca}")

# ---------------------------------------------------------------- 6. sitemap
if not os.path.exists(os.path.join(RAIZ, "sitemap.xml")):
    problemas.append("sitemap.xml não encontrado")

print()
if problemas:
    print(f"{len(problemas)} problema(s):")
    for p in problemas:
        print("  ·", p)
    sys.exit(1)
print("tudo certo: 0 problemas")
