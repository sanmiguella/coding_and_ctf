<?php

if ( isset($_POST["submit"]) ) { // IF submit button is clicked.
    $first_num = $_POST["first_num"];
    $second_num = $_POST["second_num"];
    $submit = $_POST["submit"];

    // Adds together the 2 values on the form and store the sum in a variable.
    $sum = $first_num + $second_num; 
    
    // Displays results.
    echo "<h2>Results</h2>"; 
    echo "<b>$first_num + $second_num = $sum</b><br>";
    echo "Submit value : <b>$submit</b><br><hr>";
}

?>

<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Document</title>
    <link rel='stylesheet' href='mycss.css' type='text/css'>
    <link href="https://fonts.googleapis.com/css?family=Lexend+Deca&display=swap" rel="stylesheet">

</head>
<body>

<!--

input type: number allows only entering of numbers, instead of a textbar user will see an input bar with arrows. Pressing the up/down of the input bar will increment or decrement from the starting value of 0.

-->
<form action="practice6.php" method="post">
    <b>First number</b>
    <input type="number" value=0 name="first_num"><br>

    <b>Second number</b>
    <input type="number" value=0 name="second_num"><br> 

    <input type="submit" name="submit">
</form>

</body>
</html>