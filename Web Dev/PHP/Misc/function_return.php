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

function addNumbers($number1, $number2) {
    $sum = $number1 + $number2; // Adds 2 function parameters together and store the value in a variable named $sum. 
    return $sum; // Value to be returned to calling function. 
}

// Add 2 numbers together
$arg1 = 4; // Parameter 1.
$arg2 = 5; // Parameter 2.
$sum = addNumbers($arg1, $arg2);

echo "First arg: $arg1<br>"; 
echo "Second arg: $arg2<br>";
echo "Sum: $sum<br><hr>";

echo "Sum before addition: $sum<br>";
echo "First arg: $arg1<br>";

// What it does is the same as $sum = $sum + $arg1.
$sum = addNumbers($sum, $arg1); 
echo "Sum after addition: $sum<br>";


?>

</body>
</html>