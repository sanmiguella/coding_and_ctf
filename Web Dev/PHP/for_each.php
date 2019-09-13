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

// Assigning of values to an array.
$my_array = array("test", "best", "jest", "rest", "nest", "zest"); 

echo "Before foreach loop<br><br>";

// Loops through every element in the array.
foreach($my_array as $element){
    echo "Array value : $element<br>";
}

echo "<br>After foreach loop<br>";

?>

</body>
</html>