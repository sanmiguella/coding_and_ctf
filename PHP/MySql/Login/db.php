<?php

$connection = mysqli_connect("localhost", "root", "password", "loginapps");

// Checks database connection.
if (!$connection) { // IF database connection can't be established, throw an error and continue no further.
   die("<h3>Connection failed!</h3>"); 
}

echo "<h4>DB connection ok.</h4><hr>";

?>
