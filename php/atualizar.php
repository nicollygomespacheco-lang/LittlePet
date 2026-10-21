<?php

include "conexao.php";


$id = $_POST["id"];

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


$sql = "UPDATE animais SET

nome = '$nome',

especie = '$especie',

raca = '$raca',

idade = '$idade',

sexo = '$sexo',

cor = '$cor',

peso = '$peso',

tutor = '$tutor',

telefone = '$telefone',

observacoes = '$observacoes'

WHERE id = $id";


mysqli_query($conn, $sql);


header("Location: ../lista.php");

?>