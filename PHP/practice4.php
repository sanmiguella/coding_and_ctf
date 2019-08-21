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

function calculate() {
    // Declare and initialize variables.
    $val_1 = 2; 
    $val_2 = 3; 

    echo "val_1 : $val_1<br>";
    echo "val_2 : $val_2<br>";

    // Returns the sum of 2 numbers to the calling function(). 
    return $val_1 + $val_2;
}

// Displays results, result of calculate() function will be concatenated together with other strings.
echo "Sum : " .  calculate() . "<br><hr>";

// Declare and initialize variables which will be passed to a function(). 
$num1 = 10; 
$num2 = 15; 

// Function accepts 2 parameters/arguments.
function calculate_params($param_1, $param_2) {
    echo "Param 1 : $param_1<br>";
    echo "Param 2 : $param_2<br>"; 

    // Displays results, strval converts the integers values into a string.
    echo "Sum : " . strval($param_1 + $param_2) . "<br>";
}

// Calls functions and passes 2 parameters/arguments to it.
calculate_params($num1, $num2);

?>

</body>
</html>