<?php

include "functions.php";

delete_row();

?>


<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Login Delete</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href='mycss.css' type='text/css'>
    
</head>
<body>

<div class="col-sm-6">
    <form action="login_delete.php" method="post">

        <select name="id">
            <?php show_all_data(); ?>
        </select>

        <br><br> <!-- To separate the option select option button from the update button -->

        <input class="btn btn-primary" type="submit" name="delete" value="Delete"> <!-- btn & btn-primary to make buttons looks nicer -->

    </form> 
</div>

</body>
</html>