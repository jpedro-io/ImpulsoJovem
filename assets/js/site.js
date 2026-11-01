/* Movimento Impulso Jovem — comportamento do site.
   Sem biblioteca externa, sem framework. Tudo degrada sem JavaScript. */
(function () {
  "use strict";

  var reduzirMovimento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------- menu */
  function iniciarMenu() {
    var topo = document.querySelector(".topo");
    var botao = document.querySelector(".menu-botao");
    if (!topo || !botao) return;

    function fechar() {
      topo.setAttribute("data-menu", "fechado");
      botao.setAttribute("aria-expanded", "false");
      botao.querySelector(".menu-botao__texto").textContent = "Menu";
    }
    function abrir() {
      topo.setAttribute("data-menu", "aberto");
      botao.setAttribute("aria-expanded", "true");
      botao.querySelector(".menu-botao__texto").textContent = "Fechar";
    }

    botao.addEventListener("click", function () {
      if (topo.getAttribute("data-menu") === "aberto") fechar(); else abrir();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && topo.getAttribute("data-menu") === "aberto") {
        fechar();
        botao.focus();
      }
    });
    document.querySelectorAll(".topo__nav a").forEach(function (link) {
      link.addEventListener("click", fechar);
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 860) fechar();
    });
  }

  /* ------------------------------------------------- aparecer ao rolar */
  function iniciarRevelar() {
    var alvos = document.querySelectorAll("[data-revelar]");
    if (!alvos.length) return;
    if (reduzirMovimento || !("IntersectionObserver" in window)) {
      alvos.forEach(function (el) { el.classList.add("is-visivel"); });
      return;
    }
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (entrada.isIntersecting) {
          entrada.target.classList.add("is-visivel");
          observador.unobserve(entrada.target);
        }
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.05 });
    alvos.forEach(function (el) { observador.observe(el); });
  }

  /* ------------------------------------------------------- copiar pix */
  function iniciarPix() {
    var botoes = document.querySelectorAll("[data-copiar]");
    botoes.forEach(function (botao) {
      var original = botao.innerHTML;
      botao.addEventListener("click", function () {
        var valor = botao.getAttribute("data-copiar");

        function avisar(ok) {
          var rotuloOk = botao.getAttribute("data-copiar-ok") || "Chave copiada";
          var rotuloErro = botao.getAttribute("data-copiar-erro") || "Copie: " + valor;
          botao.textContent = ok ? rotuloOk : rotuloErro;
          botao.setAttribute("aria-live", "polite");
          window.setTimeout(function () { botao.innerHTML = original; }, 3200);
        }

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(valor).then(function () { avisar(true); }, function () { avisar(false); });
          return;
        }
        // caminho antigo, pra navegador sem clipboard
        try {
          var campo = document.createElement("textarea");
          campo.value = valor;
          campo.setAttribute("readonly", "");
          campo.style.position = "fixed";
          campo.style.opacity = "0";
          document.body.appendChild(campo);
          campo.select();
          var ok = document.execCommand("copy");
          document.body.removeChild(campo);
          avisar(ok);
        } catch (erro) {
          avisar(false);
        }
      });
    });
  }

  /* -------------------------------------------------------- formulário */
  function iniciarFormulario() {
    var form = document.querySelector("form[data-formulario]");
    if (!form) return;

    var retorno = form.querySelector(".retorno");
    var botao = form.querySelector("button[type=submit]");
    var girando = false;
    // rodando fora da hospedagem (arquivo local ou servidor de teste): avisa em vez de fingir
    var demonstracao = location.protocol === "file:" ||
      /^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname);

    function campoDe(nome) { return form.elements[nome]; }
    function caixaDe(input) { return input.closest(".campo"); }

    function marcar(input, mensagem) {
      var caixa = caixaDe(input);
      if (!caixa) return;
      caixa.setAttribute("data-erro", "true");
      input.setAttribute("aria-invalid", "true");
      var erro = caixa.querySelector(".erro");
      if (erro) erro.textContent = mensagem;
    }
    function limpar(input) {
      var caixa = caixaDe(input);
      if (!caixa) return;
      caixa.removeAttribute("data-erro");
      input.removeAttribute("aria-invalid");
    }

    function mensagemDe(input) {
      if (input.name === "nome" && (!input.value.trim() || input.value.trim().length < 3)) {
        return "Escreve seu nome, do jeito que a gente te chama.";
      }
      if (input.name === "cidade" && !input.value.trim()) {
        return "Diz de que cidade você é — Divisa Alegre, Águas Vermelhas ou outra.";
      }
      if (input.name === "whatsapp") {
        var digitos = input.value.replace(/\D/g, "");
        if (digitos.length < 10 || digitos.length > 11) {
          return "Digite o número com DDD. Faltam " + Math.max(0, 11 - digitos.length) + " dígito(s).";
        }
      }
      return "";
    }

    function validar() {
      var problemas = [];
      var nome = campoDe("nome");
      var cidade = campoDe("cidade");
      var whats = campoDe("whatsapp");

      [nome, cidade, whats].forEach(limpar);

      if (!nome.value.trim() || nome.value.trim().length < 3) {
        marcar(nome, "Escreve seu nome, do jeito que a gente te chama.");
        problemas.push(nome);
      }
      if (!cidade.value.trim()) {
        marcar(cidade, "Diz de que cidade você é — Divisa Alegre, Águas Vermelhas ou outra.");
        problemas.push(cidade);
      }
      var digitos = whats.value.replace(/\D/g, "");
      if (digitos.length < 10 || digitos.length > 11) {
        marcar(whats, "Digite o número com DDD. Faltam " + Math.max(0, 11 - digitos.length) + " dígito(s).");
        problemas.push(whats);
      }
      return problemas;
    }

    // confere o campo quando a pessoa sai dele, e limpa o erro ao digitar
    function conferir(input) {
      if (!input.value.trim()) return;
      var erro = mensagemDe(input);
      if (erro) marcar(input, erro); else limpar(input);
    }
    ["nome", "cidade", "whatsapp"].forEach(function (nomeCampo) {
      var input = campoDe(nomeCampo);
      if (!input) return;
      input.addEventListener("blur", function () { conferir(input); });
      input.addEventListener("input", function () { limpar(input); });
    });

    form.addEventListener("submit", function (evento) {
      evento.preventDefault();
      if (girando) return; // trava clique duplo

      var problemas = validar();
      if (problemas.length) {
        if (retorno) retorno.removeAttribute("data-estado");
        problemas[0].focus();
        return;
      }

      girando = true;
      botao.disabled = true;
      botao.classList.add("is-carregando");
      botao.setAttribute("aria-busy", "true");
      if (retorno) retorno.removeAttribute("data-estado");

      var dados = new FormData(form);

      fetch(form.getAttribute("action"), {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(dados).toString()
      }).then(function (resposta) {
        if (!resposta.ok) throw new Error("falha");
        form.reset();
        if (retorno) {
          retorno.setAttribute("data-estado", "ok");
          retorno.innerHTML = "<strong>Recebido.</strong> A gente te chama no WhatsApp em até 48 horas. Enquanto isso, o grupo está aberto.";
        }
        retorno.focus();
      }).catch(function () {
        if (retorno) {
          retorno.setAttribute("data-estado", "falha");
          retorno.innerHTML = demonstracao
            ? "<strong>Formulário em demonstração.</strong> Neste endereço de teste não existe servidor pra receber o envio. Na hospedagem, este mesmo botão grava a resposta e avisa o movimento. Enquanto isso, entra no grupo do WhatsApp."
            : "<strong>Não conseguimos enviar agora.</strong> Tenta de novo em um minuto ou entra direto no grupo do WhatsApp.";
        }
        retorno.focus();
      }).finally(function () {
        girando = false;
        botao.disabled = false;
        botao.classList.remove("is-carregando");
        botao.removeAttribute("aria-busy");
      });
    });
  }

  /* ------------------------------------------------------- biblioteca */
  // Os livros já estão no HTML (funciona sem JavaScript). Aqui só escondemos
  // o que não casa com a busca ou com o filtro de assunto.
  function iniciarBiblioteca() {
    var grade = document.querySelector("[data-estante]");
    if (!grade) return;

    var livros = Array.prototype.slice.call(grade.querySelectorAll("[data-livro]"));
    if (!livros.length) return;

    var busca = document.querySelector("[data-busca]");
    var filtros = Array.prototype.slice.call(document.querySelectorAll("[data-filtro]"));
    var contagem = document.querySelector("[data-contagem]");
    var vazio = grade.querySelector("[data-vazio]");
    var assuntoAtual = "Todos";

    function normalizar(texto) {
      return (texto || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    }

    function desenhar() {
      var termo = normalizar(busca ? busca.value.trim() : "");
      var visiveis = 0;

      livros.forEach(function (livro) {
        var casaAssunto = assuntoAtual === "Todos" ||
          livro.getAttribute("data-area") === assuntoAtual;
        // busca pelo nome do livro ou de quem escreveu
        var casaTermo = !termo ||
          normalizar(livro.getAttribute("data-titulo")).indexOf(termo) !== -1 ||
          normalizar(livro.getAttribute("data-autor")).indexOf(termo) !== -1;
        var mostrar = casaAssunto && casaTermo;
        livro.hidden = !mostrar;
        if (mostrar) visiveis++;
      });

      if (vazio) vazio.hidden = visiveis > 0;
      if (contagem) {
        contagem.textContent = visiveis === 1
          ? "1 livro na estante"
          : visiveis + " livros na estante";
      }
    }

    if (busca) {
      busca.addEventListener("input", desenhar);
      busca.addEventListener("search", desenhar);
    }
    filtros.forEach(function (filtro) {
      filtro.addEventListener("click", function () {
        assuntoAtual = filtro.getAttribute("data-filtro");
        filtros.forEach(function (outro) {
          outro.setAttribute("aria-pressed", String(outro === filtro));
        });
        desenhar();
      });
    });

    desenhar();
  }

  /* ------------------------------------------------ topo encolhe ao rolar */
  function iniciarTopo() {
    var topo = document.querySelector(".topo");
    if (!topo) return;
    var ultimo = -1;
    function conferir() {
      var y = window.pageYOffset || document.documentElement.scrollTop;
      var rolado = y > 24;
      if (rolado !== (ultimo === 1)) {
        topo.classList.toggle("is-rolado", rolado);
        ultimo = rolado ? 1 : 0;
      }
    }
    conferir();
    window.addEventListener("scroll", conferir, { passive: true });
  }

  /* -------------------------------------------------------------- ano */
  function iniciarAno() {
    document.querySelectorAll("[data-ano]").forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    iniciarMenu();
    iniciarTopo();
    iniciarRevelar();
    iniciarPix();
    iniciarFormulario();
    iniciarBiblioteca();
    iniciarAno();
  });
})();
