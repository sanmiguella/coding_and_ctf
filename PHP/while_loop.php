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

$number = 0; // Initializing loop. 

echo "Loop start!<br><br>";

while($number < 10){ // Loop keeps repeating as long as $number is lesser than 10.
    echo "Current loop : $number<br>"; // Prints out the current loop.
    $number++; // Increment $number by 1.
}

echo "<br>Loop end!<br>";

?>

</body>
</html>