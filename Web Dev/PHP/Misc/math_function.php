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

$num = rand(1, 6); // Value between 1 to 6. 
$pow = rand(1, 3); // Power between 1 to 3.

function calculate_power($num, $pow) {
    echo "Value : $num<br>"; 
    echo "Power : $pow<br>"; 
    echo "Result : " . pow($num, $pow) . "<br>"; // Display results.
}

calculate_power($num, $pow); // Calls function() and pass 2 args. 

$random_num = rand(1, 10); // Random number between 1 to 10.
echo "<br><hr>Random number between [1 ~ 10] : $random_num<br>";

$new_num = rand(1, 5); // Value between 1 to 5. 
$new_pow = pow($new_num, 2); // Value of $new_num ^ 2.
echo "<br><hr>Square root of [$new_pow] : " . sqrt($new_pow) . "<br>";

$new_num = 4.6;

echo "<br><hr>Rounding [$new_num] to the highest number with ceil() : " . ceil($new_num) . "<br>";

echo "<br><hr>Rounding [$new_num] to the lowest number with floor() : " . floor($new_num) . "<br>";

echo "<br><hr>Rounding [$new_num] to the lowest/highest with round() : " . round($new_num) . "<br>";

?>

</body>
</html>