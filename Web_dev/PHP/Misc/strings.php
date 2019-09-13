<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Document</title>
    <link rel='stylesheet' href='mycss.css' type='text/css'>
    <link href="https://fonts.googleapis.com/css?family=Lexend+Deca&display=swap" rel="stylesheet">

</head>
<body>


<?php

$myName = "My name is harry!"; // Declare and initialize. 

echo "String : <b>$myName</b><br>";

echo "<hr>Number of chars : <b>" . strlen($myName) . "</b><br>"; // Str function() to count the number of chars in a string. 

$myName = strtoupper($myName); // Str function() to convert the string to uppercase. 
echo "<hr>String(uppercase) : <b>" . $myName . "</b><br>"; 

$myName = strtolower($myName); // Str function() to convert the string to lowercase. 
echo "<hr>String(lowercase) : <b>" . $myName . "</b><br>";

?>

</body>
</html>