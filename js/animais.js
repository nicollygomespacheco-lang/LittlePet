const API_URL = "http://localhost:5000/animais";

const tabela = document.getElementById("tabelaAnimais");
const mensagem = document.getElementById("mensagem");


async function listarAnimais() {

    try {

        const resposta = await fetch(API_URL);

        if (!resposta.ok) {
            throw new Error("Erro ao buscar animais.");
        }

        const animais = await resposta.json();

        console.log("Animais recebidos:", animais);

        tabela.innerHTML = "";

        animais.forEach(function(animal) {

            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td>${animal.id}</td>
                <td>${animal.nome}</td>
                <td>${animal.especie}</td>
                <td>${animal.idade}</td>
                <td>${animal.descricao || "Sem descrição"}</td>
                <td>
                    <button onclick="excluirAnimal(${animal.id})">
                        Excluir
                    </button>
                </td>
            `;

            tabela.appendChild(linha);
        });

    } catch (erro) {

        console.error(erro);

        mensagem.textContent =
            "Erro ao carregar os animais.";
    }
}


async function excluirAnimal(id) {

    const confirmar = confirm(
        "Deseja realmente excluir este animal?"
    );

    if (!confirmar) {
        return;
    }

    try {

        const resposta = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        const resultado = await resposta.json();

        if (!resposta.ok) {
            throw new Error(
                resultado.erro || "Erro ao excluir o animal."
            );
        }

        mensagem.textContent =
            "Animal excluído com sucesso.";

        listarAnimais();

    } catch (erro) {

        console.error(erro);

        mensagem.textContent =
            erro.message;
    }
}


listarAnimais();