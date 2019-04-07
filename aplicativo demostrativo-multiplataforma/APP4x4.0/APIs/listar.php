<?php
header("Access-Control-Allow-Origin: *");
header('Content-Type: text/html; charset=utf-8');
 //host=localhost ou  enderço servidor

$dns = "mysql:host=localhost;dbname=Guias";
$user = "root";
$pass = "";
try {
	$con = new PDO($dns, $user, $pass);
	if(!$con){
		echo "Não foi possivel conectar com Banco de Dados!";
	}		
	$query = $con->prepare('SELECT * FROM guias');
		$query->execute();
		$out = "[";
		while($result = $query->fetch()){
			if ($out != "[") {
				$out .= ",";
			}
			$out .= '{"nome": "'.$result["nome"].'",';
			$out .= '"celular": "'.$result["celular"].'",';
			$out .= '"localizacao": "'.$result["localizacao"].'"}';
		}
		$out .= "]";
		echo $out;
} catch (Exception $e) {
	echo "Erro: ". $e->getMessage();
};