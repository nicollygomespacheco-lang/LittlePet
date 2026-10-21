<?php

include "php/conexao.php";

$sql = "SELECT * FROM animais";

$resultado = mysqli_query($conn, $sql);

?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
    content="width=device-width, initial-scale=1.0">
    <title>LittlePet - Animais</title>
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

        <h2>Animais Cadastrados</h2>
        <p>Confira abaixo os animais cadastrados no LittlePet.</p>

        <div class="tabela">

            <table>

                <tr>

                    <th>ID</th>

                    <th>Nome</th>

                    <th>Espécie</th>

                    <th>Raça</th>

                    <th>Idade</th>

                    <th>Sexo</th>

                    <th>Cor</th>

                    <th>Peso</th>

                    <th>Tutor</th>

                    <th>Telefone</th>

                    <th>Observações</th>

                    <th>Ações</th>

                </tr>

                <?php

                while ($animal = mysqli_fetch_assoc($resultado)) {

                ?>

                <tr>

                    <td>
                        <?php echo $animal["id"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["nome"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["especie"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["raca"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["idade"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["sexo"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["cor"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["peso"]; ?> kg
                    </td>

                    <td>
                        <?php echo $animal["tutor"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["telefone"]; ?>
                    </td>

                    <td>
                        <?php echo $animal["observacoes"]; ?>
                    </td>

                    <td>

                        <a
                            class="editar"
                            href="editar.php?id=<?php echo $animal["id"]; ?>"
                        >
                            Editar
                        </a>


                        <a
                            class="excluir"
                            href="php/excluir.php?id=<?php echo $animal["id"]; ?>"
                            onclick="return confirm('Deseja excluir este animal?');"
                        >
                            Excluir
                        </a>

                    </td>

                </tr>

                <?php

                }

                ?>

            </table>

        </div>

    </section>

</main>

<footer>
    <p>LittlePet - Sistema de Cadastro de Animais</p>
</footer>
</body>
</html>