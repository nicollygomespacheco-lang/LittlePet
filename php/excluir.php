<?php

include "conexao.php";


$id = $_GET["id"];


$sql = "DELETE FROM animais WHERE id = $id";


mysqli_query($conn, $sql);


header("Location: ../lista.php");

?>