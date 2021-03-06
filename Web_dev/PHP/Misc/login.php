<?php

if ( isset($_POST["submit"]) ) { // IF submit button is pressed.

    $username = $_POST["username"];
    $password = $_POST["password"];

    $connection = mysqli_connect("localhost", "root", "password", "loginapp");

    // Checks database connection.
    if ($connection) {
        echo "We are connected!<br>";
    } else {
       die("Database connection failed!"); 
    }

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

<div class="container">

    <div class="col-sm-6"> <!-- Column extra small 6 -->
        <form action="login.php" method="post">
            <div class="form-group">
                <label for="username"><b>Username</b></label>

                <!-- echo $username in value echoes the typed username after post method. -->
                <input type="text" class="form-control" name="username" value="<?php echo $username; ?>">
            </div>

            <div class="form-group">
                <label for="password"><b>Password</b></label>

                <!-- echo $password in value echoes the typed password after post method. -->
                <input type="password" class="form-control" name="password" value="<?php echo $password; ?>">
            </div>

            <input class="btn btn-primary" type="submit" name="submit" value="Submit"> <!-- btn & btn-primary to make buttons looks nicer -->
        </form> 
    </div>

</div>


</body>
</html>