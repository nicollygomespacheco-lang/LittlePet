const formulario = document.querySelector("#formulario");

if (formulario) {

    formulario.addEventListener("submit", function(event) {

        let nome = document.querySelector("#nome").value;
        let especie = document.querySelector("#especie").value;
        let raca = document.querySelector("#raca").value;
        let idade = document.querySelector("#idade").value;
        let sexo = document.querySelector("#sexo").value;
        let cor = document.querySelector("#cor").value;
        let peso = document.querySelector("#peso").value;
        let tutor = document.querySelector("#tutor").value;
        let telefone = document.querySelector("#telefone").value;

        if (
            nome == "" ||
            especie == "" ||
            raca == "" ||
            idade == "" ||
            sexo == "" ||
            cor == "" ||
            peso == "" ||
            tutor == "" ||
            telefone == ""
        ) {

            event.preventDefault();

            alert("Preencha todos os campos obrigatórios!");

        }

    });

}