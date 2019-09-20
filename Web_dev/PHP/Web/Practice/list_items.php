<?php

include "functions.php";

if ( isset($_POST["display"]) ) {
    list_items();
}

?>


<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Cart Display</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href='mycss.css' type='text/css'>
    
</head>
<body>

<form action="list_items.php" method="post">

    <h4 class="text">Display Cart</h4>

    <input class="btn btn-primary" type="submit" name="display" value="Display"> <!-- btn & btn-primary to make buttons looks nicer -->

</form> 


</body>
</html>