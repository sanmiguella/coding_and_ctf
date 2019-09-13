<?php

include "functions.php"; 

if ( isset($_POST["read"]) ) { // IF submit button is pressed.
    display_data();
}

?>


<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Login read</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href='mycss.css' type='text/css'>
    
</head>
<body>

<form action="login_read.php" method="post">

    <div class="container">
        <h4 class="text">Display login account</h4><br>

        <input class="btn btn-primary" type="submit" name="read" value="Read"> <!-- btn & btn-primary to make buttons looks nicer -->
    </div>
</form> 

</body>
</html>