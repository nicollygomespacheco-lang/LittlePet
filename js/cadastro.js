const formulario = document.getElementById("formulario");

if (formulario) {

    formulario.addEventListener("submit", async function(event) {

        event.preventDefault();

        const nome = document.getElementById("nome").value.trim();
        const especie = document.getElementById("especie").value.trim();
        const idade = Number(document.getElementById("idade").value);
        const descricao = document.getElementById("descricao").value.trim();

        if (
            nome === "" ||
            especie === "" ||
            isNaN(idade) ||
            idade < 0
        ) {

            alert("Preencha corretamente os campos obrigatórios.");

            return;
        }

        const dados = {
            nome: nome,
            especie: especie,
            idade: idade,
            descricao: descricao
        };


        try {

            const resposta = await fetch(
                "http://localhost:5000/animais",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(dados)
                }
            );


            const resultado = await resposta.json();


            if (!resposta.ok) {

                throw new Error(
                    resultado.erro ||
                    "Não foi possível cadastrar o animal."
                );
            }


            alert("Animal cadastrado com sucesso!");

            formulario.reset();

            window.location.href = "animais.html";


        } catch (erro) {

            console.error(erro);

            alert(
                erro.message ||
                "Erro ao cadastrar o animal."
            );
        }

    });

}