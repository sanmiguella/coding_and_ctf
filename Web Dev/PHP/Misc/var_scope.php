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

$x = 0; // Global scope.

function convert() {
    global $x; // To allow changing of a global variable inside a function.
    $x = 1; // Assigning a new value to it.
    echo "Value of global variable inside of function(): $x<br>";
}

echo "Value of global variable outside of function(): $x<br>"; // x = 0
convert();  // x = 1
echo "Value of global variable outside of function(): $x<br>"; // x = 1


?>

</body>
</html>