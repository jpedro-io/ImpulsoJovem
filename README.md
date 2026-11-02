# Movimento Impulso Jovem — site oficial

Site do **Movimento Impulso Jovem**, movimento de juventude de esquerda de **Divisa Alegre (MG)** e
**Águas Vermelhas (MG)**. Nasceu em outubro de 2026, da união de jovens estudantes e trabalhadores
das duas cidades.

O site reúne o que o movimento defende, como participar, a prestação de contas do caixa e duas
ferramentas de formação gratuitas: a **Escola Impulso**, com 54 verbetes, e a **Biblioteca Livre**,
com 143 livros em PDF.

> Anticapitalista · Antiracista · Contra a LGBTfobia e a misoginia · Ambientalista · Antifascista

## O que tem no site

| Seção | O que é |
|---|---|
| **O Impulso** | Quem somos, princípios, como nos organizamos, núcleos e linha do tempo |
| **Bandeiras** | As 6 bandeiras do movimento — educação, trabalho, vida, clima, cidade e organização |
| **Formação** | Escola Impulso: **54 verbetes** em **7 trilhas**, com datas, conceito-chave e fontes |
| **Biblioteca** | **143 livros** com busca por título ou autor, filtro por assunto, capa, resumo e link do PDF |
| **Contato** | Formulário "fale com a gente" — a resposta chega no e-mail do movimento |
| **Apoie** | Pix do caixa único, materiais do movimento e outras formas de ajudar |
| **Código de conduta** | Regras de convivência e o que a lei diz sobre assédio e discriminação |

### As 7 trilhas da Escola Impulso

1. **Ideias** — de onde vêm as palavras que a gente usa (7 verbetes)
2. **Nossa história** — o Brasil que produziu a gente (9)
3. **Minas Gerais** — o estado que produziu a nossa região (4)
4. **Ditadura militar** — 21 anos, ato por ato: AI-1 ao AI-5, junta militar, anistia (7)
5. **O mundo** — o que aconteceu fora que mexeu aqui (10)
6. **Quem já lutou** — movimentos sociais (9)
7. **Como o poder funciona** — e como a gente usa (8)

## Stack

HTML, CSS e JavaScript puros. **Sem framework, sem build, sem banco de dados, sem CMS.**
A pasta publicada é o site — qualquer hospedagem estática serve.

- **Tipografia:** Anton (títulos), Instrument Serif (itálico de destaque), Archivo (interface) e
  Source Serif 4 (texto), todas self-hosted em `assets/fontes/`.
- **Zero requisição externa** em imagens, fontes e scripts. Nada de CDN, Google Fonts ou analytics.
- **Sem cookies.** O único envio que sai do site é o formulário de participação, que vai por e-mail
  (ver abaixo).
- **Funciona sem JavaScript:** menu, busca e links continuam utilizáveis.

## Estrutura

```
.
├── index.html                 Home
├── o-impulso.html             Quem somos
├── bandeiras.html             As 6 bandeiras
├── formacao.html              Índice das 7 trilhas
├── verbete-*.html             54 verbetes (páginas independentes)
├── biblioteca.html            Estante com 143 livros
├── participe.html             Formulário (envia por e-mail)
├── apoie.html                 Pix e materiais
├── codigo-de-conduta.html     Código de conduta
├── 404.html                   Página de erro
├── assets/
│   ├── css/estilo.css         Sistema visual completo (cores, tipografia, componentes)
│   ├── js/site.js             Menu, revelar ao rolar, busca, cópia de Pix/link, formulário
│   ├── fontes/                4 famílias self-hosted
│   ├── img/                   Fotos do movimento e logos
│   └── capas/                 Capas dos 143 livros
├── _headers                   Cabeçalhos de segurança (Netlify / Cloudflare Pages)
├── vercel.json                Os mesmos cabeçalhos + cache (Vercel)
├── sitemap.xml · robots.txt
└── _fontes/                   Scripts Python que geram as páginas (não precisam ser publicados)
```

## Formulário → e-mail

Não existe servidor nem banco de dados. O formulário de `participe.html` envia as respostas por
e-mail usando o **FormSubmit** (`formsubmit.co`), sem cadastro e sem chave de API:

- o destino é definido em `_fontes/_gerar.py`, nas constantes `EMAIL_FORM_1` (principal),
  `EMAIL_FORM_2` e `EMAIL_FORM_3` (cópias, opcionais — basta preencher);
- o envio funciona com e sem JavaScript: com JS a resposta aparece na própria página, sem JS o
  FormSubmit mostra a tela de confirmação dele;
- a CSP em `_headers` e `vercel.json` libera **apenas** `https://formsubmit.co`;
- o primeiro envio dispara um e-mail de **ativação** do FormSubmit para cada endereço de destino.
  Enquanto o link não for clicado, nenhuma resposta é entregue.

**Entrada no grupo:** o link do grupo de WhatsApp **não é público**. Quem quer entrar chama no direct
do Instagram (`ig.me/m/impulsojovem.33`) e os admins do perfil passam o link. Os botões "Chamar no
direct" no site (O Impulso, Bandeiras, Biblioteca, Apoie e Contato) apontam para lá.

## Deploy

Estático: não há comando de build nem diretório de saída.

- **Vercel:** importar o repositório em `vercel.com/new` com framework *Other*. O `vercel.json` leva
  os cabeçalhos de segurança e as regras de cache.
- **Netlify / Cloudflare Pages:** conectar o repositório ou arrastar a pasta. O `_headers` faz o
  mesmo papel.
- Ao usar domínio próprio, atualizar a URL em `sitemap.xml` e `robots.txt`.

Se o projeto estiver na Vercel com *Deployment Protection* ligada, o endereço `.vercel.app` pede
login. Para o site ser público: **Settings → Deployment Protection → Vercel Authentication →
Disabled** (ou usar domínio próprio).

## Conteúdo e edição

- **Verbetes:** texto em `_fontes/verbete_dados.py` (e complementos em `verbete_amplia.py`); rodar
  `python3 _verbetes.py` para regerar as 54 páginas e o índice das trilhas.
- **Páginas fixas:** texto direto no `.html`, ou em `_fontes/_gerar.py` quando a mudança vale para
  todas.
- **Biblioteca:** cada livro é um `<article class="livro">` com `data-titulo`, `data-autor`,
  `data-area` e o link do Drive; `_biblioteca.py` regera a estante a partir da pasta do movimento.
- **Antes de publicar:** `python3 _validar.py` confere links internos, âncoras, `id` repetido,
  classes sem CSS e arquivos ausentes.

## Créditos e licença

Textos, fotos, marca e identidade visual são do Movimento Impulso Jovem. As capas da Biblioteca são
a primeira página dos próprios PDFs (ou arte do movimento, quando o arquivo não tem capa). Os livros
seguem a licença de cada obra — domínio público, licença aberta ou material do próprio movimento.
