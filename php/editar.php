<?php

include "php/conexao.php";


if (isset($_GET["id"])) {

    $id = $_GET["id"];

    $sql = "SELECT * FROM animais WHERE id = $id";

    $resultado = mysqli_query($conn, $sql);

    $animal = mysqli_fetch_assoc($resultado);

}

?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
    content="width=device-width, initial-scale=1.0">
    <title>LittlePet - Editar</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

<header>
    <h1>LittlePet</h1>

    <nav>
        <a href="index.html">Início</a>
        <a href="sobre.html">Sobre</a>
        <a href="cadastro.html">Cadastrar</a>
        <a href="lista.php">Animais</a>
        <a href="editar.php">Editar</a>
    </nav>

</header>

<main>

    <section class="conteudo">

        <h2>Editar Animal</h2>


        <?php if (isset($animal)) { ?>


        <form action="php/atualizar.php" method="POST">


            <input
                type="hidden"
                name="id"
                value="<?php echo $animal["id"]; ?>"
            >


            <label>Nome do animal:</label>

            <input
                type="text"
                name="nome"
                value="<?php echo $animal["nome"]; ?>"
            >


            <label>Espécie:</label>

            <select name="especie">

                <option value="Cachorro"
                    <?php
                    if ($animal["especie"] == "Cachorro")
                        echo "selected";
                    ?>
                >
                    Cachorro
                </option>


                <option value="Gato"
                    <?php
                    if ($animal["especie"] == "Gato")
                        echo "selected";
                    ?>
                >
                    Gato
                </option>


                <option value="Ave"
                    <?php
                    if ($animal["especie"] == "Ave")
                        echo "selected";
                    ?>
                >
                    Ave
                </option>


                <option value="Outro"
                    <?php
                    if ($animal["especie"] == "Outro")
                        echo "selected";
                    ?>
                >
                    Outro
                </option>

            </select>


            <label>Raça:</label>

            <input
                type="text"
                name="raca"
                value="<?php echo $animal["raca"]; ?>"
            >


            <label>Idade:</label>

            <input
                type="number"
                name="idade"
                value="<?php echo $animal["idade"]; ?>"
            >


            <label>Sexo:</label>

            <select name="sexo">

                <option value="Macho"
                    <?php
                    if ($animal["sexo"] == "Macho")
                        echo "selected";
                    ?>
                >
                    Macho
                </option>


                <option value="Fêmea"
                    <?php
                    if ($animal["sexo"] == "Fêmea")
                        echo "selected";
                    ?>
                >
                    Fêmea
                </option>

            </select>


            <label>Cor:</label>

            <input
                type="text"
                name="cor"
                value="<?php echo $animal["cor"]; ?>"
            >


            <label>Peso (kg):</label>

            <input
                type="number"
                name="peso"
                step="0.1"
                value="<?php echo $animal["peso"]; ?>"
            >


            <label>Nome do tutor:</label>

            <input
                type="text"
                name="tutor"
                value="<?php echo $animal["tutor"]; ?>"
            >


            <label>Telefone:</label>

            <input
                type="text"
                name="telefone"
                value="<?php echo $animal["telefone"]; ?>"
            >


            <label>Observações:</label>

            <textarea
                name="observacoes"
                rows="4"
            ><?php echo $animal["observacoes"]; ?></textarea>


            <button type="submit">
                Salvar Alterações
            </button>

        </form>


        <?php } else { ?>


            <p>Para editar um animal, primeiro escolha um registro na lista.</p>

            <br>

            <a href="lista.php" class="botao">
                Ver Animais
            </a>

        <?php } ?>

    </section>

</main>

<footer>
    <p>LittlePet - Sistema de Cadastro de Animais</p>
</footer>
</body>
</html>