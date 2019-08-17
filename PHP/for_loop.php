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

echo "For loop starts!<br><br>";

/* 
Loop is initialized with $counter = 0
As long as $counter < 10, loop continues.
After loop finishes an iteration, $counter is incremented by 1.
*/
for($counter = 0; $counter < 10; $counter++){ 
    echo "Loop number : $counter<br>";
}

echo "<br>For loop ends!<br>";

?>

</body>
</html>