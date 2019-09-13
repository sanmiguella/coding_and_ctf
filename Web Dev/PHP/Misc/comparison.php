<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Document</title>
    <link rel='stylesheet' href='mycss.css' type='text/css'>
    <link href="https://fonts.googleapis.com/css?family=Lexend+Deca&display=swap" rel="stylesheet">

</head>
<body>

<h1>Comparison operators</h1>
<pre>
    equal == 
    idential === 
    compare > < >= <= <>
    not equal != 
    not identical !==
</pre>

<h1>Logical operators</h1>
<pre>
    And && 
    Or || 
    Not !
</pre>

<?php

$val_one = 4;
$val_two = 4;

echo "<h1>Comparison operators results</h1>";

if($val_one < $val_two) {
    echo "$val_one is lesser than $val_two.<br>";
}

if($val_one <= $val_two) {
    echo "$val_one is lesser than or equals to $val_two.<br>";
}

if ($val_one == $val_two) { // 4 is equals to 4, 4 is equals to "4" 
    echo "$val_one is equals to $val_two.<br>";
}

if ($val_one === $val_two) { // 4 is identical to 4, 4 is not identical to "4"
    echo "$val_one is identical to $val_two.<br>";
}

if ($val_one > $val_two) {
    echo "$val_one is greater than $val_two.<br>";
}

if ($val_one >= $val_two) {
    echo "$val_one is greater than or equals to $val_two.<br>";
}

if ($val_one != $val_two) {
    echo "$val_one is not equals to $val_two.<br>";
}

echo "<h1>Logical operators results</h1>";

if ($val_one == $val_two && $val_one === $val_two) {
    echo "$val_one is equal to $val_two AND $val_one is identical to $val_two.<br>";
}

if ($val_one == $val_two || $val_one === $val_two) {
    echo "$val_one is equal to $val_two OR $val_one is not identical to $val_two.<br>";
}

?>

</body>
</html>