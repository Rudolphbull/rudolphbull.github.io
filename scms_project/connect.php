<?php

    if(!empty($_POST['submit'])){

        $votersFirstName = $_POST['votersFirstName'];
        $votersLastName = $_POST['votersLastName'];
        $votersEmail = $_POST['votersEmail'];
        $phone = $_POST['phone'];
        $myPresident = $_POST['myPresident'];
        $myVicePresident = $_POST['myVicePresident'];
        $mySecretary = $_POST['mySecretary'];
        $myWelfare = $_POST['myWelfare'];
        $myDeputyWelfare = $_POST['myDeputyWelfare'];
        $myTreasurer = $_POST['myTreasurer'];
        $myFinancialSecretary = $_POST['myFinancialSecretary'];
        $myDeputyFinancialSecretary = $_POST['myDeputyFinancialSecretary'];
        $mySocialSecretary = $_POST['mySocialSecretary'];
        $toEmail = ['rudolphbull@gmail.com'];


        $mailHeaders = "votersFirstName: " . $votersFirstName . 
        "\r\n votersEmail: " . $votersEmail .
        "\r\n phone: " . $phone .
        "\r\n myPresident: " . $myPresident .
        "\r\n myVicePresident: " . $myVicePresident .
        "\r\n mySecretary: " . $mySecretary .
        "\r\n myWelfare: " . $myWelfare .
        "\r\n myDeputyWelfare: " . $myDeputyWelfare .
        "\r\n myTreasurer: " . $myTreasurer .
        "\r\n myFinancialSecretary: " . $myFinancialSecretary  .
        "\r\n myDeputyFinancialSecretary: " . $myDeputyFinancialSecretary .
        "\r\n mySocialSecretary: " .  $mySocialSecretary . "\r\n";
        
        
        if (mail('$toEmail', '$votersFirstName', '$mailHeaders')) {
            $message = "Your Information is received Successfully. ";

        }
        


    }




?>