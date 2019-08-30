<?php

include "db.php";

if ( isset($_POST["read"]) ) { // IF submit button is pressed.
 
    $query = "SELECT * FROM users"; // Query for displaying table data.
    $result = mysqli_query($connection, $query); // To store the result of the MySql query.
    
    if (!$result) { // IF result is false, it means query failed due to errors in the MySql query, program will throw an error and continue no further.
        die('<h3>Query Failed!</h3>' . mysqli_error());
    }

    $count = 0; 
    /*
    For associative array, column name will be in string.
    Array ( [id] => 2 [username] => test [password] => myP@ss ) 
I   */
    while ($row = mysqli_fetch_assoc($result)) {
        echo "Index[$count] : ";
        print_r($row); // Prints the value of each row.
        echo "<br>";

        $count++; 
    }
    echo "<hr>";
    
}

?>


<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Document</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href='mycss.css' type='text/css'>
    
</head>
<body>

<form action="login_read.php" method="post">

    <input class="btn btn-primary" type="submit" name="read" value="Read"> <!-- btn & btn-primary to make buttons looks nicer -->

</form> 


</body>
</html>