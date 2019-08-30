<?php

include "db.php";

function show_all_data() {
    /*
        If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */
    global $connection;

    $query = "SELECT * FROM users"; // Query to be send to MySql.
    $result = mysqli_query($connection, $query); // $connection is from "db.php". 

    if (!$result) { // IF query returned by mysqli_query() is FALSE. 
        die("<br>Query FAILED." . mysqli_error()); 
    }

    while ($row = mysqli_fetch_assoc($result)) {
        $id = $row['id']; 
        echo "<option value='$id'>$id</option>";
    }
}

function update_table() {
    /*
        If $connection isn't global, it means that $connection will be a local scope variable and the value in $connection will not be from db.php, it will mess up the webpage. 
    */

    global $connection;

    if ( isset($_POST["update"]) ) {

        $username = $_POST["username"]; 
        $password = $_POST["password"];
        $id = $_POST["id"];
    
        /* 
            Sample Query for selecting username password based on id:
    
            SELECT username, password from users where id = 1;
        */
    
        $query  = "SELECT username, password from users ";
        $query .= "WHERE id = $id";
    
        $result = mysqli_query($connection, $query);
    
        $row = mysqli_fetch_assoc($result); // $result only has 1 row.
        $old_username = $row["username"];
        $old_password = $row["password"];
    
        if (!$result) {
            die("<br>Query Failed!" . mysqli_error());
        }
    
        // Display old username/password.
        echo "Query string : <b><i>$query</i></b><br>";
        echo "OLD username : <b><i>$old_username</i></b><br>"; 
        echo "OLD password : <b><i>$old_password</i></b><br><br>";
    
        /*
            Sample Query for updating DB:
    
            UPDATE `users` SET `username` = 'memtest13', `password` = 'myP@ss13' WHERE `users`.`id` = 2;
        */
    
        $query  = "UPDATE users SET "; 
        $query .= "username = '$username', ";
        $query .= "password = '$password' "; 
        $query .= "WHERE id = $id";
    
        $result = mysqli_query($connection, $query);
    
        if (!$result) {
            die("<br>Query Failed!" . mysqli_error());
        }
    
        echo "Query string : <b><i>$query</i></b><br>"; 
        echo "NEW username : <b><i>$username</i></b><br>";
        echo "NEW password : <b><i>$password</i></b><br><hr>";
    }
}

?>