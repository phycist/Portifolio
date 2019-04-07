<?php

header("Access-Control-Allow-Origin:http://localhost:8100");
header("Content-Type: application/x-www-form-urlencoded");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
    //RECUPERAÇÃO DO FORMULÁRIO
    $data = file_get_contents("php://input");
    $objData = json_decode($data);
    // TRANSFORMA OS DADOS
    $id = $objData->id;
    $nome = $objData->nome;
    $celular = $objData->celular;
    $localizacao = $objData->localizacao;
    // LIMPA OS DADOS
    $id= stripslashes($id);
    $nome = stripslashes($nome);
    $celular = stripslashes($celular);
    $localizacao = stripslashes($localizacao);
    $id = trim($id);
    $nome = trim($nome);
    $celular = trim($celular);
    $localizacao = trim($localizacao);
    $dados; // RECEBE ARRAY PARA RETORNO
    // INSERE OS DADOS
                                //host=localhost ou  enderço servidor
    @$db = new PDO("mysql:host=localhost;dbname=bdcurso", "dudu", "");
   //VERIFICA SE TEM CONEXÃO
    if($db){
        $sql = " insert into Guia values(".$nome."','".$celular."','".$localizacao."')";
        $query = $db->prepare($sql);
        $query ->execute();
        if(!$query){
                   $dados = array('mensage' => "Não foi possivel enviar os dados ");
                   echo json_encode($dados);
         }
        else{
                   $dados = array('mensage' => "Os dados foram inseridos com sucesso. Obrigado e bem vindo ");
                  echo json_encode($dados);
         };
    }
   else{
          $dados = array('mensage' => "Não foi possivel conectar ao banco.");
          echo json_encode($dados);
    };