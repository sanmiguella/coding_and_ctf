<?php

include "functions.php";

update_table();

?>


<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Login update</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href='mycss.css' type='text/css'>
    
</head>
<body>

<div class="col-sm-6">
    <h4 class="text">Update login account</h4><br>

    <form action="login_update.php" method="post">

        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" name="username" class="form-control">
        </div>

        <div class="form-group"> 
            <label for="password">Password</label>
            <input type="password" name="password" class="form-control">
        </div>

        <select name="id">
            <?php show_all_data(); ?>
        </select>

        <br><br> <!-- To separate the option select option button from the update button -->

        <input class="btn btn-primary" type="submit" name="update" value=Update> <!-- btn & btn-primary to make buttons looks nicer -->

    </form> 
</div>

</body>
</html>