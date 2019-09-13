<?php

include "db.php";

function gather_data() {
    /*
    If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;

    $query = "SELECT * FROM users"; // Query to be send to MySql.
    $result = mysqli_query($connection, $query); // $connection is from "db.php". 

    if (!$result) { // IF query returned by mysqli_query() is FALSE. 
        die("<br>Query FAILED." . mysqli_error()); 
    }

    return $result;
}

function gather_specific_data($id) {
    /*
    If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;

    /*
    Query sample:

    SELECT * FROM users WHERE id = x; 
    */
    $query  = "SELECT * FROM users "; // Query to be send to MySql.
    $query .= "WHERE id = $id";

    $result = mysqli_query($connection, $query); // $connection is from "db.php". 

    if (!$result) { // IF query returned by mysqli_query() is FALSE. 
        die("<br>Query FAILED." . mysqli_error()); 
    }

    return $result;
}

function show_all_data() {

    $result = gather_data();

    /*
    While there are still rows, display the id values on the option selection box.
    */
    while ($row = mysqli_fetch_assoc($result)) {
        $id = $row['id']; 
        echo "<option value='$id'>$id</option>";
    }
}

function update_table($id, $password) {
    /*
    If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;
    
    $result = gather_specific_data($id); // Gather data for that particular row.
    $row = mysqli_fetch_assoc($result); // $result only has 1 row.

    $password = hash_password($password); // Encrypt $password.

    /*
    Sample Query for updating DB:
    UPDATE `users` SET `username` = 'memtest13', `password` = 'myP@ss13' WHERE `users`.`id` = 2;
    */
    $query  = "UPDATE users SET "; 
    $query .= "password = '$password' "; 
    $query .= "WHERE id = $id";

    $result = mysqli_query($connection, $query);

    if (!$result) { // IF there is something wrong with the MySql query.
        die("<br>Query Failed!" . mysqli_error());
    }

    echo "<p>$query</p>"; 
    echo "NEW password : $password<br>"; 
    
    $username = $row["username"]; 
    echo "<p>Updated password for <b>$username</b>!</p><hr>";
}

function delete_row() {
    /*
    If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;

    if ( !isset($_POST["id"]) ) { // IF value of ID is null, throws an error and stop further execution.
        die("<h3>ID must not be null!</h3>");
    }

    $id = $_POST["id"]; // Taken from option select value in the webpage.

    $result = gather_specific_data($id);

    $row = mysqli_fetch_assoc($result); // $result only has 1 row.

    $username = $row["username"]; // Username for that particular row.
    $password = $row["password"]; // Password for that particular row.

    /* 
    Sample query to delete particular row:
    DELETE FROM `users` WHERE `users`.`id` = 4
    */
    $query  = "DELETE FROM users ";
    $query .= "WHERE id = $id";

    $result = mysqli_query($connection, $query);
    
    if (!$result) { // IF there is something wrong with the query.
        die("<h3>Query Failed!</h3>" . mysqli_error());
    }
    
    echo "<h4>Entry deleted!</h4>";
    echo "<b><i>$username</i></b> with an id of <b><i>$id</i></b> and password as <b><i>$password</i></b> has been <b><i>deleted</i></b> from the database!<hr>";
}

function create_row($username, $password) {
    /*
    If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;

    if ($username && $password) { // IF username AND password is not blank
        /*
        Sample MySql query:
        
        INSERT INTO `users` (`id`, `username`, `password`) VALUES (NULL, 'myusername', 'P@$$');
        */
        $query  = "INSERT INTO users(username, password) ";
        $query .= "VALUES ('$username', '$password')";

        $result = mysqli_query($connection, $query);
        
        if ($result) { // IF there are no errors with the query.
            echo "<p>$query</p>";

            echo "<p<b>Entry Created!</b></p>";
            echo "<b>$username</b> as username...<br>"; 
            echo "<b>$password</b> as password...<br><hr>"; 
        }

        else { // IF there are errors with the query.
            die("<h3>Query Failed! </h3>" . mysqli_error());
        }
    }

    else { // IF username and/or password is blank.
        echo "Username/Password Field must not be blank!";
    }
}

function display_data() {
    /*
    If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;

    $result = gather_data();

    // Table header.
    echo "<div class='container'>";
    echo "<table border=1 width=30%>
                <tr>
                    <th>Username</th>
                    <th>Password</th>
                </tr>";

    // While row exist, fetch username/password and display them accordingly.
    while ($row = mysqli_fetch_assoc($result)) {
        $username = $row["username"];
        $password = $row["password"];

        echo "<tr>
                    <td>$username</td>
                    <td>$password</td>
              </tr>";
    }

    echo "</table></div><hr>"; // Closing tags.
}

function check_username_password($username, $password) {
    /*
    If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;

    if ($username && $password) { // Checks if username and password is not blank.

        // SELECT * FROM users WHERE username = x AND password = y;
        $query  = "SELECT * FROM users WHERE ";
        $query .= "username = '$username' AND  password = '$password'";

        $result = mysqli_query($connection, $query); 
        $num_rows = mysqli_num_rows($result); // Return the number of rows for the said query.

        echo "<p>$query</p>";

        if ($num_rows > 0) { // IF number of rows greater than 0, it means that username and password is found.

            echo "<h4><b>You are logged in!</b></h4><hr>";
        }

        else { // IF number of rows is lesser than 1, it means that username and password is not found. 

            echo "<h4><b>Wrong username and/or password!</b></h4><hr>";
        }
    }

    else { // Displays error if either username or password entry is left blank.
        echo "<h4>Username and/or Password must not be blank!</h4><hr>";
    }
}

function hash_password($password) {
    /*
   Blowfish hashing with a salt as follows: "$2a$", "$2x$" or "$2y$", a two digit cost parameter, "$", and 22 characters from the alphabet "./0-9A-Za-z". Using characters outside of this range in the salt will cause crypt() to return a zero-length string.

    To summarise, developers targeting only PHP 5.3.7 and later should use "$2y$" in preference to "$2a$".

    crypt ( string $str [, string $salt ] ) : string
    */
    $hash_format = "$2y$10$";
    $salt = "Th1sSaltHasT0AtLeast22";

    echo "Hash format : <b>$hash_format</b><br>"; 
    echo "Salt : <b>$salt</b><br><br>";

    $hashFormat_and_salt = $hash_format . $salt; 
    $password = crypt($password, $hashFormat_and_salt);

    return $password;
}

function check_duplicate($username) {
    /*
    If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;

    $query  = "SELECT * FROM users WHERE ";
    $query .= "username = '$username'";

    $result = mysqli_query($connection, $query); 

    $num_rows = mysqli_num_rows($result); // Return the number of rows for the said query.

    echo "<p>$query</p>";

    if ($num_rows > 0) { // IF row is greater than 0, username exists in database.
        echo "<p><b>$username</b> exists in database!</p>";
        return TRUE; 
    }

    else { // IF row is 0, username doesn't exist in database.
        return FALSE;
    }
}

?>