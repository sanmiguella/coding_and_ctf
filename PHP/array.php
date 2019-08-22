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

$list = [2, 5, 3, 13, 8, 34, 21]; // Array of integers. 
$count = 0;

foreach($list as $element) { // Loops through each element and print it out.
    echo "Element[$count] : $element<br>";
    $count++; // Increment count by 1.
}

echo "<hr>Max number : " . max($list) . "<br>"; // Display the max value of the array. 

echo "Min number : " . min($list) . "<br><hr>"; // Display the min value of the array.

echo "Unsorted:<br>";
print_r($list);

echo "<hr>Sorted:<br>";
sort($list); // Sort elements in ascending order.
print_r($list);
echo "<br><hr>";

$count = 0; 
foreach($list as $element) {
    echo "Element[$count] : $element<br>";
    $count++; 
}

?>

</body>
</html>