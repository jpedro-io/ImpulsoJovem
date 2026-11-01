# Site do Impulso Jovem — como usar

O site está pronto em `/home/user/site/`. É HTML, CSS e JavaScript puros: não precisa de
instalação, build, banco de dados nem CMS. Pra editar texto, você edita o `.html`. Pra publicar,
sobe a pasta.

**Hoje são 63 páginas:** 10 páginas fixas + 54 verbetes da Escola Impulso + a Biblioteca com
143 livros da pasta do Drive. O site inteiro pesa 6,5 MB.

---

## 1. O que tem dentro

```
site/
├── index.html                      Home
├── o-impulso.html                  O Impulso (quem somos, princípios, núcleos)
├── bandeiras.html                  As 6 bandeiras (âncoras #educacao, #trabalho…)
├── formacao.html                   Escola Impulso — índice das 7 trilhas / 54 verbetes
├── verbete-*.html                  54 verbetes (um por assunto das trilhas)
├── biblioteca.html                 143 livros com busca, capa e link direto
├── participe.html                  Formulário + portas de entrada
├── apoie.html                      Pix (copiar chave), materiais, apoio sem dinheiro
├── codigo-de-conduta.html          Conduta + o que a lei diz
├── 404.html                        Página de erro
│
├── _headers                        Cabeçalhos de segurança (Netlify / Cloudflare Pages)
├── robots.txt  sitemap.xml         62 páginas no mapa (troque o domínio antes de publicar)
├── favicon.ico / .svg / 16·32·64·192·512.png / apple-touch-icon.png
├── site.webmanifest                Ícone na tela do celular
│
├── assets/css/estilo.css           Sistema visual: cores, tipografia, componentes, animações
├── assets/js/site.js               Menu, copiar Pix/link, busca, formulário, revelar ao rolar
├── assets/fontes/                  Anton (títulos), Instrument Serif (itálico), Archivo (interface),
│                                   Source Serif 4 (texto) — todas self-hosted
├── assets/img/                     7 fotos em P&B + 3 logos
├── assets/capas/                   143 capas dos livros
│
├── _gerar.py                       gera as 10 páginas fixas (cabeçalho/menu/rodapé iguais)
├── verbete_dados.py                TEXTO dos 54 verbetes — é aqui que se edita verbete
├── verbete_amplia.py               parágrafos extras de cada verbete (o “mais explicação”)
├── _verbetes.py                    gera os 54 verbetes + formacao.html
├── _biblioteca.py                  gera biblioteca.html a partir da pasta do Drive
└── _validar.py                     confere links, âncoras, ids e arquivos de todas as páginas
```

Os cinco arquivos `.py` **não precisam ir pra hospedagem** — o site funciona sem eles. Eles
existem pra não ter que repetir menu, rodapé e ficha à mão 143 vezes.

## 2. Publicar (R$ 0)

**Netlify:** app.netlify.com → *Add new site* → *Deploy manually* → arraste a pasta `site`.

**Cloudflare Pages:** dash.cloudflare.com → *Workers & Pages* → *Create* → *Pages* → *Upload
assets* → arraste a pasta `site`.

Os dois leem o `_headers` sozinhos. Se for outra hospedagem, copie os 7 cabeçalhos no painel.
Se quiser, apague os `.py` da pasta antes de subir — o site não depende deles.

## 3. O formulário do Participe — o único ponto que falta ligar

Hoje o envio cai em "não conseguimos enviar" (e, rodando local, avisa "formulário em
demonstração"). Escolha uma das duas:

**Netlify Forms** (de graça, 100 envios/mês, só funciona no Netlify)
1. Publique no Netlify. O formulário já está marcado com `data-netlify="true"` e tem o campo
   armadilha `bot-field` (spam).
2. No painel do site: *Forms* → o formulário "participe" aparece sozinho.
3. Em *Forms → Settings → Form notifications*, coloque o e-mail ou o webhook do WhatsApp.

**Formspree / Tally** (funciona em qualquer hospedagem)
1. Crie a conta, pegue o endpoint (ex.: `https://formspree.io/f/xxxxxxx`).
2. Em `participe.html`, troque `action="/"` por esse endereço. Só isso.

## 4. Os verbetes (54)

O texto de cada verbete fica em **`verbete_dados.py`**, e é a única coisa que você precisa editar
pra mudar conteúdo. Cada bloco tem:

```python
dict(tr="1", n=3, slug="mais-valia", t="Mais-valia: de onde vem o lucro", min=7,
  datas=[("1867", "…"), ("1885", "…"), ("Hoje", "…")],
  txt=["parágrafo 1", "parágrafo 2", …],
  c="Conceito-chave em uma frase.",
  f=["Fonte 1", "Fonte 2"],
  leia=[("Título do outro verbete", "slug-do-outro")])
```

Depois de editar, rode na pasta `site/`:

```bash
python3 _verbetes.py
```

Ele reescreve os 54 `verbete-*.html` e a `formacao.html` — inclusive os links entre eles. Se
preferir editar o HTML na mão, pode: cada verbete é uma página completa e independente.
Pra **criar um verbete novo**: copie um bloco inteiro em `verbete_dados.py`, mude o `slug`, o
conteúdo e o `n`, e rode o script. O link na trilha aparece sozinho.

**Quer um verbete maior sem mexer no texto principal?** Os parágrafos extras ficam em
`verbete_amplia.py`, num dicionário com o slug como chave: cada item da lista vira um parágrafo
novo, acrescentado depois dos originais. É o jeito mais rápido de engordar um verbete.

### As sete trilhas

| # | Trilha | Verbetes |
|---|---|---|
| 1 | Ideias: de onde vêm as palavras que a gente usa | 7 |
| 2 | Nossa história: o Brasil que produziu a gente | 9 |
| 2B | Minas Gerais: o estado que produziu a nossa região | 4 |
| 3 | **Ditadura militar: 21 anos, ato por ato** | 7 |
| 4 | O mundo: o que aconteceu fora que mexeu aqui | 10 |
| 5 | Quem já lutou: movimentos sociais | 9 |
| 6 | Como o poder funciona (e como a gente usa) | 8 |

A trilha 3 é a mais nova e é cronológica dentro do regime: o que era um Ato Institucional, AI-1,
AI-2, AI-3, AI-4, AI-5 e o que veio depois (AI-6 ao AI-12, junta militar, revogação do AI-5 em
1978 e Lei de Anistia). O verbete antigo "Ditadura militar: 21 anos" continua na trilha 2, como
visão geral — a trilha 3 entra no detalhe, documento por documento.

## 5. A Biblioteca (143 livros)

Cada livro virou uma ficha com **capa, autor, ano, licença, peso do arquivo, resumo e o botão que
abre o PDF daquele livro** (não a pasta: o arquivo).

- **Capa:** é a primeira página do próprio PDF, puxada do Drive — é a capa real da edição que
  está na pasta, não uma imagem de banco.
- **Link:** `drive.google.com/file/d/<ID>/view`, um por livro. O botão vermelho **Abrir no Drive**
  abre em aba nova; a capa e o título também são clicáveis; e o botão **Copiar link** serve pra
  quando alguém quiser mandar o livro no WhatsApp em vez de abrir.
- **Busca:** por título **ou** autor. Os filtros são por assunto (Teoria, História, Brasil, Mundo,
  Economia, Raça e gênero, Educação, Trabalho, Literatura, Relatórios).
- **Seis arquivos repetidos** na pasta foram consolidados em uma ficha só.
- Pra **adicionar um livro**: copie um `<article class="livro" …>` em `biblioteca.html` e troque
  `data-titulo` (sem acento, minúsculo), `data-autor`, `data-area`, a capa, o texto e o link. Se
  quiser regerar tudo da pasta do Drive, rode `python3 _biblioteca.py` (depende das fichas em
  `../.tmp/catalogo.py`, que é onde ficam os dados de cada livro).

## 6. O que trocar antes de publicar

| O quê | Onde |
|---|---|
| Domínio no `sitemap.xml` | `https://impulsojovem.example` → seu domínio |
| Fotos | troque o arquivo em `assets/img/` mantendo o nome, ou edite o `src` |
| Textos das páginas fixas | direto no `.html` (ou em `_gerar.py`, se for mudar em todas) |
| Verbete | `verbete_dados.py` e rode `_verbetes.py` |
| Livro | `biblioteca.html` ou `../.tmp/catalogo.py` + `_biblioteca.py` |

Os links do movimento já estão no site inteiro: grupo do WhatsApp
(`chat.whatsapp.com/G4XrxaoL39H0QVfYUz4bkx`), Instagram (`instagram.com/impulsojovem.33`) e a
pasta do Drive. Se mudar algum, use *Localizar e substituir* em todos os arquivos.

## 7. Regras que o site já respeita

- **Nenhuma requisição externa.** Fontes, ícones, fotos e capas são do próprio site. Nada de
  Google Fonts, nada de CDN, nada de analytics. Nenhum cookie é gravado.
- **Sem login, sem banco.** Não tem senha pra vazar.
- **Funciona sem JavaScript.** A Biblioteca lista os 143 livros no HTML; a busca só esconde cartões.
- **Acessível:** pular para o conteúdo, foco visível, `aria-*` no menu e no formulário, contraste
  conferido, respeita "reduzir animações".
- **CSP fechada:** nenhum `style=` solto no HTML, nenhum `onclick=`. Se for editar e colocar
  estilo inline, o navegador vai bloquear — é de propósito.
- **Uma ressalva honesta:** a estante inclui edições que ainda têm direitos autorais, porque é o
  retrato da pasta do movimento. Onde o livro é comercial, o PDF é cópia de estudo — a página diz
  isso e sugere comprar a edição. Se em algum momento o movimento quiser só domínio público na
  estante, é filtrar por licença e regerar.

## 8. Conferir o site antes de publicar

```bash
cd site
python3 _validar.py
```

Ele varre as 63 páginas e avisa se algum link interno aponta pra página que não existe, se uma
âncora (`#educacao`) sumiu, se há `id` repetido, se alguma classe usada no HTML não existe no CSS
e se algum arquivo citado (fonte, foto, capa) está faltando. Hoje passa com **0 problemas**.

## 9. As animações (e como desligar)

O site tem quatro animações, todas em CSS e JavaScript puro:

1. **Faixa vermelha rolante** logo abaixo do topo (marquee com as palavras do movimento).
2. **Revelar ao rolar** — blocos de foto, cards e listas aparecem subindo quando entram na tela.
3. **Topo que encolhe** ao rolar a página, com sombra leve.
4. **Hover nos cartões** — elevação, borda vermelha, seta que anda.

Nada disso é obrigatório pra ler o site: quem tem "reduzir movimento" ligado no sistema recebe
tudo parado, e o conteúdo aparece mesmo sem JavaScript. A faixa rolante é decorativa e fica
escondida do leitor de tela (`aria-hidden`).
