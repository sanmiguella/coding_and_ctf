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

function calculate_pow($min, $max) {
    // Loop from min to max and on each iteration display the current loop index and its power of 2 value.
    for($count = $min; $count <= $max; $count++) {
        echo "Val : $count , $count<sup>2</sup> : " . pow($count, 2) . "<br>";
    }
}

$min = rand(1, 5); // Get the min index.
$max = rand(6, 10); // Get the max index.

calculate_pow($min, $max);

$string = "HeLLo WoRLd, My NAMe Is HArRY."; 
echo "<br><hr>String : <b>$string</b><br>";

echo "Uppercase : <b>" . strtoupper($string) . "</b><br>"; // Converts string to uppercase and displays it. 

echo "String length : <b>" . strlen($string) . "</b><br>";

$string = "haha"; // String to find.
$values = [123, 321, 456, "hello world", "nah", "haha"]; // Array of values.
$found = in_array($string, $values); // If string is found in the array of values, $found = True.

echo "<br><hr>String to find : <b>$string</b><br>";
print_r($values);
echo "<br>Found : <b>$found</b><br>";

function randomize_array($min, $max) {
    $array_vals = []; 
    
    // This loop will assign a random value on each iteration. The number of loops can be calculated with $max - $min.
    for($count = $min; $count <= $max; $count++) {
        array_push($array_vals, rand(1, 5)); // Push a random value into the array.
    }

    echo "<br><hr>";

    $count = 0; 

    // Loops through each element and prints out its value.
    foreach($array_vals as $element) {
        echo "Element[$count] : $element<br>";
        $count++; // Increments count by 1. 
    }
}

randomize_array($min, $max);

?>

</body>
</html>