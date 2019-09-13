<?php

// The only way submit button is going to be set is if we click the submit button.
if ( isset($_POST['submit']) ) {

    // IF both username and password entry is not empty.
    if ($_POST['username'] != "" && $_POST['password'] != "") {
        $username = $_POST['username']; // Stores the POST username value in a variable.
        $password = $_POST['password']; // Stores the POST password value in a variable.

        // Displays the entry that was entered.
        echo "You entered <b>$username</b> as username!<br>";
        echo "You entered <b>$password</b> as password!<br><hr>";
    }

    // IF both username and password text entry is empty.
    else {
        echo "Either the <b>username</b> or <b>password</b> entry is empty!<br><hr>";
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
<form action="form.php" method="post">
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