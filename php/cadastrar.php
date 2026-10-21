<?php

include "conexao.php";

$nome = $_POST["nome"];
$especie = $_POST["especie"];
$raca = $_POST["raca"];
$idade = $_POST["idade"];
$sexo = $_POST["sexo"];
$cor = $_POST["cor"];
$peso = $_POST["peso"];
$tutor = $_POST["tutor"];
$telefone = $_POST["telefone"];
$observacoes = $_POST["observacoes"];


$sql = "INSERT INTO animais
(nome, especie, raca, idade, sexo, cor, peso, tutor, telefone, observacoes)

VALUES
('$nome', '$especie', '$raca', '$idade', '$sexo', '$cor', '$peso', '$tutor', '$telefone', '$observacoes')";


mysqli_query($conn, $sql);


header("Location: ../lista.php");

?>