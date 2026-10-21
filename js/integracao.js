const API_URL = "http://localhost:5000/animais";

const formulario = document.getElementById("formAnimal");
const lista = document.getElementById("listaAnimais");
const mensagem = document.getElementById("mensagem");
const botaoAtualizar = document.getElementById("botaoAtualizar");

// GET: busca os animais cadastrados no banco
async function listarAnimais() {
    try {
        const resposta = await fetch(API_URL);

        if (!resposta.ok) {
            throw new Error("Não foi possível buscar os animais.");
        }

        const animais = await resposta.json();

        lista.replaceChildren();

        if (animais.length === 0) {
            const item = document.createElement("li");
            item.textContent = "Nenhum animal cadastrado ainda.";
            lista.appendChild(item);
        } else {
            animais.forEach((animal) => {
                const item = document.createElement("li");

                item.textContent =
                    `${animal.nome} - ${animal.especie} - ` +
                    `${animal.idade} ano(s) - ${animal.descricao || "Sem descrição"}`;

                lista.appendChild(item);
            });
        }

        mensagem.textContent = "";

    } catch (erro) {
        console.error(erro);
        mensagem.textContent =
            "Erro ao carregar os animais. Verifique se a API está funcionando.";
    }
}

// POST: envia o cadastro para a API
formulario.addEventListener("submit", async (evento) => {
    evento.preventDefault();

    const dados = {
        nome: document.getElementById("nome").value.trim(),
        especie: document.getElementById("especie").value,
        idade: Number(document.getElementById("idade").value),
        descricao: document.getElementById("descricao").value.trim()
    };

    try {
        mensagem.textContent = "Cadastrando animal...";

        const resposta = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        const resultado = await resposta.json();

        if (!resposta.ok) {
            throw new Error(resultado.erro || "Erro ao cadastrar animal.");
        }

        formulario.reset();
        mensagem.textContent = "Animal cadastrado com sucesso!";

        // Atualiza a lista sem recarregar a página
        await listarAnimais();

    } catch (erro) {
        console.error(erro);
        mensagem.textContent = erro.message ||
            "Não foi possível cadastrar o animal.";
    }
});

// Permite atualizar a lista pelo botão
botaoAtualizar.addEventListener("click", listarAnimais);

// Carrega os animais quando a página abre
listarAnimais();