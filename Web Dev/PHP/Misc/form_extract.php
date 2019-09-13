<?php

if ( isset($_POST['submit']) ) { // IF submit button is pressed.
    $username = $_POST['username'];
    $password = $_POST['password'];

    $name = array("harry", "student", "peter", "john", "maxine", "jane", "tommy");

    $username_min = 4; // Min characters for username.
    $username_max = 8; // Max characters for username.
    
    $password_min = 4; // Min characters for password. 
    $password_max = 8; // Max characters for password.

    // IF username entered is less than min no of allowed characters.
    if (strlen($username) < $username_min) {
        echo "Username has to be minimally $username_min characters.<br>";

        echo "Username entered has only " . strlen($username) . " characters.<br><br>";
    }

    // IF username entered has more than max no of allowed characters. 
    if (strlen($username) > $username_max) {
        echo "Username entered cannot be more than $username_max characters.<br>";

        echo "Username entered has " . strlen($username) . " characters.<br><br>";
    }

    // IF password entered has less than min no of allowed characters. 
    if (strlen($password) < $password_min) {
        echo "Password has to be minimally $password_min characters.<br>";

        echo "Password entered has only " . strlen($password) . " characters.<br><br>";
    }

    // IF password entered has more than max no of allowed characters. 
    if (strlen($password) > $password_max) {
        echo "Password entered cannot be more than $password_max characters.<br>";

        echo "Password entered has " . strlen($password) . " characters.<br><br>";
    }

    if (!in_array($username, $name)) { // IF username is found inside array.
        echo "Sorry, you are not allowed to login :(<br><br>";

        echo "Allowed login names:<br>";
        print_r($name);
        
        echo "<hr>";
    } else { // IF username is not found inside array.
        echo "Welcome $username!<br><hr>";
    }

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
    Once submit button is clicked, the form will be handled by form.php
    The value following the name keyword will be used by the POST method.
    Placeholder are just pseudo values the guides user.
-->
<form action="form_extract.php" method="post">
    <b>Username</b>
    <br><input type="text" placeholder="Enter name" name="username"><br>

    <b>Password</b>
    <br><input type="password" placeholder="Enter password" name="password"><br>

    <input type="submit" name="submit"><br>
</form>

<?php


?>

</body>
</html>