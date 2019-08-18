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

$name = "harry";

echo "My name is $name.<br>";

/* 
    Step 1:
    If, If-Else, Else statements.
*/
if ($name == "john") {
    echo "I love javascript!<br>"; 
}

elseif ($name == "ben") {
    echo "I love html!<br>"; 
}

else {
    echo "I love php!<br>";
}

echo "<br>";

/*
    Step 2:
    For loops.
*/
$counter = 0; 
for ($counter; $counter < 10; $counter++) {
    $i = $counter + 1;
    echo "Loop : $i<br>";
}

echo "<br>";

/*
    Step 3" 
    Switch case.
*/
$color = "blue";
switch ($color) {
    case "red":
        echo "You love red!<br>";
        break;
    
    case "yellow":
        echo "You love yello!<br>";
        break; 

    case "green":
        echo "You love green!<br>";
        break; 

    case "blue":
        echo "You love blue!<br>";
        break; 

    default:
        echo "You love rainbows!<br>";
        break; 
}

?>

</body>
</html>