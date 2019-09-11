<?php

session_start(); // Creating session cookies and allows session cookies to be accessed.

$_SESSION['greeting'] = "Good morning!"; // Assigns a value to the $_SESSION array. 

// Displays value contained inside the session array.
echo "<pre>"; 
print_r($_SESSION); 
echo "</pre><hr>"; 

?>

<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Session Cookie 1</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href="MyCss.css" type='text/css'>
    
</head>
<body>

<div class="container">
    <div class="col-sm-6"> 

        <h2 class="text">--Session Cookies 1--</h2><hr>

        <p><a href="Session2.php">Session 2</a></p>
        
    </div>
</div>


</body>
</html>